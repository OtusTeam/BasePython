import cv2

f_name = 'data/image-sm.jpg'
image = cv2.imread(f_name)
scale = 0.5
image_h, image_w, _ = image.shape
dsize = (int(image_w * scale), int(image_h * scale))
image_resized = cv2.resize(image, dsize)
cv2.imshow(f_name, image_resized)

# PILLOW -> ndarray -> save to img -> ;)

# image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
# cv2.imwrite('data/image-sm_resized_bgr.jpg', image_rgb)

# BGR
image_gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
cv2.imwrite('data/image-sm_resized_gray.jpg', image_gray)
