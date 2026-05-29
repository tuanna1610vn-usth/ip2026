import cv2
import numpy as np

image = cv2.imread("cat.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("gray.jpg", image)

print(image.shape)

kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

output = [[0 for _ in range(image.shape[1])] for _ in range(image.shape[0])]
#Create the matrix of the same size as the image, every pixel is zero.

for i in range(1, image.shape[0]-1):
    for j in range(1, image.shape[1]-1):
        patch = image[i-1:i+2, j-1:j+2]
        s = np.sum(patch * kernel)
        output[i][j] = s

filter = np.array(output, dtype=np.float32) # Convert to 32bit float to store negative value

enhanced = image.astype(np.float32) - filter # Convert to 32bit float to subtract

enhanced = np.clip(enhanced, 0, 255).astype(np.uint8) # Limit array values to 0-255 and change to 8 bit int to store

# To look at the filter safely, shift it so 0-slopes become neutral gray (128)
filter_visual = np.clip(filter + 128, 0, 255).astype(np.uint8)

cv2.imwrite("filter.jpg", filter_visual)
cv2.imwrite("enhanced.jpg", enhanced)
print("saved filter and enhanced")