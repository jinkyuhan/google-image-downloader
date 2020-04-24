import gid
config = {
        'driver_path': './chromedriver',
        'headless': False,
        'window-size': '720x480',
        'disable_gpu': False
    }

item = {
    'keyword': '펭수',
    'limit': 20,
    'download_context': "./download",
    'path': "./동물"
}
item_2 ={
    'keyword': '뽀로로',
    'limit': 20,
    'download_context': "./download",
    'path': "./동물"
}
items=[item, item_2]
downloader = gid.build(config)

try:
    downloader.download(items)
finally:
    downloader.close()