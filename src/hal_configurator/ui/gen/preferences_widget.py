# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/halicea/projects/hal_automator/utils/qtUi/PreferenceForms/Config/preferences_widget.ui'
#
# Created: Mon Nov  2 03:56:58 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PreferencesWidget(object):
    def setupUi(self, PreferencesWidget):
        PreferencesWidget.setObjectName("PreferencesWidget")
        PreferencesWidget.resize(635, 381)
        self.horizontalLayout = QtGui.QHBoxLayout(PreferencesWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tree_sections = QtGui.QTreeWidget(PreferencesWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_sections.sizePolicy().hasHeightForWidth())
        self.tree_sections.setSizePolicy(sizePolicy)
        self.tree_sections.setMinimumSize(QtCore.QSize(200, 0))
        self.tree_sections.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tree_sections.setRootIsDecorated(True)
        self.tree_sections.setUniformRowHeights(False)
        self.tree_sections.setItemsExpandable(True)
        self.tree_sections.setObjectName("tree_sections")
        item_0 = QtGui.QTreeWidgetItem(self.tree_sections)
        item_0.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.tree_sections)
        item_0.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.tree_sections.header().setVisible(False)
        self.tree_sections.header().setDefaultSectionSize(150)
        self.horizontalLayout.addWidget(self.tree_sections)
        self.widgets = QtGui.QStackedWidget(PreferencesWidget)
        self.widgets.setEnabled(True)
        self.widgets.setAutoFillBackground(False)
        self.widgets.setObjectName("widgets")
        self.gen_plugins = QtGui.QWidget()
        self.gen_plugins.setObjectName("gen_plugins")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.gen_plugins)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtGui.QScrollArea(self.gen_plugins)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.ws_content = QtGui.QWidget()
        self.ws_content.setGeometry(QtCore.QRect(0, 0, 375, 291))
        self.ws_content.setObjectName("ws_content")
        self.verticalLayout = QtGui.QVBoxLayout(self.ws_content)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gen_p1 = DirectoryChooserWidget(self.ws_content)
        self.gen_p1.setAutoFillBackground(True)
        self.gen_p1.setObjectName("gen_p1")
        self.verticalLayout.addWidget(self.gen_p1)
        self.gen_p2 = DirectoryChooserWidget(self.ws_content)
        self.gen_p2.setAutoFillBackground(True)
        self.gen_p2.setObjectName("gen_p2")
        self.verticalLayout.addWidget(self.gen_p2)
        self.gen_p3 = DirectoryChooserWidget(self.ws_content)
        self.gen_p3.setAutoFillBackground(True)
        self.gen_p3.setObjectName("gen_p3")
        self.verticalLayout.addWidget(self.gen_p3)
        self.gen_p4 = DirectoryChooserWidget(self.ws_content)
        self.gen_p4.setAutoFillBackground(True)
        self.gen_p4.setObjectName("gen_p4")
        self.verticalLayout.addWidget(self.gen_p4)
        self.gen_p5 = DirectoryChooserWidget(self.ws_content)
        self.gen_p5.setAutoFillBackground(True)
        self.gen_p5.setObjectName("gen_p5")
        self.verticalLayout.addWidget(self.gen_p5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.ws_content)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.genAction = QtGui.QDialogButtonBox(self.gen_plugins)
        self.genAction.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.genAction.setObjectName("genAction")
        self.verticalLayout_5.addWidget(self.genAction)
        self.widgets.addWidget(self.gen_plugins)
        self.ws_info = QtGui.QWidget()
        self.ws_info.setObjectName("ws_info")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.ws_info)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtGui.QLabel(self.ws_info)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.ws_path = QtGui.QLineEdit(self.ws_info)
        self.ws_path.setEnabled(False)
        self.ws_path.setObjectName("ws_path")
        self.horizontalLayout_6.addWidget(self.ws_path)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(self.ws_info)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.ws_name = QtGui.QLineEdit(self.ws_info)
        self.ws_name.setObjectName("ws_name")
        self.horizontalLayout_5.addWidget(self.ws_name)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(20, 224, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.wsInfoAction = QtGui.QDialogButtonBox(self.ws_info)
        self.wsInfoAction.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.wsInfoAction.setObjectName("wsInfoAction")
        self.verticalLayout_8.addWidget(self.wsInfoAction)
        self.widgets.addWidget(self.ws_info)
        self.ws_plugins = QtGui.QWidget()
        self.ws_plugins.setObjectName("ws_plugins")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.ws_plugins)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_2 = QtGui.QScrollArea(self.ws_plugins)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.gen_contents = QtGui.QWidget()
        self.gen_contents.setGeometry(QtCore.QRect(0, 0, 375, 291))
        self.gen_contents.setObjectName("gen_contents")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.gen_contents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ws_p1 = DirectoryChooserWidget(self.gen_contents)
        self.ws_p1.setAutoFillBackground(True)
        self.ws_p1.setObjectName("ws_p1")
        self.verticalLayout_6.addWidget(self.ws_p1)
        self.ws_p2 = DirectoryChooserWidget(self.gen_contents)
        self.ws_p2.setAutoFillBackground(True)
        self.ws_p2.setObjectName("ws_p2")
        self.verticalLayout_6.addWidget(self.ws_p2)
        self.ws_p3 = DirectoryChooserWidget(self.gen_contents)
        self.ws_p3.setAutoFillBackground(True)
        self.ws_p3.setObjectName("ws_p3")
        self.verticalLayout_6.addWidget(self.ws_p3)
        self.ws_p5 = DirectoryChooserWidget(self.gen_contents)
        self.ws_p5.setAutoFillBackground(True)
        self.ws_p5.setObjectName("ws_p5")
        self.verticalLayout_6.addWidget(self.ws_p5)
        self.ws_p4 = DirectoryChooserWidget(self.gen_contents)
        self.ws_p4.setAutoFillBackground(True)
        self.ws_p4.setObjectName("ws_p4")
        self.verticalLayout_6.addWidget(self.ws_p4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.scrollArea_2.setWidget(self.gen_contents)
        self.verticalLayout_7.addWidget(self.scrollArea_2)
        self.wsPluginsAction = QtGui.QDialogButtonBox(self.ws_plugins)
        self.wsPluginsAction.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.wsPluginsAction.setObjectName("wsPluginsAction")
        self.verticalLayout_7.addWidget(self.wsPluginsAction)
        self.widgets.addWidget(self.ws_plugins)
        self.horizontalLayout.addWidget(self.widgets)

        self.retranslateUi(PreferencesWidget)
        self.widgets.setCurrentIndex(1)
        QtCore.QObject.connect(self.genAction, QtCore.SIGNAL("accepted()"), PreferencesWidget.saveConfigPlugins)
        QtCore.QObject.connect(self.wsPluginsAction, QtCore.SIGNAL("accepted()"), PreferencesWidget.saveWSPlugins)
        QtCore.QObject.connect(self.wsInfoAction, QtCore.SIGNAL("accepted()"), PreferencesWidget.saveWSInfo)
        QtCore.QObject.connect(self.wsInfoAction, QtCore.SIGNAL("rejected()"), PreferencesWidget.loadWSInfo)
        QtCore.QObject.connect(self.wsPluginsAction, QtCore.SIGNAL("rejected()"), PreferencesWidget.loadWSPlugins)
        QtCore.QObject.connect(self.genAction, QtCore.SIGNAL("rejected()"), PreferencesWidget.loadConfigPlugins)
        QtCore.QObject.connect(self.tree_sections, QtCore.SIGNAL("itemClicked(QTreeWidgetItem*,int)"), PreferencesWidget.selectionChanged)
        QtCore.QMetaObject.connectSlotsByName(PreferencesWidget)

    def retranslateUi(self, PreferencesWidget):
        PreferencesWidget.setWindowTitle(QtGui.QApplication.translate("PreferencesWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_sections.headerItem().setText(0, QtGui.QApplication.translate("PreferencesWidget", "Root", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tree_sections.isSortingEnabled()
        self.tree_sections.setSortingEnabled(False)
        self.tree_sections.topLevelItem(0).setText(0, QtGui.QApplication.translate("PreferencesWidget", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_sections.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("PreferencesWidget", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_sections.topLevelItem(1).setText(0, QtGui.QApplication.translate("PreferencesWidget", "Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_sections.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("PreferencesWidget", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_sections.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("PreferencesWidget", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_sections.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(QtGui.QApplication.translate("PreferencesWidget", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferencesWidget", "Name:", None, QtGui.QApplication.UnicodeUTF8))

from hal_configurator.ui.directory_chooser_widget import DirectoryChooserWidget
