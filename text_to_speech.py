import io
import pygame
from gtts import gTTS

def speak(text):
    with io.BytesIO() as file:
        tts = gTTS(text=text, lang="en")
        tts.write_to_fp(file)
        file.seek(0)  # Reset file pointer to the beginning
        
        pygame.mixer.init()
        pygame.mixer.music.load(file, "mp3")  # Specify format
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.delay(100)  # Pause execution while audio plays

if __name__ == '__main__':
    print("What should I say?")
    text = input("  >> ")
    speak(text)
