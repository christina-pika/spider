import glob
import json
import os
import concurrent.futures
from selenium import webdriver

def url_redirect(url):
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get(url)


    # Get the current URL after any potential redirects
    location_url = driver.current_url

    print(url)
    print(location_url)
    print('+++++++++++++++++++++++++')

    driver.quit()

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
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(file_redirect, files)

