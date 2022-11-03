
import cv2
import numpy as np


res = cv2.imread('resim/kedi.jpg',0)
inverted = np.invert(res)
cv2.imshow("orjinal",res)

[h,w] = (res.shape)
new_res = np.zeros([h,w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
         new_res[i,j] = 255 - res[i,j]

print(res[0,0])
cv2.imshow("Ters_cevrilmis",new_res)
cv2.waitKey()






