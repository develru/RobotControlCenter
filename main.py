import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class ConnectScreen(Screen):

    """The Connect screen"""

    pass



class RobotControllApp(App):

    """The main app to controll the robot."""

    def build(self):
        sm = ScreenManager()
        sm.add_widget(ConnectScreen(name='connect'))
        return sm


if __name__ == '__main__':
    RobotControllApp().run()
