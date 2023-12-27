# Imports to be used for the UI

import streamlit as st
import requests
import io
from PIL import Image

# hide warnings
import warnings
warnings.filterwarnings("ignore")


# hiding part of the code, as this is just for adding some custom CSS styling but not a part of the main idea
hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)  # hide the CSS code from the screen as they are embedded in markdown text. Also, allow streamlit to unsafely process as HTML title of the app


st.title('Leukemia Detection App')

# description
st.write("""
Accurate detection of Leukemia from blood sample image. This can help hospitals to speed up disease detection procedures. Try it yourself.
""")

# button to start over
if st.button('Start Over'):
    uploaded_file = None
    st.empty()

# Allowing the user to upload an image
uploaded_file = st.file_uploader(
    "Choose an image...(ONLY a single image is allowed at a time)", type="jpg")

if uploaded_file is None:
    st.text("No image file uploaded. Please upload an image file")
else:
    # Displaying the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")

    # Sending the image to the FastAPI backend for processing
    st.write("Classifying...")
    files = {'file': uploaded_file.getvalue()}
    res = requests.post("http://localhost:8000/predict/", files=files)

    # Displaying the result
    st.write("Class: ", res.json())
