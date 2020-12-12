# !usr/bin/python
# -*- coding: UTF-8 -*-

from socket import *

serverPort = 50000
serverSocket = socket(AF_INET, SOCK_STREAM)
# 将服务器的端口号与该套接字关联
serverSocket.bind(('', serverPort))
# 该套接字为欢迎套接字 设置请求连接的最大数量 这里为1 至少为1
serverSocket.listen(1)

print('the server is ready to receive')

while True:
    # accept() -> (socket object, address info)
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
    # serverSocket 是保持打开的 欢迎套接字
