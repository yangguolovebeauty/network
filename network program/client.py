from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('192.168.43.62', 5566))
    in_data = bytes()
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('E:\Ayang\Pictures\Saved Pictures\\' + filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('图片已保存')

if __name__ == '__main__':
    main()