import os
import argparse
import imutils
import time
import cv2
import os
from debug import Debug

dbg = Debug()

# initialize a dictionary that maps the name of the haar cascades to
# their filenames
detectorPaths = {
	"face": "haarcascade_frontalface_default.xml",
	"face1": "haarcascade_profileface.xml",
	"face2": "haarcascade_frontalface_alt2.xml",
}

print("[INFO] loading haar cascades...")
detectors = {}
# loop over our detector paths
for (name, path) in detectorPaths.items():
	# load the haar cascade from disk and store it in the detectors
	# dictionary
    path = os.path.sep.join(['/home/xtreme/PJAS/haar_cascades_ex', path])
    detectors[name] = cv2.CascadeClassifier(path)
 
 # initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")

cam = cv2.VideoCapture(0) #webcam is 0, Logitech is 2, Freetalk is 4

if not cam.isOpened():
    print("Error: Could not open video device.")
    exit()
    
time.sleep(2.0)
# loop over the frames from the video stream
while True:
    # grab the frame from the video stream, resize it, and convert it
    # to grayscale
    ret, frame = cam.read()  # Read a frame from the camera
    
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# perform face detection using the appropriate haar cascade
    faceRects = detectors["face"].detectMultiScale(
		gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

    	# loop over the face bounding boxes
    for (fX, fY, fW, fH) in faceRects:
        
		# draw the face bounding box on the frame
        cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH),
			(0, 255, 0), 2)

    	# show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    

# do a bit of cleanup
cv2.destroyAllWindows()
cam.release()