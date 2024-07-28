from tensorflow.keras.models import load_model
import sys
import os
import tkinter as tk
from tkinter import filedialog
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\L1_Indiviual_Components\Sound_Classifier")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\L1_Indiviual_Components\Image_Classifier")ss
import image_main , sound_main

def Image_Classification():
    print("working sound")
    # open-file dialog
    filetypes = (
    ('PNG files', '*.PNG'),
    )
    root = tk.Tk()
    filename = tk.filedialog.askopenfilename(
        title='Select a file...',
    filetypes=filetypes,)
    root.destroy()
    print(filename)
    image_main.predict(filename)

def Sound_Classification():
    print("working sound")
    # open-file dialog
    filetypes = (
    ('MP4 files', '*.MP4'),
    ('WAV files', '*.WAV'),
    )
    root = tk.Tk()
    filename = tk.filedialog.askopenfilename(
        title='Select a file...',
    filetypes=filetypes,)
    root.destroy()
    print(filename)
    sound_main.predict(filename)


if __name__ == "__main__":
    print("\t\t\t\t\t\tImage & Sound Classification")
    print("Please Select")
    print("\n")
    choose = int(input("1.Image Classification\n2.Sound Classification"))

    if choose == 1:
        Image_Classification()
    else:
        Sound_Classification()



