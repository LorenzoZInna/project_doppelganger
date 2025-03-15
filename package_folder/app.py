import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications.vgg16 import preprocess_input
from emotion_to_track_mvp import get_random_track_embed_code
from tensorflow.keras.models import load_model
from google.cloud import storage
from io import BytesIO

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

# Function to upload file to Google Cloud Storage
def upload_to_gcs(bucket_name, source_file, destination_blob_name):
    # Initialize the Google Cloud Storage client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)

    # Create a new blob (i.e., file object) in the bucket
    blob = bucket.blob(destination_blob_name)

    # Upload the file to GCS
    blob.upload_from_file(source_file, content_type="image/jpeg")  # or another content type depending on your image format

    # No need to make the blob public since uniform bucket-level access is enabled

    # Return the public URL (this URL will work if the bucket has proper IAM permissions)
    return blob.public_url

# Function to display the Spotify embed code
def display_spotify_embed(emotion):
    # Set the id from the package
    embed_code_random = get_random_track_embed_code(emotion)[0]
    return st.markdown(embed_code_random, unsafe_allow_html=True)

def main():
    st.title('Mood & Doppelganger')
    st.subheader('How are you feeling today?')
    st.write('### Please upload a frontal mugshot with a white background.')

    # Create a file uploader for uploading images
    uploaded_file = st.file_uploader("Click on upload and select a frontal mugshot with a white background", type=["jpg", "jpeg"])

    # Inform the user when the file has been uploaded
    if uploaded_file is not None:
        st.success('Image uploaded successfully!')

        # Convert the uploaded image to a format suitable for the model
        image = Image.open(uploaded_file)

        # Convert PIL Image to BytesIO (memory buffer)
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format=image.format)
        img_byte_arr.seek(0)  # Go to the start of the BytesIO buffer

        # Define file name and destination
        file_name = uploaded_file.name
        destination_blob_name = file_name

        # Define your bucket name here
        bucket_name = "doppelganger-1-bucket"  # Replace with your GCS bucket name

        # Upload the file to GCS and get the public URL
        try:
            public_url = upload_to_gcs(bucket_name, img_byte_arr, destination_blob_name)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.write("File uploaded successfully! You can access it at:")
            st.write(public_url)
        except Exception as e:
            st.error(f"An error occurred while uploading the file: {e}")
            return  # Exit early if the upload fails

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Load the pre-trained model from an H5 file
        model_path = '../project_doppelganger/models/happy_sad_model.h5'  # Update this with the path to your H5 file
        model = load_trained_model(model_path)

        # Predict emotion using the model
        emotion = predict_emotion(model, processed_image)

        # Display the prediction result
        st.write(f"### The model predicts the image is {emotion}.")

        # Get Spotify Embed corresponding to the predicted emotion
        display_spotify_embed(emotion)

        # Link to your Doppelgangers (Google Lens)
        url_image_gcp = public_url  # Use the uploaded image URL from GCS
        url_google_lens = f'https://lens.google.com/uploadbyurl?url={url_image_gcp}'
        st.markdown(f"<div style='text-align: center;'><h3><a href='{url_google_lens}' target='_blank'>Click here to see your doppelgangers!</a></h3></div>", unsafe_allow_html=True)

        # Display the preprocessed image
        st.markdown("Here's what your preprocessed image looks like:")
        st.image(image, caption='Preprocessed Image', width=250)  # Adjust the width as needed

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
