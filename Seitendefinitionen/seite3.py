
import random
from Seitendefinitionen.seitenbasis import Seitenbasis

class Seite3(Seitenbasis):
    def __init__(self, **kwargs):
        self.zaehler = 0
        self.liste = ['eins', 'zwei', 'drei', 'vier']
        super(Seite3, self).__init__(**kwargs)

    def knopfdruckCallback(self):
        self.ids.test_label.text = f"{self.liste[self.zaehler % len(self.liste)]}"
        self.zaehler += 1
