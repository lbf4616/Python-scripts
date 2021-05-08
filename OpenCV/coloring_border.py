import cv2
import numpy as np
import matplotlib.pyplot as plt


def coloring_border_canny(img, color):
    ori = np.copy(img)
    gray = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)

    mask = cv2.Canny(gray, 50, 150)
    mask = np.array(mask / 255, dtype=int)
    # mask = np.array(cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1) / 255, dtype=int)

    mask = np.expand_dims(mask, axis=2)
    mask = np.concatenate((mask, mask, mask), axis=-1)

    bg = ori * (1 - mask)
    border = mask * color

    res = bg + border

    return res

def coloring_border_cornerHarris(img, color):
    ori = np.copy(img)
    gray = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    # ori[dst>0.01*dst.max()] = [0,0,255]
    corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 10)
    # corners = np.int0(corners)
    cv2.cornerSubPix(gray, corners, (5,5), (-1,1), criteria)
    # 精确调整
    corners[2] = corners[2] + 1
    corners[3] = corners[3] + 1
    corners[6] = corners[6] + 1
    corners[0][0][1] = corners[0][0][1] + 1
    corners[1][0][0] = corners[1][0][0] + 1
    corners[4][0][0] = corners[4][0][0] + 1
    
    h_corners = [[corners[6], corners[0]],
                 [corners[3], corners[2]],
                 [corners[1], corners[4]]]

    v_corners = [[corners[5], corners[0]],
                 [corners[3], corners[1]],
                 [corners[2], corners[4]]]

    r_corners = [[corners[5], corners[4]],
                 [corners[3], corners[6]],
                 [corners[2], corners[0]]]

    for i in h_corners:
        cv2.line(ori, (i[0].ravel()[0], i[0].ravel()[1]), (i[1].ravel()[0], i[1].ravel()[1]), color, 1)

    for i in v_corners:
        cv2.line(ori, (i[0].ravel()[0], i[0].ravel()[1]), (i[1].ravel()[0], i[1].ravel()[1]), color, 1)

    for i in r_corners:
        cv2.line(ori, (i[0].ravel()[0], i[0].ravel()[1]), (i[1].ravel()[0], i[1].ravel()[1]), color, 1)

    return ori

if __name__ == '__main__':
    
    # 读图
    img = cv2.imread('1.png')
    # 边缘检测
    # res = coloring_border_canny(img, (255, 0, 0))
    # 角点检测
    res = coloring_border_cornerHarris(img, (0, 0, 0))
    cv2.imwrite('res_2.png', res)
    # 显示结果
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.imshow(res)
    plt.show()