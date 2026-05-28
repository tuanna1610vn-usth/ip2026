import cv2

image = cv2.imread("cat.jpeg")
#Receive a 3D NumPy array: 3D = rows + columns; 2D = each row; 1D = 1 vector of 3 values (G, B, R)

print(image.shape, type(image.shape)) #Size and depth of each pixel (3 means B,G,R)
print(image)
print(type(image))


#convert to grayscale image
def preprocessing(image):
    print("start gray...")
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i][j]
            gray = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3
            pixel[0] = pixel[1] = pixel[2] = gray
    print("finish gray.")

preprocessing(image)

def bw(r):
    if r < 170:
        s = 0
    else:
        s = 255
    return s

cv2.imwrite("gray.jpg", image)
print("saved gray")


for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixel = image[i][j]
        s = bw(pixel[0])
        pixel[0] = s
        pixel[1] = s
        pixel[2] = s

cv2.imwrite("bw.jpg", image)
print("saved B&W")