#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# import pyexcel.ext.xlsx # no longer required if you use pyexcel >= 0.2.2
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

# In[ ]:


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
        last_page_num = int(BeautifulSoup(parsed_body, 'html.parser').find_all('span', class_='link-text')[-1].text)
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
        except:
            price = ''
        if status == 'Определение поставщика завершено':
            try:
                link_suppler = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber=' + title[
                                                                                                                      2:]
            except:
                link_suppler = ''
            #   try:
            temp = title[2:]
            url2 = 'https://zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber=' + temp
            # print(url2)
            tempos = get_html(url2, proxy=None).content.decode('utf-8')
            soup = BeautifulSoup(tempos, 'html.parser')
            suppler = soup.find_all('tbody', class_='tableBlock__body')
            # print(suppler)
            box = []
            for supple in suppler:
                out = supple.findAll('td', 'tableBlock__col')
                # j = 0
                for o in out:
                    # print(o.text)
                    # print('----')
                    # box[j] = o.text
                    # j = j + 1
                    box.append(re.sub(' +', ' ', o.text.replace('\n', '')).strip())
            box = '\t'.join(box)
            box = re.split(r'\t', box)
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
            tempa = str(str2).replace(" ", "+")
            tempas = str(str5).replace(" ", "+")
            fio = ''
            fio1 = ''
            address = ''
            address1 = ''
            inn = ''
            inn1 = ''
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
                'fio': fio,
                'address': address,
                'inn': inn,
                'fio1': fio1,
                'address1': address1,
                'inn1': inn1
            }
        )
        print(f'Спарсено {i} карточек')
        i = i + 1
    return cards


def save_doc(items, path, outxls):
    """Сохраняет csv файл для элементов списка cards"""

    with open(path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ['Номер закупки', 'Ссылка на продукт', 'Статус', 'Описание объекта', 'Организация', 'Дата размещения',
             'Цена', 'Ссылка на поставщика', 'Поле 1',
             'Поле 2', 'Поле 3', 'Поле 4', 'Поле 5', 'Поле 6', 'Поле 7', 'ФИО Руководителя (Победитель)',
             'Контактные данные (Победитель)', 'ИНН (Победитель)', 'ФИО Руководителя (Второй номер)',
             'Контактные данные (Второй номер)', 'ИНН (Второй номер)'])
        for item in items:
            writer.writerow(
                [item['title'], item['link_card'], item['status'], item['obj_short'], item['org'], item['date_first'],
                 item['price'], item['link_suppler'],
                 item['str1'], item['str2'], item['str3'], item['str4'], item['str5'], item['str6'], item['str7'],
                 item['fio'], item['address'], item['inn'], item['fio1'], item['address1'], item['inn1']])


def parser(keywords, date, ch1, ch2, ch3, ch4):
    SEARCH_STRING = keywords
    SEARCH_STRING = str(SEARCH_STRING).replace(" ", "+")
    DATE_START = date
    af = ch1
    ca = ch2
    pc = ch3
    pa = ch4
    # """Точка входа в программу"""
    # SEARCH_STRING = input('Укажите поисковой запрос: ')
    # SEARCH_STRING = str(SEARCH_STRING).replace(" ", "+")
    # print(SEARCH_STRING)
    # DATE_START = input('Укажите дату начала поиска в формате (дд.мм.гг): ')
    # DATE_START = str(DATE_START)
    # if DATE_START == '':
    #     today = date.today()
    #     DATE_START = today.strftime("%d.%m.%Y")
    #     print(DATE_START)
    # af = input('Статус "подача заявок" (on/off): ')
    # af = str(af)
    # if af == '':
    #     af = 'on'
    #     print(af)
    # ca = input('Статус "работа комиссии" (on/off): ')
    # ca = str(ca)
    # if ca == '':
    #     ca = 'on'
    #     print(ca)
    # pc = input('Статус "Закупка завершена" (on/off): ')
    # pc = str(pc)
    # if pc == '':
    #     pc = 'on'
    #     print(pc)
    # pa = input('Статус "Закупка отменена" (on/off): ')
    # pa = str(pa)
    # if pa == '':
    #     pa = 'on'
    #     print(pa)
    URL1 = URL + '?searchString=' + SEARCH_STRING + '&morphology=on&&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=' + af + '&ca=' + ca + '&pc=' + pc + '&pa=' + pa + '&currencyIdGeneral=-1&publishDateFrom=' + DATE_START
    print(URL1)
    CSV = SEARCH_STRING + DATE_START + '.csv'
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
    else:
        print('Error')


# In[ ]:


# _url = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%81%D0%B0%D0%BC%D0%B0%D1%80+%D0%B4%D0%BE%D1%80%D0%BE%D0%B3&morphology=on&&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1&publishDateFrom=01.11.2020"


# In[ ]:


# random_proxy = '90.189.116.152:3128'


# In[ ]:


# requests.get('https://ru.infobyip.com',
#                  headers=HEADERS,
#                  proxies={'https': 'http://' + random_proxy,
#                           'http': 'http://' + random_proxy}, allow_redirects=False).content


# In[ ]:


# parser(keywords, date, ch1, ch2, ch3, ch4)
# print("Спарсено за %s минут ---" % ((time.time() - start_time) / 60))
# input("Нажмите любую клавишу, чтобы продолжить")

# In[ ]:




