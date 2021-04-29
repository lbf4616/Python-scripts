import requests
from lxml import etree
import time
import prettytable as pt
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
import re
  
  
class PraseHTML():
    def __init__(self, url, dollar):
        self.url = url
        self.dollar = dollar
        self.eth_income_xpath = '/html/body/div[1]/div[1]/div/section[3]/div[2]/div/div[1]/table/tbody/tr[10]/td/div/div/div[2]/div/div[2]/div/div[3]/span[3]/div/span[2]/text()'
        self.eth_price_xpath = '/html/body/div[1]/div[1]/div/section[3]/div[2]/div/div[1]/table/tbody/tr[9]/td[4]/span[2]/text()'
        self.eth_yield_xpath = '/html/body/div[1]/div[1]/div/section[3]/div[2]/div/div[1]/table/tbody/tr[10]/td/div/div/div[2]/div/div[2]/div/div[3]/span[1]/text()'
        self.cfx_price_xpath = "/html/body/div[1]/div[1]/div/section[3]/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/span[2]/text()"
        self.cfx_yield_xpath = '/html/body/div[1]/div[1]/div/section[3]/div[2]/div/div[2]/table/tbody/tr[4]/td/div/div/div[2]/div/div[2]/div/div[3]/span[1]/text()'
        self.cfx_income_xpath = '/html/body/div[1]/div[1]/div/section[3]/div[2]/div/div[2]/table/tbody/tr[3]/td[5]/span[2]/text()'
        self.Hash = '/html/body/div[1]/div[1]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/table/thead/tr[2]/td[2]'
        self.revenue = '/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[4]/div/div/text()'

    def get_prices(self):
        tb = pt.PrettyTable()
        page = requests.get(self.url)
        page.encoding='utf-8'
        html = etree.HTML(page.text, parser=etree.HTMLParser(encoding='utf-8'))

        page_eth = requests.get(eth_wallet)
        page_eth.encoding='utf-8'
        html_eth = etree.HTML(page_eth.text, parser=etree.HTMLParser(encoding='utf-8'))

        # print(page_eth.text)

        page_cfx = requests.get(cfx_wallet)
        page_cfx.encoding='utf-8'
        html_cfx = etree.HTML(page_cfx.text, parser=etree.HTMLParser(encoding='utf-8'))

        # print(etree.tostring(html.xpath(self.cfx_income_xpath)[0]))
        eth_yield = html.xpath(self.eth_yield_xpath)[0].strip()
        eth_price = round(float(html.xpath(self.eth_price_xpath)[0].strip()), 4)
        eth_income = html.xpath(self.eth_income_xpath)[0].strip()
        eth_revenue = html_eth.xpath(self.revenue)[0].strip()
        # eth_hash_idx = re.findall('<td class="hash-15m">(.*)<span', page_eth.text)

        eth_hash = re.findall('<td class="hash-15m">(.*)\n', page_eth.text.strip())[0] + ' MH/s'

        

        cfx_yield = html.xpath(self.cfx_yield_xpath)[0].strip()
        cfx_price = round(float(html.xpath(self.cfx_price_xpath)[0].strip()), 4)
        cfx_income = html.xpath(self.cfx_income_xpath)[0].strip()
        cfx_hash = re.findall('<td class="hash-15m">(.*)\n', page_cfx.text.strip())[0] + ' MH/s'
        cfx_revenue = html_cfx.xpath(self.revenue)[0].strip()

        tb.field_names = ["NAME", "PRICE ($)", "PRICE (¥)", "Revenue / M", "$ / M", "¥ / M", "2080TI (¥)", "15m Hash", "Revenue"]
        if 51.5 * float(eth_income) > 65.7 * float(cfx_income):
            tb.add_row([Fore.LIGHTRED_EX + "ETH",eth_price, round(eth_price* self.dollar,4), eth_yield, round(float(eth_income), 3), round(float(eth_income) * self.dollar, 3), str(round(float(eth_income) * self.dollar * 51.5, 3)),
                        eth_hash, eth_revenue + Fore.RESET])
            tb.add_row(["CFX",cfx_price, round(cfx_price * self.dollar, 4), cfx_yield, round(float(cfx_income), 3), round(float(cfx_income) * self.dollar, 3), round(float(cfx_income) * self.dollar * 65.7, 3), 
                        cfx_hash, cfx_revenue])
        else:
            tb.add_row(["ETH",eth_price, round(eth_price* self.dollar,4), eth_yield, round(float(eth_income), 3), round(float(eth_income) * self.dollar, 3), str(round(float(eth_income) * self.dollar * 51.5, 3)), 
                        eth_hash, eth_revenue])
            tb.add_row([Fore.LIGHTRED_EX + "CFX",cfx_price, round(cfx_price * self.dollar, 4), cfx_yield, round(float(cfx_income), 3), round(float(cfx_income) * self.dollar, 3), str(round(float(cfx_income) * self.dollar * 65.7, 3)), 
                        cfx_hash, cfx_revenue + Fore.RESET])

        return tb


if __name__ == "__main__":
    import os
    import datetime

    dollar = 6.5
    eth_wallet = 'https://www.f2pool.com/mining-user-eth/df7576922c894000153a1184f68015e4'
    cfx_wallet = 'https://www.f2pool.com/mining-user-cfx/df7576922c894000153a1184f68015e4'
    graber = PraseHTML('https://www.f2pool.com/', dollar)
    while True:
        now_time = datetime.datetime.now()
        tb = graber.get_prices()
        a = os.system('clear')
        print(now_time.strftime('%Y-%m-%d %H:%M:%S'))
        print(tb)
        input()

# <span class="price-val money-val" data-usd-per="0.08056446" data-usd="0.08056446" data-rule="formatPriceWithoutSeparator">0.5202</span>