import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])
    if file_path:
        load_and_display_image(file_path)

def load_and_display_image(file_path):
    pil_image = Image.open(file_path)
    numpy_image = np.array(pil_image)
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
    display_image(opencv_image)
    print("Numpy Array:")
    print(numpy_image)
    
def display_image(image):
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    photo = ImageTk.PhotoImage(pil_image)
    label.config(image=photo)
    label.image=photo

window = tk.Tk()
window.title("Image Viewer")
button = tk.Button(window, text='open Image', command=open_file)
button.pack(pady=10)
label = tk.Label(window)
label.pack()
window.mainloop()