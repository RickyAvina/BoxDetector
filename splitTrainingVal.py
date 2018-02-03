import os
import shutil

# Requires images to have the same name as labels
# This version uses 5 digits: ex. 00043.png, but you can change that with numDigits

rootdir = "/home/isaac/Downloads/cubes2/"
imagesDir = rootdir+"images"
labelsDir = rootdir+"labels"
testImagesDir = rootdir + "testImages/"
testLabelsDir = rootdir + "testLabels/"

numDigits = 5

if not os.path.exists(testImagesDir):
	os.makedirs(testImagesDir)
if not os.path.exists(testLabelsDir):
	os.makedirs(testLabelsDir)
	
count = 0
for f in os.listdir(labelsDir):
	if count % 4==0: # move every 4 files
		shutil.move(imagesDir + "/" + str(f[:-4]).zfill(numDigits) + ".png", testImagesDir)
		shutil.move(labelsDir + "/" + str(f[:-4]).zfill(numDigits) + ".txt", testLabelsDir)
	count+=1

print("Finished splitting data\nTest Image Length: " + str(len(os.listdir(testImagesDir))) + "\nTest Label Length: " + str(len(os.listdir(testLabelsDir))))
