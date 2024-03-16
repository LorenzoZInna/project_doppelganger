import streamlit as st
import pickle
from PIL import Image
import numpy as np

# Specify the path to the pickle file
model_path = '../models/happy_sad_mod.pkl'

# Load the pre-trained model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Set up the Streamlit app
st.title('Project Doppelganger')
st.subheader('How are you feeling today?')
st.write('Please upload an image of a frontal mugshot with white background.')

# Create a file uploader for uploading images
uploaded_file = st.file_uploader("Upload a frontal mugshot with white background", type=["jpg", "jpeg"])

# Inform the user when the file has been uploaded
if uploaded_file is not None:
    st.success('Image uploaded successfully!')

    # Convert the uploaded image to a format suitable for the model
    image = Image.open(uploaded_file)

    # Preprocess the image
    target_size = (150, 150)  # Adjust according to your model's input size
    image = image.resize(target_size)
    image_array = np.array(image)
    image_array = image_array.astype('float32') / 255.0  # Normalize pixel values

    # Make prediction using the model
    prediction = model.predict(np.expand_dims(image_array, axis=0))

    # Display the prediction result
    if prediction[0] > 0.5:
        st.write("The model predicts the image is happy.")
    else:
        st.write("The model predicts the image is sad.")

    # Display the preprocessed image
    st.write("### Here is how your preprocessed image looks like:")
    st.image(image_array, caption='Preprocessed Image', use_column_width=True)

# Add some footer text
st.markdown(
    """
    <style>
        .footer {
            font-size: 12px;
            text-align: center;
            margin-top: 50px;
        }
    </style>
    <div class="footer">
        <p>&copy; 2024 Project Doppelganger. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
