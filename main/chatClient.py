from socket import *
from threading import*

name = input("Enter your name:")

serverName = "put server ip address here"
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


def write():
    while True:
        msg = f'{name}: {input("")}'
        clientSocket.send(msg.encode())
        if ".send" in msg:
            filename = msg.split(" ")[2]
            sendFile(filename)


def sendFile(filename):
    f = open(filename, "r")
    data = f.read(1024).encode()
    while (data):
        print("Sending...")
        clientSocket.send(data)
        data = f.read(1024).encode()

    f.close()
    clientSocket.send(" ".encode())
    print("File has been sent")
    return

receiveThread = Thread(target=recieve)
receiveThread.start()

writeThread = Thread(target=write)
writeThread.start()
