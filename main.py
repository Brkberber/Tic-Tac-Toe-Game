from PyQt5.QtWidgets import QMainWindow, QApplication
from xox import Ui_MainWindow
from PyQt5 import QtGui
import sys

class UI(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(UI, self).__init__()

        self.setupUi(self)

        self.show()

        self.setWindowTitle('Tic-Tac-Toe Game')

        self.pb_1.clicked.connect(self.game)
        self.pb_2.clicked.connect(self.game)
        self.pb_3.clicked.connect(self.game)
        self.pb_4.clicked.connect(self.game)
        self.pb_5.clicked.connect(self.game)
        self.pb_6.clicked.connect(self.game)
        self.pb_7.clicked.connect(self.game)
        self.pb_8.clicked.connect(self.game)
        self.pb_9.clicked.connect(self.game)

        self.restart.clicked.connect(self.start_over)

        self.game_turn = 1
        self.winner = None
        self.last_play = None


    def game(self):
        button = self.sender()

        if button.text() == "" and self.winner == None:
            if self.game_turn % 2 != 0:
                button.setText("X")
                button.setStyleSheet("color : red")
                self.last_play = "X"
                self.label.setText("O's Turn")

            elif self.game_turn % 2 == 0:
                button.setText("O")
                button.setStyleSheet("color : green")
                self.last_play = "O"
                self.label.setText("X's Turn")


            self.game_control()







    def start_over(self):
        self.pb_1.setText("")
        self.pb_2.setText("")
        self.pb_3.setText("")
        self.pb_4.setText("")
        self.pb_5.setText("")
        self.pb_6.setText("")
        self.pb_7.setText("")
        self.pb_8.setText("")
        self.pb_9.setText("")
        self.game_turn = 1
        self.winner = None
        self.last_play = None
        self.label.setText("X Goes First")



    def game_control(self):
        if (self.pb_1.text() == self.last_play) and (self.pb_2.text() == self.last_play) and (self.pb_3.text() == self.last_play):
            self.winner = self.last_play
            print(self.winner)

        elif (self.pb_4.text() == self.last_play) and (self.pb_5.text() == self.last_play) and (self.pb_6.text() == self.last_play):
            self.winner = self.last_play
            print(self.winner)

        elif (self.pb_7.text() == self.last_play) and (self.pb_8.text() == self.last_play) and (self.pb_9.text() == self.last_play):
            self.winner = self.last_play
            print(self.winner)

        elif (self.pb_1.text() == self.last_play) and (self.pb_4.text() == self.last_play) and (self.pb_7.text() == self.last_play):
            self.winner = self.last_play
            print(self.winner)

        elif (self.pb_2.text() == self.last_play) and (self.pb_5.text() == self.last_play) and (self.pb_8.text() == self.last_play):
            self.winner = self.last_play
            print(self.winner)

        elif (self.pb_3.text() == self.last_play) and (self.pb_6.text() == self.last_play) and (self.pb_9.text() == self.last_play):
            self.winner = self.last_play
            print(self.winner)

        elif (self.pb_1.text() == self.last_play) and (self.pb_5.text() == self.last_play) and (self.pb_9.text() == self.last_play):
            self.winner = self.last_play
            print(self.winner)

        elif (self.pb_3.text() == self.last_play) and (self.pb_5.text() == self.last_play) and (self.pb_7.text() == self.last_play):
            self.winner = self.last_play
            print(self.winner)

        elif self.game_turn == 9:
            self.winner = "draw"
            print(self.winner)

        if self.winner == None:
            self.game_turn += 1
        else:
            if self.winner == "draw":
                self.label.setText("Draw!")
            else:
                self.label.setText(f"{self.winner} Win!")




app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()