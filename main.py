import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.support import install_twisted_reactor


class ConnectScreen(Screen):

    """The Connect screen"""

    def on_connect_pressed(self):
        """The connect button was pressed, connect to the robot.
        :returns: TODO

        """
        print('Connect')
        self.manager.current = 'drive'


class DriveScreen(Screen):

    """The drive screen."""

    pass

class ScreenManagement(ScreenManager):

    """The screen management of the app."""

    pass


class RobotControllApp(App):

    """The main app to controll the robot."""

    def build(self):
        sm = ScreenManagement()
        sm.add_widget(ConnectScreen())
        sm.add_widget(DriveScreen())
        sm.current = 'connect'
        return sm


if __name__ == '__main__':
    RobotControllApp().run()
