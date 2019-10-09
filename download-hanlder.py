from time import time
from threading import Thread
import requests


class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('User/janmi/Desktop/www/python/', 'wb') as f:
            f.write(resp.content)


def main():
    resp = requests.get('http://api.tianapi.com/allnews/?key=7103a05823de3df87edebe6c939169e9&num=10&col=7')
    data_dict = resp.json()
    print(data_dict)
    for item in data_dict['newslist']:
        url = item['picUrl']
        print(url)


if __name__ == '__main__':
    main()
