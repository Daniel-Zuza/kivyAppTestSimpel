
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

class test():
    pass

class WindowManager(ScreenManager):
    class WindowManager(ScreenManager):
        pass

class MyApp(MDApp):

    def build(self):
        self.window_manager = WindowManager()
        self.designDateienLaden()
        return Builder.load_file('Seitendefinitionen/startseite.kv')

    def designDateienLaden(self):
        Builder.load_file('Seitendefinitionen/seite2.kv')
        Builder.load_file('Seitendefinitionen/seite3.kv')

if __name__ == '__main__':
    MyApp().run()





