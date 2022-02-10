# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

from pyqtgraph.Qt import QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(488, 688)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 481, 651))
        self.tabDatos = QWidget()
        self.tabDatos.setObjectName(u"tabDatos")
        self.verticalLayoutWidget = QWidget(self.tabDatos)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(120, 10, 198, 342))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.spinBox = QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_3.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.verticalLayout_3.addWidget(self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.verticalLayout_3.addWidget(self.spinBox_3)

        self.spinBox_4 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.verticalLayout_3.addWidget(self.spinBox_4)

        self.spinBox_5 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.verticalLayout_3.addWidget(self.spinBox_5)

        self.spinBox_6 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.verticalLayout_3.addWidget(self.spinBox_6)

        self.spinBox_7 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.verticalLayout_3.addWidget(self.spinBox_7)

        self.spinBox_8 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.verticalLayout_3.addWidget(self.spinBox_8)

        self.spinBox_9 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_9.setObjectName(u"spinBox_9")

        self.verticalLayout_3.addWidget(self.spinBox_9)

        self.spinBox_10 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_10.setObjectName(u"spinBox_10")

        self.verticalLayout_3.addWidget(self.spinBox_10)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_4.addWidget(self.label_13)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_4.addWidget(self.label_14)

        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_4.addWidget(self.label_15)

        self.label_16 = QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_4.addWidget(self.label_16)

        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_4.addWidget(self.label_17)

        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_4.addWidget(self.label_18)

        self.label_19 = QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_4.addWidget(self.label_19)

        self.label_20 = QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_4.addWidget(self.label_20)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.spinBox_11 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_11.setObjectName(u"spinBox_11")

        self.verticalLayout_5.addWidget(self.spinBox_11)

        self.spinBox_12 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_12.setObjectName(u"spinBox_12")

        self.verticalLayout_5.addWidget(self.spinBox_12)

        self.spinBox_13 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_13.setObjectName(u"spinBox_13")

        self.verticalLayout_5.addWidget(self.spinBox_13)

        self.spinBox_14 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_14.setObjectName(u"spinBox_14")

        self.verticalLayout_5.addWidget(self.spinBox_14)

        self.spinBox_15 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_15.setObjectName(u"spinBox_15")

        self.verticalLayout_5.addWidget(self.spinBox_15)

        self.spinBox_16 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_16.setObjectName(u"spinBox_16")

        self.verticalLayout_5.addWidget(self.spinBox_16)

        self.spinBox_17 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_17.setObjectName(u"spinBox_17")

        self.verticalLayout_5.addWidget(self.spinBox_17)

        self.spinBox_18 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_18.setObjectName(u"spinBox_18")

        self.verticalLayout_5.addWidget(self.spinBox_18)

        self.spinBox_19 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_19.setObjectName(u"spinBox_19")

        self.verticalLayout_5.addWidget(self.spinBox_19)

        self.spinBox_20 = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_20.setObjectName(u"spinBox_20")

        self.verticalLayout_5.addWidget(self.spinBox_20)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        # self.graphWidget = pg.PlotWidget()(self.tabDatos)
        # self.graphWidget.setObjectName(u"pg.PlotWidget")
        # self.graphWidget.setGeometry(QRect(10, 360, 441, 251))

        self.tabWidget.addTab(self.tabDatos, "")

        self.tabInforme = QWidget()
        self.tabInforme.setObjectName(u"tabInforme")

        self.webpdf = QWebEngineView(self.tabInforme)
        self.webpdf.setObjectName(u"QWebEngineView2")
        self.webpdf.setGeometry(QRect(10, 10, 451, 601))
        self.tabWidget.addTab(self.tabInforme, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 488, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.spinBox)
        self.label_2.setBuddy(self.spinBox_2)
        self.label_3.setBuddy(self.spinBox_3)
        self.label_4.setBuddy(self.spinBox_4)
        self.label_5.setBuddy(self.spinBox_5)
        self.label_6.setBuddy(self.spinBox_6)
        self.label_7.setBuddy(self.spinBox_7)
        self.label_8.setBuddy(self.spinBox_8)
        self.label_9.setBuddy(self.spinBox_9)
        self.label_10.setBuddy(self.spinBox_10)
        self.label_11.setBuddy(self.spinBox)
        self.label_12.setBuddy(self.spinBox)
        self.label_13.setBuddy(self.spinBox)
        self.label_14.setBuddy(self.spinBox)
        self.label_15.setBuddy(self.spinBox)
        self.label_16.setBuddy(self.spinBox)
        self.label_17.setBuddy(self.spinBox)
        self.label_18.setBuddy(self.spinBox)
        self.label_19.setBuddy(self.spinBox)
        self.label_20.setBuddy(self.spinBox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dato x1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dato x2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dato x3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dato x4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dato x5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dato x6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dato x7", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dato x8", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dato x9", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dato x10", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dato y1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Dato y2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Dato y3", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Dato y4", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Dato y5", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Dato y6", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Dato y7", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Dato y8", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Dato y9", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Dato y10", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generar Gr\u00e1fica", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generar Informe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDatos), QCoreApplication.translate("MainWindow", u"Datos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInforme), QCoreApplication.translate("MainWindow", u"Informe", None))
    # retranslateUi

