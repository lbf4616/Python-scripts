import json
from glob import glob
import shutil
import os


data_dir = '/home/blin/Pictures/huansheng/big_img/ng_all'

label = ['0', '1', '2', '3', '31', '32', '8', '4', '41', '42']
tmp_dir = data_dir.replace('ng_all', 'del')

if not os.path.exists(tmp_dir):
    os.mkdir(tmp_dir)

js_ls = glob(data_dir + '/*.json')
for js in js_ls[1:]:
    with open(js, 'r') as file:
        data = json.load(file)
    
    new_data = []
    for bad in data['shapes']:
        if bad['label'] in label:
            new_data.append(bad)
    if new_data != []:
        data['shapes'] = new_data
        with open(js, 'w') as file:
            json.dump(data, file, indent=2)
    else:
        shutil.move(js, tmp_dir)
        shutil.move(js.replace('json', 'jpg'), tmp_dir)
            