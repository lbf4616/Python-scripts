import xlrd
import os
import shutil
from glob import glob

def extract_wu(xlsx_dir, key_label, save_dir):
    data = xlrd.open_workbook(xlsx_dir)
    table = data.sheet_by_name('漏检分析')

    for key in key_label:
        if not os.path.exists(os.path.join(save_dir, key)):
            os.mkdir(os.path.join(save_dir, key))
    rowNum = table.nrows
    colNum = table.ncols
    print(rowNum)
    name_ls = []
    for i in range(1, rowNum):
        label = table.cell_value(i,8)
        name = table.cell_value(i,2)
        res = table.cell_value(i,18)
        E_V = table.cell_value(i,7)
        if res == '过检':
            for key in key_label:
                if key in label:
                    current_im_ls = glob(save_dir + '/' + name + '_' + E_V.lower() + '*.jpg')
                    # print(save_dir + '/' + name + '_' +E_V.lower() + '*.jpg')
                    current_im_ls_defect = glob(save_dir + '/' + 'defect_' + name + '_' + E_V.lower() + '*.jpg')
                    current_im_ls += current_im_ls_defect
                    # print(current_im_ls)
                    for im in current_im_ls:
                        print(im)
                        try:
                            shutil.copy(im, os.path.join(save_dir, key))
                        except:
                            pass
                        # print(label, name, res)

def extract_lou(xlsx_dir, key_label, save_dir):
    data = xlrd.open_workbook(xlsx_dir)
    table = data.sheet_by_name('MES导出')

    for key in key_label:
        if not os.path.exists(os.path.join(save_dir, key)):
            os.mkdir(os.path.join(save_dir, key))
    rowNum = table.nrows
    colNum = table.ncols
    print(rowNum)
    name_ls = []
    for i in range(1, rowNum):
        label = table.cell_value(i,10)
        name = table.cell_value(i,4)
        res = table.cell_value(i,28)
        E_V = table.cell_value(i,26)
        if res == '漏检':
            for key in key_label:
                if key in label:
                    current_im_ls = glob(save_dir + '/' + name + '*.jpg')
                    # print(current_im_ls)
                    for im in current_im_ls:
                        print(im)
                        try:
                            shutil.copy(im, os.path.join(save_dir, key))
                        except:
                            pass

if __name__ == '__main__':

    xlsx_dir = '/home/blin/Pictures/0918/108-0918/108车间过漏检统计分析表v1.8-1-0918.xlsx'
    key_label = ['破片', '分叉隐裂', '单条隐裂', '虚焊', '断栅', '失效片', '隐裂失效', '正极点虚焊', '局部虚焊', '短路', '露白', '溢胶', '异物', '汇流条偏移', '串间距不良']
    save_dir = '/home/blin/Pictures/0918/108-0918/wu'

    #　extract_wu(xlsx_dir, key_label, save_dir)

    xlsx_dir = '/home/blin/Pictures/0918/108-0918/108车间过漏检统计分析表v1.8-1-0918.xlsx'
    key_label = ['FAILED|破片|', 'FAILED|交叉|', 'FAILED|虚焊|', 'FAILED|隐裂|', 'FAILED|EL暗斑|', 'FAILED|失效|', 'FAILED|短串拼接|', 'FAILED|EL断栅|', 'FAILED|EL图不均|', 'FAILED|串间距|', 'FAILED|脏污|', 'FAILED|露白|', 'FAILED|整体偏移|', 'FAILED|异物|', 'FAILED|其他|', 'FAILED|汇流条偏移|']
    save_dir = '/home/blin/Pictures/0918/108-0918/lou'

    extract_lou(xlsx_dir, key_label, save_dir)
    