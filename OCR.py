# this code is a simple OCR (Optical Character Recognition) tool 

# that captures a screenshot of the user's screen and extracts text from it

#  using the Tesseract OCR engine. The user is prompted to take a screenshot after a 3-second delay,

#  and the extracted text is displayed in the console. 

# The code uses the pyautogui library for taking screenshots and the pytesseract library for text extraction. 

# The PIL (Pillow) library is used to handle image files.

!pip install pyautogui
!pip install pytesseract
!pip install pillow

# copyright (c) 2025 by Peter Maina peterwahomemaina003@gmail.com

import pyautogui
import pytesseract
from PIL import Image
import time

# Set up Tesseract (For Windows, change the path if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_screenshot():
    print("📸 Taking screenshot in 3 seconds... Get ready!")
    time.sleep(3)
    
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("✅ Screenshot saved as 'screenshot.png'")

def extract_text():
    print("🔍 Extracting text from the screenshot...")
    image = Image.open("screenshot.png")
    text = pytesseract.image_to_string(image)
    
    if text.strip():
        print("\n📜 Extracted Text:\n")
        print(text)
    else:
        print("❌ No text found in the image.")

def main():
    capture_screenshot()
    extract_text()

if __name__ == "__main__":
    main()


