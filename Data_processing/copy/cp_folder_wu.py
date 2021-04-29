import xlrd
import os
import shutil
from glob import glob


parent_dir = '/home/blin/tmp1/zhangyuechao/中环数据/0924_0927/0928/vi/'
xlsx_dir = 'wu.xlsx'
dst_dir = '1010//wu'


data = xlrd.open_workbook(xlsx_dir)
table = data.sheet_by_name('Sheet1')
rowNum = table.nrows
all_info = []
for i in range(1, rowNum):

    path = table.cell_value(i,1)
    line = path[1]
    E_V = table.cell_value(i,2)

    if not os.path.exists(os.path.join(dst_dir, 'wu', E_V, '108-' + line)):
        os.makedirs(os.path.join(dst_dir, 'wu', E_V, '108-' + line))
    try:
        shutil.copy(os.path.join(parent_dir, path), os.path.join(dst_dir, 'wu', E_V, '108-' + line))
    except:
        pass


