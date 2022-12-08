from PyQt5.QtWidgets import *
from gui import *
from forex_python.converter import CurrencyRates

forex = CurrencyRates()
class Forex(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        '''
        constructor to create initial state for foreign exchanger currency
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.exchange_Button.clicked.connect(lambda: self.exchange())
        self.clear_Button.clicked.connect(lambda: self.clear())


    def exchange(self) -> None:
        '''
        this function teake the from currency and change it to the to currency
        and take the amount that want to be exchanged
        '''
        try:

            currency_from = self.from_comboBox.currentText()
            currency_to = self.to_comboBox.currentText()
            amount = float(self.input_amount.text())

            exchange = forex.convert(currency_from, currency_to, amount)

            self.output_amount.setText(f"{exchange:.2f}")
        except ValueError:
            self.input_amount.setText('Enter A Numeric Number')







    def clear(self) -> None:
        '''
        this function clear all the text from the amount and the amount exchanged
        '''
        self.input_amount.setText('')
        self.output_amount.setText('')
