import json
import os
from pytube import YouTube
from tqdm import tqdm

def youtube(url, path):
    from pytube import YouTube

    yt = YouTube(url)

    title = yt.title
    thumbnail_url = yt.thumbnail_url
    stream = yt.streams.filter(progressive=True).order_by("resolution").last()
    print(stream)
    stream.download(
        output_path=path,
        max_retries=3
    )
    result = {
        'title': title,
        'thumbnail_url': thumbnail_url
    }

    return result


if __name__ == '__main__':
    print(youtube('https://www.youtube.com/watch?v=J0bs_Ud9mb0', './youtube'))
