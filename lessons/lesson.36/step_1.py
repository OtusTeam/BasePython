import cv2

f_name = 'data/image-sm.jpg'
image = cv2.imread(f_name)
print(type(image))
print(image)

print(image.shape, image.nbytes)

cv2.imshow("people", image)

key = cv2.waitKey(0)
print("exit by key", key)
