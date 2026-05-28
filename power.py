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

def power(c, gamma, r):
    if r == 0:
        return 0
    
    s = c*math.pow(r/255, gamma)*255
    
    if s > 255:
        s = 255
    return s

cv2.imwrite("gray.jpg", image)
print("saved gray")

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixel = image[i][j]
        s = power(1, 0.67, pixel[0])
        pixel[0] = pixel[1] = pixel[2] = s

cv2.imwrite("power.jpg", image)
print("saved power")