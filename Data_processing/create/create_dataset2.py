import xlrd
import os
import shutil
from glob import glob
from tqdm import tqdm


def extract_pic_EL(data_dir, save_dir, xlsx_dir):
    print('loading xlsx')
    data = xlrd.open_workbook(xlsx_dir)
    print('loaded')
    table = data.sheet_by_name('MES导出')
    tabel2 = data.sheet_by_name('过检分析')
    im_dir_ls = {}
    rowNum2 = tabel2.nrows
    print(rowNum2)
    for i in range(1, rowNum2):
        im_dir = tabel2.cell_value(i, 6)
        # print(im_dir)
        key1 = im_dir.split('/')[-1][:-7]
        print(key1)
        im_dir_ls[key1] = im_dir
    if not os.path.exists(os.path.join(save_dir, 'OK')):
        os.makedirs(os.path.join(save_dir, 'OK'))
    rowNum = table.nrows
    for i in tqdm(range(1, rowNum)):
        label = table.cell_value(i,10)
        name = table.cell_value(i,4)
        res = table.cell_value(i,7)
        E_V = table.cell_value(i,26)
        line = table.cell_value(i,3)
        
        if res == 'PASS':
            res = 'OK'
        elif label == 'FAILED|破片|':
            res = '破片'
        elif label == 'FAILED|异物|':
            res = '异物'
        elif res == 'NG' and E_V == 'EL':
            res = 'NG'
        else:
            res = 'OK'
        # print(name, res, E_V, line)
        current_im_ls = glob(data_dir + '/' + name + '*.jpg')
        # print(current_im_ls)
        for im in current_im_ls:
            try:
                shutil.copy(im, os.path.join(save_dir, res, line))
                print(im)
            except:
                pass

def extract_pic_VI(data_dir, xlsx_dir):
    data = xlrd.open_workbook(xlsx_dir)
    table = data.sheet_by_name('MES导出')
    rowNum = table.nrows
    for i in tqdm(range(1, rowNum)):
        label = table.cell_value(i,10)
        name = table.cell_value(i,4)
        res = table.cell_value(i,7)
        E_V = table.cell_value(i,26)
        line = table.cell_value(i,3)

        if res == 'PASS':
            res = 'OK'
        elif res == 'NG' and E_V == 'VI':
            res = 'NG'
        elif res == 'NG' and label == 'FAILED|破片|':
            res = 'NG'
        else:
            res = 'OK'
        # print(name, res, E_V, line)
        current_im_ls = glob(data_dir + '/' + name + '*.jpg')
        for im in current_im_ls:
            try:
                if os.path.exists(os.path.join(data_dir, res, line)):
                    shutil.copy(im, os.path.join(data_dir, res, line))
                    print(im)
            except:
                pass


if __name__ == "__main__":

    data_dir = "/data/public/"
    save_dir = '/data/collected_im/'
    xlsx_dir = './108过漏检统计分析表v1.8.2-0927-只统计第一次检测.xlsx'
    print('sb')
    extract_pic_EL(data_dir, save_dir, xlsx_dir)
    # extract_pic_VI(data_dir, xlsx_dir)