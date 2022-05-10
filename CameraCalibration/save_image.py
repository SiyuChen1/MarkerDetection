import numpy as np
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)
i = 0
while True:
    # Capture the video frame by frame
    ret, frame = vid.read()

    pressed_key = cv2.waitKey(1)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if pressed_key & 0xFF == ord('q'):
        break
    elif pressed_key & 0xFF == ord('s'):
        cv2.imwrite('data/chessboard_' + str(i) + '.jpg', frame)
        i += 1

    cv2.imshow('img', frame)

cv2.destroyAllWindows()