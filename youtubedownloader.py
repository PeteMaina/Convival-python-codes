# Ever wanted a youtube downloader on your machine without ads
# This snippet does the job both in mp3 and mp4 alias video
!pip install pytube

from pytube import YouTube
import ipywidgets as widgets
from IPython.display import display

# Function to download the video/audio
def download_youtube_content(url, file_type):
    try:
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")

        if file_type == "mp3":
            # Download audio (320kbps)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(filename=f"{yt.title}.mp3")  # You can customize the filename here
            print("Audio downloaded successfully!")
        elif file_type == "video":
            # Download video (1080p)
            video_stream = yt.streams.filter(res="1080p").first()
            if video_stream:
                video_stream.download(filename=f"{yt.title}.mp4")  # You can customize the filename here
                print("Video downloaded successfully!")
            else:
                print("1080p video not available. Downloading the highest available resolution.")
                yt.streams.get_highest_resolution().download(filename=f"{yt.title}.mp4")
        else:
            print("Invalid file type selected.")

    except Exception as e:
        print(f"An error occurred: contact Pete")


# Create input widgets
url_input = widgets.Text(
    placeholder='Enter YouTube URL',
    description='URL:',
    disabled=False
)

file_type_dropdown = widgets.Dropdown(
    options=['mp3', 'video'],
    value='mp3',
    description='File Type:',
    disabled=False,
)

download_button = widgets.Button(description="Download")

# Function to handle button click
def on_download_button_clicked(b):
    url = url_input.value
    file_type = file_type_dropdown.value
    download_youtube_content(url, file_type)

download_button.on_click(on_download_button_clicked)

# Display the widgets
display(url_input)
display(file_type_dropdown)
display(download_button)