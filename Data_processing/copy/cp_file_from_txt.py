import csv
import os
from tqdm import tqdm
import shutil

csv_path = '/home/blin/Downloads/select_img.txt'
dst_dir = '/home/blin/Pictures/99/'
root = '/home/blin/Pictures/中环数据/data/el/ly_20201219_with_2_0/'

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
os.makedirs(dst_dir)
    
    
img_path_list = []
with open(csv_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        # print(line)
        # new_path = line.replace('/workspace/gitlab', '/home/blin/tmp2/gitlab').strip()
        # new_path = new_path.replace('/workspace/di_group1', '/home/blin/di')
        new_path = os.path.join(root, line.strip())
        img_path_list.append(new_path)


for img_path in tqdm(img_path_list):
    try:
        shutil.copy(img_path, dst_dir)
        shutil.copy(img_path.replace('.png', '.json'), dst_dir)
    except:
        pass
    