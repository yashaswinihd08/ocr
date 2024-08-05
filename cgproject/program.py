import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def select_image_file():
    # Open the file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif")]
    )
    return file_path

def perform_ocr(image_path): 
    # Open the selected image file
    img = Image.open(image_path)

    # Perform OCR using pytesseract
    ocr_result = pytesseract.image_to_string(img)

    return ocr_result

def save_text_to_file(text):
    # Open the file dialog to save the text file
    file_path = filedialog.asksaveasfilename(
        title="Save as",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text)
        messagebox.showinfo("Success", "Text has been saved to file.")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("OCR Image to Text")
    root.geometry("400x300")

    # Add a button to select an image file
    btn_select = tk.Button(root, text="Select Image", command=process_image)
    btn_select.pack(pady=20)

    root.mainloop()

def process_image():
    img_file = select_image_file()
    if img_file:
        ocr_result = perform_ocr(img_file)
        if ocr_result:
            save_text_to_file(ocr_result)
        else:
            messagebox.showwarning("Warning", "No text found in the image.")
    else:
        messagebox.showwarning("Warning", "No file selected.")

if __name__ == "__main__":
    main()
