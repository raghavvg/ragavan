import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import pickle

# Load the saved encoder and model
with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

model = tf.keras.models.load_model('updated_file1.h5')

# Define the feature names
important_features = ['gill-spacing', 'cap-color', 'ring-type', 'veil-color', 'gill-color', 'stalk-surface-below-ring']

# Streamlit app
st.title("Mushroom Poison Prediction")
st.write("Enter the following features to determine if a mushroom is poisonous or edible:")

# Create input fields for the user to enter data
gill_spacing = st.selectbox("Gill Spacing", ["close", "crowded"])
cap_color = st.selectbox("Cap Color", ["brown", "yellow", "white", "gray"])
ring_type = st.selectbox("Ring Type", ["pendant", "evanescent"])
veil_color = st.selectbox("Veil Color", ["white", "yellow"])
gill_color = st.selectbox("Gill Color", ["black", "brown"])
stalk_surface_below_ring = st.selectbox("Stalk Surface Below Ring", ["smooth", "scaly"])

# When the user clicks "Predict"
if st.button("Predict"):
    # Create a dataframe for the input
    input_data = pd.DataFrame({
        'gill-spacing': [gill_spacing],
        'cap-color': [cap_color],
        'ring-type': [ring_type],
        'veil-color': [veil_color],
        'gill-color': [gill_color],
        'stalk-surface-below-ring': [stalk_surface_below_ring]
    })

    # One-hot encode the input data
    input_encoded = encoder.transform(input_data).astype('float32')

    # Predict the class using the model
    prediction = model.predict(input_encoded)

    # Display the result
    prediction_label = "Poisonous" if prediction[0] > 0.5 else "Edible"
    st.write(f"The mushroom is likely **{prediction_label}**.")
