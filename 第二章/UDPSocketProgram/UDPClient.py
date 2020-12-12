from socket import *
# 提供服务器的主机名或者IP 和 端口号
serverName = '127.0.0.1'
serverPort = 12000

# 创建客户端套接字 参数
clientSocket = socket(AF_INET, SOCK_DGRAM)
# raw_input()  input() 在py3.x整合为input()
message = input('Input lowercase sentence:')

# sendto UDP发送消息函数 将数据发送到套接字，address 是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数
# param1 为数据的字节形式 param2为地址是一个元组的形式包含(主机名或IP地址, 端口号)
clientSocket.sendto(message.encode(), (serverName, serverPort))

# 接受UDP数据recvfrom 返回值是(data, adress) param 是字节数 接受多少字节的数据
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()