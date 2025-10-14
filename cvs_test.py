import cv2

cam = cv2.VideoCapture(4)#webcam is 0, Logitech is 2, Freetalk is 4

if not cam.isOpened():
    print("Error: Could not open video device.")
    exit()
    
while True:
    ret, frame = cam.read()  # Read a frame from the camera

    if not ret:  # If reading the frame failed
        print("Error: Failed to read frame.")
        break

    cv2.imshow('PJAS', frame)  # Display the frame in a window

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break
    
cam.release()
cv2.destroyAllWindows()