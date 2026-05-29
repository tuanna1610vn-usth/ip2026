import cv2
import numpy as np

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

def maximum(patch):
    return np.max(patch)

output = [ [  [0, 0, 0] for _ in range(image.shape[1])] for _ in range(image.shape[0])]

for i in range(1, image.shape[0]-1):
    for j in range(1, image.shape[1]-1):
        #extract 3x3: image[row_start:row_stop, col_start:col_stop]
        patch = image[i-1:i+2, j-1:j+2]
        s = int(maximum(patch))
        pixel = output[i][j]
        pixel[0] = s
        pixel[1] = s
        pixel[2] = s

out = np.array(output)

cv2.imwrite("maximum.jpg", out)
print("saved maximum")