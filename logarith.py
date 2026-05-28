import cv2
import math

image = cv2.imread("cat.jpeg")

print(image.shape, type(image.shape))
print(image)
print(type(image))

def preprocessing(image):
    print("start gray...")
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i][j]
            gray = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3
            pixel[0] = pixel[1] = pixel[2] = gray
    print("finish gray.")

preprocessing(image)

def logarith(c, r):
    s = c*math.log(1+r/255)*255
    if s > 255:
        s = 255
    return s

cv2.imwrite("gray.jpg", image)
print("saved gray")

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixel = image[i][j]
        s = logarith(1, pixel[0])
        pixel[0] = pixel[1] = pixel[2] = s

cv2.imwrite("logarith.jpg", image)
print("saved logarith")