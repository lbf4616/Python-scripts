import requests
from lxml import etree
import time
import prettytable as pt
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
import re
  
  
class PraseHTML():
    def __init__(self, url):
        self.url = url

    def get_accounts(self):
        tb = pt.PrettyTable()
        # page = requests.get(self.url)
        # page.encoding='utf-8'
        # html = etree.HTML(page.text, parser=etree.HTMLParser(encoding='utf-8'))
        # good_list = html.xpath('//div[@class="goods_item"]')
        response = requests.get(self.url)
        accont_ls = response.json()["data"]
        tb.field_names = ["TITLE", "CAR", "PRICE", "UPDATE TIME", "URL"]

        for accont in accont_ls[:]:
            try:
                car = int(re.findall('稀有载具:(.*),', accont["accountName"])[0])
            except:
                continue
            if car >= 7:
                response = requests.get('https://www.xizai.com/trade/api/accountinfo?ids=' + str(accont["accountId"]))
                price = response.json()["accountInfoList"][0]["price"]
                if response.json()["accountInfoList"][0]["secondaryName"] != 1:
                    continue
                    
                url = 'https://www.xizai.com/goods?accountId=' + str(accont["accountId"])
                
                tb.add_row([accont["accountName"], car, price, accont["shopTime"], url])

        return tb


if __name__ == "__main__":
    import os
    import datetime

    graber = PraseHTML('https://www.xizai.com/trade/api/accountinfolist?pageSize=1000&pageNum=1&categoryId=26&tradeType=2&gameJson=%E5%AE%89%E5%8D%93QQ')
    while True:
        now_time = datetime.datetime.now()
        tb = graber.get_accounts()
        a = os.system('clear')
        print(now_time.strftime('%Y-%m-%d %H:%M:%S'))
        print(tb)
        input()