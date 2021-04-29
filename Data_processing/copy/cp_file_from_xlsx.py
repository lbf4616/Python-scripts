import csv
import os
from tqdm import tqdm
import shutil
import xlrd

pic_dir = '/home/blin/di/dataset/project_data/algorithm_data/ats_sz/data_processed/'
xlsx_dir = '/home/blin/di/dataset/project_data/algorithm_data/ats_sz/data_processed/doc/poly/20210129/dataset.xls'
dst_dir = '/home/blin/Pictures/data/atesi_sz/poly/20210129'
 
if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
os.makedirs(dst_dir)

data = xlrd.open_workbook(xlsx_dir)
""
table = data.sheet_by_name('data')

rowNum = table.nrows

name_ls = []
for i in tqdm(range(1, rowNum)):
    dir = os.path.join(pic_dir, table.cell_value(i,0))
    
    shutil.copy(dir, dst_dir)
    shutil.copy(dir.replace('png', 'json'), dst_dir)



    

# for roots, dirs, files in tqdm(os.walk(pic_dir)):
#     for file in files:
#         if file.split('_')[0] in name_ls:
#             shutil.copy(os.path.join(roots, file), dst_dir)

# for img_path in tqdm(img_path_list):
#     shutil.copy(img_path, dst_dir)
#     shutil.copy(img_path.replace('.png', '.json'), dst_dir)
    