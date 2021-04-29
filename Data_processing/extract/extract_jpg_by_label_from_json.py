import json
from glob import glob
import os
from tqdm import tqdm

data_dir = '/media/blin/Elements SE/vi/1028/train/'
label_cnt = {'31':0, '71':0}
js_ls = glob(data_dir + '*.json')
for js in tqdm(js_ls):
    with open(js, 'r') as file:
        data = json.load(file)

        for bad in data['shapes']:
            label = bad['label']
            if label == '31' or label == '71':
                label_cnt[label] += 1

print(label_cnt)