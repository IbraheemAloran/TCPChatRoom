from socket import*
from threading import*
from datetime import*
import sys

buffer = 1024
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

def recFile(client, filename):
    f = open(filename, "w")
    data = client.recv(1024)
    while True:
        print("Receiving...")
        
        f.write(data.decode())
        if data.decode()[-1] == " ":
            break
        data = client.recv(1024)
    

    f.close()
    print("File has been received")
    return

def showFile(client, filename):
    f = open(filename, "r")
    data = f.read(1024).encode()
    while (data):
        print("Sending...")
        client.send(data)
        data = f.read(1024).encode()

    f.close()
    print("File has been sent")

    return
