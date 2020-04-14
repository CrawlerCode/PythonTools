from pythontools.sockets import relay
from threading import Thread

RELAY = relay.Relay(password="PASSWORD")

RELAY.enableRelayServerEncrypt('SECRET_KEY')

Thread(target=RELAY.start, args=["RELAY-HOST-IP", 15759, "SERVER-HOST-IP", 15749]).start()
