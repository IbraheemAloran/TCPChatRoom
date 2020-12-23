from socket import*
from threading import*
from datetime import*
import sys


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)




clients = []
names = []



def recMsg(client):
    chatlog = open("ChatLog.txt", "a")
    chat = ""
    while True:
        time = datetime.now().strftime("%H:%M")
        try:
            msg = client.recv(1024).decode()
            broadcast(f'{time} {msg}'.encode())
            print(f'{time} {msg}')
            chat += f'{time} {msg}\n'
            if ".send" in msg:
                filename = msg.split(" ")[2]
                recFile(client, filename)
            if ".show" in msg:
                filename = msg.split(" ")[2]
                showFile(client, filename)
        except:
            index = clients.index(client)
            clients.remove(clients[index])
            client.close()
            name = names[index]
            print(f'{time} {name} left the chat')
            broadcast(f'{time} {name} left the chat'.encode())
            chat += f'{time} {name} left the chat'
            names.remove(name)
            break
        chatlog.write(chat)
        chat = ""
    chatlog.close()

def recieve():
    chat = ""
    
    while True:
        client, addr = serverSocket.accept()
        chatlog = open("ChatLog.txt", "a")
        time = datetime.now().strftime("%H:%M")
        print(f'{time} connected with {str(addr)}')
        chat += f'{time} connected with {str(addr)}\n'  
        client.send('Name:'.encode())
        name = client.recv(1024).decode()
        names.append(name)
        clients.append(client)
        print(f'Name of the client is {name}')
        broadcast(f'{time} {name} has joined the chat'.encode())
        chat += f'{time} {name} has joined the chat\n'
        chatlog.write(chat)
        chat = ""
        chatlog.close()
        thread = Thread(target=handle, args=(client, ))
        thread.start()
        

def broadcast(msg):
    for client in clients:
        client.send(msg)
     

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

print("The server is ready to receive")
recieve()




