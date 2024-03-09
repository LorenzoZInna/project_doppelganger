import streamlit as st

# Set up the Streamlit app
st.title('Project Doppelganger')
st.subheader('How are you feeling today?')
st.write('Select an emotion from the dropdown menu and click the button to save your input.')

# Display a centered image slot with a larger image
st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <div style="text-align: center;">
            <img src="https://media.istockphoto.com/id/1328201960/vector/two-theater-masks-comedy-and-drama-symbol.jpg?s=612x612&w=0&k=20&c=jsmOqB1ojCFrMCvpWmpwlwKetm2zFdaM_4_RfkhHZCc=" style="width: 350px;">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Create a dropdown menu for selecting emotions
emotions = ['Very Sad', 'Sad', 'Neutral', 'Happy', 'Very Happy']
selected_emotion = st.selectbox('Select your emotion:', emotions)

# Add a button to save the selected emotion to a CSV file
if st.button('Save Emotion'):
    # Save the selected emotion to a CSV file (you can implement this logic here)

    # Confirmation message
    st.success('Emotion saved successfully!')

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
