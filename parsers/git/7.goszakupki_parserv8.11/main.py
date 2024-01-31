from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Form
#from ui import Example
import glob
import csv
import time
import re
from time import sleep
import requests
from bs4 import BeautifulSoup
import csv
import os.path
import os
import cfscrape
import more_itertools as mit
from random import choice, randint
from datetime import date
from lxml import html
import openpyxl
import codecs
#from playsound import playsound
import winsound

#def sound():
    #sound = os.path.dirname(__file__) + "\\sound.mp3"
    #winsound.PlaySound(sound, winsound.SND_ASYNC)
    #playsound(sound)

CSV = ''
#создание аппликации
app = QtWidgets.QApplication(sys.argv)
FLAG = 0
#инициализация формы
Form = QtWidgets.QWidget()
#ex = Example()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
#Логика

# class WinTable(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.title = "регион спарсен"
#         self.top = 700
#         self.left = 1500
#         self.width = 300
#         self.height = 150
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         sound()


if FLAG == 1:
    ui.lineEdit.setDisabled(True)

def bp(self):
    keywords = ui.lineEdit.text()
    date = ui.dateEdit.text()
    date_end = ui.dateEdit_1.text()
    if ui.checkBox.isChecked():
        ch1 = 'on'
    else:
        ch1 = 'off'
    if ui.checkBox_2.isChecked():
        ch2 = 'on'
    else:
        ch2 = 'off'
    if ui.checkBox_3.isChecked():
        ch3 = 'on'
    else:
        ch3 = 'off'
    if ui.checkBox_4.isChecked():
        ch4 = 'on'
    else:
        ch4 = 'off'
    #regions()
    #ui.lineEdit_2.setText(keywords + date+ ch1 +ch2 + ch3 + ch4)
    parser(keywords, date, date_end, ch1, ch2, ch3, ch4)
ui.pushButton.clicked.connect(bp)

"""Отмечаем все чек-боксы"""
def checking():
    ui.checkBox_reg1.toggle()
    ui.checkBox_reg2.toggle()
    ui.checkBox_reg3.toggle()
    ui.checkBox_reg4.toggle()
    ui.checkBox_reg5.toggle()
    ui.checkBox_reg6.toggle()
    ui.checkBox_reg7.toggle()
    ui.checkBox_reg8.toggle()
    ui.checkBox_reg9.toggle()
    ui.checkBox_reg10.toggle()
    ui.checkBox_reg11.toggle()
    ui.checkBox_reg12.toggle()
    ui.checkBox_reg13.toggle()
    ui.checkBox_reg14.toggle()
    ui.checkBox_reg15.toggle()
    ui.checkBox_reg16.toggle()
    ui.checkBox_reg17.toggle()
    ui.checkBox_reg18.toggle()
    ui.checkBox_reg19.toggle()
    ui.checkBox_reg20.toggle()
    ui.checkBox_reg21.toggle()
    ui.checkBox_reg22.toggle()
    ui.checkBox_reg23.toggle()
    ui.checkBox_reg24.toggle()
    ui.checkBox_reg25.toggle()
    ui.checkBox_reg26.toggle()
    ui.checkBox_reg27.toggle()
    ui.checkBox_reg28.toggle()
    ui.checkBox_reg29.toggle()
    ui.checkBox_reg30.toggle()
    ui.checkBox_reg31.toggle()
    ui.checkBox_reg32.toggle()
    ui.checkBox_reg33.toggle()
    ui.checkBox_reg34.toggle()
    ui.checkBox_reg35.toggle()
    ui.checkBox_reg36.toggle()
    ui.checkBox_reg37.toggle()
    ui.checkBox_reg38.toggle()
    ui.checkBox_reg39.toggle()
    ui.checkBox_reg40.toggle()
    ui.checkBox_reg41.toggle()
    ui.checkBox_reg42.toggle()
    ui.checkBox_reg43.toggle()
    ui.checkBox_reg44.toggle()
    ui.checkBox_reg45.toggle()
    ui.checkBox_reg46.toggle()
    ui.checkBox_reg47.toggle()
    ui.checkBox_reg48.toggle()
    ui.checkBox_reg49.toggle()
    ui.checkBox_reg50.toggle()
    ui.checkBox_reg51.toggle()
    ui.checkBox_reg52.toggle()
    ui.checkBox_reg53.toggle()
    ui.checkBox_reg54.toggle()
    ui.checkBox_reg55.toggle()
    ui.checkBox_reg56.toggle()
    ui.checkBox_reg57.toggle()
    ui.checkBox_reg58.toggle()

