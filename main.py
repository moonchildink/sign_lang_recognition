# """
# 测试
# """
# # import cv2
# from cv2 import cvtColor,COLOR_RGB2BGR,COLOR_BGR2RGB
# # import numpy as np
# # import os
# # from matplotlib import pyplot as plt
# # import time
# import mediapipe as mp
# #
# # mp_holistics = mp.solutions.holistic
# # mp.drawing = mp.solutions.drawing_utils
# #
# # Python program to explain cv2.imshow() method

# # importing cv2

# def mediapipe_detection(image, model):
#     image = cvtColor(image, COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
#     image.flags.writeable = False  # Image is no longer writeable
#     results = model.process(image)  # Make prediction
#     image.flags.writeable = True  # Image is now writeable
#     image = cvtColor(image, COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
#     return image, results

# import cv2

# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     ret, frame = cap.read()
#     # image, results = mediapipe_detection(frame,)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


def func(x, y):
    return (x - 2) ** 2 + (y - 1) ** 2

def subject_func_2(x, y):
    return x ** 2 / 4 - y ** 2 + 1

n = 10

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-n, n, 20)
y = np.linspace(-n, n, 20)

xx, yy = np.meshgrid(x, y)

# surf1 = ax.plot_surface(xx, yy, func(xx, yy), rstride=1,
                        # cstride=1, color='g', alpha=0.5)
# surf2 = ax.plot_surface(xx,yy,0,)
surf2 = ax.plot_surface(xx, yy, subject_func_2(xx, yy),cmap = 'BuGn')
# surf = ax.plot_surface(xx, yy, subject_func_2(xx, yy), cmap='BuGn')
# ax.contourf(xx, yy, func(xx, yy), offset=2, cmap='BuGn')
# fig.colorbar(surf1,surf2)
plt.show()
