import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import streamlit as st

from streamlit_background import set_full_background

solardetection = tf.keras.models.load_model('/Users/apple/Documents/Guvi/Projects/Solar gaurd /Intelligent Defect Detection on Solar Panels/solardetection_model_500_E18.h5')

detect_name=["Bird drop panel",
             "Cleaned panel","Dust panel","Electrical problem","Physical damage","Snow problem"]



#class_names = list(class_labels.keys())

# === Streamlit App ===

# stting page layout
img_path="/Users/apple/Documents/Guvi/Projects/Solar gaurd /Intelligent Defect Detection on Solar Panels/sun_solar.png"
set_full_background(img_path)

# stting page layout
#st.set_page_config(layout="wide")

#st.title("🔍 Solar Panel Defect Detection")
st.markdown(
    "<h4 style='color:#070983; font-size:45px; font-weight:700; margin-bottom:10px;'>🔍 Solar Panel Defect Detection</h4>",
    unsafe_allow_html=True
)
#st.write("Upload a solar panel image to detect the type of fault.")
st.write(
    "<h4 style='color:#5D0783; font-size:20px; font-weight:700; margin-bottom:10px;'>Upload a solar panel image to detect the type of fault.</h4>",
    unsafe_allow_html=True
)
# === File uploader ===
uploaded_file = st.file_uploader(":blue[Choose an image...]", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    #img_path="/Users/apple/Documents/Guvi/Projects/Solar gaurd /Intelligent Defect Detection on Solar Panels/test_image/Bird (1).jpeg"
    #img = Image.open(uploaded_file)
    #st.image(img, caption="Uploaded Image", use_column_width=True)
    #st.image(img, caption="Uploaded Image", width=300)


    img = Image.open(uploaded_file)
    resized_img = img.resize((500, 250))  # Width = 300, Height = 200
    st.image(resized_img, caption="Uploaded Image")

    # Preprocess image
    img = img.resize((500, 500))
    #img = image.load_img(img, target_size=(224, 224))
    # === Load and preprocess the image ===
    
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Rescale like training
    img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 224, 224, 3)

    # === Make prediction ===
    predictions = solardetection.predict(img_array)

    # === Get predicted class index ===
    predicted_class_index = np.argmax(predictions[0])
    


    # Show prediction
    #st.success(f"🔎 Predicted: *** {detect_name[predicted_class_index]} ***")
    #st.write(f"### {detect_name[predicted_class_index]}")

    st.write(
    f"<h4 style='color:#761306; font-size:20px; font-weight:700; margin-bottom:10px;'>The above uploade Image is {detect_name[predicted_class_index]}.</h4>",
    unsafe_allow_html=True
)