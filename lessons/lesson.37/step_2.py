import cv2

f_name = 'data/image-sm.jpg'
image = cv2.imread(f_name)
scale = 0.5
image_h, image_w, _ = image.shape
dsize = (int(image_w * scale), int(image_h * scale))
image_resized = cv2.resize(image, dsize)
cv2.imshow(f_name, image_resized)

# key = cv2.waitKey(0)
# print(key)
# matpoltlib
# plt.show()
cv2.imwrite('data/image-sm_resized.jpg', image_resized)
