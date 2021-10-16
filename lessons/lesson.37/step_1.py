import cv2

f_path = './data/image-sm.jpeg'
image = cv2.imread(f_path)
# print(dir(image))
print(image.shape)
# BGR vs RGB


cv2.imshow('image', image)
key = cv2.waitKey(0)
# print(key)  # ESC -> 27, ENTER -> 13
