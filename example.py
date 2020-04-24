import gid
config = {
        'driver_path': './chromedriver',
        'headless': False,
        'window-size': '720x480',
        'disable_gpu': False
    }
arguments = {
    'keywords': ['펭수', '뽀로로'],
    'limit': 300,
    'download_path': "./download"
}

downloader = gid.build(config)
try:
    downloader.download(arguments)
finally:
    downloader.close()