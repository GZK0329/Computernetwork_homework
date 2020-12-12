# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
# Fill in end
serverPort = 80
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('webServer is ready to receive')
    connectionSocket, addr = serverSocket.accept()  # Fill in start  #Fill in end
    try:
        message = connectionSocket.recv(1024).decode()  # Fill in start  #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read(-1)  # Fill in start  #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        # Fill in end
        header = 'HTTP/1.1 200 OK \nConnection:close\nContent-Type:text/html\nContent-Length:%d\n\n' % (len(outputdata))
        # list(header)

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        header = 'HTTP/1.1 404Not Found'
        connectionSocket.send(header.encode())

        connectionSocket.close()

    # Send response message for file not found
    # Fill in start
    # Fill in end

    # Close client socket
    # Fill in start
    # Fill in end
serverSocket.close()
