import numpy as np
import cv2

image = np.zeros((300, 300, 3), dtype=np.uint8)

size = 50
image[100:100+size, 100:100+size] = [255, 0, 0]
image[100:100+size, 150:150+size] = [0, 0, 255]


cv2.imshow("My Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()