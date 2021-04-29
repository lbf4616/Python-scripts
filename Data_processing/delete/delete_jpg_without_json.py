import os
from glob import glob
from tqdm import tqdm


data_dir = '/home/blin/Pictures/huansheng/big_img/'
subdir = ['ng_all']

for sub in subdir:
    im_ls = glob(data_dir + sub + '/*.jpg')
    for im in tqdm(im_ls):
        js = im.replace('.jpg', '.json')
        if not os.path.exists(js):
            os.remove(im)
            print(im)