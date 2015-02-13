#!/usr/bin/python3
# File: country.py.py
# Author: Matthijs Bonnema
# Date: 2/13/15
# Info:

import sys
from PyQt4 import *


class Country(QDialog):
    def __init__(self, country):


        grid = QGridLayout()
        grid.addWidget(self.fromcombo, 0, 0)
        grid.addWidget(self.label, 0, 0)

        fileName = QFileDialog.getOpenFileName(self.parent, "Open Image", "/", "Image Files (*.png *.jpg *.bmp *.tiff)");
        img = QtGui.QPixmap(fileName[0])
        scaled_img = img.scaled(self.ui.img_label.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.img_label.setPixmap(scaled_img)



    def __str__(self):
        print("Hello from {0}".format(country))

    def ui(self):
        '''Update the UI; get the currency to convert and convert it'''
        to = str(self.tocombo.currentText())
        fromlabel = str(self.fromcombo.currentText())
        convert = (self.rates[fromlabel] / self.rates[to]) * self.fromspin.value()
        self.tolabel.setText("%0.2f" % convert)


if __name__ == "__main__":
    app = QApplication(sys.argv)