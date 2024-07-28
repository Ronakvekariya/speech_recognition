import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

def predict(file_path , img_size = (128,512)):
<<<<<<< HEAD
    model01 = load_model('resnet_50.keras')
=======
    # model01 = load_model('resnet_50.ker/as')
>>>>>>> 8a958cf38a2e5a34994a64582ec1402c5e724c18
    # model02 = load_model('manual_cnn.keras')
    img = Image.open(file_path)
    img = img.resize(img_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    print(img_array)

<<<<<<< HEAD
    label01 = model01.predict(img_array)
=======
    # label01 = model01.predict(img_array)
>>>>>>> 8a958cf38a2e5a34994a64582ec1402c5e724c18
    # label02 = model02.predict(img_array)





