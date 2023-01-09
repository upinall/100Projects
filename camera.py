import cv2 # import openCV

# define video output variable.

vid = cv2.VideoCapture(1) # the one signifies which camera to utilize. (0 for first camera, 1 for second camera, 2, 3 and so on.)

i = 0 # frame counter

while(True): # start the live feed
    
    ret, frame = vid.read()
  
    # Display the feed to a window
    cv2.imshow('frame', frame)
    
    i += 1 # add to frame counter
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    # when clicked it should save the current frame then close the program.
    if cv2.waitKey(1) & 0xFF == ord('s'): cv2.imwrite('Frame'+str(i)+'.jpg', frame) # switched to take picture every time s is hit.
    elif cv2.waitKey(1) & 0xFF == ord('q'): break # close program when q is hit.
  
# After loop release all hardware and software resources to avoid issues with other programs using camera
vid.release()
# Close/Destroy the windows
cv2.destroyAllWindows()


'''
Camera Utility by Ernesto Aguilera @ Southwire

Welcome to this silly one shot camera tool! This was created to experiment with opencv and if it was possible to make a camera that can take live feed and take pictures.

No bugtesting/cleaning was done to this program and only shared to be used with other tools.

Read comments to learn about how the program runs only opencv is needed to run the program.

What to do externally: From this point make it able to return the path for other programs to take the camera output (for other programs)

'''
