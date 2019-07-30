# from time import time
# from threading import Thread
# import requests
#
# class DownloadHandler(Thread):
#
#     def __init__(self,url):
#         super.__init__()
#         self.url = url
#
#     def run(self):
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('/Users/Ayang'+filename,'wb') as f:
#             f.write(resp.content)
#
#
# def main():
#     url = 'http://api.tianapi.com/meinv/?key=APIKey&num=10'
#     resp = requests.get(url)
#
#     data_model = resp.json()
#     for mm_dict in data_model['newslist']:
#         url = mm_dict['picUrl']
#         DownloadHandler(url).start()
#
#
# if __name__ == '__main__':
#     main()

# from time import time
# from threading import Thread
# import requests
#
# #继承Thread类创建自定义的线程类
# class DownloadHanlder(Thread):
#
#     def __init__(self, url):
#         super().__init__()
#         self.url = url
#
#     def run(self):
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('E:\Study\Python\pycharmr\\test\\network program\downloadhandler\\' + filename, 'wb') as f:
#             f.write(resp.content)
#
#
# def main():
#     # 通过requests模块的get函数获取网络资源
#     # 下面的代码中使用了天行数据接口提供的网络API
#     # 要使用该数据接口需要在天行数据的网站上注册
#     # 然后用自己的Key替换掉下面代码的中APIKey即可
#     resp = requests.get(
#         'http://api.tianapi.com/meinv/?key=APIKey&num=39cee757e3b681cdbe39d8a309ec6e4e')
#     # 将服务器返回的JSON格式的数据解析为字典
#     data_model = resp.json()
#     for mm_dict in data_model['newslist']:
#         url = mm_dict['picUrl']
#         # 通过多线程的方式实现图片下载
#         DownloadHanlder(url).start()
#
# if __name__ == '__main__':
#     main()



# from socket import socket, SOCK_STREAM, AF_INET
# from datetime import datetime
#
# def main():
#     server = socket(family=AF_INET, type= SOCK_STREAM)    ## ipv4 tcp
#     server.bind(('192.168.43.62',4567))                   #将套接字绑定到地址, 在AF_INET下,以元组（host,port）的形式表示地址.
#     server.listen(512)
#     print('服务器启动开始监听...')
#     while True:
#         client, addr = server.accept()
#         print(str(addr) + '连接到了服务器')
#         client.send(str(datetime.now()).encode('utf-8'))
#         client.close()
#
# if __name__ == '__main__':
#     main()
# #服务器


#
# from socket import socket
#
# def main():
#     client = socket()
#     client.connect(('192.168.43.62', 4567))
#     print(client.recv(1024).decode('utf-8'))
#     client.close()
#
# if __name__ == '__main__':
#     main()

from socket import socket
from base64 import b64encode
from json import dumps
from threading import Thread
from os import path
def main():

    class FileTransferHandler(Thread):
        def __init__(self, client):
            super.__init__()
            self.client = client
        def run(self):
            mydict = {}
            mydict['filename'] = 'crystal liu.jpg'
            mydict['filedata'] = data
            json_str = dumps(mydict)
            self.client.send(json_str.encode('utf-8'))
            self.client.close()


    server = socket()
    server.bind(('10.160.83.248',4567))
    server.listen(5)
    print('服务器启动开始监听...')
    with open(path.abspath('.') + '\downloadhandler\crystal liu.jpg','rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()

if __name__ == '__main__':
    main()