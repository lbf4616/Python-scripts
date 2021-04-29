import cv2
import numpy as np
import os


im_path = "/home/blin/Pictures/huansheng/lou/NG/108-2/Q43D10574946_el.jpg"
save_dir = './'
img = cv2.imread(im_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.equalizeHist(gray)
cv2.imwrite(os.path.basename(im_path), dst)