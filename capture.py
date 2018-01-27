import cv2
import sys
print("Using opencv version: " + str(cv2.__version__))

camera = cv2.VideoCapture(1)
camera.set(3, 540)
camera.set(4, 360)

#camera.set(CAP_PROP_FRAME_WIDTH,540);
#camera.set(CAP_PROP_FRAME_HEIGHT,360);
#camera.open()

print("Camera is opened: " + str(camera.isOpened))

#count = 0

def capture(countStart):
	count = countStart
	ret, frame = camera.read()
	
	while 1:
		inp = input("Press q to quit or any key to capture.")
		ret, frame = camera.read()
		
		if input == 'q':
			break
		print("images/"+(str(count).zfill(5))+'.png')
		cv2.imwrite("images/"+(str(count)+'.png').zfill(5), frame)
		count+=1;

	camera.release()
	cv2.destroyAllWindows()
	
capture(631)