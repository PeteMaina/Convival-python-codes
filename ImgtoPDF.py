# Ever wanted to conver your images to a PDF file
# This snippet does the job till you're able to download the PDF

!pip install img2pdf

import img2pdf
import os
import ipywidgets as widgets
from IPython.display import display, HTML

# Create a file upload widget
uploader = widgets.FileUpload(
    accept='image/*',  # Accept all image types
    multiple=True  # Allow multiple files to be uploaded
)

# Display the upload widget
display(uploader)

# Create a button to trigger the PDF conversion
convert_button = widgets.Button(description="Convert to PDF")

# Function to handle button click and convert images to PDF
def on_convert_button_clicked(b):
    if uploader.value:
        # Get the uploaded file contents
        uploaded_file_contents = [uploader.value[key]['content'] for key in uploader.value]

        # Limit to a maximum of 10 images
        if len(uploaded_file_contents) > 10:
            print("Error: Maximum 10 images allowed.")
            return

        # Convert images to PDF
        try:
            pdf_bytes = img2pdf.convert(uploaded_file_contents)

            # Save the PDF to a file
            with open("output.pdf", "wb") as f:
                f.write(pdf_bytes)

            print("Images converted to PDF successfully!")

            # Create and display a download link
            download_link = HTML(f'<a href="output.pdf" download>Download PDF</a>')
            display(download_link)

        except Exception as e:
            print(f"An error occurred during conversion: {e}")
    else:
        print("Please upload image files first.")

# Link the button click event to the function
convert_button.on_click(on_convert_button_clicked)

# Display the convert button
display(convert_button)