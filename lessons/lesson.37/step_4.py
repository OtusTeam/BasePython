import cv2

img_f = './data/image-sm.jpg'
img = cv2.imread(img_f)

# img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite(img_f.replace('.jpg', '_bgr.jpg'), img_cvt)
