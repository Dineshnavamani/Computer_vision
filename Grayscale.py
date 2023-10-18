import cv2
immport numpy as np
kernel = np.ones((5,5).uint8)
print(kernel)
path = "
img = cv2.imread(path)
imgGray =
cv2.cvtColor(img.cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(1)
cv2.deatroyALLWindows()
