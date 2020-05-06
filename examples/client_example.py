from pythontools.core import events
from pythontools.sockets import client
from threading import Thread

CLIENT = client.Client(password="PASSWORD", clientID="MY_CLIENT_ID", clientType="CLIENT")

def ON_CONNECT():
    pass

def ON_RECEIVE(data):
    METHOD = data["METHOD"]
    # recipe the test message
    if METHOD == "TEST":
        print("test:", data["mydata"])

CLIENT.ON_CONNECT(ON_CONNECT)
CLIENT.ON_RECEIVE(ON_RECEIVE)

CLIENT.enableEncrypt('SECRET_KEY')

Thread(target=CLIENT.connect, args=["HOST-IP", 15749]).start()