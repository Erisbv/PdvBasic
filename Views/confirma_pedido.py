# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirma_pedido.ui'
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

class Ui_Dialog_pedido(object):
    def setConfPedido(self, Dialog_pedido):
        Dialog_pedido.setObjectName(_fromUtf8("Dialog_pedido"))
        Dialog_pedido.resize(400, 250)
        self.frame = QtGui.QFrame(Dialog_pedido)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.frame.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 380, 230))
        self.frame_2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.lb_titulo_modal = QtGui.QLabel(self.frame_2)
        self.lb_titulo_modal.setGeometry(QtCore.QRect(90, 20, 200, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.lb_titulo_modal.setFont(font)
        self.lb_titulo_modal.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_titulo_modal.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_titulo_modal.setObjectName(_fromUtf8("lb_titulo_modal"))
        self.lb_info = QtGui.QLabel(self.frame_2)
        self.lb_info.setGeometry(QtCore.QRect(70, 70, 110, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_info.setFont(font)
        self.lb_info.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info.setObjectName(_fromUtf8("lb_info"))
        self.lb_info_2 = QtGui.QLabel(self.frame_2)
        self.lb_info_2.setGeometry(QtCore.QRect(70, 105, 110, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_info_2.setFont(font)
        self.lb_info_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_info_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info_2.setObjectName(_fromUtf8("lb_info_2"))
        self.tx_valor_entrada = QtGui.QLineEdit(self.frame_2)
        self.tx_valor_entrada.setGeometry(QtCore.QRect(190, 105, 110, 25))
        self.tx_valor_entrada.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_valor_entrada.setReadOnly(True)
        self.tx_valor_entrada.setObjectName(_fromUtf8("tx_valor_entrada"))
        self.lb_info_3 = QtGui.QLabel(self.frame_2)
        self.lb_info_3.setGeometry(QtCore.QRect(70, 140, 110, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_info_3.setFont(font)
        self.lb_info_3.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_info_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info_3.setObjectName(_fromUtf8("lb_info_3"))
        self.tx_saldo_devedor = QtGui.QLineEdit(self.frame_2)
        self.tx_saldo_devedor.setGeometry(QtCore.QRect(190, 140, 110, 25))
        self.tx_saldo_devedor.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_saldo_devedor.setReadOnly(True)
        self.tx_saldo_devedor.setObjectName(_fromUtf8("tx_saldo_devedor"))
        self.bt_ok_pedido = QtGui.QPushButton(self.frame_2)
        self.bt_ok_pedido.setGeometry(QtCore.QRect(75, 180, 100, 30))
        self.bt_ok_pedido.setObjectName(_fromUtf8("bt_ok_pedido"))
        self.bt_cancel_pedido = QtGui.QPushButton(self.frame_2)
        self.bt_cancel_pedido.setGeometry(QtCore.QRect(195, 180, 100, 30))
        self.bt_cancel_pedido.setObjectName(_fromUtf8("bt_cancel_pedido"))
        self.tx_data_entrega = QtGui.QLineEdit(self.frame_2)
        self.tx_data_entrega.setGeometry(QtCore.QRect(190, 70, 110, 25))
        self.tx_data_entrega.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_data_entrega.setReadOnly(True)
        self.tx_data_entrega.setObjectName(_fromUtf8("tx_data_entrega"))

        self.tradConfPedido(Dialog_pedido)
        QtCore.QMetaObject.connectSlotsByName(Dialog_pedido)

    def tradConfPedido(self, Dialog_pedido):
        Dialog_pedido.setWindowTitle(_translate("Dialog_pedido", "Confirma????o", None))
        self.lb_titulo_modal.setText(_translate("Dialog_pedido", "Confirmar Pedido", None))
        self.lb_info.setText(_translate("Dialog_pedido", "Data de Entrega", None))
        self.lb_info_2.setText(_translate("Dialog_pedido", "Entrada", None))
        self.lb_info_3.setText(_translate("Dialog_pedido", "Saldo devedor", None))
        self.bt_ok_pedido.setText(_translate("Dialog_pedido", "OK", None))
        self.bt_cancel_pedido.setText(_translate("Dialog_pedido", "Cancelar", None))

