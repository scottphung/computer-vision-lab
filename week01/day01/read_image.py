import cv2

image = cv2.imread("HEHEH.jpg")

crop = image[120:720, 350:900].copy()
crop[:, :] = [0, 0, 255]

print(crop.shape)
print(image.dtype)

cv2.imshow("Original", image)
cv2.imshow("Crop", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()