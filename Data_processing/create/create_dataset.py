import xlrd
import os
import shutil
from glob import glob
from tqdm import tqdm


def extract_pic_EL(data_dir, xlsx_dir):
    data = xlrd.open_workbook(xlsx_dir)
    table = data.sheet_by_name('MES导出')
    rowNum = table.nrows
    for i in tqdm(range(1, rowNum)):
        # label = table.cell_value(i,10)
        name = table.cell_value(i,4)
        res = table.cell_value(i,7)
        E_V = table.cell_value(i,26)
        line = table.cell_value(i,3)
        if res == 'PASS':
            res = 'OK'
        elif res == 'NG' and E_V == 'EL':
            res = 'NG'
        else:
            res = 'OK'
        # print(name, res, E_V, line)
        current_im_ls = glob(data_dir + '/' + name + '*.jpg')
        for im in current_im_ls:
            try:
                shutil.move(im, os.path.join(data_dir, res, line))
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
                shutil.move(im, os.path.join(data_dir, res, line))
            except:
                pass


if __name__ == "__main__":

    el_data_dir = "/home/blin/tmp/project_data/huansheng/工厂反馈/20200918/108-0918/collect_images/el"
    vi_data_dir = "/home/blin/tmp/project_data/huansheng/工厂反馈/20200918/108-0918/collect_images/vi"
    xlsx_dir = '/home/blin/Pictures/0918/108-0918/108车间过漏检统计分析表v1.8-1-0918.xlsx'
    # extract_pic_EL(el_data_dir, xlsx_dir)
    extract_pic_VI(vi_data_dir, xlsx_dir)