#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from array import *



class Example(QWidget):

    initialCoords = array('i', [20, 20]) #initial coordinates of a square
    squareSize = 20 #size of a square

    def __init__(self):
        super().__init__()

        self.initialCoords = array('i', [20, 20]) #initial coordinates of a square
        self.squareSize = 20 #size of a square
        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('gravity test')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()


    def drawLines(self, qp):

        x = self.initialCoords[0]
        y = self.initialCoords[1]
        
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(x, y, x + self.squareSize, y)
        
        qp.setPen(pen)
        qp.drawLine(x, y, x, y + self.squareSize)
        
        qp.setPen(pen)
        qp.drawLine(x, y + self.squareSize, x + self.squareSize, y + self.squareSize)
        
        qp.setPen(pen)
        qp.drawLine(x + self.squareSize, y, x + self.squareSize, y + self.squareSize)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
