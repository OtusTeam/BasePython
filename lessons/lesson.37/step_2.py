# scale image

import cv2

file_name = "data/img-cat.jpeg"
image = cv2.imread(file_name)

print(image.shape)

image_h, image_w, _ = image.shape

scale = 0.5

target_d = int(image_w * 0.5), int(image_h * 0.5)

image_small = cv2.resize(image, target_d)
print(image_small.shape)
# cv2.imshow("Small cat", image_small)
# cv2.waitKey(0)

cv2.imwrite("data/img-cat_small.jpeg", image_small)


