#coding:utf-8  
''''' 
@author: linbofan@matrixtime.com
'''  
import pandas as pd
import csv
from urllib import request
import requests
import re   
from bs4 import BeautifulSoup  
from distutils.filelist import findall  
from selenium import webdriver
import time
import argparse
from selenium.webdriver.common.action_chains import ActionChains
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', default='./single.csv', type=str)
parser.add_argument('--output_file', default='./output.csv', type=str)
parser.add_argument('--output_pic_file', default='./output_pic.csv', type=str)

args = parser.parse_args()
# pic_list = pd.read_csv(args.input_file)
input_fl = open(args.input_file)
pic_list = csv.reader(input_fl)
browser = webdriver.Chrome()
browser.get('http://10.227.40.27:8888/mycim2/main/main.html?version=1.0')
# 登录
browser.find_element_by_name("username").send_keys("CS1")
browser.find_element_by_name("password").send_keys("123456")
browser.find_element_by_class_name("i5k-login-button").click()

# url = browser.current_url
login_handle = browser.current_window_handle
handles = browser.window_handles

while len(handles) == 1:
    time.sleep(0.5)
    handles = browser.window_handles

out_file = open(args.output_file, 'a', newline='' "")
out_pic_file = open(args.output_pic_file, 'a', newline='' "")
writer = csv.writer(out_file)
writer2 = csv.writer(out_pic_file)
writer.writerow(["不良原因", "不良位置", "判定工步", "判定日期", "判断时间", "判定人员", "版型", "电池片数", "组件号"])
writer2.writerow(["组件号", "判定日期", "路径"])
# 组件查询
part_search = "/html/body/div[2]/div[1]/div[2]/div[2]/div[1]"
# 查询组件详细信息
detailed_part_search = "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]"
# 组件EL测试与IV测试信息查询
EL_search = "/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]"
# 切换到弹出窗口
interface_handle = None
for handle in handles:
    if handle != login_handle:
        interface_handle = handle
browser.switch_to_window(interface_handle)
browser.find_element_by_xpath(part_search).click()
browser.find_element_by_xpath(detailed_part_search).click()



for i, pic in enumerate(pic_list):

    out_file = open(args.output_file, 'a', newline='' "")
    out_pic_file = open(args.output_pic_file, 'a', newline='' "")
    writer = csv.writer(out_file)
    writer2 = csv.writer(out_pic_file)
    # 切换框架 查询组件详细信息——搜索框
    browser.switch_to_frame("mainFrame")
    base_name = pic[0].split('/')[-1].split('.')[0]
    pic_name = pic[0].split('/')[-1].split('.')[0].split('_')[0]
    print(i, pic_name)
    browser.find_element_by_name("lotId").clear()
    browser.find_element_by_name("lotId").send_keys(pic_name)
    # 确认
    browser.find_element_by_xpath("/html/body/table[3]/tbody/tr/td/table[2]/tbody/tr/td/div/input[1]").click()
    try:
        # alert = browser.switch_to_alert()
        browser.switch_to.alert.accept()
        # alert.find_element_by_link_text("确定").click()
        print("批次不存在!")
        browser.switch_to_window(interface_handle)
        # browser.switch_to_frame("mainFrame")
        
        continue
    except:
        print("找到批次！")

    piece_nums_ele = browser.find_elements_by_xpath('//*[@id="fld1"]/table/tbody/tr[6]/td[2]/input')
    piece_model_ele = browser.find_elements_by_xpath('//*[@id="fld1"]/table/tbody/tr[2]/td[4]/input')   
    piece_nums = piece_nums_ele[0].get_attribute("value")
    piece_model = piece_model_ele[0].get_attribute("value")
    # print(piece_nums, piece_model)
    td_content = browser.find_elements_by_xpath('//*[@id="fld5"]/table')
    lst = []
    infos = td_content[0].text
    infos = infos.split("\n")
    if len(infos)>0:
        for info in infos[1:]:
            info_list = info.strip("\n").split(" ")
            info_list[4] = info_list[4][:-2]
            info_list.append(piece_model)
            info_list.append(piece_nums)
            info_list.append(pic_name + '\t')
            print(info_list)
            writer.writerow(info_list)

    # 回到default_content / EL 查询
    browser.switch_to_default_content()
    browser.find_element_by_xpath(EL_search).click()
    browser.switch_to_frame("mainFrame")
    browser.find_element_by_name("lotId").send_keys(pic_name)

    browser.find_element_by_xpath("/html/body/table[3]/tbody/tr/td/table[2]/tbody/tr/td/div/input[1]").click()
    td_content = browser.find_elements_by_xpath('//*[@id="fld11"]/table')
    td_list = td_content[0].find_elements_by_class_name("myfield")
    # url_list = td_content[0].find_elements_by_xpath('//*[@id="fld11"]/table/tbody/tr[2]/td/a')
    url_list = []
    for i in range(len(td_list)):
        url = td_content[0].find_elements_by_xpath('//*[@id="fld11"]/table/tbody/tr[' + str(i+1) + ']/td/a')
        url = url[0].get_attribute('href')
        url_list.append(url)
        r = requests.get(url)
        folder = url.split('public/')[-1].split("/")[:-1]

        save_path = './'
        for path in folder:
            save_path = save_path + "/" + path

        isExists = os.path.exists(save_path)
        if not isExists:
            os.makedirs(save_path)
        save_img = save_path + '/' + base_name + '.jpg'
        with open(save_img, 'wb') as f:
            f.write(r.content)
        f.close()
    time_list = []
    for td in td_list:
        time_list.append(td.text)
    
    for i, td in enumerate(time_list):
        write_list = []
        write_list.append(base_name + '\t')
        write_list.append(td + '\t')
        write_list.append(url_list[i])
        writer2.writerow(write_list)
    # pic_info = td_content[0].text
    # urls = td_content[0].href
    # print(pic_info, urls)

    
    browser.switch_to_default_content()
    browser.find_element_by_xpath(detailed_part_search).click()
    out_file.close()
    out_pic_file.close()
# print(lst)