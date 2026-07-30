
import streamlit as st
import pickle
import pandas as pd

# Your complete Streamlit app code goes here


requirements = """
streamlit
scikit-learn
numpy
"""

with open("requirements.txt", "w") as f:
    f.write(requirements)

print("requirements.txt created successfully!")
from google.colab import files

files.download("app.py")
files.download("requirements.txt")
