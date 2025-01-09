# The code herein allows one to upload anything(most items) and get to generate ithe QR code
# Also added is a text to qr code generating
!pip install qrcode
!pip install ipywidgets

import qrcode
import ipywidgets as widgets
from IPython.display import display, Image

# Function to generate and display QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Display the QR code image
    display(img)


# Text input for manual entry
text_input = widgets.Text(
    placeholder='Enter text here',
    description='Text:',
    disabled=False
)

# File upload for files
file_upload = widgets.FileUpload(
    accept='',  # Accept all file types
    multiple=False
)

# Button to trigger QR code generation
generate_button = widgets.Button(description="Generate QR Code")

# Function to handle button click
def on_generate_button_clicked(b):
    data = ""
    if text_input.value:
        data = text_input.value
    elif file_upload.value:
        # Get the content of the uploaded file
        uploaded_file_content = file_upload.value[list(file_upload.value.keys())[0]]['content']
        data = uploaded_file_content  # Use file content as data

    if data:
        generate_qr_code(data)
    else:
        print("Please enter text or upload a file.")


generate_button.on_click(on_generate_button_clicked)

# Display the widgets
display(text_input)
display(file_upload)
display(generate_button)
