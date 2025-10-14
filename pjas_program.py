import time
import argparse
import csv
import datetime
import imutils
import cv2
from imutils.video import VideoStream
import os
from debug import Debug # type: ignore
avg = None
motionCounter = 0
minarea = 1000
delta_thresh = 5
info = 0
loopcount = 0
countaverage = 0
bbaverage = 0

csvfile = open('wether_data.csv', 'a')

dbg = Debug()
ap = argparse.ArgumentParser()

dbg.INFO('Intilized')

ap.add_argument('-g', '-goof', action='store_true', help='how to goof off and test')
ap.add_argument('-n', type=int, help='put a number here')
ap.add_argument('-t', '-title', type=str, default='PJAS Camera Feed', help='camera feed title')
args = ap.parse_args()

dbg.INFO('Set up arguments')

csvfileWriter = csv.DictWriter(csvfile, ['Time', 'Number of drops per frame'])
#csvfileWriter.writeheader()

# Kept as refrence
"""if args.g and args.n:
    for i in range(args.n):
        print('SPAM', i+1)
elif args.g:
    print('SPAM')
elif args.n:
    print('add -g!!')"""
    
cam = cv2.VideoCapture(2) #webcam is 0, Logitech is 2, Freetalk is 4

if not cam.isOpened():
    print("Error: Could not open video device.")
    exit()

dbg.INFO('Succesfully set up camera')
dbg.INFO('Warming up camera...')
time.sleep(2.5)

#startTime = time.time()

while True:
    bbnum = 0
    ret, frame = cam.read()  # Read a frame from the camera

    if not ret:  # If reading the frame failed
        print("Error: Failed to read frame.")
        break
    
    if info == 0:
        dbg.INFO('Succesfully read camera frame')
    
    timestamp = datetime.datetime.now()
    text = "No"
 
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
	# if the average frame is None, initialize it
    if avg is None:
        dbg.INFO('Starting Background')
        avg = gray.copy().astype("float")
        continue
    
    cv2.accumulateWeighted(gray, avg, 0.5)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    thresh = cv2.threshold(frameDelta, delta_thresh, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    if info == 0:
        dbg.INFO('Succesfully grabbed countures')
    
    for c in cnts:
		# if the contour is too small, ignore it
        if cv2.contourArea(c) < minarea:
            continue
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Yes"
        bbnum += 1
	# draw the text and timestamp on the frame
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, "Rain?: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "bb per frame: {}".format(bbnum), (10, 50),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.35, (0, 0, 255), 1)
    
    #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timestamp = datetime.datetime.now().isoformat()
    
    if info == 0:
        dbg.INFO('Succesfully drew bounding boxes')

	# display the security feed
    cv2.imshow(args.t, frame)
    if info == 0:
        info = 1
        dbg.INFO('Displaying feed...')
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
    """bbaverage += bbnum
    
    if startTime > 1:
        countaverage = 0
        countaverage = round(bbaverage/round(time.time()-startTime, 2), 2)
        loopcount = -1
        bbaverage = 0
        startTime = time.time()"""
    if bbnum > 0:    
        csvfileWriter.writerow({'Time': timestamp, 'Number of drops per frame': bbnum})
    
    loopcount += 1
    
cam.release()
cv2.destroyAllWindows()
dbg.INFO('Ending program')