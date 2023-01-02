
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

class Seitenbasis(Screen):
    def __init__(self, **kwargs):
        super(Seitenbasis, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def seiteAufrufen(self, *args, **kwargs):
        self.manager.transition.direction = 'right'
        print("self.app.root",self.app.root.ids)
        self.app.root.current = kwargs['seiten_name']

