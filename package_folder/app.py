import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications.vgg16 import preprocess_input
from emotion_to_track_mvp import get_random_track_embed_code
from tensorflow.keras.models import load_model
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI

# Function to load the trained model
def load_trained_model(model_path):
    model = load_model(model_path)

    # Print the summary of the loaded model
    print(model.summary())

    return model

# Function to preprocess the image
def preprocess_image(image):
    target_size = (150, 150)  # Adjust according to your model's input size
    resized_image = image.resize(target_size)
    image_array = np.array(resized_image)
    preprocessed_image = preprocess_input(image_array)
    return preprocessed_image

# Function to predict emotion using the loaded model
def predict_emotion(model, image):
    prediction = model.predict(np.expand_dims(image, axis=0))
    emotion = "happy" if prediction[0] > 0.5 else "sad"
    return emotion

def display_spotify_embed(emotion):
    embed_code_random = get_random_track_embed_code(emotion)[0]
    embed_code_with_style = f"""
    <div style='height:100%; width:100%; display: flex; justify-content: center; align-items: center;'>
        <style>
            iframe {{
                margin: 0 !important;
                padding: 0 !important;
                height: 232px !important; /* Adjust height as necessary */
                width: 100% !important;
            }}
        </style>
        {embed_code_random}
    </div>
    """
    return st.markdown(embed_code_with_style, unsafe_allow_html=True)

def main():
    st.title('Project Doppelganger')
    st.subheader('How are you feeling today?')
    st.write('### Want to discover a song that matches your mood?')

    # Layout with two columns
    col1, col2 = st.columns([3, 1])  # Adjust the ratio of the column widths as needed

    with col1:
        # Create a file uploader for uploading images
        uploaded_file = st.file_uploader("Please upload a frontal portrait photo of yourself with a white background", type=["jpg", "jpeg"])


    # If a file is uploaded, display it in the second column
    if uploaded_file is not None:
        with col2:
            st.write("<div style='display: flex; height: 100%; align-items: center; justify-content: center;'>", unsafe_allow_html=True)
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', width=150)
            st.write("</div>", unsafe_allow_html=True)


    # Only proceed with loading the model and predicting if an image is uploaded
    if uploaded_file is not None:

        st.success('Image processed successfully!')

        # Convert the uploaded image to a format suitable for the model
        image = Image.open(uploaded_file)

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Load the pre-trained model from an H5 file
        model_path = '../models/happy_sad_model.h5'  # Update this with the path to your H5 file
        model = load_trained_model(model_path)

        # Predict emotion using the model
        emotion = predict_emotion(model, processed_image)

        # Display the prediction result
        st.write(f"### The model predicts you're {emotion.upper()}, here's a song for you:")

        # Get Spotify Embed corresponding to the predicted emotion
        spotify_embed = display_spotify_embed(emotion)

        # Link to your Doppelgangers (Google Lens)
        #url_image_gcp = 'https://storage.googleapis.com/doppelganger-1-bucket/NilSadWhite.JPG'
        #url_google_lens = f'https://lens.google.com/uploadbyurl?url={url_image_gcp}'
        #st.markdown(f"<div style='text-align: center;'><h3><a href='{url_google_lens}' target='_blank'>Doppelganger Identification Feature Coming Soon ------> Stay Tuned!</a></h3></div>", unsafe_allow_html=True)


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
