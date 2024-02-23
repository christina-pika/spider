from selenium import webdriver
import re
import os

# 检测是否存在data文件夹
if not os.path.exists('data_adobe'):
    os.makedirs('data_adobe')

driver = webdriver.Chrome()
# 最小化
driver.minimize_window()


def get_page(page):
    url = 'https://stock.adobe.com/jp/search/video?filters%5Bcontent_type%3Aphoto%5D=0&filters%5Bcontent_type%3Aillustration%5D=0&filters%5Bcontent_type%3Azip_vector%5D=0&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=0&filters%5Bcontent_type%3A3d%5D=0&filters%5Bcontent_type%3Aaudio%5D=0&filters%5Bcontent_type%3Aimage%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&order=relevance&safe_search=1&search_page=' + str(
        page) + '&load_type=page&search_type=pagination&get_facets=0'
    driver.get(url)
    html = driver.page_source

    # <script type="application/json" id="image-detail-json"> 正则匹配
    pattern = re.compile(r'<script type="application/json" id="image-detail-json">(.+?)</script>')
    matches = pattern.findall(html)[0]

    return matches


if __name__ == '__main__':
    for page in range(1, 101):
        if os.path.exists('./data_adobe/page_' + str(page) + '.json'):
            print('page' + str(page) + '已存在')
            continue
        else:
            print('page' + str(page) + '不存在')

            # 尝试获取数据
            try:
                result = get_page(page)
            except Exception as e:
                print(e)
                continue

            # 保存数据
            with open('./data_adobe/page_' + str(page) + '.json', 'w', encoding='utf-8') as f:
                f.write(result)
