# -*- coding: utf8 -*-
import cv2
import random

# OpenCV face detection
face_patterns = cv2.CascadeClassifier('C:/Users/sdzar/Documents/GitHub/crossin/face_detect/haarcascade_frontalface_default.xml')
sample_image = cv2.imread('C:/Users/sdzar/Documents/GitHub/crossin/face_detect/img/face3.jpg')
faces = face_patterns.detectMultiScale(sample_image,
                                       scaleFactor=1.0087,
                                       minNeighbors=1,
                                       minSize=(0, 0))
# add hats to a list
hats = []
for i in range(4):
    hats.append(cv2.imread('C:/Users/sdzar/Documents/GitHub/crossin/face_detect/img/hat%d.png' % i, -1))

for face in faces:
    # random choose a hat
    hat = random.choice(hats)
    # adject the size of hat
    scale = face[3] / hat.shape[0] * 1.25
    hat = cv2.resize(hat, (0, 0), fx=scale, fy=scale)
    # adject the position of the hat
    x_offset = int(face[0] + face[2] / 2 - hat.shape[1] / 2)
    y_offset = int(face[1] - hat.shape[0] / 2)
    # calclulate the position of the png
    x1, x2 = max(x_offset, 0), min(x_offset + hat.shape[1], sample_image.shape[1])
    y1, y2 = max(y_offset, 0), min(y_offset + hat.shape[0], sample_image.shape[0])
    hat_x1 = max(0, -x_offset)
    hat_x2 = hat_x1 + x2 - x1
    hat_y1 = max(0, -y_offset)
    hat_y2 = hat_y1 + y2 - y1
    # transparent
    alpha_h = hat[hat_y1:hat_y2, hat_x1:hat_x2, 3] / 255
    alpha = 1 - alpha_h
    # combine picture
    for c in range(0, 3):
        sample_image[y1:y2, x1:x2, c] = (alpha_h * hat[hat_y1:hat_y2, hat_x1:hat_x2, c] + alpha * sample_image[y1:y2, x1:x2, c])

# save result
cv2.imwrite('C:/Users/sdzar/Documents/GitHub/crossin/face_detect/img/faces_detect.png', sample_image)
