# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 651)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ct_topo = QtGui.QFrame(self.centralwidget)
        self.ct_topo.setGeometry(QtCore.QRect(0, 0, 900, 80))
        self.ct_topo.setStyleSheet(_fromUtf8("background-color: #FFF"))
        self.ct_topo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_topo.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_topo.setObjectName(_fromUtf8("ct_topo"))
        self.bt_inicio = QtGui.QPushButton(self.ct_topo)
        self.bt_inicio.setEnabled(True)
        self.bt_inicio.setGeometry(QtCore.QRect(120, 25, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bt_inicio.setFont(font)
        self.bt_inicio.setStyleSheet(_fromUtf8(""))
        self.bt_inicio.setIconSize(QtCore.QSize(90, 30))
        self.bt_inicio.setObjectName(_fromUtf8("bt_inicio"))
        self.lb_logo = QtGui.QLabel(self.ct_topo)
        self.lb_logo.setGeometry(QtCore.QRect(5, 5, 80, 70))
        self.lb_logo.setText(_fromUtf8(""))
        self.lb_logo.setObjectName(_fromUtf8("lb_logo"))
        self.bt_estoque = QtGui.QPushButton(self.ct_topo)
        self.bt_estoque.setGeometry(QtCore.QRect(340, 25, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bt_estoque.setFont(font)
        self.bt_estoque.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt_estoque.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_estoque.setStyleSheet(_fromUtf8(""))
        self.bt_estoque.setIconSize(QtCore.QSize(90, 30))
        self.bt_estoque.setObjectName(_fromUtf8("bt_estoque"))
        self.bt_clientes = QtGui.QPushButton(self.ct_topo)
        self.bt_clientes.setGeometry(QtCore.QRect(450, 25, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bt_clientes.setFont(font)
        self.bt_clientes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt_clientes.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_clientes.setStyleSheet(_fromUtf8(""))
        self.bt_clientes.setIconSize(QtCore.QSize(90, 30))
        self.bt_clientes.setObjectName(_fromUtf8("bt_clientes"))
        self.bt_usuarios = QtGui.QPushButton(self.ct_topo)
        self.bt_usuarios.setGeometry(QtCore.QRect(560, 25, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bt_usuarios.setFont(font)
        self.bt_usuarios.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt_usuarios.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_usuarios.setStyleSheet(_fromUtf8(""))
        self.bt_usuarios.setIconSize(QtCore.QSize(90, 30))
        self.bt_usuarios.setObjectName(_fromUtf8("bt_usuarios"))
        self.bt_tarefas = QtGui.QPushButton(self.ct_topo)
        self.bt_tarefas.setGeometry(QtCore.QRect(670, 25, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bt_tarefas.setFont(font)
        self.bt_tarefas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt_tarefas.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_tarefas.setStyleSheet(_fromUtf8(""))
        self.bt_tarefas.setIconSize(QtCore.QSize(90, 30))
        self.bt_tarefas.setObjectName(_fromUtf8("bt_tarefas"))
        self.bt_pedidos = QtGui.QPushButton(self.ct_topo)
        self.bt_pedidos.setGeometry(QtCore.QRect(780, 25, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bt_pedidos.setFont(font)
        self.bt_pedidos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bt_pedidos.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_pedidos.setStyleSheet(_fromUtf8(""))
        self.bt_pedidos.setIconSize(QtCore.QSize(90, 30))
        self.bt_pedidos.setObjectName(_fromUtf8("bt_pedidos"))
        self.bt_caixa = QtGui.QPushButton(self.ct_topo)
        self.bt_caixa.setEnabled(True)
        self.bt_caixa.setGeometry(QtCore.QRect(230, 25, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bt_caixa.setFont(font)
        self.bt_caixa.setStyleSheet(_fromUtf8(""))
        self.bt_caixa.setIconSize(QtCore.QSize(90, 30))
        self.bt_caixa.setObjectName(_fromUtf8("bt_caixa"))
        self.ct_conteudo = QtGui.QFrame(self.centralwidget)
        self.ct_conteudo.setGeometry(QtCore.QRect(0, 85, 900, 524))
        self.ct_conteudo.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.ct_conteudo.setFrameShape(QtGui.QFrame.NoFrame)
        self.ct_conteudo.setFrameShadow(QtGui.QFrame.Plain)
        self.ct_conteudo.setObjectName(_fromUtf8("ct_conteudo"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 80, 900, 5))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuArquivo = QtGui.QMenu(self.menuBar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        MainWindow.setMenuBar(self.menuBar)
        self.action_configurar = QtGui.QAction(MainWindow)
        self.action_configurar.setObjectName(_fromUtf8("action_configurar"))
        self.action_sair = QtGui.QAction(MainWindow)
        self.action_sair.setObjectName(_fromUtf8("action_sair"))
        self.menuArquivo.addAction(self.action_configurar)
        self.menuArquivo.addAction(self.action_sair)
        self.menuBar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_sair, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bt_inicio.setText(_translate("MainWindow", "ínicio (Alt+H)", None))
        self.bt_estoque.setText(_translate("MainWindow", "Estoque (F3)", None))
        self.bt_clientes.setText(_translate("MainWindow", "Clientes (F4)", None))
        self.bt_usuarios.setText(_translate("MainWindow", "Usuários (F5)", None))
        self.bt_tarefas.setText(_translate("MainWindow", "Tarefas (F6)", None))
        self.bt_pedidos.setText(_translate("MainWindow", "Pedidos (F7)", None))
        self.bt_caixa.setText(_translate("MainWindow", "Caixa (F2)", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.action_configurar.setText(_translate("MainWindow", "Configurar", None))
        self.action_configurar.setShortcut(_translate("MainWindow", "Ctrl+Shift+P", None))
        self.action_sair.setText(_translate("MainWindow", "sair", None))

