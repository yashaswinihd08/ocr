# OCR Image to Text

This project allows you to extract text from images using Optical Character Recognition (OCR) via the `pytesseract` library. The extracted text can then be saved to a text file.
The user interface is built with `tkinter`, a Python library for creating graphical user interfaces (GUIs).

## Features
- Select an image file (supports various formats like JPG, PNG, BMP, TIFF).
- Perform OCR to extract text from the image.
- Save the extracted text into a `.txt` file.
- Simple and intuitive GUI built with `tkinter`.

## Prerequisites

Before you can run this project, make sure you have the following installed:

- Python 3.x
- Tesseract-OCR (needed by `pytesseract` for OCR functionality)

### Install Python Libraries

You will need to install the required Python libraries. You can do this by running the following command:

```bash
pip install pytesseract Pillow