"""Ищем по регионам"""
def regions():
    keywords = []
    if ui.checkBox_reg1.isChecked():
        keywords.append('[01]адыге дорог')
        keywords.append('[01]майкоп дорог')
    if ui.checkBox_reg2.isChecked():
        keywords.append('[02]башкортостан дорог')
        keywords.append('[02]уфа дорог')
    if ui.checkBox_reg3.isChecked():
        keywords.append('бурят дорог')
    if ui.checkBox_reg4.isChecked():
        keywords.append('Алтай дорог')
        keywords.append('барнаул дорог')
        keywords.append('горно-алтайск дорог')
    if ui.checkBox_reg5.isChecked():
        keywords.append('[07]кабардино-балкар дорог')
        keywords.append('[07]нальчик дорог')
    if ui.checkBox_reg6.isChecked():
        keywords.append('[08]калмык дорог')
        keywords.append('[08]элиста дорог')
    if ui.checkBox_reg7.isChecked():
        keywords.append('карачаев дорог')
    if ui.checkBox_reg8.isChecked():
        keywords.append('[10]карел дорог')
        keywords.append('[10]петрозаводск дорог')
    if ui.checkBox_reg9.isChecked():
        keywords.append('[11]республика коми дорог')
        keywords.append('[11]сыктывкар дорог')
    if ui.checkBox_reg10.isChecked():
        keywords.append('[12]марий эл дорог')
        keywords.append('[12]йошкар-ола дорог')
    if ui.checkBox_reg11.isChecked():
        keywords.append('[13]мордов дорог')
        keywords.append('[13]саранск дорог')
    if ui.checkBox_reg12.isChecked():
        keywords.append('осетия дорог')
    if ui.checkBox_reg13.isChecked():
        keywords.append('[16]татарстан дорог')
        keywords.append('[16]казань дорог')
    if ui.checkBox_reg14.isChecked():
        keywords.append('тыва дорог')
    if ui.checkBox_reg15.isChecked():
        keywords.append('[18]удмурт дорог')
        keywords.append('[18]ижевск дорог')
    if ui.checkBox_reg16.isChecked():
        keywords.append('хакаси дорог')
    if ui.checkBox_reg17.isChecked():
        keywords.append('чуваш дорог')
    if ui.checkBox_reg18.isChecked():
        keywords.append('[23]краснодар дорог')
    if ui.checkBox_reg19.isChecked():
        keywords.append('[26]ставрополь дорог')
        keywords.append('[26]пятигорск дорог')
        keywords.append('[26]кисловодск дорог')
    if ui.checkBox_reg20.isChecked():
        keywords.append('[29]архангельск дорог')
    if ui.checkBox_reg21.isChecked():
        keywords.append('[30]астрахан дорог')
    if ui.checkBox_reg22.isChecked():
        keywords.append('[31]белгород дорог')
    if ui.checkBox_reg23.isChecked():
        keywords.append('[32]брянск дорог')
    if ui.checkBox_reg24.isChecked():
        keywords.append('[33]владимир дорог')
    if ui.checkBox_reg25.isChecked():
        keywords.append('[34]волгоград дорог')
    if ui.checkBox_reg26.isChecked():
        keywords.append('[35]волог дорог')
        keywords.append('[35]череповец дорог')
    if ui.checkBox_reg27.isChecked():
        keywords.append('[36]воронеж дорог')
    if ui.checkBox_reg28.isChecked():
        keywords.append('[37]иванов дорог')
    if ui.checkBox_reg29.isChecked():
        keywords.append('[40]калуга дорог')
        keywords.append('[40]калуж дорог')
    if ui.checkBox_reg30.isChecked():
        keywords.append('кемеров дорог')
    if ui.checkBox_reg31.isChecked():
        keywords.append('[43]киров дорог')
    if ui.checkBox_reg32.isChecked():
        keywords.append('[44]костром дорог')
    if ui.checkBox_reg33.isChecked():
        keywords.append('курган дорог')
    if ui.checkBox_reg34.isChecked():
        keywords.append('[46]курск дорог')
    if ui.checkBox_reg35.isChecked():
        keywords.append('[47]ленинград дорог')
    if ui.checkBox_reg36.isChecked():
        keywords.append('[48]липецк дорог')
    if ui.checkBox_reg37.isChecked():
        keywords.append('москва дорог')
        keywords.append('московск дорог')
    if ui.checkBox_reg38.isChecked():
        keywords.append('[51]мурманск дорог')
    if ui.checkBox_reg39.isChecked():
        keywords.append('[52]нижний новгород дорог')
        keywords.append('[52]нижегород дорог')
    if ui.checkBox_reg40.isChecked():
        keywords.append('[53]великий новгород дорог')
        keywords.append('[53]новгородск дорог')
    if ui.checkBox_reg41.isChecked():
        keywords.append('[56]орел дорог')
        keywords.append('[56]орловск дорог')
    if ui.checkBox_reg42.isChecked():
        keywords.append('[58]пенз дорог')
    if ui.checkBox_reg43.isChecked():
        keywords.append('[59]перм дорог')
    if ui.checkBox_reg44.isChecked():
        keywords.append('[60]псков дорог')
    if ui.checkBox_reg45.isChecked():
        keywords.append('[61]ростов дорог')
    if ui.checkBox_reg46.isChecked():
        keywords.append('[62]рязан дорог')
    if ui.checkBox_reg47.isChecked():
        keywords.append('[63]самар дорог')
    if ui.checkBox_reg48.isChecked():
        keywords.append('[64]саратов дорог')
    if ui.checkBox_reg49.isChecked():
        keywords.append('[67]смоленск дорог')
    if ui.checkBox_reg50.isChecked():
        keywords.append('[68]тамбов дорог')
    if ui.checkBox_reg51.isChecked():
        keywords.append('[69]твер дорог')
    if ui.checkBox_reg52.isChecked():
        keywords.append('[71]тула дорог')
        keywords.append('[71]тульск дорог')
    if ui.checkBox_reg53.isChecked():
        keywords.append('тюмен дорог')
    if ui.checkBox_reg54.isChecked():
        keywords.append('[73]ульяновск дорог')
    if ui.checkBox_reg55.isChecked():
        keywords.append('челябинск дорог')
    if ui.checkBox_reg56.isChecked():
        keywords.append('[76]ярослав дорог')
    if ui.checkBox_reg57.isChecked():
        keywords.append('[78]санкт-петербург дорог')
    if ui.checkBox_reg58.isChecked():
        keywords.append('[27]Красноярск дорог')
        keywords.append('[27]Ачинск дорог')
        keywords.append('[27]Боготол дорог')
        keywords.append('[27]Бородино дорог')
        keywords.append('[27]Дивногорск дорог')
        keywords.append('[27]Енисейск дорог')
        keywords.append('[27]Канск дорог')
        keywords.append('[27]Лесосибирск дорог')
        keywords.append('[27]Минусинск дорог')
        keywords.append('[27]Назарово дорог')
        keywords.append('[27]Норильск дорог')
        keywords.append('[27]Сосновоборск дорог')
        keywords.append('[27]Шарыпово дорог')
    FLAG = 1
    for key in keywords:
        bp_reg(key)
