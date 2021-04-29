import csv
import os
from tqdm import tqdm
from glob import glob
import shutil


def find(target_path, save_dir):
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.makedirs(save_dir)
        
    img_list = []
    name_ls = glob(target_path + '/*.png')

    for name in name_ls:
        name = os.path.basename(name)
        tmp = name.split('-')
        basename = max(tmp, key=len, default='')
        basename = basename.split('_')[-1]
        img_list.append(basename + '.jpg')

    all_name = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file in img_list:
                all_name.append(os.path.join(root, file))


    for name in tqdm(all_name):
        try:
            shutil.copy(name, save_dir)
        except:
            continue


if __name__ == "__main__":
    target_root = '/home/blin/tmp2/gitlab/xiaozhiheng/data/huansheng/汇流条偏移_data/object_detection/NG_train/'
    data_dir = '/home/blin/tmp/project_data/huansheng/data_raw/recognition/train/'
    dst_dir = '/home/blin/Pictures/huiliutiao/NG/'
    for path in os.listdir(target_root):
        print(os.path.join(target_root, path))
        find(os.path.join(target_root, path), os.path.join(dst_dir, path))
    # find(target_root, dst_dir)
