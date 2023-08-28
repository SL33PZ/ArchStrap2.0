from PyQt6 import QtCore, QtGui, QtWidgets

from lists.desktopEnvironments import DESKTOP_ENVIRONMENT
from lists.displayManagers import DISPLAY_MANAGER
from lists.languages import LANGUAGE
from lists.timezones import TIMEZONE
from lists.kernels import KERNELS

import resource_rc
import sys, os, subprocess

import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 503)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 503))
        MainWindow.setBaseSize(QtCore.QSize(800, 500))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/images/ArchStrapIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        self.mainWidget = QtWidgets.QWidget(parent=MainWindow)
        self.mainWidget.setStyleSheet("QWidget#mainWidget {\n"
"    background-image: url(:/images/Gradient.png);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid rgba(0, 0, 0, 0);\n"
"    font: 11pt \"Comfortaa\";\n"
"    color: rgb(246, 245, 244);\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    \n"
"    background-image: url(:/images/input_field.png);\n"
"    border: 0.5px solid grey;\n"
"    border-radius: 5px;\n"
"    font: 11pt \"Comfortaa\";\n"
"    color: rgb(246, 245, 244);\n"
"}\n"
"\n"
"QCheckBox {\n"
"    font: 11pt \"Comfortaa\";\n"
"    color: rgb(246, 245, 244);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/images/checkBox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/images/checkBox_unchecked.png);\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-image: url(:/images/input_field.png);\n"
"    border: 0.5px solid grey;\n"
"    border-radius: 5px;\n"
"    font: 11pt \"Comfortaa\";\n"
"    color: rgb(246, 245, 244);\n"
"    combobox-popup: 0;\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    font: 11pt \"Comfortaa\";\n"
"    color: rgb(246, 245, 244);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    font: 11pt \"Comfortaa\";\n"
"    color: rgb(246, 245, 244);\n"
"    border-left-width: 0.5px;\n"
"    border-left-color: rgba(0, 0, 0, 0);\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/images/down_arrow.png);\n"
"    margin-right: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"}\n"
"")
        self.mainWidget.setObjectName("mainWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_left = QtWidgets.QWidget(parent=self.mainWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.widget_left.setFont(font)
        self.widget_left.setObjectName("widget_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_left)
        self.verticalLayout_2.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_environment = QtWidgets.QGroupBox(parent=self.widget_left)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.groupBox_environment.setFont(font)
        self.groupBox_environment.setTitle("")
        self.groupBox_environment.setObjectName("groupBox_environment")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_environment)
        self.verticalLayout_3.setContentsMargins(50, 0, 0, 30)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_language = QtWidgets.QComboBox(parent=self.groupBox_environment)
        self.comboBox_language.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_language.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.comboBox_language.setFont(font)
        self.comboBox_language.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.comboBox_language.setEditable(False)
        self.comboBox_language.setMaxVisibleItems(10)
        self.comboBox_language.setMaxCount(999)
        self.comboBox_language.setMinimumContentsLength(1)
        self.comboBox_language.setObjectName("comboBox_language")
        self.verticalLayout_3.addWidget(self.comboBox_language)
        self.comboBox_timezone = QtWidgets.QComboBox(parent=self.groupBox_environment)
        self.comboBox_timezone.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_timezone.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.comboBox_timezone.setFont(font)
        self.comboBox_timezone.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.comboBox_timezone.setAutoFillBackground(False)
        self.comboBox_timezone.setMaxVisibleItems(10)
        self.comboBox_timezone.setMaxCount(999)
        self.comboBox_timezone.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.comboBox_timezone.setMinimumContentsLength(1)
        self.comboBox_timezone.setObjectName("comboBox_timezone")
        self.verticalLayout_3.addWidget(self.comboBox_timezone)
        self.comboBox_desktopEnvironment = QtWidgets.QComboBox(parent=self.groupBox_environment)
        self.comboBox_desktopEnvironment.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_desktopEnvironment.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.comboBox_desktopEnvironment.setFont(font)
        self.comboBox_desktopEnvironment.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.comboBox_desktopEnvironment.setMaxVisibleItems(10)
        self.comboBox_desktopEnvironment.setMaxCount(999)
        self.comboBox_desktopEnvironment.setMinimumContentsLength(1)
        self.comboBox_desktopEnvironment.setObjectName("comboBox_desktopEnvironment")
        self.verticalLayout_3.addWidget(self.comboBox_desktopEnvironment)
        self.comboBox_displayManager = QtWidgets.QComboBox(parent=self.groupBox_environment)
        self.comboBox_displayManager.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_displayManager.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.comboBox_displayManager.setFont(font)
        self.comboBox_displayManager.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.comboBox_displayManager.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.comboBox_displayManager.setMaxVisibleItems(10)
        self.comboBox_displayManager.setMaxCount(999)
        self.comboBox_displayManager.setMinimumContentsLength(1)
        self.comboBox_displayManager.setObjectName("comboBox_displayManager")
        self.verticalLayout_3.addWidget(self.comboBox_displayManager)
        self.comboBox_kernel = QtWidgets.QComboBox(parent=self.groupBox_environment)
        self.comboBox_kernel.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_kernel.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.comboBox_kernel.setFont(font)
        self.comboBox_kernel.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.comboBox_kernel.setMaxVisibleItems(10)
        self.comboBox_kernel.setMaxCount(999)
        self.comboBox_kernel.setMinimumContentsLength(1)
        self.comboBox_kernel.setObjectName("comboBox_kernel")
        self.verticalLayout_3.addWidget(self.comboBox_kernel)
        self.verticalLayout_2.addWidget(self.groupBox_environment, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_optionals = QtWidgets.QGroupBox(parent=self.widget_left)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.groupBox_optionals.setFont(font)
        self.groupBox_optionals.setObjectName("groupBox_optionals")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_optionals)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_klassy = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_klassy.setFont(font)
        self.checkBox_klassy.setObjectName("checkBox_klassy")
        self.gridLayout.addWidget(self.checkBox_klassy, 2, 0, 1, 1)
        self.checkBox_geany = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_geany.setFont(font)
        self.checkBox_geany.setObjectName("checkBox_geany")
        self.gridLayout.addWidget(self.checkBox_geany, 4, 2, 1, 1)
        self.checkBox_figma = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_figma.setFont(font)
        self.checkBox_figma.setObjectName("checkBox_figma")
        self.gridLayout.addWidget(self.checkBox_figma, 2, 2, 1, 1)
        self.checkBox_miniconda = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_miniconda.setFont(font)
        self.checkBox_miniconda.setObjectName("checkBox_miniconda")
        self.gridLayout.addWidget(self.checkBox_miniconda, 2, 1, 1, 1)
        self.checkBox_yay = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_yay.setFont(font)
        self.checkBox_yay.setObjectName("checkBox_yay")
        self.gridLayout.addWidget(self.checkBox_yay, 0, 0, 1, 1)
        self.checkBox_micro = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_micro.setFont(font)
        self.checkBox_micro.setObjectName("checkBox_micro")
        self.gridLayout.addWidget(self.checkBox_micro, 3, 1, 1, 1)
        self.checkBox_kitty = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_kitty.setFont(font)
        self.checkBox_kitty.setObjectName("checkBox_kitty")
        self.gridLayout.addWidget(self.checkBox_kitty, 3, 2, 1, 1)
        self.checkBox_neofetch = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_neofetch.setFont(font)
        self.checkBox_neofetch.setObjectName("checkBox_neofetch")
        self.gridLayout.addWidget(self.checkBox_neofetch, 4, 0, 1, 1)
        self.checkBox_npm = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_npm.setFont(font)
        self.checkBox_npm.setObjectName("checkBox_npm")
        self.gridLayout.addWidget(self.checkBox_npm, 0, 2, 1, 1)
        self.checkBox_lightly = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_lightly.setFont(font)
        self.checkBox_lightly.setObjectName("checkBox_lightly")
        self.gridLayout.addWidget(self.checkBox_lightly, 1, 2, 1, 1)
        self.checkBox_inkscape = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_inkscape.setFont(font)
        self.checkBox_inkscape.setObjectName("checkBox_inkscape")
        self.gridLayout.addWidget(self.checkBox_inkscape, 3, 0, 1, 1)
        self.checkBox_bleachBit = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_bleachBit.setFont(font)
        self.checkBox_bleachBit.setObjectName("checkBox_bleachBit")
        self.gridLayout.addWidget(self.checkBox_bleachBit, 0, 1, 1, 1)
        self.checkBox_vscode = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_vscode.setFont(font)
        self.checkBox_vscode.setObjectName("checkBox_vscode")
        self.gridLayout.addWidget(self.checkBox_vscode, 1, 1, 1, 1)
        self.checkBox_chromium = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_chromium.setFont(font)
        self.checkBox_chromium.setObjectName("checkBox_chromium")
        self.gridLayout.addWidget(self.checkBox_chromium, 1, 0, 1, 1)
        self.checkBox_lolcat = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_lolcat.setFont(font)
        self.checkBox_lolcat.setObjectName("checkBox_lolcat")
        self.gridLayout.addWidget(self.checkBox_lolcat, 4, 1, 1, 1)
        self.checkBox_okular = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_okular.setFont(font)
        self.checkBox_okular.setObjectName("checkBox_okular")
        self.gridLayout.addWidget(self.checkBox_okular, 5, 0, 1, 1)
        self.checkBox_fontManager = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_fontManager.setFont(font)
        self.checkBox_fontManager.setObjectName("checkBox_fontManager")
        self.gridLayout.addWidget(self.checkBox_fontManager, 5, 1, 1, 1)
        self.checkBox_gparted = QtWidgets.QCheckBox(parent=self.groupBox_optionals)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.checkBox_gparted.setFont(font)
        self.checkBox_gparted.setObjectName("checkBox_gparted")
        self.gridLayout.addWidget(self.checkBox_gparted, 5, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_optionals, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addWidget(self.widget_left)
        self.widget_right = QtWidgets.QWidget(parent=self.mainWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.widget_right.setFont(font)
        self.widget_right.setObjectName("widget_right")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_right)
        self.verticalLayout.setContentsMargins(0, 28, 0, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_userSettings = QtWidgets.QGroupBox(parent=self.widget_right)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.groupBox_userSettings.setFont(font)
        self.groupBox_userSettings.setTitle("")
        self.groupBox_userSettings.setObjectName("groupBox_userSettings")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_userSettings)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_names = QtWidgets.QGroupBox(parent=self.groupBox_userSettings)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.groupBox_names.setFont(font)
        self.groupBox_names.setTitle("")
        self.groupBox_names.setObjectName("groupBox_names")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_names)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_hostname = QtWidgets.QLineEdit(parent=self.groupBox_names)
        self.lineEdit_hostname.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_hostname.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lineEdit_hostname.setFont(font)
        self.lineEdit_hostname.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly|QtCore.Qt.InputMethodHint.ImhLatinOnly)
        self.lineEdit_hostname.setMaxLength(16)
        self.lineEdit_hostname.setCursorPosition(0)
        self.lineEdit_hostname.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_hostname.setObjectName("lineEdit_hostname")
        self.verticalLayout_6.addWidget(self.lineEdit_hostname)
        self.lineEdit_username = QtWidgets.QLineEdit(parent=self.groupBox_names)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly|QtCore.Qt.InputMethodHint.ImhLatinOnly|QtCore.Qt.InputMethodHint.ImhLowercaseOnly)
        self.lineEdit_username.setMaxLength(16)
        self.lineEdit_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout_6.addWidget(self.lineEdit_username)
        self.verticalLayout_4.addWidget(self.groupBox_names)
        self.groupBox_userPw = QtWidgets.QGroupBox(parent=self.groupBox_userSettings)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.groupBox_userPw.setFont(font)
        self.groupBox_userPw.setTitle("")
        self.groupBox_userPw.setObjectName("groupBox_userPw")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_userPw)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_userPw = QtWidgets.QLineEdit(parent=self.groupBox_userPw)
        self.lineEdit_userPw.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_userPw.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lineEdit_userPw.setFont(font)
        self.lineEdit_userPw.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhLatinOnly|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.lineEdit_userPw.setMaxLength(16)
        self.lineEdit_userPw.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_userPw.setCursorPosition(0)
        self.lineEdit_userPw.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_userPw.setObjectName("lineEdit_userPw")
        self.verticalLayout_7.addWidget(self.lineEdit_userPw)
        self.lineEdit_userPw_confirm = QtWidgets.QLineEdit(parent=self.groupBox_userPw)
        self.lineEdit_userPw_confirm.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_userPw_confirm.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lineEdit_userPw_confirm.setFont(font)
        self.lineEdit_userPw_confirm.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhLatinOnly|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.lineEdit_userPw_confirm.setMaxLength(16)
        self.lineEdit_userPw_confirm.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_userPw_confirm.setCursorPosition(0)
        self.lineEdit_userPw_confirm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_userPw_confirm.setObjectName("lineEdit_userPw_confirm")
        self.verticalLayout_7.addWidget(self.lineEdit_userPw_confirm)
        self.verticalLayout_4.addWidget(self.groupBox_userPw)
        self.groupBox_rootPw = QtWidgets.QGroupBox(parent=self.groupBox_userSettings)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.groupBox_rootPw.setFont(font)
        self.groupBox_rootPw.setTitle("")
        self.groupBox_rootPw.setObjectName("groupBox_rootPw")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_rootPw)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_rootPw = QtWidgets.QLineEdit(parent=self.groupBox_rootPw)
        self.lineEdit_rootPw.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_rootPw.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lineEdit_rootPw.setFont(font)
        self.lineEdit_rootPw.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhLatinOnly|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.lineEdit_rootPw.setMaxLength(16)
        self.lineEdit_rootPw.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_rootPw.setCursorPosition(0)
        self.lineEdit_rootPw.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_rootPw.setObjectName("lineEdit_rootPw")
        self.verticalLayout_8.addWidget(self.lineEdit_rootPw)
        self.lineEdit_rootPw_confirm = QtWidgets.QLineEdit(parent=self.groupBox_rootPw)
        self.lineEdit_rootPw_confirm.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_rootPw_confirm.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lineEdit_rootPw_confirm.setFont(font)
        self.lineEdit_rootPw_confirm.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhLatinOnly|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.lineEdit_rootPw_confirm.setMaxLength(16)
        self.lineEdit_rootPw_confirm.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_rootPw_confirm.setCursorPosition(0)
        self.lineEdit_rootPw_confirm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_rootPw_confirm.setObjectName("lineEdit_rootPw_confirm")
        self.verticalLayout_8.addWidget(self.lineEdit_rootPw_confirm)
        self.verticalLayout_4.addWidget(self.groupBox_rootPw)
        self.verticalLayout.addWidget(self.groupBox_userSettings)
        self.groupBox_partitions = QtWidgets.QGroupBox(parent=self.widget_right)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.groupBox_partitions.setFont(font)
        self.groupBox_partitions.setTitle("")
        self.groupBox_partitions.setObjectName("groupBox_partitions")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_partitions)
        self.verticalLayout_5.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBox_efi = QtWidgets.QComboBox(parent=self.groupBox_partitions)
        self.comboBox_efi.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_efi.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.comboBox_efi.setFont(font)
        self.comboBox_efi.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox_efi.setMaxCount(10)
        self.comboBox_efi.setObjectName("comboBox_efi")
        self.verticalLayout_5.addWidget(self.comboBox_efi)
        self.comboBox_swap = QtWidgets.QComboBox(parent=self.groupBox_partitions)
        self.comboBox_swap.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_swap.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.comboBox_swap.setFont(font)
        self.comboBox_swap.setMaxCount(10)
        self.comboBox_swap.setObjectName("comboBox_swap")
        self.verticalLayout_5.addWidget(self.comboBox_swap)
        self.comboBox_root = QtWidgets.QComboBox(parent=self.groupBox_partitions)
        self.comboBox_root.setMinimumSize(QtCore.QSize(250, 25))
        self.comboBox_root.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.comboBox_root.setFont(font)
        self.comboBox_root.setMaxCount(10)
        self.comboBox_root.setObjectName("comboBox_root")
        self.verticalLayout_5.addWidget(self.comboBox_root)
        self.verticalLayout.addWidget(self.groupBox_partitions)
        self.groupBox_buttons = QtWidgets.QGroupBox(parent=self.widget_right)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.groupBox_buttons.setFont(font)
        self.groupBox_buttons.setTitle("")
        self.groupBox_buttons.setObjectName("groupBox_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_buttons)
        self.horizontalLayout_2.setContentsMargins(0, 20, 0, 0)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_exit = QtWidgets.QToolButton(parent=self.groupBox_buttons)
        self.toolButton_exit.setMinimumSize(QtCore.QSize(98, 98))
        self.toolButton_exit.setMaximumSize(QtCore.QSize(98, 98))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.toolButton_exit.setFont(font)
        self.toolButton_exit.setStyleSheet("QToolButton#toolButton_exit {\n"
"    background-image: url(:/images/button_exit.png);\n"
" }\n"
"\n"
"QToolButton#toolButton_exit::hover {    \n"
"    background-image: url(:/images/button_exit_hover.png);\n"
" }")
        self.toolButton_exit.setText("")
        self.toolButton_exit.setIconSize(QtCore.QSize(94, 94))
        self.toolButton_exit.setObjectName("toolButton_exit")
        self.horizontalLayout_2.addWidget(self.toolButton_exit)
        self.toolButton_start = QtWidgets.QToolButton(parent=self.groupBox_buttons)
        self.toolButton_start.setMinimumSize(QtCore.QSize(98, 98))
        self.toolButton_start.setMaximumSize(QtCore.QSize(98, 98))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.toolButton_start.setFont(font)
        self.toolButton_start.setStyleSheet("QToolButton#toolButton_start {\n"
"    background-image: url(:/images/button_start.png);\n"
" }\n"
"\n"
"QToolButton#toolButton_start::hover {\n"
"    background-image: url(:/images/button_start_hover.png);\n"
" }")
        self.toolButton_start.setText("")
        self.toolButton_start.setIconSize(QtCore.QSize(94, 94))
        self.toolButton_start.setObjectName("toolButton_start")
        self.horizontalLayout_2.addWidget(self.toolButton_start)
        self.verticalLayout.addWidget(self.groupBox_buttons, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout.addWidget(self.widget_right, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        MainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox_language, self.comboBox_timezone)
        MainWindow.setTabOrder(self.comboBox_timezone, self.comboBox_desktopEnvironment)
        MainWindow.setTabOrder(self.comboBox_desktopEnvironment, self.comboBox_displayManager)
        MainWindow.setTabOrder(self.comboBox_displayManager, self.lineEdit_hostname)
        MainWindow.setTabOrder(self.lineEdit_hostname, self.lineEdit_username)
        MainWindow.setTabOrder(self.lineEdit_username, self.lineEdit_userPw)
        MainWindow.setTabOrder(self.lineEdit_userPw, self.lineEdit_userPw_confirm)
        MainWindow.setTabOrder(self.lineEdit_userPw_confirm, self.lineEdit_rootPw)
        MainWindow.setTabOrder(self.lineEdit_rootPw, self.lineEdit_rootPw_confirm)
        MainWindow.setTabOrder(self.lineEdit_rootPw_confirm, self.comboBox_efi)
        MainWindow.setTabOrder(self.comboBox_efi, self.comboBox_swap)
        MainWindow.setTabOrder(self.comboBox_swap, self.comboBox_root)
        MainWindow.setTabOrder(self.comboBox_root, self.checkBox_yay)
        MainWindow.setTabOrder(self.checkBox_yay, self.checkBox_bleachBit)
        MainWindow.setTabOrder(self.checkBox_bleachBit, self.checkBox_npm)
        MainWindow.setTabOrder(self.checkBox_npm, self.checkBox_chromium)
        MainWindow.setTabOrder(self.checkBox_chromium, self.checkBox_vscode)
        MainWindow.setTabOrder(self.checkBox_vscode, self.checkBox_lightly)
        MainWindow.setTabOrder(self.checkBox_lightly, self.checkBox_klassy)
        MainWindow.setTabOrder(self.checkBox_klassy, self.checkBox_miniconda)
        MainWindow.setTabOrder(self.checkBox_miniconda, self.checkBox_figma)
        MainWindow.setTabOrder(self.checkBox_figma, self.checkBox_inkscape)
        MainWindow.setTabOrder(self.checkBox_inkscape, self.checkBox_micro)
        MainWindow.setTabOrder(self.checkBox_micro, self.checkBox_kitty)
        MainWindow.setTabOrder(self.checkBox_kitty, self.checkBox_neofetch)
        MainWindow.setTabOrder(self.checkBox_neofetch, self.checkBox_lolcat)
        MainWindow.setTabOrder(self.checkBox_lolcat, self.checkBox_geany)
        MainWindow.setTabOrder(self.checkBox_geany, self.checkBox_okular)
        MainWindow.setTabOrder(self.checkBox_okular, self.checkBox_fontManager)
        MainWindow.setTabOrder(self.checkBox_fontManager, self.checkBox_gparted)
        MainWindow.setTabOrder(self.checkBox_gparted, self.toolButton_exit)
        MainWindow.setTabOrder(self.toolButton_exit, self.toolButton_start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ArchStrap2.0"))
        self.comboBox_language.setPlaceholderText(_translate("MainWindow", "Language"))
        self.comboBox_timezone.setPlaceholderText(_translate("MainWindow", "Timezone"))
        self.comboBox_desktopEnvironment.setPlaceholderText(_translate("MainWindow", "Desktop Environment"))
        self.comboBox_displayManager.setPlaceholderText(_translate("MainWindow", "Display Manager"))
        self.comboBox_kernel.setPlaceholderText(_translate("MainWindow", "Kernel"))
        self.groupBox_optionals.setTitle(_translate("MainWindow", "Optionals"))
        self.checkBox_klassy.setText(_translate("MainWindow", "Klassy"))
        self.checkBox_geany.setText(_translate("MainWindow", "Geany"))
        self.checkBox_figma.setText(_translate("MainWindow", "Figma"))
        self.checkBox_miniconda.setText(_translate("MainWindow", "Miniconda"))
        self.checkBox_yay.setText(_translate("MainWindow", "Yay"))
        self.checkBox_micro.setText(_translate("MainWindow", "Micro"))
        self.checkBox_kitty.setText(_translate("MainWindow", "Kitty"))
        self.checkBox_neofetch.setText(_translate("MainWindow", "Neofetch"))
        self.checkBox_npm.setText(_translate("MainWindow", "NPM"))
        self.checkBox_lightly.setText(_translate("MainWindow", "Lightly"))
        self.checkBox_inkscape.setText(_translate("MainWindow", "Inkscape"))
        self.checkBox_bleachBit.setText(_translate("MainWindow", "BleachBit"))
        self.checkBox_vscode.setText(_translate("MainWindow", "VSCode"))
        self.checkBox_chromium.setText(_translate("MainWindow", "Chromium"))
        self.checkBox_lolcat.setText(_translate("MainWindow", "Lolcat"))
        self.checkBox_okular.setText(_translate("MainWindow", "Okluar"))
        self.checkBox_fontManager.setText(_translate("MainWindow", "F. Manager"))
        self.checkBox_gparted.setText(_translate("MainWindow", "GParted"))
        self.lineEdit_hostname.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#e01b24;\">*Must have a length between 4-16 characters</span></p><p><span style=\" font-style:italic; color:#e01b24;\">*Only Alphanumeric</span></p></body></html>"))
        self.lineEdit_hostname.setPlaceholderText(_translate("MainWindow", "Hostname"))
        self.lineEdit_username.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#e01b24;\">*Must have a length between 4-16 characters</span></p><p><span style=\" font-style:italic; color:#e01b24;\">*Only Alphanumeric and lowercase are allowed</span></p></body></html>"))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_userPw.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#e01b24;\">*Must have a length between 1-16 characters</span></p><p><span style=\" font-style:italic; color:#e01b24;\">*All characters are allowed</span></p></body></html>"))
        self.lineEdit_userPw.setPlaceholderText(_translate("MainWindow", "User Password..."))
        self.lineEdit_userPw_confirm.setPlaceholderText(_translate("MainWindow", "Confirm Password..."))
        self.lineEdit_rootPw.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#e01b24;\">*Must have a length between 1-16 characters</span></p><p><span style=\" font-style:italic; color:#e01b24;\">*All characters are allowed</span></p></body></html>"))
        self.lineEdit_rootPw.setPlaceholderText(_translate("MainWindow", "Root Password..."))
        self.lineEdit_rootPw_confirm.setPlaceholderText(_translate("MainWindow", "Confirm Password..."))
        self.comboBox_efi.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Set your EFI Partition</span></p></body></html>"))
        self.comboBox_efi.setPlaceholderText(_translate("MainWindow", "EFI Partition"))
        self.comboBox_swap.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Set your Swap Partition</span></p></body></html>"))
        self.comboBox_swap.setPlaceholderText(_translate("MainWindow", "Swap Partition"))
        self.comboBox_root.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Set your Root Partition</span></p></body></html>"))
        self.comboBox_root.setPlaceholderText(_translate("MainWindow", "Root Partition"))
        self.toolButton_exit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#e01b24;\">Exit\'s the ArchStrap2.0 Installer</span></p></body></html>"))
        self.toolButton_start.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#e01b24;\">Start\'s the Installation process</span></p></body></html>"))


# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××× LOGIC ××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
        self.toolButton_exit.clicked.connect(self.quit_app)
        self.lineEdit_hostname.textChanged.connect(self.validateHostname)
        self.lineEdit_username.textChanged.connect(self.validateUsername)
        self.lineEdit_userPw.textChanged.connect(self.validate_user_password)
        self.lineEdit_userPw_confirm.textChanged.connect(self.validate_user_password_confirm)
        self.lineEdit_rootPw.textChanged.connect(self.validate_root_password)
        self.lineEdit_rootPw_confirm.textChanged.connect(self.validate_root_password_confirm)
        self.comboBox_language.currentTextChanged.connect(self.validate_language)
        self.comboBox_timezone.currentTextChanged.connect(self.validate_timezone)
        self.comboBox_desktopEnvironment.currentTextChanged.connect(self.validate_desktop)
        self.comboBox_displayManager.currentTextChanged.connect(self.validate_display)
        self.toolButton_start.pressed.connect(self.control_instance)
        
        devices = ["sda", "nvme0n1"]
        partitions = []

        for device in devices:
            device_path = f"/dev/{device}"
            if os.path.exists(device_path):
                with open("/proc/partitions") as f:
                    lines = f.readlines()
                    for line in lines[2:]:
                        _, _, _, name = line.split()
                        if name.startswith(device):
                            partition = name[len(device):]
                            partitions.append(partition)

        for partition in partitions:
            self.comboBox_efi.addItem(f"{device}{partition}")
            self.comboBox_swap.addItem(f"{device}{partition}")
            self.comboBox_root.addItem(f"{device}{partition}")
            
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ×××××××××××××××××××××××××××××××××× INSERT LISTS ××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #

        self.comboBox_language.addItems(LANGUAGE)
        self.comboBox_timezone.addItems(TIMEZONE)
        self.comboBox_desktopEnvironment.addItems(DESKTOP_ENVIRONMENT)
        self.comboBox_displayManager.addItems(DISPLAY_MANAGER)
        self.comboBox_kernel.addItems(KERNELS)

# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ×××××××××××××××××××××××××××××××××××× HELPERS ×××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #
# ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××× #

        self.checkBoxes = [
            self.checkBox_klassy,
            self.checkBox_geany,
            self.checkBox_figma,
            self.checkBox_miniconda,
            self.checkBox_yay,
            self.checkBox_micro,
            self.checkBox_kitty,
            self.checkBox_neofetch,
            self.checkBox_npm,
            self.checkBox_lightly,
            self.checkBox_inkscape,
            self.checkBox_bleachBit,
            self.checkBox_vscode,
            self.checkBox_chromium,
            self.checkBox_lolcat,
            self.checkBox_okular,
            self.checkBox_fontManager,
            self.checkBox_gparted
    ]
        
        self.checkBoxes_names = [
            "KLASSY",
            "GEANY",
            "FIGMA",
            "MINICONDA",
            "YAY",
            "MICRO",
            "KITTY",
            "NEOFETCH",
            "NPM",
            "LIGHTLY",
            "INKSCAPE",
            "BLEACHBIT",
            "VSCODE",
            "CHROMIUM",
            "LOLCAT",
            "OKULAR",
            "FONTMANAGER",
            "GPARTED"
        ]

        self.check_desktop = False
        self.check_display = False,
        self.check_kernel = False,
        self.check_lang = False
        self.check_time = False
        self.check_host = False
        self.check_user = False
        self.check_root_password = False
        self.check_user_password = False     


    def quit_app(self):
        os._exit(0)
        
    def control_instance(self):
        controlles = [
            self.check_desktop,
            self.check_display,
            self.check_kernel,
            self.check_lang,
            self.check_time,
            self.check_host,
            self.check_user,
            self.check_root_password,
            self.check_user_password
        ]

        if all(controlles):
            self.toolButton_start.setStyleSheet(
                "QToolButton#toolButton_start {"
                "    background-image: url(:/images/button_start_hover.png);"
                " }"
            )
            if os.path.isfile("tmp/.env"):
                os.remove("tmp/.env")

            env_data = [
                ("LANGUAGE", self.get_dictionary_value(LANGUAGE, self.comboBox_language)),
                ("TIMEZONE", self.comboBox_timezone.currentText()),
                ("DESKTOP_ENVIRONMENT", self.get_dictionary_value(DESKTOP_ENVIRONMENT, self.comboBox_desktopEnvironment)),
                ("DISPLAY_MANAGER", self.get_dictionary_value(DISPLAY_MANAGER, self.comboBox_displayManager)),
                ("KERNEL", self.get_dictionary_value(KERNELS, self.comboBox_kernel)),
                ("HOSTNAME", self.lineEdit_hostname.text()),
                ("USERNAME", self.lineEdit_username.text()),
                ("PASSWORD", self.lineEdit_userPw.text()),
                ("ROOT_PASSWORD", self.lineEdit_rootPw.text())
            ]   

            with open("tmp/.env", "a") as env:
                for key, value in env_data:
                    env.write(f"{key}='{value}'\n")

                for item, name in zip(self.checkBoxes, self.checkBoxes_names):
                    if item.isChecked():
                        env.write(f"{name}=true\n")

            self.close()

            subprocess.run(["bash", "lib/prepare.sh"], shell=False)

        else:
            self.toolButton_start.setStyleSheet(
                "QToolButton#toolButton_start {"
                "    background-image: url(:/images/button_error.png);"
                " }"
            )
        
        

    def get_dictionary_value(self, dictionary, combobox):
        return dictionary.get(combobox.currentText())
        
    def validate_language(self):
        self.check_lang = self.comboBox_language.currentIndex() != -1
        if self.check_lang:
            self.get_dictionary_value(LANGUAGE, self.comboBox_language)
            
    def validate_timezone(self):
        self.check_time = self.comboBox_timezone.currentIndex() != -1
            
    def validate_desktop(self):
        self.check_desktop = self.comboBox_desktopEnvironment.currentIndex() != -1
        if self.check_desktop:
            self.get_dictionary_value(DESKTOP_ENVIRONMENT, self.comboBox_desktopEnvironment)
            
    def validate_display(self):
        self.check_display = self.comboBox_displayManager.currentIndex() != -1
        if self.check_display:
            self.get_dictionary_value(DISPLAY_MANAGER, self.comboBox_displayManager)
            
    def validate_kernel(self):
        self.check_kernel = self.comboBox_kernel.currentIndex() != -1
        if self.check_kernel:
            self.get_dictionary_value(KERNELS, self.comboBox_kernel)
        
    def validate_user_password(self):
        password = self.lineEdit_userPw.text()
        if not password:
            self.neutral(self.lineEdit_userPw)
        elif 1 <= len(password) <= 16:
            self.success(self.lineEdit_userPw)
        else:
            self.error(self.lineEdit_userPw)

    def validate_user_password_confirm(self):
        user_pw_confirm = self.lineEdit_userPw_confirm.text()
        user_pw = self.lineEdit_userPw.text()

        if not user_pw_confirm or len(user_pw_confirm) < 1:
            self.neutral(self.lineEdit_userPw_confirm)
        elif user_pw_confirm == user_pw:
            self.success(self.lineEdit_userPw_confirm)
            self.check_user_password = True
        else:
            self.error(self.lineEdit_userPw_confirm)
            self.check_user_password = False
                
    def validate_root_password(self):
        root_pw = self.lineEdit_rootPw.text()
        if not root_pw or len(root_pw) < 1:
            self.neutral(self.lineEdit_rootPw)
        elif 1 <= len(root_pw) <= 16:
            self.success(self.lineEdit_rootPw)
        else:
            self.error(self.lineEdit_rootPw)

    def validate_root_password_confirm(self):
        password_confirm = self.lineEdit_rootPw_confirm.text()
        password = self.lineEdit_rootPw.text()

        if not password_confirm:
            self.neutral(self.lineEdit_rootPw_confirm)
        elif password_confirm == password:
            self.success(self.lineEdit_rootPw_confirm)
            self.check_root_password = True
        else:
            self.error(self.lineEdit_rootPw_confirm)
            self.check_root_password = False

    def validateHostname(self):
        hostname = self.lineEdit_hostname.text()
        if len(hostname) == 0 or len(hostname) < 4:
            self.neutral(self.lineEdit_hostname)
        elif hostname and hostname[0].isalnum() and 4 <= len(hostname) <= 16:
            self.success(self.lineEdit_hostname)
            self.check_host = True
        else:
            self.error(self.lineEdit_hostname)
            self.check_host = False

    def validateUsername(self):
        username = self.lineEdit_username.text()
        if len(username) == 0 or len(username) < 4:
            self.neutral(self.lineEdit_username)
        elif username and username[0].isalnum() and 4 <= len(username) <= 16 and username.islower():
            self.success(self.lineEdit_username)
            self.check_user = True
        else:
            self.error(self.lineEdit_username)
            self.check_root = False

    def success(self, line_edit):
        line_edit.setStyleSheet("QLineEdit { background-image: url(:/images/input_field_success.png); border: 1px solid green; border-radius: 5px; font: 11pt \"Comfortaa\"; color: rgb(246, 245, 244); }")
        
    def error(self, line_edit):
        line_edit.setStyleSheet(
            "QLineEdit {background-image: url(:/images/input_field_error.png);"
            "border: 1px solid red;border-radius: 5px;font: 11pt \"Comfortaa\";"
            "color: rgb(246, 245, 244);}"
        )

    def neutral(self, line_edit):
        line_edit.setStyleSheet(
            """
            QLineEdit {
                background-image: url(:/images/input_field.png);
                border: 0.5px solid gray;
                border-radius: 5px;
                font: 11pt "Comfortaa";
                color: rgb(246, 245, 244);
            }
            """
        )
