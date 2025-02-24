
'''This code performs local/offline conversion of PDF documents to word(.docx)
    
    code written by Peter Maina
    All Rights reserved
    
    Email me : peterwahomemaina003@gmail.com'''

!pip install docx2txt
!pip install PyPDF2
!pip install ipywidgets
!pip install python-docx # Install python-docx

import docx2txt
import PyPDF2
import ipywidgets as widgets
from IPython.display import display, clear_output, Javascript
from io import BytesIO
import re

# Function to clean text for XML compatibility
def clean_text(text):
    """Removes invalid XML characters from text."""
    # Remove NULL bytes and control characters
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', text)
    # Replace non-Unicode characters with their Unicode equivalents
    text = text.encode('ascii', 'xmlcharrefreplace').decode('ascii')
    return text

# Function to convert PDF to Word
def pdf_to_word(pdf_file):
    """Converts a PDF file to a Word document (.docx)."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    text = ""
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # Clean the extracted text
    text = clean_text(text) # Call the clean_text function

    # Create a new Word document
    from docx import Document # Import Document here
    document = Document()
    document.add_paragraph(text)
    return document

# Function to handle file upload
def on_upload_change(change):
    global uploaded_file  # Make uploaded_file accessible
    if change['new']:
        # Get the first (and only) uploaded file's content
        uploaded_filename = next(iter(change['new']))
        uploaded_file_content = change['new'][uploaded_filename]['content'] 
        uploaded_file = BytesIO(uploaded_file_content)  # Store file content in BytesIO
        with output:
            clear_output(wait=True)
            print("File uploaded successfully!")

#handle convert button click
def on_convert_click(b):
    global uploaded_file  # Access uploaded_file
    if uploaded_file:
        try:
            word_doc = pdf_to_word(uploaded_file)  # Convert to Word
            with output:
                clear_output(wait=True)
                print("Conversion complete!")
            # Make download button visible
            download_button.layout.visibility = 'visible'
            # Store the Word document for download
            global word_doc_content
            word_doc_content = BytesIO()
            word_doc.save(word_doc_content)
            word_doc_content.seek(0)  # Reset file pointer
            # Get filename for download
            uploaded_filename = list(uploader.value)[0]  # Get the filename directly
            download_button.description = f"Download {uploaded_filename[:-4]}.docx"
        except Exception as e:
            with output:
                clear_output(wait=True)
                print(f"Error during conversion: {e}")
    else:
        with output:
            clear_output(wait=True)
            print("Please upload a PDF file first.")

# handle download button click
def on_download_click(b):
    global word_doc_content
    if word_doc_content:
        uploaded_filename = list(uploader.value)[0]
        download_button.description = f"Download {uploaded_filename[:-4]}.docx"
        with output:
            clear_output(wait=True)
            print("Downloading...")

        
        js_download = """
        var link = document.createElement('a');
        link.href = URL.createObjectURL(new Blob([new Uint8Array(%s)], {type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}));
        link.download = '%s';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        """ % (list(word_doc_content.getvalue()), f"{uploaded_filename[:-4]}.docx")

        # Execute the JavaScript to download the file
        display(Javascript(js_download))

# Create widgets
uploader = widgets.FileUpload(accept='.pdf', multiple=False)
convert_button = widgets.Button(description="Convert to Word")
download_button = widgets.Button(description="Download", layout=widgets.Layout(visibility='hidden'))
output = widgets.Output()

# event handlers
uploader.observe(on_upload_change, names='value')
convert_button.on_click(on_convert_click)
download_button.on_click(on_download_click)

# widgets
display(uploader)
display(convert_button)
display(download_button)
display(output)