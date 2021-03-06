import os
import copy
from PySide import QtGui, QtCore
from PySide.QtCore import QThread
from config_widget import ConfigForm
from hal_configurator.lib import app_config
from hal_configurator.lib.app_config import config
from hal_configurator.lib.app_configurator import AppConfigurator,\
    ConfigBuildFilter
from hal_configurator.lib.config_loaders import FileConfigLoader
from hal_configurator.lib.logers import ZmqChainedLoger
from hal_configurator.lib.plugin_loader import get_plugins
from hal_configurator.ui.bundle_selector import BundleSelector
from hal_configurator.ui.config_runner_thread import ConfigRunnerThread
from hal_configurator.ui.console_output import ConsoleOutput
from hal_configurator.ui.gen.configwindow import Ui_ConfigWindow
from hal_configurator.ui.message_subscriber import MessageSubsriberThread
from hal_configurator.lib.config_validator import ConfigurationValidator
from hal_configurator.ui.regex_tool import RegexTool
from hal_configurator.lib.workspace_manager import Workspace
from hal_configurator.ui.preferences_widget import PreferencesWidget

class ConfigWindow(QtGui.QMainWindow, Ui_ConfigWindow):
    def __init__(self, main_window, *args, **kwargs):
        super(ConfigWindow, self).__init__(*args, **kwargs)
        self.viewMode = 'admin'
        self.debug = False
        self.verbose = app_config.is_verbose()
        self.config_path = None
        self.working_dir = None
        self.main_window = main_window or self
        self.working_dir_choser = None
        self.messages_thread = None
        self.cw = None
        self.bundlesModel = QtGui.QStandardItemModel()
        self.set_plugins()
        self.setupUi()
        self.set_message_receiver()
        self.start_last_if_any()
    
    def set_plugins(self):
        self.plugins =[]
        for d in config.plugin_dirs:
            self.plugins.extend(get_plugins(d))

    def setupUi(self):
        super(ConfigWindow, self).setupUi(self)
        title="Configurator Version:%s"%(app_config.get_version())
        self.setWindowTitle(title)
        self.cbChooseWorkingDir.clicked.connect(self.chose_working_dir)
        self.set_menu_bar()
        self.set_recent_config_actions()
        self.tool = None
        self.workspace = app_config.get_current_workspace()
        if not self.workspace:
            self.switch_workspace()
        else:
            self.workspace.set_loger(ZmqChainedLoger(1234))
        self.viewMode = self.workspace.mode
        self.actionViewAsAdmin.setChecked(self.viewMode=='admin')
        self.actionViewAsModerator.setChecked(self.viewMode=='moderator')

    def bindUi(self):
        if self.viewMode != 'admin':
            self.tool = self.detailsContainer
        else:
            self.tool = None
        title = os.path.basename((os.path.dirname(os.path.dirname(self.config_path))))
        title +="         -- Configurator Version:%s" % (app_config.get_version())
        self.setWindowTitle(title)
        self.txtWorkingDir.setText(self.working_dir)

        if self.cw:
            self.ltv_content.removeWidget(self.cw)
            self.cw.close()
        self.cw = ConfigForm(self.loader, parent=self, details_parent = self.tool)
        #self.tool.setModel(ToolsListModel(self.plugins, False))
        self.menubar.setWindowTitle(title)
        self.build_output = None
        self.set_bundles_model()

        self.ltv_content.addWidget(self.cw)
        # if self.viewMode!='admin':
        #     self.cw.tlbx_bundles.hide()
        #     self.widget.hide()
        #     width = self.splitter_2.sizeHint().width()
        #     self.splitter_2.setSizes([width*0.3, width*0.7])
        # else:
        #     width = self.splitter_2.sizeHint().width()
        #     self.splitter_2.setSizes([width, 0])
            
    def start_last_if_any(self):
        try:
            config_history = app_config.get_config_history()
            if config_history:
                self.set_configuration(config_history[-1])
        except Exception as ex:
                print(ex)

    def set_configuration(self, config_path, working_dir=None):
        self.config_path = config_path
        if working_dir:
            self.working_dir = working_dir
        else:
            self.working_dir = app_config.get_working_dir()
        self.loader = FileConfigLoader(self.config_path)
        self.configuration = self.loader.load_config()
        self.bindUi()

    def set_bundles_model(self):
        self.bundlesModel.clear()
        work_mode = Workspace.current.mode
        bundle_filter = ConfigBuildFilter(included=Workspace.registered_bundles)
        d = self.get_mode_config_for_key(work_mode, 'bundles')
        bundle_filter.extend_from_dict(d)
        for bundle in self.configuration['Content']['OperationBundles']:
            dataItem = QtGui.QStandardItem(bundle['Name'])
            dataItem.setCheckable(True)
            check_state = bundle_filter.allowed(bundle['Name']) and QtCore.Qt.CheckState.Checked or QtCore.Qt.CheckState.Unchecked
            dataItem.setCheckState(check_state)
            self.bundlesModel.appendRow(dataItem)
    
    def get_mode_config_for_key(self, work_mode, key):
        if self.configuration.has_key('Builds'):
            if self.configuration['Builds'].has_key(work_mode):
                bc = self.configuration['Builds'][work_mode]
                if bc.has_key(key):
                    return copy.deepcopy(bc[key])
        return {}

    def get_included_bundles(self):
        i = 0
        includedBundles = []
        while self.bundlesModel.item(i):
            dataItem = self.bundlesModel.item(i)
            if dataItem.checkState():
                includedBundles.append(dataItem.text())
            i += 1
        return includedBundles
            
    def chose_working_dir(self):
        """
        Choses the current working directory for the current configuration
        """
        res = QtGui.QFileDialog.getExistingDirectory(caption="Choose working directory")
        if res:
            app_config.set_working_dir(res)
            self.working_dir = res
            self.txtWorkingDir.setText(res)


    def show_bundle_selector(self):
        self.bundleSelectorWidget = BundleSelector(self.bundlesModel)
        self.bundleSelectorWidget.show()


    def validate_configuration(self):
        validator = ConfigurationValidator(self.config_path)
        result = validator.validate(self.configuration)
        title = result.is_valid and 'Valid Configuration' or 'Invalid Configurration'
        message = 'Errors:\n'+'\n'.join(['\t'+x for x in result.errors])
        message+= '\nWarnings:\n'+'\n'.join(['\t'+x for x in result.warnings])
        message+= '\nSuggestions:\n'+'\n'.join(['\t'+x for x in result.suggestions])
        msgBox = QtGui.QMessageBox()
        msgBox.setText(title)
        msgBox.setInformativeText(message)
        msgBox.exec_()

    def open_regex_tool(self):
        self.rtool = RegexTool()
        self.rtool.show()


    def sync_workspace(self):
        self.build_output = ConsoleOutput()
        self.build_output.show()
        class thc(QtCore.QThread):
            def __init__(self, workspace):
                self.workspace = workspace
                super(thc, self).__init__()
            def run(self):
                print "running..."
                self.workspace.sync()
        self.th = thc(self.workspace)
        self.th.start()

    def switch_workspace(self, custom_title = None):
        self.workspacedialog = QtGui.QFileDialog(None, custom_title or 'Choose your Workspace!')
        self.workspacedialog.setFileMode(QtGui.QFileDialog.Directory)
        self.workspacedialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
        res = self.workspacedialog.exec_()
        if res:
            dirpath = self.workspacedialog.selectedFiles()[0]
            app_config.set_current_workspace(dirpath)
        while not app_config.get_current_workspace():
            self.switch_workspace('You must choose a valid workspace in order to open the app')
        self.workspace = app_config.get_current_workspace()
        self.workspace.set_loger(ZmqChainedLoger(1234))
        self.workspacedialog.close()

    def reset_workspace(self):
        self.build_output = ConsoleOutput()
        self.build_output.show()
        class thc(QtCore.QThread):
            def __init__(self, workspace):
                self.workspace = workspace
                super(thc, self).__init__()
            def run(self):
                print "running..."
                self.workspace.reset()
        self.th = thc(self.workspace)
        self.th.start()

    def setViewMode(self, modeUsed=None):
        newViewMode = None
        if modeUsed=='moderator':
            self.actionViewAsAdmin.setChecked(not self.actionViewAsModerator.isChecked())
            newViewMode = self.actionViewAsModerator.isChecked() and 'moderator' or 'admin'
        else:
            self.actionViewAsModerator.setChecked(not self.actionViewAsAdmin.isChecked())
            newViewMode = self.actionViewAsAdmin.isChecked() and 'admin' or 'moderator'

        if newViewMode !=self.viewMode and self.config_path:
            self.viewMode = newViewMode
            self.workspace.mode = newViewMode
            self.set_configuration(self.config_path, self.working_dir)

    def set_menu_bar(self):
        def save(is_new, is_cloning_empty):
            def fn ():
                if self.cw:
                    self.cw.save_config(is_new, is_cloning_empty)
            return fn
        def viewModeSetter(mode):
            def fn ():
                return self.setViewMode(mode)
            return fn
        self.actionRun.triggered.connect(self.on_run_click)
        self.actionClose.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.open_config)
        self.actionNew.triggered.connect(self.create_new_config)
        self.actionEnable_Disable_Bundles.triggered.connect(self.show_bundle_selector)
        self.actionVallidate.triggered.connect(self.validate_configuration)
        self.actionRegex.triggered.connect(self.open_regex_tool)
        self.actionSync.triggered.connect(self.sync_workspace)
        self.actionSwitch_Workspace.triggered.connect(self.switch_workspace)
        self.actionReset.triggered.connect(self.reset_workspace)
        self.actionSave.triggered.connect(save(False, False))
        self.actionSave_As.triggered.connect(save(True, False))
        self.actionClone.triggered.connect(save(True, True))
        self.actionViewAsAdmin.triggered.connect(viewModeSetter('admin'))
        self.actionViewAsModerator.triggered.connect(viewModeSetter('moderator'))
        self.actionVerbose.triggered.connect(self.setVerbosity)
        self.actionVerbose.setChecked(app_config.is_verbose())
        self.actionDebug_2.triggered.connect(self.debugChanged)

    def debugChanged(self):
        self.debug = self.actionDebug.isChecked()

    def setVerbosity(self):
        app_config.set_verbose(self.actionVerbose.isChecked())
        self.verbose = self.actionVerbose.isChecked()

    def create_new_config(self):
        params = {"caption":"Choose Configuration","filter":"bc.halc"}
        if len(app_config.get_config_history())>0:
            last_config = app_config.get_config_history()[-1]
            last_config = last_config.replace("'", '')
            params["dir"] = os.path.dirname(last_config)
            
        f = QtGui.QFileDialog.getSaveFileName(**params)
        if f[0]:
            self.config_path = f[0]
            FileConfigLoader.new(self.config_path)
            app_config.add_config_to_history(self.config_path)
            self.set_configuration(self.config_path, self.working_dir)

    def set_recent_config_actions(self):
        history = app_config.get_config_history()
        history.reverse()
        self.historyActions = []
        for k in history:
            a = QtGui.QAction(self)
            a.triggered.connect(self.open_recent)
            a.setText(k)
            self.historyActions.append(a)
            self.menuRecent.addAction(a)

    def open_recent(self, *args, **kwargs):
        app_config.add_config_to_history(self.sender().text())
        self.set_configuration(self.sender().text(), self.working_dir)

    def open_config(self):
        cur_dir = None
        if app_config.get_config_history():
            cur_dir = app_config.get_config_history()[-1]

        params = {"caption":"Choose Configuration","filter":"Config Files(bc.json *.halc)"}
        if cur_dir:
            params["dir"] = app_config.get_config_history()[-1]
        f = QtGui.QFileDialog.getOpenFileName(**params)

        if f[0]:
            self.config_path = f[0]
            app_config.add_config_to_history(self.config_path)
            self.set_configuration(self.config_path, self.working_dir)

    def on_run_click(self):
        root_url = os.path.dirname(self.config_path)
        if os.name!='posix':
            root_url = '/'+root_url
        if self.build_output:
            self.build_output.close()
        self.build_output = ConsoleOutput()
        self.build_output.show()
        config_loader = FileConfigLoader(self.config_path)
        builder = AppConfigurator(config_loader, ZmqChainedLoger(1234), verbose=self.verbose)
        builder.set_execution_dir(self.working_dir)
        builder.include_bundles(self.get_included_bundles())
        self.set_message_receiver()
        if self.debug:
            builder.apply()
        else:
            self.worker = ConfigRunnerThread(builder)
            self.worker.start()
            self.worker.finished.connect(self.on_worker_finished)

    def on_worker_finished(self):
        self.worker.builder = None
        del self.worker

    def set_message_receiver(self):
        if not self.messages_thread:
            self.messages_thread = MessageSubsriberThread(1234)
            self.messages_thread.on_message_received.connect(self.on_message_received)
            self.messages_thread.start(QThread.TimeCriticalPriority)

    def on_message_received(self, message):
        if self.build_output:
            self.build_output.txt_output.append("%s" % message)

      
    @QtCore.Slot()
    def showOptionsMenu(self):
        self.prefs = PreferencesWidget()
        self.prefs.show()