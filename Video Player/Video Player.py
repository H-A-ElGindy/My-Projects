import cv2  

# video resized for 1920 * 1080 (my screen) , you can adjust width and height as desired
cap = cv2.VideoCapture("your video")  
desired_width = 1920 
desired_height = 1080 

while cap.isOpened():  
    ret, frame = cap.read()  
    if not ret:  
        break 
    resized_frame = cv2.resize(frame, (desired_width, desired_height), interpolation=cv2.INTER_AREA)  
    
    # Display the frame  
    cv2.imshow('Video Playback', resized_frame) 
    # press q to close 
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
cap.release()  
cv2.destroyAllWindows()  