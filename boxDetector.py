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
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import Dropout
# from keras.layers import Flatten
# from keras.constraints import maxnorm
# from keras.optimizers import SGD
# from keras.layers.convolutional import Conv2D
# from keras.layers.convolutional import MaxPooling2D
# from keras.utils import np_utils


# def alternateModel():
#     # Create the model
#     model = Sequential()
#     model.add(Conv2D(32, (3, 3), input_shape=(720, 1080, 3), padding='same', activation='relu', kernel_constraint=maxnorm(3)))
#     model.add(Dropout(0.2))
#     model.add(Conv2D(32, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#     model.add(Flatten())
#     model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
#     model.add(Dropout(0.5))
#     model.add(Dense(4, activation='softmax'))
#     # Compile model
#     epochs = 100
#     lrate = 0.01
#     decay = lrate/epochs
#     sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
#     model.compile(loss='mean_squared_error', optimizer="adam", metrics=['accuracy'])
#     print(model.summary())
#     return model

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
    x = Dense(64)(merged)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)
    #Final output
    output = Dense(4, name="output")(x)
    boxModel = Model(input=[img], output=[output])
    boxModel.compile(optimizer="adam", loss="mean_squared_error")
    print(boxModel.summary())
    return boxModel

def trainModel(model, images, labels):
    model.fit(x=images, y=labels, batch_size=2, epochs=100, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
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

    labelArr = fd.getLabels()
    bm = model()
    # am = alternateModel()
    # print(bm)
    bm = trainModel(bm, imageArr, labelArr)
    #testModel(boxModel, )

main()
# if __name__ == '__main__':
#         # Parse the input arguments for common Cloud ML Engine options
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#       '--train-file',
#       help='Cloud Storage bucket or local path to training data')
#     parser.add_argument(
#       '--job-dir',
#       help='Cloud storage bucket to export the model and store temp files')
#     args = parser.parse_args()
#     arguments = args.__dict__
#     main(**arguments)
