import cv2

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_36h10)

# define a video capture object
vid = cv2.VideoCapture(0)

while True:

    # capture the video frame
    # by frame
    ret, frame = vid.read()

    image_copy = frame.copy()

    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, dictionary)

    if ids is not None and len(ids) > 0:
        cv2.aruco.drawDetectedMarkers(image_copy, corners, ids)
        # Display the resulting frame
        cv2.imshow('frame', image_copy)
    else:
        cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()