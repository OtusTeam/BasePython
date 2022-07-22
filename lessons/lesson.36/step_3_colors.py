import cv2
# import numpy

f_name = 'data/image-sm.jpg'
image = cv2.imread(f_name)

# print("cv2.COLOR_BGR2RGB", cv2.COLOR_BGR2RGB)
# image_new = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_new = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


print(image.shape)
print(image_new.shape)
print(image[0])
print(image_new[0])

# print(image - image_new)
# cv2.imshow("new image", image_new)
# cv2.waitKey(0)

cv2.imwrite('data/image-sm_gray.jpg', image_new)
