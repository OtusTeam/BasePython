import cv2

file_name = "data/img-cat.jpeg"
image = cv2.imread(file_name)

print(type(image))
# print(image)
print(image.shape)
print(image.nbytes)

cv2.imshow("Cat", image)
key = cv2.waitKey(0)
print("exit by key", key)

