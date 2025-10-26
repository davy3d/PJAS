import cv2
import datetime
from time import sleep


while True:
    
    # Access the default camera
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        
    else:
        # Capture a single frame
        ret, frame = cap.read()
        
        timestamp = datetime.datetime.now().isoformat()

        if ret:
            # Save the captured frame
            cv2.imwrite(f"image_{timestamp}.jpg", frame)
            print("Image saved as captured_image.jpg")
        else:
            print("Failed to capture image.")
            
        # Release the camera
        cap.release()
        sleep(30)
