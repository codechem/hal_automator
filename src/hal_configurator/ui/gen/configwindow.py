# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/configwindow.ui'
#
# Created: Mon Nov  2 04:57:25 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigWindow(object):
    def setupUi(self, ConfigWindow):
        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(1026, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/images/HAL-9000-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfigWindow.setWindowIcon(icon)
        ConfigWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        ConfigWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(ConfigWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ltv_content = QtGui.QVBoxLayout()
        self.ltv_content.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.ltv_content.setObjectName("ltv_content")
        self.verticalLayout_2.addLayout(self.ltv_content)
        ConfigWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecent = QtGui.QMenu(self.menuFile)
        self.menuRecent.setObjectName("menuRecent")
        self.menuWorkspace = QtGui.QMenu(self.menuFile)
        self.menuWorkspace.setObjectName("menuWorkspace")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuRun = QtGui.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        ConfigWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(ConfigWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 227, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 241, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 113, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 151, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 227, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 241, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 227, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 241, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 113, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 151, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 227, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 241, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 113, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 227, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 241, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 113, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 151, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 113, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 113, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 227, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 227, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 227, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.toolBar.setPalette(palette)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setObjectName("toolBar")
        ConfigWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dock_tools = QtGui.QDockWidget(ConfigWindow)
        self.dock_tools.setFloating(False)
        self.dock_tools.setObjectName("dock_tools")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.lv_tools = QtGui.QVBoxLayout()
        self.lv_tools.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.lv_tools.setObjectName("lv_tools")
        self.listWidget = PluginsList(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setSpacing(5)
        self.listWidget.setViewMode(QtGui.QListView.IconMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setWordWrap(False)
        self.listWidget.setObjectName("listWidget")
        self.lv_tools.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.lv_tools, 1, 0, 1, 1)
        self.txt_plugin_filter = QtGui.QLineEdit(self.dockWidgetContents)
        self.txt_plugin_filter.setObjectName("txt_plugin_filter")
        self.gridLayout.addWidget(self.txt_plugin_filter, 0, 0, 1, 1)
        self.dock_tools.setWidget(self.dockWidgetContents)
        ConfigWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_tools)
        self.dock_working_dir = QtGui.QDockWidget(ConfigWindow)
        self.dock_working_dir.setObjectName("dock_working_dir")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtWorkingDir = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.txtWorkingDir.setEnabled(False)
        self.txtWorkingDir.setObjectName("txtWorkingDir")
        self.horizontalLayout.addWidget(self.txtWorkingDir)
        self.cbChooseWorkingDir = QtGui.QToolButton(self.dockWidgetContents_2)
        self.cbChooseWorkingDir.setObjectName("cbChooseWorkingDir")
        self.horizontalLayout.addWidget(self.cbChooseWorkingDir)
        self.cbStepThruBundles = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.cbStepThruBundles.setEnabled(False)
        self.cbStepThruBundles.setMaximumSize(QtCore.QSize(0, 16777215))
        self.cbStepThruBundles.setStyleSheet("")
        self.cbStepThruBundles.setObjectName("cbStepThruBundles")
        self.horizontalLayout.addWidget(self.cbStepThruBundles)
        self.cbStepThruOps = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.cbStepThruOps.setEnabled(False)
        self.cbStepThruOps.setMaximumSize(QtCore.QSize(0, 16777215))
        self.cbStepThruOps.setStyleSheet("")
        self.cbStepThruOps.setObjectName("cbStepThruOps")
        self.horizontalLayout.addWidget(self.cbStepThruOps)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.dock_working_dir.setWidget(self.dockWidgetContents_2)
        ConfigWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dock_working_dir)
        self.dock_console = QtGui.QDockWidget(ConfigWindow)
        self.dock_console.setObjectName("dock_console")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = ConsoleOutput(self.dockWidgetContents_3)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.dock_console.setWidget(self.dockWidgetContents_3)
        ConfigWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dock_console)
        self.dock_resources = QtGui.QDockWidget(ConfigWindow)
        self.dock_resources.setObjectName("dock_resources")
        self.resources_widget = ResourcesWidget()
        self.resources_widget.setObjectName("resources_widget")
        self.dock_resources.setWidget(self.resources_widget)
        ConfigWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_resources)
        self.actionSave = QtGui.QAction(ConfigWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttons/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionRun = QtGui.QAction(ConfigWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buttons/images/debug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon2)
        self.actionRun.setObjectName("actionRun")
        self.actionCopy_2 = QtGui.QAction(ConfigWindow)
        self.actionCopy_2.setObjectName("actionCopy_2")
        self.actionPaste = QtGui.QAction(ConfigWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtGui.QAction(ConfigWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_As = QtGui.QAction(ConfigWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtGui.QAction(ConfigWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClone = QtGui.QAction(ConfigWindow)
        self.actionClone.setObjectName("actionClone")
        self.actionOpen = QtGui.QAction(ConfigWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtGui.QAction(ConfigWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionEnable_Disable_Bundles = QtGui.QAction(ConfigWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/buttons/images/select_bundles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnable_Disable_Bundles.setIcon(icon3)
        self.actionEnable_Disable_Bundles.setObjectName("actionEnable_Disable_Bundles")
        self.actionRun_2 = QtGui.QAction(ConfigWindow)
        self.actionRun_2.setObjectName("actionRun_2")
        self.actionDebug = QtGui.QAction(ConfigWindow)
        self.actionDebug.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/buttons/images/debug-bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDebug.setIcon(icon4)
        self.actionDebug.setObjectName("actionDebug")
        self.actionPackage = QtGui.QAction(ConfigWindow)
        self.actionPackage.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/buttons/images/package.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPackage.setIcon(icon5)
        self.actionPackage.setObjectName("actionPackage")
        self.actionSwitch_Workspace = QtGui.QAction(ConfigWindow)
        self.actionSwitch_Workspace.setObjectName("actionSwitch_Workspace")
        self.actionSync = QtGui.QAction(ConfigWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/buttons/images/sync.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSync.setIcon(icon6)
        self.actionSync.setObjectName("actionSync")
        self.actionReset = QtGui.QAction(ConfigWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/buttons/images/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset.setIcon(icon7)
        self.actionReset.setObjectName("actionReset")
        self.actionVallidate = QtGui.QAction(ConfigWindow)
        self.actionVallidate.setIcon(icon3)
        self.actionVallidate.setObjectName("actionVallidate")
        self.actionRegex = QtGui.QAction(ConfigWindow)
        self.actionRegex.setObjectName("actionRegex")
        self.actionViewAsModerator = QtGui.QAction(ConfigWindow)
        self.actionViewAsModerator.setCheckable(True)
        self.actionViewAsModerator.setEnabled(True)
        self.actionViewAsModerator.setObjectName("actionViewAsModerator")
        self.actionRemote_Build = QtGui.QAction(ConfigWindow)
        self.actionRemote_Build.setIcon(icon2)
        self.actionRemote_Build.setObjectName("actionRemote_Build")
        self.actionViewAsAdmin = QtGui.QAction(ConfigWindow)
        self.actionViewAsAdmin.setCheckable(True)
        self.actionViewAsAdmin.setObjectName("actionViewAsAdmin")
        self.actionAbout_Halicea = QtGui.QAction(ConfigWindow)
        self.actionAbout_Halicea.setObjectName("actionAbout_Halicea")
        self.actionVerbose = QtGui.QAction(ConfigWindow)
        self.actionVerbose.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/buttons/images/verbose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVerbose.setIcon(icon8)
        self.actionVerbose.setObjectName("actionVerbose")
        self.actionDebug_2 = QtGui.QAction(ConfigWindow)
        self.actionDebug_2.setCheckable(True)
        self.actionDebug_2.setIcon(icon4)
        self.actionDebug_2.setObjectName("actionDebug_2")
        self.actionOptions = QtGui.QAction(ConfigWindow)
        self.actionOptions.setIcon(icon3)
        self.actionOptions.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionOptions.setObjectName("actionOptions")
        self.actionToggle_Toolbar = QtGui.QAction(ConfigWindow)
        self.actionToggle_Toolbar.setCheckable(True)
        self.actionToggle_Toolbar.setObjectName("actionToggle_Toolbar")
        self.menuWorkspace.addAction(self.actionSync)
        self.menuWorkspace.addAction(self.actionReset)
        self.menuWorkspace.addSeparator()
        self.menuWorkspace.addAction(self.actionSwitch_Workspace)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionClone)
        self.menuFile.addAction(self.menuWorkspace.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionCopy_2)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout)
        self.menuRun.addAction(self.actionEnable_Disable_Bundles)
        self.menuRun.addAction(self.actionVallidate)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionRun)
        self.menuRun.addAction(self.actionRemote_Build)
        self.menuRun.addAction(self.actionDebug)
        self.menuRun.addAction(self.actionPackage)
        self.menuTools.addAction(self.actionRegex)
        self.menuTools.addAction(self.actionOptions)
        self.menuView.addAction(self.actionViewAsModerator)
        self.menuView.addAction(self.actionViewAsAdmin)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionVerbose)
        self.menuView.addAction(self.actionDebug_2)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionToggle_Toolbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionVallidate)
        self.toolBar.addAction(self.actionVerbose)

        self.retranslateUi(ConfigWindow)
        QtCore.QObject.connect(self.txt_plugin_filter, QtCore.SIGNAL("textEdited(QString)"), self.listWidget.filter)
        QtCore.QObject.connect(self.actionOptions, QtCore.SIGNAL("triggered()"), ConfigWindow.showOptionsMenu)
        QtCore.QObject.connect(self.actionToggle_Toolbar, QtCore.SIGNAL("toggled(bool)"), self.toolBar.setVisible)
        QtCore.QMetaObject.connectSlotsByName(ConfigWindow)

    def retranslateUi(self, ConfigWindow):
        ConfigWindow.setWindowTitle(QtGui.QApplication.translate("ConfigWindow", "Configuration Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setAccessibleName(QtGui.QApplication.translate("ConfigWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setAccessibleDescription(QtGui.QApplication.translate("ConfigWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("ConfigWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRecent.setTitle(QtGui.QApplication.translate("ConfigWindow", "Recent Configs", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWorkspace.setTitle(QtGui.QApplication.translate("ConfigWindow", "Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("ConfigWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("ConfigWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRun.setTitle(QtGui.QApplication.translate("ConfigWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("ConfigWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("ConfigWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("ConfigWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dock_tools.setWindowTitle(QtGui.QApplication.translate("ConfigWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.txt_plugin_filter.setPlaceholderText(QtGui.QApplication.translate("ConfigWindow", "Search ...", None, QtGui.QApplication.UnicodeUTF8))
        self.dock_working_dir.setWindowTitle(QtGui.QApplication.translate("ConfigWindow", "Working Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.txtWorkingDir.setPlaceholderText(QtGui.QApplication.translate("ConfigWindow", "Please select excution directory", None, QtGui.QApplication.UnicodeUTF8))
        self.cbChooseWorkingDir.setText(QtGui.QApplication.translate("ConfigWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cbStepThruBundles.setText(QtGui.QApplication.translate("ConfigWindow", "Step Thru Bundles", None, QtGui.QApplication.UnicodeUTF8))
        self.cbStepThruOps.setText(QtGui.QApplication.translate("ConfigWindow", "Step Thru Ops", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("ConfigWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("ConfigWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy_2.setText(QtGui.QApplication.translate("ConfigWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy_2.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("ConfigWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("ConfigWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("ConfigWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("ConfigWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClone.setText(QtGui.QApplication.translate("ConfigWindow", "Clone", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClone.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("ConfigWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("ConfigWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnable_Disable_Bundles.setText(QtGui.QApplication.translate("ConfigWindow", "Enable/Disable Bundles", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnable_Disable_Bundles.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+Shift+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_2.setText(QtGui.QApplication.translate("ConfigWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDebug.setText(QtGui.QApplication.translate("ConfigWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDebug.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPackage.setText(QtGui.QApplication.translate("ConfigWindow", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPackage.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+Shift+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSwitch_Workspace.setText(QtGui.QApplication.translate("ConfigWindow", "Switch Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSync.setText(QtGui.QApplication.translate("ConfigWindow", "Sync", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSync.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset.setText(QtGui.QApplication.translate("ConfigWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+0", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVallidate.setText(QtGui.QApplication.translate("ConfigWindow", "Vallidate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVallidate.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+Shift+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegex.setText(QtGui.QApplication.translate("ConfigWindow", "Regex", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewAsModerator.setText(QtGui.QApplication.translate("ConfigWindow", "Moderator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemote_Build.setText(QtGui.QApplication.translate("ConfigWindow", "Remote Build", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewAsAdmin.setText(QtGui.QApplication.translate("ConfigWindow", "Admin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Halicea.setText(QtGui.QApplication.translate("ConfigWindow", "About Halicea", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVerbose.setText(QtGui.QApplication.translate("ConfigWindow", "Verbose Output", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDebug_2.setText(QtGui.QApplication.translate("ConfigWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptions.setText(QtGui.QApplication.translate("ConfigWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggle_Toolbar.setText(QtGui.QApplication.translate("ConfigWindow", "Toggle Toolbar", None, QtGui.QApplication.UnicodeUTF8))

from hal_configurator.ui.custom_widgets.plugins_list import PluginsList
from hal_configurator.ui.custom_widgets.resources_widget import ResourcesWidget
from hal_configurator.ui.console_output import ConsoleOutput
import images_rc
