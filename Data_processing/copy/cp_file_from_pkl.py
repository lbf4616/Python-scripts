import csv
import os
from tqdm import tqdm
import shutil
import pickle as pkl

im_path = '/home/blin/atesi/ats_pytorch/test/atesi_0201_poly/val/img_path.pkl'
dst_dir = '/home/blin/atesi/data/atesi/poly/20210201/val'
remove_dir = False

if remove_dir:
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)
    
    
img_path_list = []
with open(im_path, 'rb') as f:
    lines = pkl.load(f)

for line in lines:
    print(line)
    new_path = line.replace('/workspace/gitlab', '/home/blin/tmp2/gitlab')
    new_path = new_path.replace('/disk1/tmp/nfs_di', '/home/blin/di')
    new_path = new_path.replace('/workspace/tmp_75', '/home/blin/tmp1')
    img_path_list.append(new_path)


for img_path in tqdm(img_path_list):
    shutil.copy(img_path, dst_dir)
    # shutil.copy(img_path.replace('.png', '.json'), dst_dir)
    