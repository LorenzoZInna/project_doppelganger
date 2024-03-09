import streamlit as st
import pandas as pd

# Set up the Streamlit app
st.title('Project Doppelganger')
st.subheader('How are you feeling today?')
st.write('Select an emotion from the dropdown menu and click the button to save your input.')

# Create a dropdown menu for selecting emotions
emotions = ['Very Sad', 'Sad', 'Neutral', 'Happy', 'Very Happy']
selected_emotion = st.selectbox('Select your emotion:', emotions)

# Add a button to save the selected emotion to a CSV file
if st.button('Save Emotion'):
    # Create a DataFrame with the selected emotion
    df = pd.DataFrame({'Emotion': [selected_emotion]})
    
    # Save the DataFrame to a CSV file
    df.to_csv('user_emotions.csv', index=False)
    
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

