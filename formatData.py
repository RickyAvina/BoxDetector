from PIL import Image
import numpy as np
import glob
import os
import sys

cwd = os.getcwd()

def getTrainingImages(p):
    #Parses the filepath to access files
    print("Starting to get Training images...")
    if p.startswith("/"):
        if p.endswith("/"):
            path = p
        else :
            path = p + "/"
    else:
        if p.endswith("/"):
            path = os.getcwd() + "/" + p
        else:
            path = os.getcwd() + "/" + p + "/"

    print("Path: " + path)
    pixelList = []

    for f in glob.glob(path+"*.jpg"):
        im = Image.open(f)
        # print("GOT HERE")
        pixelArray = imageToPixels(im)
        pixelArray = np.array(pixelArray)
        # print("PSHAPE")
        # print(pixelArray.shape)
        # meme = input()
        pixelList.append(pixelArray)
        #print(pixelArray[0][0])

    pixelList = np.array(pixelList)
    print("SHAPE")
    print(pixelList.shape)
    return pixelList

def imageToPixels(image):
    #Resizes the image and extracts pixels
    #resize = image.resize((672, 376), Image.NEAREST)
    img = np.array(image)
    return img

def getLabels():
    labelArr = []

    for g in glob.glob("labels/*.txt"):
        f = open(g, 'r').read()
        f = f[:-1]
        f = f.split(' ')
        f = f[4:8]
        labelArr.append(f)

    labelArr = np.array(labelArr)
    print(labelArr.shape)
    return labelArr

#getTrainingImages("images")
getLabels()
