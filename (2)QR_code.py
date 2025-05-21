!pip install qrcode[pil] pillow

import qrcode
from PIL import Image, ImageDraw
import io
from IPython.display import display, Image as IPyImage
import ipywidgets as widgets
from google.colab import files

# === Widgets ===
data_input = widgets.Textarea(
    value='https://example.com',
    placeholder='Enter any data...',
    description='Data:',
    layout=widgets.Layout(width='100%', height='100px')
)

fg_color1 = widgets.ColorPicker(description='Primary FG:', value='#000000')
fg_color2 = widgets.ColorPicker(description='Secondary FG:', value='#ff0000')
bg_color = widgets.ColorPicker(description='BG Color:', value='#ffffff')

icon_uploader = widgets.FileUpload(
    accept='.png',
    multiple=False,
    description='Upload Icon'
)

filename_input = widgets.Text(
    value='modern_qr.png',
    placeholder='Output file name',
    description='Save As:',
    layout=widgets.Layout(width='50%')
)

generate_btn = widgets.Button(description="Generate QR Code", button_style='success')

# Display all inputs
display(data_input, fg_color1, fg_color2, bg_color, icon_uploader, filename_input, generate_btn)

# === Function to generate QR code ===

def generate_qr_code(b):
    data = data_input.value.strip()
    fg1 = fg_color1.value
    fg2 = fg_color2.value
    bg = bg_color.value
    file_name = filename_input.value.strip()

    if not data or not file_name:
        print("❌ Please provide both data and filename.")
        return

    # Generate QR matrix
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    box_size = 10
    border = 4
    qr_size = (len(matrix) + border * 2) * box_size
    img = Image.new("RGB", (qr_size, qr_size), bg)
    draw = ImageDraw.Draw(img)

    # Center icon settings
    icon = None
    icon_size = (qr_size // 5, qr_size // 5)
    icon_padding = 8
    center_start = (qr_size - icon_size[0]) // 2 - icon_padding
    center_end = (qr_size + icon_size[0]) // 2 + icon_padding

    # Draw QR code using alternating colors
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val:
                x = (c + border) * box_size
                y = (r + border) * box_size
                # Skip if inside icon safe area
                if center_start <= x <= center_end and center_start <= y <= center_end:
                    continue
                color = fg1 if (r + c) % 2 == 0 else fg2
                draw.rectangle([x, y, x + box_size - 1, y + box_size - 1], fill=color)

    # Paste icon in center with proper size and transparency
    if icon_uploader.value:
        try:
            icon_info = list(icon_uploader.value.values())[0]
            icon_bytes = io.BytesIO(icon_info['content'])
            icon = Image.open(icon_bytes).convert("RGBA")

            icon = icon.resize(icon_size, Image.LANCZOS)

            # Clear area for icon
            mask = Image.new("RGB", icon.size, bg)
            img.paste(mask, ((qr_size - icon.size[0]) // 2, (qr_size - icon.size[1]) // 2))

            # Paste icon with transparency
            img.paste(icon, ((qr_size - icon.size[0]) // 2, (qr_size - icon.size[1]) // 2), icon)
        except Exception as e:
            print("⚠️ Failed to insert icon:", e)

    # Save and output
    img.save(file_name)
    display(IPyImage(file_name))
    files.download(file_name)

# Button event
generate_btn.on_click(generate_qr_code)
