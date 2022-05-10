import numpy as np
import cv2

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# define a video capture object
vid = cv2.VideoCapture(0)
i = 0
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    pressed_key = cv2.waitKey(1)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if pressed_key & 0xFF == ord('q'):
        break
    elif pressed_key & 0xFF == ord('s'):
        cv2.imwrite('gray_camera_' + str(i) + '.jpg', frame)
        i += 1

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)

        # If found, add object points, image points (after refining them)
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners)
            # Draw and display the corners
            cv2.drawChessboardCorners(gray, (9, 6), corners2, ret)

            # print(gray.shape[::-1])
            # ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1])
            # print('Matrix and Distortion', mtx, dist)

    cv2.imshow('img', gray)

cv2.destroyAllWindows()