from socket import *
from threading import*

name = input("Enter your name:")

serverName = "enter server address here"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


def recieve():
    while True:
        try:
            msg = clientSocket.recv(1024).decode()
            if msg == 'Name:':
                clientSocket.send(name.encode())
            else:
                print(msg)

        except:
            print("an error occurred")
            clientSocket.close()
            break

receiveThread = Thread(target=recieve)
receiveThread.start()
