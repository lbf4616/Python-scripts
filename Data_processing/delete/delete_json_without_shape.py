import json
from glob import glob
import os
from tqdm import tqdm

data_dir = '/home/blin/Pictures/中环数据/0907/'
subdir = ['train']

for sub in subdir:
    js_ls = glob(data_dir + sub + '/*.json')
    for js in tqdm(js_ls):
        with open(js, 'r') as file:
            data = json.load(file)
        if data['shapes'] == []:
            print(js)
            os.remove(js)