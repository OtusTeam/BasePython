# 24 = 8 * 3
import cv2

img_f = './data/image-sm.jpg'
img = cv2.imread(img_f)
# print(type(img))
# print(dir(img))
print(img.shape)
# BGR <=> RGB
b_channel = img[:, :, 0]
# g_channel = img[:, :, 1]
# r_channel = img[:, :, 2]
print(b_channel.shape, b_channel.min())
cv2.imshow('image', img)
cv2.waitKey(0)
