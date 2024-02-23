import json
import os
import random

import requests
import glob
import concurrent.futures

import time

import requests
from bs4 import BeautifulSoup
import pdb

def get_proxy(page):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.kuaidaili.com/free/fps/' + str(page) + '/', headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    # table class="table table-b table-bordered table-striped"
    table = soup.find('table', class_='table table-b table-bordered table-striped')

    tr = table.find_all('tr')

    result = []

    for i in tr:
        try:
            result.append({
                'https': 'http://' + i.find_all('td')[0].get_text() + ':' + i.find_all('td')[1].get_text()
            })
        except:
            continue

    return result

# def get_proxy(page):
#     cookies = {
#         'channelid': '0',
#         'sid': '1708006578792712',
#         '_gid': 'GA1.2.765037959.1708006580',
#         '__51uvsct__K3h4gFH3WOf3aJqX': '1',
#         '__51vcke__K3h4gFH3WOf3aJqX': '90aaef22-4169-5a61-9b85-c7f8454bcfa3',
#         '__51vuft__K3h4gFH3WOf3aJqX': '1708006583700',
#         '_gcl_au': '1.1.949383800.1708007133',
#         '_ga_DC1XM0P4JL': 'GS1.1.1708007133.1.1.1708007328.11.0.0',
#         '_ga': 'GA1.1.416113693.1708006580',
#         '__vtins__K3h4gFH3WOf3aJqX': '%7B%22sid%22%3A%20%225ee25d26-a895-5584-8ab5-d2e2c8b16709%22%2C%20%22vd%22%3A%208%2C%20%22stt%22%3A%20745318%2C%20%22dr%22%3A%204616%2C%20%22expires%22%3A%201708009129016%2C%20%22ct%22%3A%201708007329016%7D',
#     }

#     headers = {
#         'authority': 'www.kuaidaili.com',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'accept-language': 'zh-CN,zh;q=0.9',
#         'cache-control': 'max-age=0',
#         # 'cookie': 'channelid=0; sid=1708006578792712; _gid=GA1.2.765037959.1708006580; __51uvsct__K3h4gFH3WOf3aJqX=1; __51vcke__K3h4gFH3WOf3aJqX=90aaef22-4169-5a61-9b85-c7f8454bcfa3; __51vuft__K3h4gFH3WOf3aJqX=1708006583700; _gcl_au=1.1.949383800.1708007133; _ga_DC1XM0P4JL=GS1.1.1708007133.1.1.1708007328.11.0.0; _ga=GA1.1.416113693.1708006580; __vtins__K3h4gFH3WOf3aJqX=%7B%22sid%22%3A%20%225ee25d26-a895-5584-8ab5-d2e2c8b16709%22%2C%20%22vd%22%3A%208%2C%20%22stt%22%3A%20745318%2C%20%22dr%22%3A%204616%2C%20%22expires%22%3A%201708009129016%2C%20%22ct%22%3A%201708007329016%7D',
#         'referer': 'https://www.kuaidaili.com/free/fps/2/',
#         'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
#     }

#     response = requests.get('https://www.kuaidaili.com/free/fps/' + str(page) + '/', cookies=cookies, headers=headers)

#     soup = BeautifulSoup(response.text, 'lxml')

#     # table class="table table-b table-bordered table-striped"
#     table = soup.find('table', class_='table table-b table-bordered table-striped')

#     tr = table.find_all('tr')

#     result = []

#     for i in tr:
#         try:
#             result.append({
#                 'https': 'http://' + i.find_all('td')[0].get_text() + ':' + i.find_all('td')[1].get_text()
#             })
#         except:
#             continue

#     return result


def url_redirect(url):
    proxies = get_proxy(random.randint(1, 788))[random.randint(1, 10)]
    print(proxies)
    response = requests.get(url, proxies=proxies)

    # 获取重定向后的 url
    if response.history:
        # 获取最后一个 Response 对象
        last_response = response.history[-1]
        location_url = last_response.headers['Location']
        print(url)
        print(location_url)
        print('+++++++++++++++++++++++++')
        return location_url



def file_redirect(input_file):
    output_file = './data_1/' + os.path.basename(input_file)
    if os.path.exists(output_file):
        print(f'{output_file} exists')
        return
    print(input_file)
    json_data = json.load(open(input_file, 'r', encoding='utf-8'))
    after_json_data = []

    for i in json_data:
        for attempt in range(5):
            try:
                i['downloadUrl'] = url_redirect(i['contentUrl'])
                break
            except Exception as e:
                print(e.args)
                if attempt < 4:  # i.e. 0, 1, 2, 3
                    continue
                else:
                    print("Failed after 5 attempts")
                    return

        after_json_data.append(i)
    print(output_file)
    json.dump(after_json_data, open(output_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)



if __name__ == '__main__':
    if not os.path.exists('./data_1'):
        os.makedirs('./data_1')

    files = glob.glob('/Users/christina/Desktop/spider/pixelbay/video/data/**/*.json', recursive=True)

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     executor.map(file_redirect, files)

    for file in files:
        file_redirect(file)

# if __name__ == '__main__':
#     if not os.path.exists('./data_1'):
#         os.makedirs('./data_1')

#     files = glob.glob('/Users/christina/Desktop/spider/pixelbay/video/data/**/*.json', recursive=True)
#     # print(len(files))
#     # pdb.set_trace()

#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         executor.map(file_redirect, files)
