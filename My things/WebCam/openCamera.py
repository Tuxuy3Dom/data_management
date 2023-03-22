import cv2

# Create camera object number 0
cap = cv2.VideoCapture(0)
# icon = cv2.imread("camera.jpg")

# window_name = "WebCam"
# title = "WebCam title"
# width = 920
# height = 640

# def open_window(window_name, width, height, title):
#     """ Open the display window """
#     # Create a named window and set its size
#     cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
#     cv2.resizeWindow(window_name, width, height)
#     cv2.setWindowTitle(window_name, title)


# Set the size of the camera window
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

# Adding an icon to the name of the camera window

# cv2.setWindowProperty('Camera', 920, 640)

# The main loop of the program
while True:
    # Read the frame from the camera
    ret, frame = cap.read()

    # Display the frame on the screen
    cv2.imshow('Camera', frame)

    # Check if a key has been pressed ESC
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# Realease the camera object and close the windows 
cap.release()
cv2.destroyAllWindows()