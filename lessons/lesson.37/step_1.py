import cv2

f_name = 'data/image-sm.jpg'
image = cv2.imread(f_name)
print(type(image))
print(image.shape, image.nbytes)
scale = 0.5
image_h, image_w, _ = image.shape
print(image_w, image_h)
dsize = (int(image_w * scale), int(image_h * scale))
print(dsize)
image_sm = cv2.resize(image, dsize)
print(image_sm.shape)
cv2.imshow(f_name, image_sm)

key = cv2.waitKey(0)
print(key)

# with open(f_name, 'rb') as f:
#     image_bin = f.read()  # jpg -> bitmap
