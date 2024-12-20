# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_management.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_panel = QFrame(self.centralwidget)
        self.left_panel.setObjectName(u"left_panel")
        self.gridLayout = QGridLayout(self.left_panel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.left_panel)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(141, 41))
        font = QFont()
        font.setFamilies([u"\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53"])
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.add_button = QPushButton(self.left_panel)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(141, 51))

        self.verticalLayout.addWidget(self.add_button)

        self.edit_button = QPushButton(self.left_panel)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setMinimumSize(QSize(141, 51))

        self.verticalLayout.addWidget(self.edit_button)

        self.delete_button = QPushButton(self.left_panel)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMinimumSize(QSize(141, 51))

        self.verticalLayout.addWidget(self.delete_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.left_panel)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(141, 41))
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.search_input = QLineEdit(self.left_panel)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(141, 31))

        self.verticalLayout.addWidget(self.search_input)

        self.search_button = QPushButton(self.left_panel)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(141, 51))

        self.verticalLayout.addWidget(self.search_button)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.left_panel)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(611, 0))

        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.left_panel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u7ba1\u7406\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u9762\u677f", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5b66\u751f", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u5b66\u751f", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5b66\u751f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5b66\u751f...", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
    # retranslateUi

