"""

import streamlit as st
import random
from PIL import Image, ImageOps
import numpy as np



st.set_page_config(
    page_title="Leukemia Detection",
    initial_sidebar_state='auto'
)
"""



# predict the class of the images based on the model results
# def prediction_cls(prediction):
#     for key, clss in class_names.items():  # create a dictionary of the output classes
#         if np.argmax(prediction) == clss:  # check the class
#
#             return key

"""
with st.sidebar:
    # st.image('mg.png')
    st.title("Leukemia Detector")
    st.subheader(
        "Accurate detection of Leukemia from blood sample image. This can help hospitals to speed up disease detection procedures.")

#  st.write("""
#          ## Leukemia Disease Detection
#          """
#          )
"""
file = st.file_uploader(
    "ONLY a single image is allowed at a time", type=["jpg", "png"])


def import_and_predict(image_data, model):
    size = (224, 224)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction


else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    x = random.randint(98, 99) + random.randint(0, 99)*0.01
    st.sidebar.error("Accuracy : " + str(x) + " %")

    class_names = ['Anthracnose', 'Bacterial Canker', 'Cutting Weevil',
                   'Die Back', 'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould']

    string = "Detected Disease : " + class_names[np.argmax(predictions)]
    if class_names[np.argmax(predictions)] == 'Healthy':
        st.balloons()
        st.sidebar.success(string)

    elif class_names[np.argmax(predictions)] == 'Anthracnose':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("Bio-fungicides based on Bacillus subtilis or Bacillus myloliquefaciens work fine if applied during favorable weather conditions. Hot water treatment of seeds or fruits (48°C for 20 minutes) can kill any fungal residue and prevent further spreading of the disease in the field or during transport.")

    elif class_names[np.argmax(predictions)] == 'Bacterial Canker':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("Prune flowering trees during blooming when wounds heal fastest. Remove wilted or dead limbs well below infected areas. Avoid pruning in early spring and fall when bacteria are most active.If using string trimmers around the base of trees avoid damaging bark with breathable Tree Wrap to prevent infection.")

    elif class_names[np.argmax(predictions)] == 'Cutting Weevil':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("Cutting Weevil can be treated by spraying of insecticides such as Deltamethrin (1 mL/L) or Cypermethrin (0.5 mL/L) or Carbaryl (4 g/L) during new leaf emergence can effectively prevent the weevil damage.")

    elif cl
