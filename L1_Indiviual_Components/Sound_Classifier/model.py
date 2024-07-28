import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer , Dense , MaxPooling2D , Flatten , BatchNormalization , Dropout , Input , Conv2D

from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.optimizers import Adam


def model_manual(num_class) :
    inp = Input(shape=(128,512,3) , name = 'input_image')

    # first layer
    c1 = Conv2D(16 , (3,3) , activation='relu')(inp)
    m1 = MaxPooling2D(64 , (2,2) , padding='same')(c1)

    # second layer
    c2 = Conv2D(32 , (3,3) , activation= 'relu')(m1)
    m2 = MaxPooling2D(64 , (2,2) , padding = 'same')(c2)

    # layer three
    c3 = Conv2D(128 , (4,4) , activation= 'relu')(m2)
    m3 = MaxPooling2D(64 , (2,2) , padding = 'same')(c3)

    # final embedding block
    c4 = Conv2D(256 , (4,4) , activation= 'relu')(m3)
    f1 = Flatten()(c4)
    d1 = Dense(128 , activation= 'relu')(f1)
    d2 = Dense(64 , activation= 'relu')(d1)
    d3 = Dense(num_class , activation= 'relu')(d2)


    return Model(inputs = [inp]  ,outputs = [d3] , name = 'sound_classifier_manual')


def model_transfer_learning_restnet_50(num_classes):
    base_model = ResNet50(weights='imagenet', include_top=False)

    # Add custom layers on top of the base model
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    output = Dense(num_classes, activation='softmax')(x)  # Adjust num_classes to your task
    
    # This is the model we will train
    model = Model(inputs=base_model.input, outputs = output , name = 'sound_classifier_restnet_50')

    # First: train only the top layers (which were randomly initialized)
    # i.e. freeze all convolutional ResNet layers
    for layer in base_model.layers:
        layer.trainable = False

    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    return model