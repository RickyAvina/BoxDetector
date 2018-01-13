import numpy as np
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
# from helperFunctions import imageToPixels
from keras.utils import plot_model
import keras
import time
from PIL import Image, ImageDraw
# import cv2
from os.path import expanduser
import h5py
import os
import sys
from formatData import getTrainingImages
import glob

imageModel = load_model(os.getcwd()+"/mostCurrent.h5")

def inferBoundingBox(testDirName):
    imagePixelLists = getTrainingImages(testDirName)
    output = imageModel.predict(imagePixelLists, batch_size=2, verbose=2)
    try:
        print("Hello")
        print("Image: " + str(output))
        return output
    except:
        pass
    return 0

def showResultForImage(number):
    base = Image.open(os.getcwd()+"/images/"+str(number)+".jpg").convert('RGBA')
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt, "RGBA")

    csvfile = open(os.getcwd()+"/csvout/output.csv",'r')
    csvFileArray = []
    for row in csv.reader(csvfile):
        csvFileArray.append(row)

    coor = csvFileArray[0]
    draw.rectangle(((float(coor[0]), float(coor[1])), (float(coor[2]), float(coor[3]))), fill=(200,60,40,200))
    outp = Image.alpha_composite(base, txt)
    print(outp)
    outp.show()

out = inferBoundingBox(os.getcwd()+"/images/")

import csv
with open(os.getcwd()+"/csvout/output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(out)

showResultForImage(1)
showResultForImage(2)
showResultForImage(3)
showResultForImage(4)
showResultForImage(5)
