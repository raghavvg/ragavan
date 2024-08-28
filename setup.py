from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'pandas',
        'numpy',
        'tensorflow',
        'scikit-learn',
        'h5py',
        'protobuf',
        'setuptools>=58.0.0',
        'wheel',
    ],
)
