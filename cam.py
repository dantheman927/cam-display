import imutils
import cv2
import tkinter as tk

# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)



root = tk.Tk()
root.withdraw()  # Hide the root window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
 




# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    frame = imutils.resize(frame, screen_width,screen_height)   # Display the resulting frame
    cv2.imshow('Smart-Mirror',frame)
 
    # Press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
 
# When everything done, release the video capture object
cap.release()
 
# Closes all windows
cv2.destroyAllWindows()