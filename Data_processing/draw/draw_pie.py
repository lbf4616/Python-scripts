import xlrd
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
from matplotlib.font_manager import FontProperties

class statistic(object):
    def __init__(self, xlrd, title):
        self.el_wu = {'破片':0, '分叉隐裂':0, '单条隐裂':0, '虚焊':0, '断栅':0, '失效片':0, '隐裂失效':0, '正极点虚焊':0, '局部虚焊':0, '短路/死片':0}
        self.vi_wu = {'破片':0, '露白':0, '溢胶':0, '异物':0, '汇流条偏移':0, '串间距不良':0, '整体偏移':0}
        self.el_lou = {}
        self.vi_lou = {}
        self.el_num = [0, 0]
        self.vi_num = [0, 0]
        self.title = title
        self.xlxs_dir = xlrd
        self.count(self.xlxs_dir)

    def draw_pie(self):
        font = FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', size=8)
        plt.figure(figsize=(12,12))
        label_el_wu = []
        values_el_wu = []
        label_vi_wu = []
        values_vi_wu = []
        for info in self.el_wu: 
            if info[1] > 0:
                label_el_wu.append(info[0] + ' (' + str(info[1]) + ')')
                values_el_wu.append(info[1])
        
        for info in self.vi_wu: 
            if info[1] > 0:
                label_vi_wu.append(info[0] + ' (' + str(info[1]) + ')')
                values_vi_wu.append(info[1])
        
        explode_el_wu = [0.01 for i in range(len(label_el_wu))]
        explode_vi_wu = [0.01 for i in range(len(label_vi_wu))]

        label_el_lou = []
        values_el_lou = []
        label_vi_lou = []
        values_vi_lou = []
        for info in self.el_lou: 
            if info[1] > 0:
                label_el_lou.append(info[0] + ' (' + str(info[1]) + ')')
                values_el_lou.append(info[1])
        
        for info in self.vi_lou: 
            if info[1] > 0:
                label_vi_lou.append(info[0] + ' (' + str(info[1]) + ')')
                values_vi_lou.append(info[1])
        
        explode_el_lou = [0.01 for i in range(len(label_el_lou))]
        explode_vi_lou = [0.01 for i in range(len(label_vi_lou))]

        plt.figure(1)

        # figure, ax = plt.subplots()
        plt.suptitle(self.title, fontproperties=font)
        ax1 = plt.subplot(221)
        plt.pie(values_el_wu,explode=explode_el_wu,labels=label_el_wu,autopct='%1.1f%%', textprops= {'fontsize':8,'color':'black','fontproperties':font})#绘制饼图
        ax1.set_title('EL误报类别统计(' + str(self.el_num[0]) + ')', fontproperties=font)#绘制标题

        ax2 = plt.subplot(222)
        plt.pie(values_vi_wu,explode=explode_vi_wu,labels=label_vi_wu,autopct='%1.1f%%', textprops= {'fontsize':8,'color':'black','fontproperties':font})#绘制饼图
        ax2.set_title('VI误报类别统计(' + str(self.vi_num[0]) + ')', fontproperties=font)#绘制标题

        ax3 = plt.subplot(223)
        plt.pie(values_el_lou,explode=explode_el_lou,labels=label_el_lou,autopct='%1.1f%%', textprops= {'fontsize':8,'color':'black','fontproperties':font})#绘制饼图
        ax3.set_title('EL漏报类别统计(' + str(self.el_num[1]) + ')', fontproperties=font)#绘制标题

        ax4 = plt.subplot(224)
        plt.pie(values_vi_lou,explode=explode_vi_lou,labels=label_vi_lou,autopct='%1.1f%%', textprops= {'fontsize':8,'color':'black','fontproperties':font})#绘制饼图
        ax4.set_title('VI漏报类别统计(' + str(self.vi_num[1]) + ')', fontproperties=font)#绘制标题
        
        plt.savefig(os.path.join(os.path.dirname(self.xlxs_dir), self.title))#保存图片
        plt.show()

    def count(self, xlsx_dir):
        print('loading xlsx')
        data = xlrd.open_workbook(xlsx_dir)
        print('loaded')
        table = data.sheet_by_name('过检分析')
        table2 = data.sheet_by_name('漏检分析')
        rowNum = table.nrows
        rowNum2 = table2.nrows
        el_num = [0, 0]
        vi_num = [0, 0]
        for i in tqdm(range(1, rowNum)):
            E_V = table.cell_value(i,7).lower()
            label = table.cell_value(i,8)
            first_label = label.split(',')[0]
            print(E_V, first_label)
            try:
                eval('self.' + E_V + '_wu')[first_label] += 1
                eval(E_V + '_num')[0] += 1
            except:
                continue

        for i in tqdm(range(1, rowNum2)):
            E_V = table2.cell_value(i,19).lower()
            label = table2.cell_value(i,2)
            print(E_V, label)
            try:
                eval('self.' + E_V + '_lou')[label] += 1
            except:
                eval('self.' + E_V + '_lou')[label] = 1
            eval(E_V + '_num')[1] += 1
        self.el_num = el_num
        self.vi_num = vi_num
        self.el_wu = sorted(self.el_wu.items(), key=lambda item:item[1], reverse=True)
        self.vi_wu = sorted(self.vi_wu.items(), key=lambda item:item[1], reverse=True)
        self.el_lou = sorted(self.el_lou.items(), key=lambda item:item[1], reverse=True)
        self.vi_lou = sorted(self.vi_lou.items(), key=lambda item:item[1], reverse=True)
        print('el 误报：', self.el_wu)
        print('vi 误报：', self.vi_wu)
        print('el 漏报：', self.el_lou)
        print('vi 漏报：', self.vi_lou)


if __name__ == '__main__':
    xlsx_dir = '/home/blin/Documents/中环/v1.4/1016/过漏检分析1016.xlsx'
    xlsx_dir = '/home/blin/Downloads/20201113y-过漏检及耗时统计v4.0.xlsx'
    title = '1114_108车间误报统计'
    statis = statistic(xlsx_dir, title)
    statis.draw_pie()
