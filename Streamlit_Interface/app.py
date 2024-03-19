import streamlit as st
import requests
from PIL import Image
import numpy as np
import cv2
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications import VGG16
import pickle
from tensorflow.keras.models import load_model as tf_load_model

# Function to load the pre-trained VGG16 model
def load_model(model_path):
    model = tf_load_model(model_path)
    return model

# Function to preprocess image
def preprocess_image(image):
    # Resize image to fit VGG16 input dimensions
    target_size = (150, 150)  # Adjust according to your model's input size
    resized_image = image.resize(target_size)
    # Convert to numpy array
    image_array = np.array(resized_image)
    # Preprocess image for VGG16 model
    preprocessed_image = preprocess_input(image_array)
    return preprocessed_image

# Function to predict emotion using the loaded model
def predict_emotion(model, image):
    # Make prediction using the loaded model
    prediction = model.predict(np.expand_dims(image, axis=0))
    # Convert prediction to human-readable label
    emotion = "happy" if prediction[0] > 0.5 else "sad"
    return emotion

# Function to make request to API
def get_spotify_link(emotion):
    # Replace 'your_api_endpoint' with your actual API endpoint
    # Here, we'll just return dummy links for demonstration purposes
    if emotion == "happy":
        return "https://open.spotify.com/playlist/37i9dQZF1DX7KNKjOK0o75"  # Example happy playlist link
    else:
        return "https://open.spotify.com/playlist/37i9dQZF1DWZd79rJ6a7lp"  # Example sad playlist link

def main():
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
        processed_image = preprocess_image(image)

        # Load the pre-trained model from an H5 file
        model_path = '../models/happy_sad_mod.h5'  # Update this with the path to your H5 file
        model = load_model(model_path)

        # Predict emotion using the model
        emotion = predict_emotion(model, processed_image)

        # Get Spotify link corresponding to the predicted emotion
        spotify_link = get_spotify_link(emotion)

        # Display the prediction result
        st.write(f"The model predicts the image is {emotion}.")

        # Display the Spotify link
        st.write('Spotify Link:', spotify_link)

        # Display the preprocessed image
        st.write("### Here is how your preprocessed image looks like:")
        st.image(image, caption='Preprocessed Image', use_column_width=True)

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


if __name__ == "__main__":
    main()
