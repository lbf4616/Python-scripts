from glob import glob
import os
import shutil
from tqdm import tqdm

def rn(el_dir, vi_dir):
    el_ls = glob(el_dir + '/*.jpg')
    vi_ls = glob(vi_dir + '/*.jpg')
    for idx, el in tqdm(enumerate(el_ls)):
        name = os.path.basename(el)
        vi_ori_name = os.path.basename(vi_ls[idx])
        os.rename(vi_ls[idx], vi_ls[idx].replace(vi_ori_name, name))


if __name__ == "__main__":
    el_dir = '/home/blin/tmp1/luochangzhi/data_for_joint_debug_20210113/images/双玻/el'
    vi_dir = '/home/blin/tmp1/luochangzhi/data_for_joint_debug_20210113/images/双玻/vi'
    rn(el_dir, vi_dir)