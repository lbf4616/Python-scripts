import csv
from glob import glob
import cv2
import os
from tqdm import tqdm
import json
data_dir = "vi-ng.txt"

outdir = '/home/blin/tmp/gitlab/linbofan/output/vi'
with open(data_dir, 'r') as f:
    data = f.readlines()

data = [line[:-1] + ".jpg" for line in data]
# print(data)

js_dir = "/home/blin/tmp/gitlab/luochangzhi/golden_message_huansheng_all/vi"
pic_dir = "/home/blin/tmp/gitlab/luochangzhi/golden_data_huansheng/vi/ng/1"
pic_ls = glob(pic_dir + "/*.jpg")

for pic in tqdm(data[:]):
    im = cv2.imread(os.path.join(pic_dir, pic))
    js = os.path.join(pic_dir, pic).replace('.jpg', '.json')
    with open(js, 'r') as f:
        js_data = json.load(f)
    bboxes = js_data['shapes']
    for bad in bboxes:
        x1 = bad['points'][0][0]
        y1 = bad['points'][0][1]
        x2 = bad['points'][1][0]
        y2 = bad['points'][1][1]
        cv2.rectangle(im, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
    im = cv2.pyrDown(im)
    # cv2.imshow("1", im)
    # cv2.waitKey()
    cv2.imwrite(os.path.join(outdir, os.path.basename(pic)), im)