def bp_reg(keywords):
    date = ui.dateEdit.text()
    date_end = ui.dateEdit_1.text()
    if ui.checkBox.isChecked():
        ch1 = 'on'
    else:
        ch1 = 'off'
    if ui.checkBox_2.isChecked():
        ch2 = 'on'
    else:
        ch2 = 'off'
    if ui.checkBox_3.isChecked():
        ch3 = 'on'
    else:
        ch3 = 'off'
    if ui.checkBox_4.isChecked():
        ch4 = 'on'
    else:
        ch4 = 'off'
    #ui.lineEdit_2.setText(keywords + date+ ch1 +ch2 + ch3 + ch4)
    parser(keywords, date, date_end, ch1, ch2, ch3, ch4)
ui.pushButton_reg2.clicked.connect(regions)
ui.pushButton_reg.clicked.connect(checking)
HOST = 'https://zakupki.gov.ru/'
URL = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

start_time = time.time()


# In[ ]:


def get_proxies():
    """Получение списка проксей с hidemy"""
    scraper = cfscrape.create_scraper()
    content = scraper.get("https://hidemy.name/en/proxy-list/?&maxtime=600&type=h&anon=34#list").content
    soup = BeautifulSoup(content, 'lxml')

    proxy = []

    td = soup.find_all('td')
    td_list = []
    for a in td:
        td_list.append(a.text)

    i = 0
    while i < len(td_list):
        proxy.append(str(td_list[i] + ':' + td_list[i + 1]))
        i += 7

    proxy_list = list(set(proxy))
    try:
        proxy_list.remove('IP address:Port')
    except ValueError:
        pass

    return proxy_list


