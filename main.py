__version__ = '0.1'
__author__ = 'rschwalk'
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty

from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.internet import reactor, protocol


class DriveClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.app.print_message(str(data))


class DriveFactory(protocol.ClientFactory):
    protocol = DriveClient

    def __init__(self, app):
        self.app = app

    def clientConnectionLost(self, conn, reason):
        self.app.print_message("connection lost: " + str(reason))

    def clientConnectionFailed(self, conn, reason):
        self.app.print_message("connection failed")


class ConnectScreen(Screen):

    """The Connect screen"""

    ip_input = ObjectProperty(None)
    port_input = ObjectProperty(None)

    def on_connect_pressed(self):
        """The connect button was pressed, connect to the robot.
        :returns: TODO

        """
        print('Connect')
        app = App.get_running_app()
        app.connect_to_server(self.ip_input.text, self.port_input.text)
        self.manager.current = 'drive'


class DriveScreen(Screen):

    """The drive screen."""

    log_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DriveScreen, self).__init__(**kwargs)
#        self._keyboard = Window.request_keyboard(self._keyboard_closed, self,
#                                                'text')
#        self._keyboard.bind(on_key_down=self._on_keyboard_down)
#        self._app = App.get_running_app()
#        Window.softinput_mode = 'pan'
#
#    def _keyboard_closed(self):
#        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
#        self._keyboard = None
#
#    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
#        print('The key', keycode, 'have been pressed')
#        print(' - text is %r' % text)
#        print(' - modifiers are %r' % modifiers)
#
#        if keycode[1] == 'up':
#            self._app.send_message(b'FW')
#        elif keycode[1] == 'left':
#            self._app.send_message(b'LT')
#        elif keycode[1] == 'right':
#            self._app.send_message(b'RT')
#        elif keycode[1] == 'down':
#            self._app.send_message(b'BW')
#        elif keycode[1] == 'rshift':
#            self._app.send_message(b'ST')
#
#
#        return True

class ScreenManagement(ScreenManager):

    """The screen management of the app."""

    pass


class RobotControllApp(App):
    connection = None

    """The main app to controll the robot."""

    def build(self):
        self.dv = DriveScreen()
        sm = ScreenManagement()
        sm.add_widget(ConnectScreen())
        sm.add_widget(self.dv)
        sm.current = 'connect'
        return sm

    def connect_to_server(self, ip, port):
        """Connect to the robot.
        :returns: TODO

        """
        reactor.connectTCP(ip, int(port), DriveFactory(self))
        print('connect to server '+ ip + ':' + port)
        self.dv.log_label.text += '\nHello'

    def on_connection(self, connection):
        self.print_message('connected successfully')
        self.connection = connection

    def send_message(self, msg):
        if msg and self.connection:
            self.connection.write(msg)

    def print_message(self, msg):
        self.dv.log_label.text += '\n' + msg


if __name__ == '__main__':
    RobotControllApp().run()
