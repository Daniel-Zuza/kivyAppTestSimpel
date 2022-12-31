
import random
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class Seite(Screen):
    def __init__(self, **kwargs):
        super(Seite, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def knopfdruckCallback(self):
        self.ids.test_label.text = f"{random.randint(0, 100)}"

class MyApp(MDApp):

    def build(self):
        return Builder.load_file("design.kv")

if __name__ == '__main__':
    MyApp().run()





