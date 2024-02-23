import json
import os
import random
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from DrissionPage import ChromiumPage
from DrissionPage._configs.chromium_options import ChromiumOptions

# If folders named 'music' and 'json_data' do not exist, create them to store music files and JSON data
if not os.path.exists('music'):
    os.makedirs('music')
if not os.path.exists('json_data'):
    os.makedirs('json_data')

# Add a lock to synchronize file writing operations in multithreading
lock = threading.Lock()


def save_json(data, name):
    # Open the file and write the data in JSON format
    with open(f'json_data/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        # Print a message indicating the JSON data has been saved
        print(f'{name} JSON data saved')


def download_music(url, name):
    # Make a request to download the music file
    r = requests.get(url)
    # Open the file in binary write mode and write the downloaded music content to the file
    with open(f'music/{name}.mp3', 'wb') as f:
        f.write(r.content)
        # Print a message indicating the download is complete
        print(f'{name} audio data saved')


def safe_file_name(name):
    # Remove or replace characters not allowed in file names
    return re.sub(r'[\\/*?:"<>|]', '', name)


# Modified page_list function, accepts a lock as a parameter
def page_list(pagi, lock):
    # Create a browser configuration object, specifying the browser path
    co = ChromiumOptions().set_browser_path(r'C:\Users\宝\.cache\selenium\chrome\win64\121.0.6167.85\chrome.exe')
    # Create a page object with the configuration
    page = ChromiumPage(addr_or_opts=co)

    try:
        # Concatenate URL and visit the music search page
        page.get("https://pixabay.com/music/search/?pagi=" + str(pagi))
        # Wait for the webpage to fully load
        time.sleep(random.uniform(1, 2))
        # Get the current page's source code
        html = page.html

        # Use regular expression to match __BOOTSTRAP_URL__ on the page, usually used to fetch dynamically loaded data
        bootstrap = re.compile(r'window.__BOOTSTRAP_URL__ = \'(.+?)\';')
        # Find the match and get the first result
        result = bootstrap.findall(html)[0]
        # Print the result (for debugging)
        print(result)
        # Use the found URL to make another request
        page.get("https://pixabay.com/" + result)
        # Wait for the webpage to fully load
        time.sleep(random.uniform(1, 2))
        # Use regular expression to match the <pre> tag containing music data
        pre = re.compile(r'pre-wrap;">(.+?)</pre></body></html>')
        # Find the match and get the first result
        result = pre.findall(page.html)[0]
        print(result)
        # Check if data was retrieved
        if not result:
            raise ValueError(f"Music data not found on page {pagi}")
        # Parse the matched result as JSON format
        json_data = json.loads(result)['page']['results']

        # Iterate through each music item in the list and save relevant data
        for item in json_data:
            # Construct the required JSON structure, extracting relevant information about the music
            item_data = {
                'src': item['sources']['src'],
                'alt': item['alt'],
                'description': item['description'],
                'id': item['id'],
                'title': item['title'],
                'rating': item['rating'],
                'qualityStatus': item['qualityStatus'],
                'isLowQuality': item['isLowQuality']
            }

            # Clean the file name
            safe_name = safe_file_name(item['name'])

            # Use the lock to ensure thread safety during file writing
            with lock:
                # Save JSON data using the cleaned file name
                save_json(item_data, safe_name)
                # # Download the music file
                # download_music(item_data['src'], item['name'])

    except Exception as e:
        print(f"An error occurred on page {pagi}: {e}")
    finally:
        # Close the browser regardless of success
        page.close()


# save_json and download_music functions can remain unchanged

# Main program entry
if __name__ == '__main__':
    # Use ThreadPoolExecutor to create a thread pool
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Loop through all pagination pages (example from 1 to 2589)
        for page_number in range(1, 2589):
            # Submit tasks to the thread pool
            executor.submit(page_list, page_number, lock)
