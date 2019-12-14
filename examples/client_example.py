from pythontools.core import events
from pythontools.sockets import client
from threading import Thread

CLIENT = client.Client(password="PASSWORD", clientID="MY_CLIENT_ID", clientType="CLIENT")

def ON_CONNECT(params):
    pass

def ON_RECEIVE(params):
    client = params[0]
    data = params[1]
    METHOD = data["METHOD"]
    # recipe the test message
    if METHOD == "TEST":
        print("test:", data["mydata"])

events.registerEvent("ON_CONNECT", ON_CONNECT)
events.registerEvent("ON_RECEIVE", ON_RECEIVE)

Thread(target=CLIENT.connect, args=["HOST-IP", 15749, True]).start()