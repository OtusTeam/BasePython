import cv2
# PIL

f_name = 'data/image-sm.jpg'  # heic
image = cv2.imread(f_name)
print(type(image))
# print(image.shape)
# print(image[:, :, 2].min())
# print(image[:, :, 2].max())

print(image.shape, image.nbytes)
scale = 0.5
image_h, image_w, _ = image.shape
# a, b, c, d = b, a, d, c

print(image_w, image_h)
dsize = (int(image_w * scale), int(image_h * scale))
print(dsize)
image_sm = cv2.resize(image, dsize)
print(image_sm.shape)
cv2.imshow(f_name, image_sm)

key = cv2.waitKey(0)
print(key)
cv2.imwrite('data/image-sm_resized.jpg', image_sm)

# with open(f_name, 'rb') as f:
#     image_bin = f.read()  # jpg -> bitmap
