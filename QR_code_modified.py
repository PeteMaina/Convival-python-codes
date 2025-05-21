# Install required packages
!pip install qrcode[pil] pillow

import qrcode
from PIL import Image
import io
from IPython.display import display, Image as IPyImage
import ipywidgets as widgets
from google.colab import files

# === Input Widgets ===

# Text to encode
data_input = widgets.Textarea(
    value='https://example.com',
    placeholder='Enter text, link, or any data...',
    description='Data:',
    layout=widgets.Layout(width='100%', height='100px')
)

# Foreground color
fg_color = widgets.ColorPicker(
    concise=False,
    description='FG Color:',
    value='#000000'
)

# Background color
bg_color = widgets.ColorPicker(
    concise=False,
    description='BG Color:',
    value='#ffffff'
)

# Icon upload
icon_uploader = widgets.FileUpload(
    accept='.png',
    multiple=False,
    description='Upload Icon'
)

# Output file name
filename_input = widgets.Text(
    value='my_qrcode.png',
    placeholder='Filename (e.g. qrcode.png)',
    description='Save As:',
    layout=widgets.Layout(width='50%')
)

# Generate button
generate_btn = widgets.Button(description="Generate QR Code", button_style='success')

# Display widgets
display(data_input, fg_color, bg_color, icon_uploader, filename_input, generate_btn)

# === QR Generation Function ===

def generate_qr_code(b):
    data = data_input.value.strip()
    fg = fg_color.value
    bg = bg_color.value
    file_name = filename_input.value.strip()

    if not data or not file_name:
        print("❌ Please provide both data and a file name.")
        return

    # Create QR code
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fg, back_color=bg).convert("RGB")

    # Embed icon if provided
    if icon_uploader.value:
        try:
            icon_info = list(icon_uploader.value.values())[0]
            icon_bytes = io.BytesIO(icon_info['content'])
            icon = Image.open(icon_bytes)

            qr_width, qr_height = qr_img.size
            factor = 4
            icon_size = (qr_width // factor, qr_height // factor)
            icon = icon.resize(icon_size, Image.LANCZOS)

            pos = ((qr_width - icon_size[0]) // 2, (qr_height - icon_size[1]) // 2)
            qr_img.paste(icon, pos, mask=icon if icon.mode == 'RGBA' else None)
        except Exception as e:
            print("⚠️ Failed to insert icon:", e)

    # Save and display
    qr_img.save(file_name)
    display(IPyImage(file_name))
    files.download(file_name)

# Bind button click
generate_btn.on_click(generate_qr_code)
