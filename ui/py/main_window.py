# Form implementation generated from reading ui file 'ui/qt/mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1251, 837)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vuz = QtWidgets.QComboBox(parent=self.centralwidget)
        self.vuz.setEditable(True)
        self.vuz.setObjectName("vuz")
        self.gridLayout.addWidget(self.vuz, 6, 0, 1, 1)
        self.obl = QtWidgets.QComboBox(parent=self.centralwidget)
        self.obl.setEditable(True)
        self.obl.setObjectName("obl")
        self.gridLayout.addWidget(self.obl, 6, 3, 1, 1)
        self.clear_filter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_filter.setObjectName("clear_filter")
        self.gridLayout.addWidget(self.clear_filter, 7, 3, 1, 1)
        self.set_filter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.set_filter.setObjectName("set_filter")
        self.gridLayout.addWidget(self.set_filter, 7, 4, 1, 1)
        self.city = QtWidgets.QComboBox(parent=self.centralwidget)
        self.city.setEditable(True)
        self.city.setObjectName("city")
        self.gridLayout.addWidget(self.city, 6, 1, 1, 1)
        self.subject = QtWidgets.QComboBox(parent=self.centralwidget)
        self.subject.setEditable(True)
        self.subject.setObjectName("subject")
        self.gridLayout.addWidget(self.subject, 6, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.grnti_code = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grnti_code.sizePolicy().hasHeightForWidth())
        self.grnti_code.setSizePolicy(sizePolicy)
        self.grnti_code.setObjectName("grnti_code")
        self.gridLayout.addWidget(self.grnti_code, 6, 4, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAccessibleDescription("")
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setAutoFillBackground(False)
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(parent=self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView.setFont(font)
        self.tableView.setAutoFillBackground(False)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setAutoFillBackground(False)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableView_2 = QtWidgets.QTableView(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView_2.setFont(font)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout_3.addWidget(self.tableView_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setAutoFillBackground(False)
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableView_3 = QtWidgets.QTableView(parent=self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView_3.setFont(font)
        self.tableView_3.setObjectName("tableView_3")
        self.gridLayout_4.addWidget(self.tableView_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setAutoFillBackground(False)
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableView_4 = QtWidgets.QTableView(parent=self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView_4.setFont(font)
        self.tableView_4.setObjectName("tableView_4")
        self.gridLayout_5.addWidget(self.tableView_4, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.tableView_13 = QtWidgets.QTableView(parent=self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView_13.setFont(font)
        self.tableView_13.setObjectName("tableView_13")
        self.gridLayout_14.addWidget(self.tableView_13, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableView_14 = QtWidgets.QTableView(parent=self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView_14.setFont(font)
        self.tableView_14.setObjectName("tableView_14")
        self.gridLayout_6.addWidget(self.tableView_14, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 5, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1251, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menubar.setFont(font)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.about = QtWidgets.QMenu(parent=self.menubar)
        self.about.setTearOffEnabled(False)
        self.about.setToolTipsVisible(True)
        self.about.setObjectName("about")
        self.export_2 = QtWidgets.QMenu(parent=self.menubar)
        self.export_2.setTearOffEnabled(False)
        self.export_2.setToolTipsVisible(True)
        self.export_2.setObjectName("export_2")
        self.menu = QtWidgets.QMenu(parent=self.export_2)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtGui.QAction(parent=MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtGui.QAction(parent=MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtGui.QAction(parent=MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menu.addAction(self.action_7)
        self.menu.addAction(self.action_8)
        self.menu.addAction(self.action_3)
        self.export_2.addAction(self.menu.menuAction())
        self.menubar.addAction(self.export_2.menuAction())
        self.menubar.addAction(self.about.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vuz.setCurrentText(_translate("MainWindow", "ВУЗ"))
        self.vuz.setProperty("placeholderText", _translate("MainWindow", "ВУЗ"))
        self.obl.setCurrentText(_translate("MainWindow", "Регион"))
        self.obl.setProperty("placeholderText", _translate("MainWindow", "Субъект Федерации"))
        self.clear_filter.setText(_translate("MainWindow", "Очистить фильтры"))
        self.set_filter.setText(_translate("MainWindow", "Установить фильтр"))
        self.city.setCurrentText(_translate("MainWindow", "Город"))
        self.city.setProperty("placeholderText", _translate("MainWindow", "Город"))
        self.subject.setCurrentText(_translate("MainWindow", "Субъект Федерации"))
        self.subject.setProperty("placeholderText", _translate("MainWindow", "Регион"))
        self.label_5.setText(_translate("MainWindow", "Таблицы данных"))
        self.grnti_code.setPlaceholderText(_translate("MainWindow", "Код ГРНТИ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "ВУЗы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Гранты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "НТП"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Тем. планы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Сводка по ВУЗам"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Рубрики ГРНТИ"))
        self.about.setTitle(_translate("MainWindow", "Помощь"))
        self.export_2.setTitle(_translate("MainWindow", "Отчёт"))
        self.menu.setTitle(_translate("MainWindow", "Анализ"))
        self.action.setText(_translate("MainWindow", "Отчёт"))
        self.action_2.setText(_translate("MainWindow", "Отчёт"))
        self.action_5.setText(_translate("MainWindow", "Распределение НИР по вузам"))
        self.action_6.setText(_translate("MainWindow", "Распределение НИР по федеральным округам"))
        self.action_7.setText(_translate("MainWindow", "Распределение НИР по статусам"))
        self.action_8.setText(_translate("MainWindow", "Распределение НИР по характеру"))
        self.action_9.setText(_translate("MainWindow", "Сводка"))
        self.action_3.setText(_translate("MainWindow", "Распределение НИР по кол-ву работ рубрики ГРНТИ"))
