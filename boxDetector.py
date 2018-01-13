import tensorflow as tf
import numpy as np
import matplotlib
from matplotlib.pyplot import imshow
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
#import cv2
from keras.utils import plot_model
import formatData as fd

def model():
    # Model with 3 hidden layers that takes in an image as an input
    # images for now are 1080 × 720
    img = Input(shape=(720, 1080, 3), name="img")
    # layer 1
    x = Convolution2D(8, 3, 3)(img)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    # layer 2
    x = Convolution2D(16, 3, 3)(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    #Convolution/Pooling Layer 3
    x = Convolution2D(32, 3, 3)(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    #Flattens into 1D array for Usage in final layer
    merged = Flatten()(x)
    #One final fully connected layer for figuring output values
    x = Dense(128)(merged)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)
    #Final output
    output = Dense(14, name="output")(x)
    boxModel = Model(input=[img], output=[output])
    boxModel.compile(optimizer="adam", loss="mean_squared_error")
    print(boxModel.summary())
    return boxModel

def trainModel(model, images, labels):
    model.fit(x=images, y=labels, batch_size=2, epochs=5, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = input("Trained model's name: ")
    modelName = modelName + ".h5"
    model.save(modelName)
    print("Model saved successfully as " + modelName)
    return model

def testModel(model, testX, testY):
    scores = model.evaluate(testX, testY)
    print("/nAccuracy: " + model.metrics_name[1], scores[1]*100)

def main():
    imagePath = "/images"
    labelsPath = "/labels"
    imageArr = fd.getTrainingImages("images")
    print("Image Shape: ")
    print(imageArr.shape)
    # g = input("")
    labelArr = fd.getLabels()
    bm = model()
    bm = trainModel(bm, imageArr, labelArr)
    #testModel(boxModel, )

main()
