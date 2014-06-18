__author__ = 'develru'

from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor


class Control(Protocol):

    def dataReceived(self, data):
        print(data)


class ControlClientFactory(ClientFactory):

    def startedConnecting(self, connector):
        print('Started connecting...')

    def buildProtocol(self, addr):
        print('Connected.')
        return Control()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection. Reason: ', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Client connection failed. Reason: ', reason)


class ControlConnection():

    def connect_to_host(self, host, port):
        reactor.connectTCP(host, port, ControlClientFactory())
        reactor.run()