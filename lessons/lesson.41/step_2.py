import cv2

f_name = 'data/image-sm.jpg'
image = cv2.imread(f_name)
# PILLOW -> ndarray -> save to img -> ;)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imwrite('data/image-sm_bgr_rgb.jpg', image_rgb)

# Gray
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('data/image-sm_gray.jpg', image_gray)
