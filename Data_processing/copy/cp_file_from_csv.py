import csv
import os
from tqdm import tqdm
import shutil

csv_path = '/home/blin/Downloads/环晟el图片路径(1)/csv/train.csv'
dst_dir = '/disk/data/huansheng/el/20210224/train/'
remove_dir = True

if remove_dir:
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
os.makedirs(dst_dir)
    
img_path_list = []
with open(csv_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        new_path = line.replace('/workspace/gitlab', '/home/blin/tmp2/gitlab').strip()
        new_path = new_path.replace('/workspace/di_group1', '/home/blin/di')
        new_path = new_path.replace('/workspace/tmp_75', '/home/blin/tmp1')
        img_path_list.append(new_path)

for img_path in tqdm(img_path_list):
    shutil.copy(img_path, dst_dir)
    try:
        shutil.copy(img_path.replace('.png', '.json'), dst_dir)
        
    except:
        pass
    