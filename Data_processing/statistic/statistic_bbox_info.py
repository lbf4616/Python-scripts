import csv
import os
from glob import glob
import json
from tqdm import tqdm

data_dir = '/home/blin/tmp1/zhangyuechao/中环数据/el_ann_second'
subsets = os.listdir(data_dir)
f = open('label_info_EL.csv','w',encoding='utf-8')
csv_writer = csv.writer(f)

title = ['json_name', 'bbox_idx', 'label', '宽', '高', '面积']
csv_writer.writerow(title)
for subset in tqdm(subsets[:]):
    print(subset)
    js_ls = glob(os.path.join(data_dir, subset) + '/*.json')
    for js in js_ls[:]:
        if "-11" in js:
            continue
        with open(js, 'r') as file:
            data = json.load(file)
            for idx, bad in enumerate(data['shapes']):
                x1, y1 = bad['points'][0][0], bad['points'][0][1]
                x2, y2 = bad['points'][1][0], bad['points'][1][1]
                w = abs(x2 - x1)
                h = abs(y2 - y1)
                area = h * w
                label = bad['label']
                write_line = [subset + '/' + os.path.basename(js), idx + 1, label, w, h, area]
                csv_writer.writerow(write_line)