def get_proxy(proxy_list):
    try:
        random_proxy = choice(proxy_list)
        return random_proxy
    except:
        return None


def myip(head, random_proxy):
    """Проверка работоспособности прокси сервера"""

    scraper = cfscrape.create_scraper()

    # Проверка работосопособности прокси-сервера
    try:
        rp = scraper.get('https://ru.infobyip.com',
                         headers=head,
                         proxies={'https': 'http://' + random_proxy,
                                  'http': 'http://' + random_proxy}, allow_redirects=False)

        soup = BeautifulSoup(rp.content, 'lxml')

        try:
            current_ip = soup.find("div", {"class": "yourip"}).text
            # Если всё ОК, вернётся ip-адрес текущего прокси-сервера
            return current_ip

        except AttributeError:
            print('IP не найден')
            return None
    except:
        print('Дохлый proxy', random_proxy)
        return None


def get_working_proxy():
    """Функция для вызова из кода, возвращает рабочий ip адрес прокси-сервера"""

    _proxy_list = get_proxies()

    _working_proxy = None

    _random_proxy = get_proxy(_proxy_list)
    #     for _random_proxy in _proxy_list:

    #         if myip(HEADERS, _random_proxy) is not None:
    #             _working_proxy = _random_proxy
    #             break
    #         else:
    #             continue
    #     if _working_proxy is None:
    #         get_working_proxy()

    return _random_proxy


