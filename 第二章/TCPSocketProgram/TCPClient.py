# !usr/bin/python
# -*- coding: UTF-8 -*-

from socket import *

serverName = '127.0.0.1'
serverPort = 50000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('please enter lowercase sentence:')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1024)
print('from server receive:', modifiedMessage.decode())
clientSocket.close()
