# for run this code "streamlit run app_text_to_speech.py" enter in terminal
import io
import pygame
import streamlit as st
from gtts import gTTS

# Function to convert text to speech
def speak(text):
    with io.BytesIO() as file:
        tts = gTTS(text=text, lang="en")
        tts.write_to_fp(file)
        file.seek(0)  # Reset file pointer

        pygame.mixer.init()
        pygame.mixer.music.load(file, "mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.delay(100)  # Wait until audio finishes playing

# Streamlit UI
st.title("🗣️ Text-to-Speech Web App")
st.write("Enter text below and click the button to hear it.")

# User input
text = st.text_area("Enter text:", "")

# Button to trigger speech
if st.button("Speak"):
    if text.strip():
        speak(text)
        st.success("Playing the speech...")
    else:
        st.warning("Please enter some text before clicking 'Speak'.")