def get_last_page_num(parsed_body):
    """Получение номера последней страницы с постами"""

    # Получение и приведение типа номера последней страницы
    try:
        last_page_num = (BeautifulSoup(parsed_body, 'html.parser').find('div', class_='search-results__total').get_text(strip=True))
        print(last_page_num)
        l = len(last_page_num)
        res = ''
        i = 0
        integ =[]
        for i in range(l):
            a = last_page_num[i]
            if '0' <= a <= '9':
                res += a
                i += 1
                # if i < l:
                #     a = last_page_num[i]
                # else:
                #     break
        last_page_num = res
        print(last_page_num)
        last_page_num = int(last_page_num)
        last_page_num = (last_page_num // 50) + 2
        print(last_page_num)
    except:
        last_page_num = 1
    return last_page_num


def get_html(url, proxy, params=''):
    """Получение объекта страницы"""

    if proxy is None:
        r = requests.get(url, headers=HEADERS, params=params)
    else:
        r = requests.get(url, headers=HEADERS, params=params, proxies={'https': 'http://' + proxy,
                                                                       'http': 'http://' + proxy},
                         allow_redirects=False)

    sleep(1)

    return r


def get_content(html):
    """Парсер html, возвращает список нужных элементов страницы"""

    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='row no-gutters registry-entry__form mr-0')
    cards = []
    i = 1
    for item in items:
        try:
            title = item.find('div', class_='registry-entry__header-mid__number').get_text(strip=True)
        except:
            title = ''
        try:
            link_card = HOST + item.find('div', class_='registry-entry__header-mid__number').find('a').get('href')
        except:
            link_card = ''
        try:
            status = item.find('div', class_='registry-entry__header-mid__title').get_text(strip=True)
        except:
            status = ''
        try:
            obj_short = item.find('div', class_='registry-entry__body-value').get_text(strip=True)
            obj_short = re.sub("^\s+|\n|\r|\s+$", '', obj_short)
        except:
            obj_short = ''
        try:
            org = item.find('div', class_='registry-entry__body-href').get_text(strip=True)
        except:
            org = ''
        try:
            date_first = item.find('div', class_='data-block__value').get_text()
        except:
            date_first = ''
        try:
            price = item.find('div', class_='price-block__value').get_text(strip=True)
            price = price[:-1]
        except:
            price = ''
        if status == 'Определение поставщика завершено':
            try:
                link_suppler = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber=' + title[2:]
            except:
                link_suppler = ''
            #   try:
            temp = title[2:]
            url2 = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber=' + temp
            # print(url2)
            tempos = get_html(url2, proxy=None).content.decode('utf-8')
            soup = BeautifulSoup(tempos, 'html.parser')
            suppler = soup.findAll('tbody', class_='tableBlock__body')
            box = []
            for supple in suppler:
                out = supple.findAll('td', 'tableBlock__col')
                # j = 0
                for o in out:
                    print(o.text)
                    print('----')
                    # box[j] = o.text
                    # j = j + 1
                    box.append(re.sub(' +', ' ', o.text.replace('\n', '')).strip())
            box = '\t'.join(box)
            box = re.split(r'\t', box)
            #print(box)
            str1 = ''
            str2 = ''
            str3 = ''
            str4 = ''
            str5 = ''
            str6 = ''
            str7 = ''
            try:
                str1 = re.sub("\t", '', box[0])
            except:
                str1 = ''
            try:
                str2 = re.sub("\t", '', box[1])
            except:
                str2 = ''
            try:
                str3 = re.sub("\t", '', box[2])
            except:
                str3 = ''
            try:
                str4 = re.sub("\t", '', box[3])
            except:
                str4 = ''
            try:
                str5 = re.sub("\t", '', box[4])
            except:
                str5 = ''
            try:
                str6 = re.sub("\t", '', box[5])
            except:
                str6 = ''
            try:
                str7 = re.sub("\t", '', box[6])
            except:
                str7 = ''
            try:
                url3 = 'https://zakupki.gov.ru/epz/order/notice/rpec/search-results.html?orderNum=' + temp
                print(url3)
                tempos = get_html(url3, proxy=None).content.decode('utf-8')
                soup = BeautifulSoup(tempos, 'html.parser')
                link_inn = soup.find('a').get('href')
                print(link_inn)
                url4 = HOST + link_inn
                print(url4)
                tempos = get_html(url4, proxy=None).content.decode('utf-8')
                soup = BeautifulSoup(tempos, 'html.parser')
                inn = soup.find_all('span', class_='section__info')[-2].get_text(strip=True)
                print("ИНН: " + inn)
                """ПОлучаем урл карточки контракта"""
                url4 = 'https://zakupki.gov.ru/epz/contract/search/results.html?searchString=&orderNumber='
                + temp 
                + '&openMode=USE_DEFAULT_PARAMS&fz44=on&priceFrom=0&priceTo=200000000000&contractStageList=0%2C1%2C2%2C3&budgetaryFunds = on & extraBudgetaryFunds = on'
                #url4 = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html?regNumber=' + temp
                print(url4)
                tempos = get_html(url4, proxy=None).content.decode('utf-8')
                soup = BeautifulSoup(tempos, 'html.parser')
                contract_url = soup.find('div', class_='registry-entry__header-mid__number').find('a').get('href')
                print(contract_url)
                """Забираем срок и контакты из карточки"""
                url5 = HOST + contract_url
                tempos = get_html(url5, proxy=None).content.decode('utf-8')
                soup = BeautifulSoup(tempos, 'html.parser')
                contract_start = soup.find_all('span', class_='cardMainInfo__content')[4].get_text(strip=True)
                print(contract_start)
                contract_end = soup.find_all('span', class_='cardMainInfo__content')[5].get_text(strip=True)
                print(contract_end)
                contract_number = soup.find('span', class_='cardMainInfo__purchaseLink').get_text(strip=True)
                contract_number = contract_number[2:]
                print(contract_number)
                """ПОлучаем контакты поставщика"""
                url6 = 'https://zakupki.gov.ru//epz/contract/contractCard/participants.html?reestrNumber=' + contract_number
                adress = soup.find_all('td', class_='tableBlock__col')[2].get_text(strip=True)
                print(adress)
                contacts = soup.find_all('td', class_='tableBlock__col')[4].get_text(strip=True)
                print(contacts)
            except:
                print('нет')
                inn = ''
                contract_start = ''
                contract_end = ''
                adress = ''
                contacts = ''
            tempa = str(str2).replace(" ", "+")
            tempas = str(str5).replace(" ", "+")
            fio = ''
            fio1 = ''
            address = ''
            address1 = ''
            inn1 = ''
            """Забираем сведения о контратке из реееста контрактов"""
            try:
                tempos = get_html(url2, proxy=None).content.decode('utf-8')
                soup = BeautifulSoup(tempos, 'html.parser')
                table = soup.findAll('tbody', class_='tableBlock__body')[-1].find('tr', class_='tableBlock__row')\
                    .find('td', class_='tableBlock__col').find('a').get('href')
                print(table)
                link_reestr = HOST+ table
            except:
                print('нет реестра')
                link_reestr = ''
            #"""Забираем инн победителя"""
            # try:
            #     url3 = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber=' + temp
            #     # print(url2)
            #     tempos = get_html(url2, proxy=None).content.decode('utf-8')
            #     soup = BeautifulSoup(tempos, 'html.parser')
            #     suppler = soup.find_all('tbody', class_='tableBlock__body')
            # host_link = 'https://www.list-org.com/'
            # url_list_pobed = 'https://www.list-org.com/search?type=all&val=' + tempa
            # url_list_vtoroi = 'https://www.list-org.com/search?type=all&val=' + tempas
            # print(url_list_pobed)
            # print(url_list_vtoroi)
            # # Получение адреса прокси
            # random_proxy = get_working_proxy()
            #
            #     # Получаем страницу через прокси-сервер
            #     #r1 = session.get(url_list_pobed, headers=HEADERS, proxies={'http': 'http://' + random_proxy}).content.decode('utf-8')
            #     #r2 = session.get(url_list_vtoroi, headers=HEADERS, proxies={'http': 'http://' + random_proxy}).content.decode('utf-8')
            # #r1 = requests.get(url_list_pobed, headers=HEADERS, proxies={'http': 'http://' + random_proxy}, allow_redirects=False).content.decode('utf-8')
            # #r2 = requests.get(url_list_vtoroi, headers=HEADERS, proxies={'http': 'http://' + random_proxy}, allow_redirects=False).content.decode('utf-8')
            # r1 = get_html(url_list_pobed, proxy=None).content.decode('utf-8')
            # r2 = get_html(url_list_vtoroi, proxy=None).content.decode('utf-8')
            # print(r1)
            # print('------')
            # print(r2)
            # print('------')
            #     #tempi = get_html_with_proxy(test).content.decode('utf-8')
            #     #tempi.status_code
            #     #print(tempi.status_code)
            #     #tempos = get_html_with_proxy(url_list_pobed).content.decode('utf-8')
            #     #if tempos.status_code == 200:
            # soup = BeautifulSoup(r1, 'html.parser')
            # company = soup.find('div', class_='org_list').find('a').get('href')
            # print(company)
            # url_target = host_link + company
            # target = session.get(url_target, headers=HEADERS, proxies={'http': 'http://' + random_proxy}).content.decode('utf-8')
            # soup = BeautifulSoup(target, 'html.parser')
            # fio = soup.find('a', class_='upper').get_text()
            # print(fio)
            # address = soup.find_all('div', class_='c2m')[1].get_text(strip=True) #.find('span', class_='upper')
            # print(address)
            # inn = soup.find_all('div', class_='c2m')[2].find('p').get_text()
            #     #парсим данные второго номера#
            #     #tempos = get_html_with_proxy(url_list_vtoroi).content.decode('utf-8')
            #     #print(tempos)
            # soup = BeautifulSoup(r2, 'html.parser')
            # company = soup.find('div', class_='org_list').find('a').get('href')
            # print(company)
            # url_target1 = host_link + company
            # target = session.get(url_target1, headers=HEADERS, proxies={'http': 'http://' + random_proxy}).content.decode('utf-8')
            # print(target)
            # soup = BeautifulSoup(target, 'html.parser')
            # fio1 = soup.find('a', class_='upper').get_text()
            # print(fio1)
            # address1 = soup.find_all('div', class_='c2m')[1].get_text(strip=True)  # .find('span', class_='upper')
            # print(address1)
            # inn1 = soup.find_all('div', class_='c2m')[2].find('p').get_text()
            # except:
            #    str1 = ''
            #    str2 = ''
            #    str3 = ''
            #    str4 = ''
            #    str5 = ''
            #    str6 = ''
            #    str7 = ''
            #    fio = ''
            #    address = ''
            #    inn = ''
            #    fio1 = ''
            #    address1 = ''
            #    inn1 = ''
            ### Функция загрузки файлов###
            # try:
            #    """Загрузка вложений"""
            #    url3 = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/documents.html?regNumber=' + temp
            #    files_prepare = get_html(url3).content.decode('utf-8')
            #    soup = BeautifulSoup(files_prepare, 'html.parser')
            #    files = soup.find_all('span', class_='section__value')
            # print(files)
            # print('--------------')
            #    box = []
            #    for file in files:
            #        out = file.find('a')
            #        print(out.get('href'))
            #        print(out.get('title'))
            #        name = out.get('title')
            #        print('--------------')
            #        url = out.get('href')
            #        os.chdir("docs")
            # print(os.getcwd())
            #        os.makedirs("№" + temp, exist_ok=True)
            #       os.chdir("№" + temp)
            #        print(os.getcwd())
            #        #path = r'..\№' + temp + '\Z' + name
            #        r = requests.get(url, allow_redirects=True, headers=HEADERS)
            #        with open(name, 'wb') as f:
            #            f.write(r.content)
            #        os.chdir("..")
            #        print(os.getcwd())
            #        os.chdir("..")
            #        print(os.getcwd())
            #        print('Файл загружен')
            # except:
            #    pass
        else:
            link_suppler = ''
            str1 = ''
            str2 = ''
            str3 = ''
            str4 = ''
            str5 = ''
            str6 = ''
            str7 = ''
            fio = ''
            address = ''
            inn = ''
            fio1 = ''
            address1 = ''
            inn1 = ''
            contract_start = ''
            contract_end = ''
            adress = ''
            contacts = ''
            link_reestr = ''
        cards.append(
            {
                'title': title,
                'link_card': link_card,
                'status': status,
                'obj_short': obj_short,
                'org': org,
                'date_first': date_first,
                'price': price,
                'link_suppler': link_suppler,
                'str1': str1,
                'str2': str2,
                'str3': str3,
                'str4': str4,
                'str5': str5,
                'str6': str6,
                'str7': str7,
                'contract_start': contract_start,
                'contract_end': contract_end,
                'fio': fio,
                'adress': adress,
                'inn': inn,
                'contacts': contacts,
                'link_reestr': link_reestr
            }
        )
        print(f'Спарсено {i} карточек')
        #output_line('Процесс закончен')
        i = i + 1
    return cards


