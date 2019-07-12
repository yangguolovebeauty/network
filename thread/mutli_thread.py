# from multiprocessing import Process
# from time import time,sleep
#
# counter = 0
#
# def sub_task(string):
#     global counter
#     while counter < 10:
#         print(string,end='',flush=True)
#         counter += 1
#         sleep(0.01)
#
# def main():
#     Process(target=sub_task, args=('ping',)).start()
#     Process(target=sub_task,args=('pong',)).start()
#
# if __name__ == '__main__':
#     main()

from random import randint
from threading import Thread
from time import time,sleep

def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%.2f秒' % (filename,time_to_download))

def main():
    start = time()
    t1 = Thread(target=download,args=('Python从入门到放弃.pdf',))
    t1.start()
    t2 = Thread(target=download,args=('机器学习.pdf',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('下载完成！共耗费%.2f秒' %(end - start))

if __name__ == '__main__':
    main()