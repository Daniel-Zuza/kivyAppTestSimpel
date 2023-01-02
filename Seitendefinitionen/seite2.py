
import random
from Seitendefinitionen.seitenbasis import Seitenbasis

class Seite2(Seitenbasis):
    def __init__(self, **kwargs):
        super(Seite2, self).__init__(**kwargs)

    def knopfdruckCallback(self):
        self.ids.test_label.text = f"{random.randint(-1000, 0)}"
