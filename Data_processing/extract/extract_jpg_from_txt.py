import xlrd
import os
import shutil
from glob import glob


def extract_pic_VI(data_dir, save_dir, xlsx_dir):

    data = xlrd.open_workbook(xlsx_dir)
    print('loaded')
    table = data.sheet_by_name('Sheet1')
    rowNum = table.nrows
    names = []
    dir_dic = {'line1':'108-1', 'line2':'108-2', 'line3':'108-3'}
    for i in range(0, rowNum):
        name = table.cell_value(i,0)
        # print('name', name)
        names.append(name)

    for root, dirs, files in os.walk(data_dir, topdown=False):
        for f in files:
            if f.split('_')[0] in names:
                try:
                    cur_save_dir = os.path.join(save_dir, dir_dic[root[-5:]])
                    if not os.path.exists(cur_save_dir):
                        os.makedirs(cur_save_dir)
                    print(f)
                    shutil.copy(os.path.join(root, f), cur_save_dir)
                        
                except:
                    continue
        # current_im_ls = glob(data_dir + '/' + name + 'vi.jpg')

        # for im in current_im_ls:
        #     try:
        #         shutil.move(im, os.path.join(save_dir, line, label))
        #     except:
        #         pass


if __name__ == "__main__":

    data_dir = "/home/blin/Downloads/108-1025漏检图片/"
    save_dir = '/home/blin/Pictures/huansheng/lou/NG/'
    xlsx_dir = '/home/blin/Downloads/108-1025漏检图片/el.xlsx'

    # extract_pic_EL(data_dir, save_dir, xlsx_dir)
    extract_pic_VI(data_dir, save_dir, xlsx_dir)