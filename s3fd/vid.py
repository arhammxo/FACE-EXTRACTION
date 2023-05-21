# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("C:\\Users\\Arham\\Desktop\\work\\FACE-ANNOTATOR\\s3fd\\videoplayback.mp4")
fps = cam.get(cv2.CAP_PROP_FPS)

print(fps)

try:
	
	# creating a folder named data
	if not os.path.exists('frames'):
		os.makedirs('frames')

# if not created then raise error
except OSError:
	print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):
	
	# reading from frame
	ret,frame = cam.read()

	if ret:
		if (currentframe%fps) == 0:
			# if video is still left continue creating images
			name = './frames/' + str(currentframe) + '.jpg'
			print ('Creating...' + name)

			# writing the extracted images
			cv2.imwrite(name, frame)
			#cv2.imwrite(os.path.join(path, name), frame)
			# increasing counter so that it will
			# show how many frames are created
		currentframe += 1
	else:
		break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
