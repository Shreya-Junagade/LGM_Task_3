
import cv2

import matplotlib.pyplot as plt
plt.show()

image = cv2.imread(r'C:\Users\User\Pictures\test.png')
cv2.imshow("original_image", image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#image inversion
inverted_image = 255 - gray_image

#create the pencil sketch by mixing the grayscale image with inverted blurry gray_image
blurred = cv2.GaussianBlur(inverted_image,(21,21),0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale = 256.0)

#output
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of test", pencil_sketch)

cv2.imwrite('test.png',pencil_sketch)
print("Image saved successfully:", pencil_sketch)
cv2.waitKey(0)