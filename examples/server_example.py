from pythontools.sockets import server
from threading import Thread

SERVER = server.Server(password="PASSWORD")

def ON_CLIENT_CONNECT(client):
    # send a message to client on connect by clientSocket
    SERVER.sendTo(client["clientSocket"], {"METHOD": "HELLO"})

def ON_CLIENT_DISCONNECT(client):
    pass

def ON_RECEIVE(client, data):
    METHOD = data["METHOD"]

SERVER.ON_CLIENT_CONNECT(ON_CLIENT_CONNECT)
SERVER.ON_CLIENT_DISCONNECT(ON_CLIENT_DISCONNECT)
SERVER.ON_RECEIVE(ON_RECEIVE)

#SERVER.enableEncrypt('SECRET_KEY')  # optional
#SERVER.enableWhitelistIp([])  # optional
#SERVER.enableWhitelistMac([])  # optional

Thread(target=SERVER.start, args=["HOST-IP", 15749]).start()

# send a message to client by clientID
SERVER.sendToClientID("MY_CLIENT_ID", {"METHOD": "TEST", "mydata": "123"})