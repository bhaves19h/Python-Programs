-----------------//img to text //------------------
install the tesseract in the .README

from PIL import Image
import pytesseract
import os

# Optional: Set Tesseract path if it's not in your system's PATH
# For Windows (only needed if tesseract is not recognized)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def extract_code_from_image(image_path):
    try:
        # Open the image
        image = Image.open(image_path)

        # Extract text using OCR
        extracted_text = pytesseract.image_to_string(image)

        return extracted_text

    except FileNotFoundError:
        return "❌ Error: Image file not found."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Example usage
image_path = "./image.png"  # Use forward slashes or raw string for Windows paths
code = extract_code_from_image(image_path)

# ✅ Step 3: Save the text to a .txt file
output_file = "img_converted.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(code)

print(f"✅ Extracted text saved to {output_file}")

print("🔍 Extracted Code:\n")
print(code)
print(output_file)
