# -*- coding:utf-8 -*-
'''
Created on 18 de Set de 2013

@author: carlos
'''

from OpenFile.analyse_file import AnalyseFile
from PyQt4 import *
from PySide import QtCore, QtGui
from PySide.QtCore import *
from PySide.QtGui import *
from openFile_interface import *
import sys


'''Classe que apresenta a interface da Tool da Gerar XML'''
class Open_Files(QDialog, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Open_Files, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.Button_openFile, QtCore.SIGNAL("clicked()"), self.evt_abrir)
        self.connect(self.Button_pastaSaida, QtCore.SIGNAL("clicked()"), self.evt_EscolherTXT)
        
        self.buttonBox.accepted.connect(self.evt_ButtonOK)
        self.buttonBox.rejected.connect(self.evt_ButtonCancel)
        
        pass
    pass

    # Evento do Botão Ok 
    def evt_ButtonOK(self):
        # Saber lista de directorias e nome ficheiro
        caminhoFile = self.fname#self.lineEdit_fileName.text()
        print caminhoFile
        listaDirectorias = caminhoFile.split("/")
        print  listaDirectorias
        
        # Saber o nome do Fiheiro
        nomeFicheiro = listaDirectorias[-1]
        print nomeFicheiro
        
        # Saber a extenção do ficheiro
        lista = nomeFicheiro.split(".")
        ext = lista[-1]
        print ext
        
        # Saber o caminho de Saida para gerar os XML
        caminhoPastaSaida = self.lineEdit_pastaSaida.text()
        
        if caminhoFile != "" and caminhoPastaSaida != "":
            # Faz a verificação de se a extenção do 
            # ficheiro é csv ou CSV
            if ext == "psd" or ext == "PSD":
                
                msgBox = QMessageBox()
                msgBox.setText("Deseja fazer as estatisticas ao ficheiro {0}?"\
                               .format(nomeFicheiro).decode("utf-8"))
                sim = msgBox.addButton(self.tr("Sim"), QMessageBox.YesRole)
                msgBox.addButton(self.tr("Nao"), QMessageBox.NoRole)
                msgBox.setIconPixmap(QPixmap("../Imagens/questionPequeno.png"))
                msgBox.exec_()
                if msgBox.clickedButton() == sim:
                    
                    try:
                        # Trata o ficheiro
                        AnalyseFile(caminhoFile)
                        pass
                    except Exception as ex:
                        QMessageBox.critical(self, "Atenção".decode("utf-8"), \
                        "Mensagem de erroo! \n"+str(ex)+"".decode("utf-8"))
                        pass
                    pass
                pass
            else:
                QMessageBox.critical(self, "Atenção".decode("utf-8"), \
                        "O Ficheiro que tentou abrir não é um ficheiro .PSD"\
                        .decode("utf-8"))
                pass
            pass
        else: # Caso o caminho do ficheiro a abrir
            # e o caminho da pasta de saida
            # estejam vazios, muda a cor das labels (*) e 
            # avisa o utilizado com a mensagem 
            palette = QtGui.QPalette()
            
            # Muda a cor das labels dos campos Obrigatórios
            if caminhoFile == "": 
                palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
                self.label_1_asterisco.setPalette(palette)
                pass
            if caminhoPastaSaida == "":
                palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
                self.label_2_asterisco.setPalette(palette)
                pass
            else:
                pass
            
            QMessageBox.warning(self, "Atenção".decode("utf-8"), \
                        "Deve preencher os Campos Obrigatórios - (*)"\
                        .decode("utf-8"))
            pass
             
        pass
    
    
    # Evento do escolher o ficheiro txt
    def evt_EscolherTXT(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '')
        self.lineEdit_pastaSaida.setText(fname)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.black)
        self.label_2_asterisco.setPalette(palette)
        pass
    
    # Evento do Botão Cancelar
    def evt_ButtonCancel(self):
        self.close()
        exit(0)
        pass

    # Evento de abrir o ficheiro
    def evt_abrir(self):
        
       
        dialog = QFileDialog(self)
        self.fname, _ = dialog.getOpenFileName(self, 'Abrir Ficheiro', '', filter="Ficheiros PSD (*.psd)")
      
        self.lineEdit_fileName.setText(self.fname)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.black)
        self.label_1_asterisco.setPalette(palette)
        pass
    
    pass # FIM DA CLASS