def save_doc(items, path, outxls):
    """Сохраняет csv файл для элементов списка cards"""

    with open(path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ['№ закупки', 'Ссылка на продукт', 'Статус', 'Описание объекта', 'Организация', 'Дата размещения','Цена', 'Ссылка на поставщика', 'Заказчик','Победитель', 'ИНН', 'Статус№1', 'Цена победителя', '№2', 'Статус №2', 'Цена №2','Дата окончания контракта', 'Дата начала контракта', 'Ссылка на реестровую запись', 'Адрес', 'Контакты', 'ФИО Руководителя'])
        for item in items:
            writer.writerow(
                [item['title'], item['link_card'], item['status'], item['obj_short'], item['org'], item['date_first'],item['price'], item['link_suppler'],item['str1'], item['str2'], item['inn'], item['str3'], item['str4'], item['str5'], item['str6'], item['str7'],
                item['contract_start'], item['contract_end'], item['link_reestr'], item['adress'], item['contacts'], item['fio']])
    save_xls(path)

"""Экспорт в xlsx"""
def save_xls(csvfile):
        wb = openpyxl.Workbook()
        ws = wb.active
        with open(csvfile, mode='r', encoding='utf-8') as f:
            reader = csv.reader((line.replace('\0','') for line in f), delimiter=';')
            for r, row in enumerate(reader, start=1):
                for c, val in enumerate(row, start=1):
                    ws.cell(row=r, column=c).value = val
        wb.save(csvfile[:-3] + '.xlsx')


