# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kostamihajlov/MyProjects/hal_automator/automator_project/utils/qtUi/mainwindow.ui'
#
# Created: Tue Dec  3 19:53:59 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 443)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmb_brands = QtGui.QComboBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_brands.sizePolicy().hasHeightForWidth())
        self.cmb_brands.setSizePolicy(sizePolicy)
        self.cmb_brands.setObjectName("cmb_brands")
        self.horizontalLayout_2.addWidget(self.cmb_brands)
        self.cmb_platforms = QtGui.QComboBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_platforms.sizePolicy().hasHeightForWidth())
        self.cmb_platforms.setSizePolicy(sizePolicy)
        self.cmb_platforms.setFrame(False)
        self.cmb_platforms.setObjectName("cmb_platforms")
        self.horizontalLayout_2.addWidget(self.cmb_platforms)
        self.btn_show_config = QtGui.QToolButton(self.centralWidget)
        self.btn_show_config.setObjectName("btn_show_config")
        self.horizontalLayout_2.addWidget(self.btn_show_config)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_reset_scm = QtGui.QPushButton(self.centralWidget)
        self.btn_reset_scm.setObjectName("btn_reset_scm")
        self.horizontalLayout_2.addWidget(self.btn_reset_scm)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_revert = QtGui.QCheckBox(self.centralWidget)
        self.cb_revert.setChecked(False)
        self.cb_revert.setObjectName("cb_revert")
        self.horizontalLayout.addWidget(self.cb_revert)
        self.cb_verbose = QtGui.QCheckBox(self.centralWidget)
        self.cb_verbose.setChecked(True)
        self.cb_verbose.setObjectName("cb_verbose")
        self.horizontalLayout.addWidget(self.cb_verbose)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.txt_output = QtGui.QTextEdit(self.centralWidget)
        self.txt_output.setEnabled(True)
        self.txt_output.setReadOnly(False)
        self.txt_output.setObjectName("txt_output")
        self.verticalLayout.addWidget(self.txt_output)
        self.btn_configure = QtGui.QPushButton(self.centralWidget)
        self.btn_configure.setObjectName("btn_configure")
        self.verticalLayout.addWidget(self.btn_configure)
        self.btn_build = QtGui.QPushButton(self.centralWidget)
        self.btn_build.setObjectName("btn_build")
        self.verticalLayout.addWidget(self.btn_build)
        self.btn_sign = QtGui.QPushButton(self.centralWidget)
        self.btn_sign.setObjectName("btn_sign")
        self.verticalLayout.addWidget(self.btn_sign)
        self.btn_install_on_device = QtGui.QPushButton(self.centralWidget)
        self.btn_install_on_device.setObjectName("btn_install_on_device")
        self.verticalLayout.addWidget(self.btn_install_on_device)
        self.pb_build_progress = QtGui.QProgressBar(self.centralWidget)
        self.pb_build_progress.setEnabled(True)
        self.pb_build_progress.setStyleSheet("display:none;")
        self.pb_build_progress.setProperty("value", 24)
        self.pb_build_progress.setObjectName("pb_build_progress")
        self.verticalLayout.addWidget(self.pb_build_progress)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 767, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTest = QtGui.QMenu(self.menuBar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRegex_Tool = QtGui.QAction(MainWindow)
        self.actionRegex_Tool.setObjectName("actionRegex_Tool")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionCloneTo = QtGui.QAction(MainWindow)
        self.actionCloneTo.setObjectName("actionCloneTo")
        self.actionConfig_Editor = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/images/HAL-9000-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfig_Editor.setIcon(icon)
        self.actionConfig_Editor.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionConfig_Editor.setObjectName("actionConfig_Editor")
        self.actionDeclarative_View = QtGui.QAction(MainWindow)
        self.actionDeclarative_View.setObjectName("actionDeclarative_View")
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionCloneTo)
        self.menuTools.addAction(self.actionRegex_Tool)
        self.menuTools.addAction(self.actionConfig_Editor)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTest.addAction(self.actionDeclarative_View)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_show_config.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset_scm.setText(QtGui.QApplication.translate("MainWindow", "SCM to HEAD", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_revert.setText(QtGui.QApplication.translate("MainWindow", "Revert", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_verbose.setText(QtGui.QApplication.translate("MainWindow", "Verbose", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_configure.setText(QtGui.QApplication.translate("MainWindow", "Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_build.setText(QtGui.QApplication.translate("MainWindow", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_sign.setText(QtGui.QApplication.translate("MainWindow", "Sign", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_install_on_device.setText(QtGui.QApplication.translate("MainWindow", "Install On Device", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTest.setTitle(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegex_Tool.setText(QtGui.QApplication.translate("MainWindow", "Regex Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegex_Tool.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "SaveAs...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCloneTo.setText(QtGui.QApplication.translate("MainWindow", "CloneTo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCloneTo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfig_Editor.setText(QtGui.QApplication.translate("MainWindow", "Config Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfig_Editor.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeclarative_View.setText(QtGui.QApplication.translate("MainWindow", "Declarative View", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
