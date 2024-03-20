import streamlit as st
import pickle
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model


def main():
    # Specify the path to the pickle file
    """ TO DO!!!
    must be saved as h5 in model!
    the call to model must be done in api file!!!
    !!!
    """
    # model_path = 'models/happy_sad_mod.h5'
    model_path = 'models/happy_sad_mod.pkl'

    # Load the pre-trained model
    with open(model_path, 'rb') as f:
        # !!! model = load_model(model_path)
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
        """
        !!! TO DO!!!
        must load to GCP
        wait to have it loaded to GCP
        !!!
        """

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
