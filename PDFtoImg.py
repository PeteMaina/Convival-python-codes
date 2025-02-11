# Ever wanted to convert your PDF to a Image/s file
# This snippet does the job download the Image/s too.
# Email : peterwahomemaina003@gmail.com | Whatsapp : +254794797796

!pip install PyPDF2
!pip install ipywidgets

import PyPDF2
import io
import ipywidgets as widgets
from IPython.display import display, HTML

# Create a file upload widget for PDF files
pdf_uploader = widgets.FileUpload(
    accept='.pdf',  # Accept only PDF files
    multiple=False  # Allow only one file to be uploaded
)

# Display the upload widget
display(pdf_uploader)

# Create a button to trigger the PDF conversion
convert_button = widgets.Button(description="Convert to PDF")

# Display the convert button
display(convert_button)

# Function to handle button click and convert images to PDF
def on_convert_button_clicked(b):
    if pdf_uploader.value:  # Check if a file has been uploaded
        # Access the uploaded file content
        # Get the key of the uploaded file (there should be only one since multiple=False)
        uploaded_file_key = list(pdf_uploader.value.keys())[0] 
        uploaded_pdf_content = pdf_uploader.value[uploaded_file_key]['content'] # Get the content

        # Open the PDF file using PyPDF2
        with io.BytesIO(uploaded_pdf_content) as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Extract images from each page
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                for image_num, image in enumerate(page.images):
                    try:
                        # Extract image data
                        image_data = image.data
                        image_name = f"page_{page_num + 1}_image_{image_num + 1}.{image.name.split('.')[-1]}"

                        # Save the image to a file
                        with open(image_name, "wb") as f:
                            f.write(image_data)

                        # Create and display a download link for the image
                        download_link = HTML(f'<a href="{image_name}" download>Download {image_name}</a>')
                        display(download_link)
                    except PyPDF2.errors.PdfReadError as e:
                        print(f"Error extracting image on page {page_num + 1}, image {image_num + 1}: {e}")
                        # You might want to log the error or handle it differently
                        continue  # Skip to the next image

            print("PDF conversion completed. Some images may have been skipped due to errors.")

    else:
        print("Please upload a PDF file first.")

# Link the button click event to the function
convert_button.on_click(on_convert_button_clicked)