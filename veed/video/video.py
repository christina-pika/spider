# https://www.veed.io/videos?1d67476d_page=1

import os
from selenium import webdriver
from bs4 import BeautifulSoup

# Check if the data folder exists
if not os.path.exists('data'):
    os.makedirs('data')


def main():
    driver = webdriver.Chrome()
    driver.minimize_window()
    for page in range(1, 23):
        url = 'https://www.veed.io/videos?1d67476d_page=' + str(page)
        driver.get(url)
        html = driver.page_source

        # <div class="div-block-129">

        soup = BeautifulSoup(html, 'lxml')
        div = soup.find_all('div', class_='div-block-129')

        result = []

        for i in div:
            # <div class="div-block-136">  h2 tag
            file_name = i.find('div', class_='div-block-136').find('h2').get_text()
            # <a class="video-btn w-button"
            download_url = i.find('a', class_='video-btn w-button')['href']

            result.append({
                'file_name': file_name,
                'download_url': download_url
            })

        print(result)

        with open('./data/page_' + str(page) + '.json', 'w', encoding='utf-8') as f:
            f.write(str(result))


if __name__ == '__main__':
    main()
