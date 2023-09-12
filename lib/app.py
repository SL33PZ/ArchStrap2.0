import os
import shutil
import subprocess
import sys
import path

from functions.helpers import (add_combobox_scrollbar, add_list,
                               get_available_partitions, quit_app,
                               validate_combobox, validate_partition,
                               validate_password, validate_string, get_dictionary_value
                               )
from functions.lists import (DESKTOP_ENVIRONMENT, DISPLAY_MANAGER, KERNEL,
                             LANGUAGE, OPTIONALS, TIMEZONE)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from window import MainWindow
import fileinput
tempDir = QTemporaryDir()


checked = []

class UnmountThread(QThread):
    command_output = pyqtSignal(str)
    
    def __init__(self, device):
        super().__init__()
        self.device = device
        
        
    def run(self):
        try:
            process = subprocess.Popen(['sudo', 'umount', '-l',self.device], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in process.stdout:
                self.command_output.emit(line.rstrip().decode('utf-8'))
        finally:
            process.stdout.close()
            process.wait()

class ExecutionThread(QThread):
    command_output = pyqtSignal(str)

    def __init__(self, script_path):
        super().__init__()
        self.script_path = script_path

    def run(self):
        try:
            process = subprocess.Popen(['sudo', 'bash', '-x', self.script_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in process.stdout:
                self.command_output.emit(line.rstrip().decode('utf-8'))
        finally:
            process.stdout.close()
            process.wait()


class MainWindow(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.tempdir = tempDir
        self.list_view = self.logView
        self.model = QStandardItemModel()
        self.list_view.setModel(self.model)
        self.dst=self.tempdir.path()
        self.thread = ExecutionThread(f"{self.dst}/script.sh")
        self.thread.command_output.connect(lambda line: self.model.appendRow(QStandardItem(line)))

        self.insert_path_in_script("lib/functions/umount.py", self.dst, 4)        
            
        self.pushButton_finish.setEnabled(True)
        self.pushButton_next.setEnabled(True)
        
        for box, list in zip([self.comboBox_language, self.comboBox_timezone, 
                              self.comboBox_desktopEnvironment, self.comboBox_displayManager, 
                              self.comboBox_kernel], 
                             [ LANGUAGE, TIMEZONE, DESKTOP_ENVIRONMENT, DISPLAY_MANAGER, KERNEL ]):
            
            add_list(box, list)
            add_combobox_scrollbar(box)
            box.setCurrentIndex(-1)
            box.currentIndexChanged.connect(self.validate)
            box.view().parentWidget().setStyleSheet('background-color: #2e2e2e;')

        for partition in [self.comboBox_efi, self.comboBox_swap, self.comboBox_root]:
            get_available_partitions(partition)
            partition.setCurrentIndex(-1)
            partition.currentIndexChanged.connect(self.validate)

        for line_edit in [self.lineEdit_hostname, self.lineEdit_username, 
                      self.lineEdit_upasswd, self.lineEdit_upasswd_confirm, 
                      self.lineEdit_rpasswd, self.lineEdit_rpasswd_confirm]:
            
            line_edit.textChanged.connect(self.validate)
        
        self.optionals = set(self.optionals)
        
        self.pushButton_start.clicked.connect(self.change_index_settings)
        self.pushButton_next.clicked.connect(self.change_index_optionals)
        self.pushButton_back2.clicked.connect(self.change_index_settings)
        self.pushButton_next2.clicked.connect(self.write_config_file)
        self.pushButton_next2.clicked.connect(self.change_index_process)
        self.pushButton_finish.clicked.connect(self.graceful_exit)
        self.pushButton_exit.clicked.connect(self.graceful_exit)

    def execute_bash_script(self, list_view: QListView, script_path: str):
        
        list_view = QListView()
        model = QStandardItemModel()
        list_view.setModel(model)

        self.exec_thread = ExecutionThread(script_path)
        self.exec_thread.command_output.connect(lambda line: model.appendRow(QStandardItem(line)))
        


        timer = QTimer()
        timer.timeout.connect(lambda: None)
        timer.start(1000)

        self.exec_thread.start()
        
        if self.exec_thread.isFinished():
            try:
                self.exec_thread.quit()
            except Exception:
                pass
    def validate(self):
        for string in [ self.lineEdit_hostname, self.lineEdit_username]:
            names = validate_string(string)
            
        for combobox, dictionary in zip([self.comboBox_language, self.comboBox_desktopEnvironment, self.comboBox_displayManager, self.comboBox_kernel], 
                                 [ LANGUAGE, DESKTOP_ENVIRONMENT, DISPLAY_MANAGER, KERNEL ]):
            lang = validate_combobox(combobox, dictionary)
            
        user_pw = validate_password(self.lineEdit_upasswd, self.lineEdit_upasswd_confirm)
        rootpw = validate_password(self.lineEdit_rpasswd, self.lineEdit_rpasswd_confirm)

        efi = validate_partition(self.comboBox_efi, self.comboBox_swap, self.comboBox_root)
        swap = validate_partition(self.comboBox_swap, self.comboBox_efi, self.comboBox_root)
        root = validate_partition(self.comboBox_root, self.comboBox_efi, self.comboBox_swap)
        
        if all([names, lang, user_pw, rootpw, efi, swap, root]):
            self.pushButton_next.setEnabled(True)
        if not all([names, lang, user_pw, rootpw, efi, swap, root]):
            self.pushButton_next.setEnabled(False)

    def write_config_file(self):
        
        self.get_checked_optionals()
        optionals_keys = []
        optionals_values = []
        
        set_language = get_dictionary_value(self.comboBox_language, LANGUAGE)
        set_timezone = self.comboBox_timezone.currentText()
        set_desktop = get_dictionary_value(self.comboBox_desktopEnvironment, DESKTOP_ENVIRONMENT)
        set_display = get_dictionary_value(self.comboBox_displayManager, DISPLAY_MANAGER)
        set_kernel = get_dictionary_value(self.comboBox_kernel, KERNEL)
        set_hostname = self.lineEdit_hostname.text()
        set_username = self.lineEdit_username.text()
        set_upasswd = self.lineEdit_upasswd.text()
        set_rpasswd = self.lineEdit_rpasswd.text()
        set_efi = self.comboBox_efi.currentText()
        set_swap = self.comboBox_swap.currentText()
        set_root = self.comboBox_root.currentText()

        
        shutil.copyfile('tmp/archlinux-bootstrap-x86_64.tar.gz', f"{self.dst}/archlinux-bootstrap-x86_64.tar.gz")
        
        with open(f"{self.dst}/.env", 'w') as file:
            for name, set in zip(['LANGUAGE', 'TIMEZONE', 'DESKTOP_ENVIRONMENT', 
                   'DISPLAY_MANAGER', 'KERNEL', 'HOSTNAME', 
                   'USERNAME', 'UPASSWD', 'RPASSWD', 
                   'EFI', 'SWAP', 'ROOT'], [set_language, set_timezone, set_desktop, 
                    set_display, set_kernel, set_hostname, 
                    set_username, set_upasswd, set_rpasswd, 
                    set_efi, set_swap, set_root]):
                
                file.write(f"{name}='{set}'\n")

            for items in self.optionals:
                if items.isChecked():
                    optionals_keys.append(items.text())
                    
            for special, key in zip(['Figma', 'Miniconda', 'Oh-My-Zsh'], ['FIGMA', 'MINICONDA', 'OHMYZSH']):
                if special in optionals_keys:
                    value = OPTIONALS.get(special)
                    file.write(f"{key}='{value}'\n")
                    optionals_keys.remove(special)
                    
            for keys in optionals_keys:
                values = OPTIONALS.get(keys)
                optionals_values.append(values)

            optionals_values = str(optionals_values).replace('"', '').replace(',', '').replace('[', '(').replace(']', ')')
            
            file.write(f"OPTIONALS={optionals_values}")

    def get_checked_optionals(self):
                
        for opt in self.optionals:
            if opt.isChecked():
                selected_key = opt.text()
                get = OPTIONALS.get(selected_key)
                checked.append(get)
                
        return checked
     
    def insert_path_in_script(self, script_path, tempdir_path, line_number):
        with fileinput.FileInput(script_path, inplace=True) as file:
            for line_count, line in enumerate(file, start=1):
                if line_count == line_number:
                    print(f'temp="{tempdir_path}"')
                print(line, end='')
   
    def change_index_settings(self):
        self.mainStacked.setCurrentIndex(1)

    def change_index_optionals(self):
        self.mainStacked.setCurrentIndex(2)
        
    def change_index_process(self):
        
        shutil.copyfile('copy_process.sh', f"{self.dst}/script.sh")
        self.insert_path_in_script(f"{self.dst}/script.sh", self.dst, 4)
        self.mainStacked.setCurrentIndex(3)
        shutil.copyfile(f"{self.dst}/script.sh", './script(backup).sh')
        self.thread.start()
  
    def graceful_exit(self):
        quit_app()
        
        
      

        
if __name__ == "__main__":

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
