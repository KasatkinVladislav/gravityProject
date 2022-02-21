#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from array import *



# class Example(QWidget):

    # initialCoords = array('i', [20, 20]) #initial coordinates of a square
    # squareSize = 10 #size of a square

    # def __init__(self):
        # super().__init__()

        # self.initialCoords = array('i', [20, 20]) #initial coordinates of a square
        # self.squareSize = 20 #size of a square
        # self.initUI()


    # def initUI(self):

        # self.setGeometry(300, 300, 280, 270)
        # self.setWindowTitle('gravity test')
        # self.show()


    # def paintEvent(self, e):

        # qp = QPainter()
        # qp.begin(self)
        # self.drawLines(qp)
        # qp.end()


    # def drawLines(self, qp):

        # x = self.initialCoords[0]
        # y = self.initialCoords[1]
        
        # pen = QPen(Qt.black, 2, Qt.SolidLine)

        # qp.setPen(pen)
        # qp.drawLine(x, y, x + self.squareSize, y)
        
        # qp.setPen(pen)
        # qp.drawLine(x, y, x, y + self.squareSize)
        
        # qp.setPen(pen)
        # qp.drawLine(x, y + self.squareSize, x + self.squareSize, y + self.squareSize)
        
        # qp.setPen(pen)
        # qp.drawLine(x + self.squareSize, y, x + self.squareSize, y + self.squareSize)

# class gravityTetris(QMainWindow):

    # def __init__(self):
        # super().__init__()

        # self.initUI()


    # def initUI(self):

        # self.tboard = tetrisBoard(self)
        # self.setCentralWidget(self.tboard)

        # self.statusbar = self.statusBar()
        # self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        # self.tboard.start()

        # self.resize(180, 380)
        # self.center()
        # self.setWindowTitle('Tetris')
        # self.show()


    # def center(self):

        # screen = QDesktopWidget().screenGeometry()
        # size = self.geometry()
        # self.move((screen.width()-size.width())/2,
            # (screen.height()-size.height())/2)

# class tetrisBoard(QFrame):

    # msg2Statusbar = pyqtSignal(str)

    # BoardWidth = 10
    # BoardHeight = 22
    # Speed = 300

    # def __init__(self, parent):
        # super().__init__(parent)

        # self.initBoard()


    # def initBoard(self):

        # self.timer = QBasicTimer()
        # self.isWaitingAfterLine = False

        # self.curX = 0
        # self.curY = 0
        # self.numLinesRemoved = 0
        # self.board = []

        # self.setFocusPolicy(Qt.StrongFocus)
        # self.isStarted = False
        # self.isPaused = False
        # self.clearBoard()
        
    # def shapeAt(self, x, y):
        # return self.board[(y * Board.BoardWidth) + x]

    # def setShapeAt(self, x, y, shape):
        # self.board[(y * Board.BoardWidth) + x] = shape

    # def squareWidth(self):
        # return self.contentsRect().width() // Board.BoardWidth


    # def squareHeight(self):
        # return self.contentsRect().height() // Board.BoardHeight
        
    # def DrawCube(self):
        # x = self.initialCoords[0]
        # y = self.initialCoords[1]
        
        # pen = QPen(Qt.black, 2, Qt.SolidLine)

        # qp.setPen(pen)
        # qp.drawLine(x, y, x + self.squareSize, y)
        
        # qp.setPen(pen)
        # qp.drawLine(x, y, x, y + self.squareSize)
        
        # qp.setPen(pen)
        # qp.drawLine(x, y + self.squareSize, x + self.squareSize, y + self.squareSize)
        
        # qp.setPen(pen)
        # qp.drawLine(x + self.squareSize, y, x + self.squareSize, y + self.squareSize)
        

#есть класс доска, есть класс главное окно, есть класс фигурка
#в главном окне инициализируем доску, в доске располагаем логику игры
#у фигурки есть её размеры и масса
#как вариант, можно сделать поле двухмерным массивом, в котором располагаем кубики


class tetrisBoard(QFrame):
    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 20 #ширина в 20 маленьких клеточек
    BoardHeight = 44 #высота в 44 маленькие клеточки
    Speed = 300
    theBoard = [] #пустой массив, в котором хранятся занятые значения

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()


    def initBoard(self):

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.theBoard = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()


# if __name__ == '__main__':

    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())
