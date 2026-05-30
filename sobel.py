import cv2
import numpy as np

image = cv2.imread("cat.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("gray.jpg", image)

print(image.shape)

kernel_1 = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])

kernel_2 = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

Gx = [[0 for _ in range(image.shape[1])] for _ in range(image.shape[0])]
Gy = [[0 for _ in range(image.shape[1])] for _ in range(image.shape[0])]
#Create the matrix of the same size as the image, every pixel is zero.

for i in range(1, image.shape[0]-1):
    for j in range(1, image.shape[1]-1):
        patch = image[i-1:i+2, j-1:j+2].astype(np.float32)
        Gx[i][j] = np.sum(patch * kernel_1)
        Gy[i][j] = np.sum(patch * kernel_2)

Gx = np.array(Gx, dtype=np.float32)
Gy = np.array(Gy, dtype=np.float32)

G_mag = np.sqrt(Gx**2 + Gy**2)

sobel = np.clip(G_mag, 0, 255).astype(np.uint8)

cv2.imwrite("sobel.jpg", sobel)
print("saved sobel")