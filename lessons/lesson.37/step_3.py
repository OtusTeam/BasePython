import cv2

img_f = './data/image-sm.jpg'
img = cv2.imread(img_f)
im_h, im_w, _ = img.shape
print(im_w, im_h)

scale = 0.75
new_size = (int(im_w * scale), int(im_h * scale))
img_scaled = cv2.resize(img, new_size)
print(img_scaled.shape)
cv2.imwrite(img_f.replace('.jpg', '_scaled.jpg'), img_scaled)
