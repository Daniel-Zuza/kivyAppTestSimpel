
import random
from Seitendefinitionen.seitenbasis import Seitenbasis

class Startseite(Seitenbasis):
    def __init__(self, **kwargs):
        super(Startseite, self).__init__(**kwargs)

    def knopfdruckCallback(self):
        self.ids.test_label.text = f"{random.randint(0, 100)}"
