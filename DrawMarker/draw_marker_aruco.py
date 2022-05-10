import cv2

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
marker_size_t = 144
markerImage = cv2.aruco.drawMarker(dictionary, 23, marker_size_t, 1)
cv2.imwrite(f"aruco_marker_23_{marker_size_t}.png", markerImage)