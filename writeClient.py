from socket import *
from threading import*

name = input("Enter your name:")

serverName = "Enter your IP address here"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

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

writeThread = Thread(target=write)
writeThread.start()
