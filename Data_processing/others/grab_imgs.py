from glob import glob
import os
import shutil


data_dir = '/home/blin/Pictures/152/5*77/20200916/'
sub_folders = os.listdir(data_dir)
dst_dir = '/home/blin/Pictures/152/5*77/20200916/all/'

# if not os.path.exists:
#     os.makedirs(dst_dir)

for folder in sub_folders:
    subs = os.listdir(os.path.join(data_dir, folder))
    for sub in subs:
        dir = os.path.join(data_dir, folder, sub)
        im_ls = glob(dir + '/*.jpg')
        for im in im_ls:
            shutil.copy(im, dst_dir)