# -*- coding:utf-8 -*-
'''
Created on 18 de Set de 2013

@author: carlos
'''
from OpenFile.openFiles import Open_Files
from PyQt4 import *
from PySide import QtCore, QtGui
from PySide.QtCore import *
from PySide.QtGui import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = Open_Files()
    a.exec_()
    app.exec_()
    pass






   