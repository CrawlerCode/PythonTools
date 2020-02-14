from pythontools.core import events
from pythontools.sockets import server
from threading import Thread

SERVER = server.Server(password="PASSWORD")

def ON_CLIENT_CONNECT(params):
    client = params[0]
    # send a message to client on connect by clientSocket
    SERVER.sendTo(client["clientSocket"], {"METHOD": "HELLO"})

def ON_CLIENT_DISCONNECT(params):
    client = params[0]

def ON_RECEIVE(params):
    client = params[0]
    data = params[1]
    METHOD = data["METHOD"]

events.registerEvent("ON_CLIENT_CONNECT", ON_CLIENT_CONNECT)
events.registerEvent("ON_CLIENT_DISCONNECT", ON_CLIENT_DISCONNECT)
events.registerEvent("ON_RECEIVE", ON_RECEIVE)

Thread(target=SERVER.start, args=["HOST-IP", 15749]).start()

# send a message to client by clientID
SERVER.sendToClientID("MY_CLIENT_ID", {"METHOD": "TEST", "mydata": "123"})