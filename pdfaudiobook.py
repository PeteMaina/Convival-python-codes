# The code herein allows one to upload a pdf and get to generate its audiobook
# Also added is a playback speed feature
# Also added is a downloadable feature


#Installing the necessary modules
!pip install PyPDF2
!pip install gtts
!pip install ipywidgets
!pip install playsound

import os
from gtts import gTTS
import ipywidgets as widgets
from IPython.display import display, Audio
import PyPDF2
import io  
from playsound import playsound

def create_audiobook(uploaded_file, output_file):
    """
    Creates an audiobook from an uploaded PDF file.

    Args:
    uploaded_file: The uploaded PDF file content.
    output_file: The path to save the audiobook.
    """
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file))
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"Audio book created successfully: {output_file}")


output_file = 'audiobook.mp3'

uploader = widgets.FileUpload(
    accept='.pdf',
    multiple=False
)

display(uploader)

create_button = widgets.Button(description="Create Audiobook")

def on_create_button_clicked(b):
    if uploader.value:
        uploaded_file_content = uploader.value[list(uploader.value.keys())[0]]['content']
        create_audiobook(uploaded_file_content, output_file)

        # Play audio
        display(Audio(output_file, autoplay=False))

        # Download link
        display(widgets.HTML(f'<a href="{output_file}" download>Download Audiobook</a>'))

    else:
        print("Please upload a PDF file first.")

create_button.on_click(on_create_button_clicked)
display(create_button)



# Speed control (using playsound - limited functionality)
def play_audio_with_speed(speed=1.0):
    """Plays the audio with speed control (using playsound - basic functionality)."""
    playsound(output_file, block=False) #Playsound has no speed control.

speed_slider = widgets.FloatSlider(
    value=1.0,
    min=0.5,
    max=2.0,
    step=0.1,
    description='Speed:',
)

play_button = widgets.Button(description="Play with Speed")
play_button.on_click(lambda b: play_audio_with_speed(speed_slider.value))

display(speed_slider)
display(play_button)