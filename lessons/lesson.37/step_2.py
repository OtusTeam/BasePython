# 24 = 8 * 3
import cv2

img_f = './data/image-sm.jpg'
img = cv2.imread(img_f)
img_dark = img * 0.85
img_dark = img_dark.astype('int8')
cv2.imshow('image', img_dark)
# b_channel = img[:, :, 0]
# cv2.imshow('image', b_channel)
key = cv2.waitKey(0)
print(key)
