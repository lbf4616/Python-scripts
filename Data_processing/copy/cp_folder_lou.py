import xlrd
import os
import shutil
from glob import glob


parent_dir = '/home/blin/tmp1/zhangyuechao/中环数据/0924_0927/0928/vi/'
xlsx_dir = 'lou.xlsx'
dst_dir = '1010//lou'


data = xlrd.open_workbook(xlsx_dir)
table = data.sheet_by_name('Sheet1')
rowNum = table.nrows
all_info = []
for i in range(1, rowNum):
    line = table.cell_value(i,0)
    name = table.cell_value(i,1)
    E_V = table.cell_value(i,5)
    all_info.append([line, name, E_V])

for root, dirs, files in os.walk(parent_dir, topdown=False):
    for name in dirs:
        for info in all_info:
            if name == info[1]:
                sub_dir = sorted(os.listdir(os.path.join(root, name)))
                im = glob(os.path.join(root, name, sub_dir[0]) + '*' + info[2].lower + '.jpg')
                for img in im:
                    try:
                        if not os.path.exists(os.path.join(dst_dir, 'lou', info[0])):
                            os.makedirs(os.path.join(dst_dir, 'lou', info[0]))
                        shutil.copy(img, os.path.join(dst_dir, 'lou', info[0]))
                    except:
                        pass
