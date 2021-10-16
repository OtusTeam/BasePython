import cv2

f_path = './data/image-sm.jpeg'
image = cv2.imread(f_path)
im_h, im_w, _ = image.shape

# BGR vs RGB
# HSL, LAB
image_cvt = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(f_path.replace('.jpeg', '_bw.jpg'), image_cvt)

# cv2.imshow('image', image_cvt)
# key = cv2.waitKey(0)
