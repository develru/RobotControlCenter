import kivy
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class MainLayout(GridLayout):

    """The main layout of the kivy app"""

    pass

class RobotControllApp(App):

    """The main app to controll the robot."""

    def build(self):
        return MainLayout()


if __name__ == '__main__':
    RobotControllApp().run()
