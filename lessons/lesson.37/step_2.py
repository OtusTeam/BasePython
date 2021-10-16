import cv2

f_path = './data/image-sm.jpeg'
image = cv2.imread(f_path)
im_h, im_w, _ = image.shape
print(im_w, im_h)
# BGR vs RGB
scale = 0.75
image_scaled = cv2.resize(image, (int(im_w * scale), int(im_h * scale)))
print(image_scaled.shape)
cv2.imwrite(f_path.replace('.jpeg', '_scaled.jpg'), image_scaled)

# cv2.imshow('image', image_scaled)
# key = cv2.waitKey(0)
