import xlrd
import os
import shutil
from glob import glob
from tqdm import tqdm


def extract_pic_EL(data_dir, save_dir, xlsx_dir):
    data = xlrd.open_workbook(xlsx_dir)
    table = data.sheet_by_name('Sheet1')
    rowNum = table.nrows
    for i in tqdm(range(1, rowNum)):
        # label = table.cell_value(i,10)
        name = table.cell_value(i,4)
        level = table.cell_value(i,5)
        line = table.cell_value(i,3)
        date = table.cell_value(i,7)
        bad =  table.cell_value(i,10)
        # if line == '108-3':
        #     continue
        res = ''
        if (level == 'A' or level == 'B') and bad == '':
            res = 'OK'
        else:
            res = 'NG'
        # print(name, res, E_V, line)
        dates = ['2020-10-01', '2020-10-02', '2020-10-03', '2020-10-04', '2020-10-05', '2020-10-06', '2020-10-07', '2020-10-08', '2020-10-09', '2020-10-10', '2020-10-11', '2020-10-12', '2020-10-13', '2020-10-14', '2020-10-15', '2020-10-16', '2020-10-17']
        bans = ['白班', '晚班']
        subdir = ['subset0', 'subset1','subset2','subset3','subset4','subset5','subset6','subset7','subset8','subset9','subset10', 'subset11','subset12','subset13','subset14','subset15','subset16','subset17','subset18','subset19','subset20','subset21','subset22','subset23','subset24','subset25','subset26','subset27']
        for date in dates:
            for ban in bans:
                # im = os.path.join(data_dir, 'line'+line[-1], date, ban, name + '.jpg')
                # print(im)
                try:
                    im = os.path.join(data_dir, 'line'+line[-1], date, ban, name + '.jpg')
                    if not os.path.exists(os.path.join(save_dir, res, line)):
                        os.makedirs(os.path.join(save_dir, res, line))
                    shutil.copy(im, os.path.join(save_dir, res, line))
                    print(name)
                except:
                    pass
        for sub in subdir:
            try:
                im = os.path.join(data_dir, 'line'+line[-1], sub, name + '.jpg')
                if not os.path.exists(os.path.join(save_dir, res, line)):
                    os.makedirs(os.path.join(save_dir, res, line))
                shutil.copy(im, os.path.join(save_dir, res, line))
                print(name)
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

    el_data_dir = "/home/blin/tmp/project_data/huansheng/data_raw/recognition/cenghou/el/20201019/108"
    save_dir = '/home/blin/Pictures/huansheng/cenghou/1103/'
    # vi_data_dir = "/home/blin/tmp/project_data/huansheng/工厂反馈/20200918/108-0918/collect_images/vi"
    xlsx_dir = '/home/blin/Documents/中环/cenghou/108-层后EL查询导出-16天数据-表1_line123.xlsx'
    extract_pic_EL(el_data_dir, save_dir, xlsx_dir)
    # extract_pic_VI(vi_data_dir, xlsx_dir)