import streamlit as st
from PIL import Image
import requests
from tensorflow.keras.models import load_model


def main():

    st.title('Project Doppelganger')
    st.subheader('How are you feeling today?')
    st.write('Please upload an image of a frontal mugshot with white background.')

    # Create a file uploader for uploading images
    uploaded_file = st.file_uploader("Upload a frontal mugshot with white background", type=["jpg", "jpeg","png"])

    print(f"The type of the chosen image is {type(uploaded_file)}")

    # Check the uploaded Image
    if uploaded_file is not None:
        # Read Image file
        image = Image.open(uploaded_file)
        print(image)
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        #predict url - it will change after each docker build run

        predict_url = 'https://mvp-wjxeo2hbwa-ew.a.run.app/return_song?emotion=happy'
        #Predict Button
        predict_button = st.button('Prediction')
        # When the Button "Prediction" is pushed >> Link it to Model
        if predict_button:
            files = {'img': uploaded_file.getvalue()}

            response = requests.post(predict_url, files=files).json()

            print(f"RESPONSE FOR API FROM MODEL: {response}")
            print(response["Emotion"])
            #result = response.json()
            st.write("The emotion is ", response["Emotion"], "with probability", response["with probability of"])

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
