import cv2
import matplotlib.pyplot as plt
import numpy as np
img  = cv2.imread("C:/Users/riberygao/Desktop/10.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
# hsv[:,:,2] += value
h, s, v = cv2.split(hsv)
value = 255
s_before = s.copy()
# s[:,:]=0

v[v<value]=0
v[v>=value] =value
final_hsv = cv2.merge((h, s, v))
height, width = img.shape[:2]
img_decrease_v = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
img_decrease_v = cv2.resize(img_decrease_v, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_AREA)

decodeDat = cv2.cvtColor(img_decrease_v,cv2.COLOR_BGR2GRAY)

cv2.imshow("de",decodeDat)
# circle = cv2.HoughCircles(decodeDat, cv2.HOUGH_GRADIENT, 1, 100, param2=50, minRadius=5, maxRadius=200)
# print(circle)
# circles = circle[0, :, :]  # 提取为二维
# circles = np.uint16(np.around(circles))  # 四舍五入，取整
# for i in circles[:]:
#     cv2.circle(decodeDat, (i[0], i[1]), i[2], (255, 0, 0), 5)  # 画圆
#     cv2.circle(decodeDat, (i[0], i[1]), 2, (255, 0, 255), 10)  # 画圆心
#     print((i[0], i[1]))
# cv2.imshow("cir", decodeDat)
# cv2.waitKey()
# cv2.imshow("hsv", img_decrease_v)
# cv2.waitKey()


# plt.figure()
# f, axes = plt.subplots(1, 4, figsize=(20, 10))
# ax = axes.ravel()
# ax[0].hist(h.ravel(), bins=256)
# ax[0].set_title('h')
# ax[1].hist(s_before.ravel(), bins=256)
# ax[1].set_title('s')
# ax[2].hist(v.ravel(), bins=256)
# ax[2].set_title('v')
# ax[3].hist(s.ravel(), bins=256)
# ax[3].set_title('s_after')
# # plt.imshow(cv2.cvtColor(img_decrease_v, cv2.COLOR_BGR2RGB))
# plt.figure()
# f, axes = plt.subplots(1, 2, figsize=(20, 10))
# ax = axes.ravel()
# ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# ax[1].imshow(cv2.cvtColor(img_decrease_v, cv2.COLOR_BGR2RGB))
