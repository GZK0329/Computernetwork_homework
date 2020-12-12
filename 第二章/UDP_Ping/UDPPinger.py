import time
from socket import *

serverName = '81.70.76.47'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)

for i in range(0, 10):
    curTime = time.time()
    try:
        message = (("Ping %d time:%s") % (i + 1, curTime)).encode()
        clientSocket.sendto(message, (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rtt = time.time() - curTime
        print('Sequence %d reveive from server : %s cost %.3f time in a RTT' % (i+1, serverName, rtt))
    except Exception as e:
        print('Sequence '+str(i+1)+': Request time out!')

clientSocket.close()