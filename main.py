from controll import *


def main():
    app = QApplication([])
    window = Forex()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
