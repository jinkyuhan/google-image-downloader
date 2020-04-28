# Google Images Download using Selenium


## Usage

```python3
import gids

config = {
    'driver_path': './chromedriver',
    'headless': True,
    'window-size': '720x480',
    'disable_gpu': False
}

item = {
    'keyword': '햇반',
    'limit': 10,
    'download_context': './data',
    'path': './'
}

items = [item]

downloader = build(config)

downloader.download(items)