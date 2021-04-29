import xlrd
import os
import shutil
from glob import glob


def extract_pic_VI(data_dir, save_dir, xlsx_dir):

    data = xlrd.open_workbook(xlsx_dir)
    print('loaded')
    table = data.sheet_by_name('MES')
    rowNum = table.nrows
    all_info = {}
    for i in range(1, rowNum):
        label = table.cell_value(i,10)
        name = table.cell_value(i,4)
        line = table.cell_value(i,3)
        all_info[name] = label + ' ' + line
    
    for root, dirs, files in os.walk(data_dir, topdown=False):
        for f in files:
            try:
                cur_save_dir = os.path.join(save_dir, all_info[f.split('.')[0]].split(' ')[1], all_info[f.split('.')[0]].split(' ')[0])
                if not os.path.exists(cur_save_dir):
                    os.makedirs(cur_save_dir)
                    shutil.copy(os.path.join(root, f), os.path.join(cur_save_dir, f))
            except:
                continue
        # current_im_ls = glob(data_dir + '/' + name + 'vi.jpg')

        # for im in current_im_ls:
        #     try:
        #         shutil.move(im, os.path.join(save_dir, line, label))
        #     except:
        #         pass


if __name__ == "__main__":

    data_dir = "Y://"
    save_dir = ''
    xlsx_dir = 'NG_VI.xlsx'

    # extract_pic_EL(data_dir, save_dir, xlsx_dir)
    extract_pic_VI(data_dir, save_dir, xlsx_dir)