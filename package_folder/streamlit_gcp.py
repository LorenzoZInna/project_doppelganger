import streamlit as st
import pickle
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from google.cloud import storage

def main():
    # Specify the path to the pickle file
    """ TO DO!!!
    must be saved as h5 in model!
    the call to model must be done in api file!!!
    !!!
    """
    client = storage.Client()

    # Set up the Streamlit app
    st.title('Project Doppelganger')
    st.subheader('How are you feeling today?')
    st.write('Please upload an image of a frontal mugshot with white background.')

    # Create a file uploader for uploading images
    uploaded_file = st.file_uploader("Upload a frontal mugshot with white background", type=["jpg", "jpeg"])

    # Inform the user when the file has been uploaded
    if uploaded_file is not None:

        bucket_name = "doppelganger-1-bucket "
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(uploaded_file.name)
        blob.upload_from_file(uploaded_file, content_type=uploaded_file.type)
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button("Upload to GCP Bucket"):
             image_url = upload_to_gcp_bucket(uploaded_file)
             st.success(f"Image uploaded successfully! URL: {image_url}")

        return blob.public_url



        # Convert the uploaded image to a format suitable for the model
        """
        !!! TO DO!!!
        must load to GCP
        must open from bucket
        !!!
        """

###############################################


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
            st.write("The model predicts the image is happy.", emotion='happy')
        else:
            st.write("The model predicts the image is sad.", emotion='sad')

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

if __name__ == "__main__":
    main()