def output_line(line):
    text = line
    ui.lineEdit_2.setText(text)

def parser(keywords, date, date_end, ch1, ch2, ch3, ch4):
    zapros = keywords
    print(zapros)
    SEARCH_STRING = keywords[4:]
    print(SEARCH_STRING)
    SEARCH_STRING = str(SEARCH_STRING).replace(" ", "+")
    DATE_START = date
    DATE_END = date_end
    af = ch1
    ca = ch2
    pc = ch3
    pa = ch4
    if DATE_END == '01.01.2000':
        DATE_END = ''
    if SEARCH_STRING.isdecimal():
        URL1 = f'https://zakupki.gov.ru/epz/contract/search/results.html?morphology=on&search-filter=%D0%A6%D0%B5%D0%BD%D0%B5&fz44=on&supplierTitle={SEARCH_STRING}&sortBy=PRICE&sortDirection=false&recordsPerPage=_50'
    else:
        URL1 = URL + '?searchString=' + SEARCH_STRING + '&morphology=on&&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false&sortBy=PUBLISH_DATE&fz44=on&fz223=on&af=' + af + '&ca=' + ca + '&pc=' + pc + '&pa=' + pa + '&currencyIdGeneral=-1&publishDateFrom=' + DATE_START +'&&publishDateTo=' + DATE_END
    print(URL1)
    CSV = zapros + DATE_START + '-' + DATE_END + '.csv'
    OUTXLS = SEARCH_STRING + DATE_START + '.xls'
    print(f'Файл с результатом: {CSV}')
    # os.makedirs("docs", exist_ok=True) //Загрузка файлов
    # print(os.getcwd())

    html = get_html(URL1, proxy=None)

    last_page = get_last_page_num(html.content.decode('utf-8'))
    # printProgressBar(0, last_page, prefix='Выполнение:', suffix='Выполнение закончено', length=50)
    if html.status_code == 200:
        cards = []
        j = 0
        for page in range(1, last_page + 1):
#            ex.handleTimer(page, last_page)
            print(f'Парсим страницу: {page}/{last_page}')
            pagetmp = str(page)
            pagenum = '&pageNumber=' + pagetmp
            print(URL1 + pagenum)
            html = get_html(URL1 + pagenum, proxy=None)
            # print(html)
            cards.extend(get_content(html.text))
            save_doc(cards, CSV, OUTXLS)
            # printProgressBar(j + 1, last_page, prefix='Выполнение:', suffix='Выполнение закончено', length=50)
        pass
        print("Спарсено за %s минут ---" % ((time.time() - start_time) / 60))
#        ui.winTable = WinTable()
#        ui.winTable.show()
    else:
        print('Error')
#Run main loop
sys.exit(app.exec_())