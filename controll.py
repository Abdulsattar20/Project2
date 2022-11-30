from PyQt5.QtWidgets import *
from gui import *
from forex_python.converter import CurrencyRates


class Forex(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
    