import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\L1_Indiviual_Components\Image_Classifier")


script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the script's directory
model_path_mobilenet = os.path.join(script_dir, 'models', 'mobilenetLarge.keras')
model_path_resnet50 = os.path.join(script_dir, 'models', 'resnet50.keras')

def predict(file_path):

    decode_dict = {0 : 'cat' , 1 : 'cow' , 2 : 'dog' , 3 : 'hen' , 4 : 'snake' , 5 : 'squirrel'}
    model01 = load_model(model_path_mobilenet)
    model02 = load_model(model_path_resnet50)
    img = image.load_img(file_path, target_size=(224, 224))
            # Convert the image to a numpy array
    img_array = image.img_to_array(img)
        
        # Expand dimensions to match the input shape of the model (batch_size, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)
        
        # Preprocess the image (same as during model training)
    # img_array1 = pre1(img_array)
    img_array_resnet = preprocess_input(img_array)
    img_array_mobilenet = img_array / 255.0
        
        # Make predictions
    predictions1 = model01.predict(img_array_mobilenet)
    predictions2 = model02.predict(img_array_resnet)
    predicted_class1 = np.argmax(predictions1, axis=1)[0]
    predicted_class2 = np.argmax(predictions2, axis=1)[0]
    print(decode_dict[predicted_class1] , ' ' , decode_dict[predicted_class2])
    # print(predictions1 , ' ' , predictions2)

    return decode_dict[predicted_class1] ,  decode_dict[predicted_class2]

    # label01 = model01.predict(img_array)
    # label02 = model02.predict(img_array)

    # label01 = model01.predict(img_array)
    # label02 = model02.predict(img_array)


def Image_Classification():
    print("working image")
    # open-file dialog
    filetypes = (
    ('All image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff'),
    ('PNG files', '*.png'),
    ('JPEG files', '*.jpg;*.jpeg'),
    ('BMP files', '*.bmp'),
    ('GIF files', '*.gif'),
    ('TIFF files', '*.tiff')
    )
    root = tk.Tk()
    filename = tk.filedialog.askopenfilename(
        title='Select a file...',
    filetypes=filetypes,)
    root.destroy()
    print(filename)
    predict(filename)


if __name__ == "__main__":
    Image_Classification()

