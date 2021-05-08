import cv2
import numpy as np
import matplotlib.pyplot as plt


def cross_conv(img, width):
    # 构造卷积核
    weight = 1 / (width * width)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (width, width)) * weight
    # 卷积操作
    res = cv2.filter2D(img, -1, kernel)

    return res

if __name__ == "__main__":

    # 读图
    img = cv2.imread('1.png')
    res = cross_conv(img, 3)
    # 显示结果
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.imshow(res)
    plt.show()