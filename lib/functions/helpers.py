import re
import subprocess

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *





def add_combobox_scrollbar(component: QComboBox):
    component.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

def add_list(component: QComboBox, list: list):
    component.addItems(list)

def validate_password(first_password: QLineEdit, second_password: QLineEdit):
    
    pattern_1 = r"^.{1,}$" # at least 1 character
    pattern_2 = r'^{}$'.format(re.escape(first_password.text())) # matches first_password
    pattern_3 = r'^$' # empty

    if re.match(pattern_3, first_password.text()):
        default_1(first_password)
        first_pw = False
        
    elif re.match(pattern_1, first_password.text()):
        success_1(first_password)
        first_pw = True
        
    if re.match(pattern_3, second_password.text()):
        default_1(second_password)
        second_pw = False
    elif re.match(pattern_2, second_password.text()):
        success_1(second_password)
        second_pw = True
    elif not re.match(pattern_2, second_password.text()):
        error_1(second_password)
        second_pw = False

    if all([first_pw, second_pw]):
        return True
    else:
        return False
    
def get_available_partitions(comboBox: QComboBox) -> list:
    partitions = subprocess.check_output(['lsblk', '-lp', '-o', 'NAME']).decode().split('\n')
    for partition in partitions:
        if '/dev/nvme0n1' in partition or '/dev/sda' in partition:
            comboBox.addItem(partition)
    
def get_dictionary_value(comboBox: QComboBox, dictionary: dict):
    selected_key = comboBox.currentText()
    return dictionary.get(selected_key)    
             
def quit_app():
    """Terminate the application."""
    raise SystemExit

def validate_string(component: QLineEdit):
    component_text: str = component.text()
    pattern_1 = r"^(?![A-Z])[a-zA-Z0-9]{4,12}$"
    pattern_2 = r"^.{0,3}$"

    if re.match(pattern_1, component_text):
            success_1(component)
            return True

    else:
        if not re.match(pattern_2, component_text):
            error_1(component)
            return False
        if re.match(pattern_2, component_text):
            default_1(component)
            return False

def validate_partition(partition_1: QComboBox, partition_2: QComboBox, partition_3: QComboBox):

        if partition_1.currentIndex() == -1:
            default_2(partition_1)
            stat_1 = False
        elif partition_1.currentIndex() == partition_2.currentIndex() or partition_1.currentIndex() == partition_3.currentIndex():
            error_2(partition_1)
            stat_1 = False
        else:
            default_2(partition_1)
            stat_1 = True
        
        if partition_2.currentIndex() == -1:
            default_2(partition_2)
            stat_2 = False
        elif partition_2.currentIndex() == partition_3.currentIndex() or partition_2.currentIndex() == partition_1.currentIndex():
            error_2(partition_2)
            stat_2 = False
        else:
            default_2(partition_2)
            stat_2 = True
        
        if partition_3.currentIndex() == -1:
            default_2(partition_3)
            stat_3 = False
        elif partition_3.currentIndex() == partition_1.currentIndex() or partition_3.currentIndex() == partition_2.currentIndex():
            error_2(partition_3)
            stat_3 = False
        else:
            default_2(partition_3)
            stat_3 = True
            
        if all([stat_1, stat_2, stat_3]):
            return True
        elif not all([stat_1, stat_2, stat_3]):
            return False
  
def validate_combobox(component: QComboBox, dictionary: dict):
    key=get_dictionary_value(component, dictionary)
    
    if component.currentIndex() == -1:
        default_2(component)
        return False
    elif key == 1:
        error_2(component)
        return False
    elif key != 1:
        default_2(component)
        return True
    
def default_1(component) -> None:
    """
    Set the default_1 style sheet for a QLineEdit or QComboBox widget.

    Args:
        component (Union[QLineEdit, QComboBox]): The widget to set the style sheet for.
    """
    component.setStyleSheet(
        """
        background-image: url(:/input_field.png);
        border: 1px solid gray;
        border-radius: 3px;
        color: rgb(255, 255, 255);
        """
    )
    
def default_2(component) -> None:
    """
    Set the default_2 style sheet for a QLineEdit or QComboBox widget.

    Args:
        component (Union[QLineEdit, QComboBox]): The widget to set the style sheet for.
    """
    component.setStyleSheet(
        """
        border: 1px solid gray;
        border-radius: 3px;
        color: rgb(255, 255, 255);
        """
    )

def success_1(component) -> None:
    """
    Set the default_1 style sheet for a QLineEdit or QComboBox widget.

    Args:
        component (Union[QLineEdit, QComboBox]): The widget to set the style sheet for.
    """
    component.setStyleSheet(
        """
        background-image: url(:/input_field_success.png);
        border: 1px solid green;
        border-radius: 3px;
        color: rgb(255, 255, 255);
        """
    )
    
def error_1(component) -> None:
    """
    Set the default_1 style sheet for a QLineEdit or QComboBox widget.

    Args:
        component (Union[QLineEdit, QComboBox]): The widget to set the style sheet for.
    """
    component.setStyleSheet(
    """
        background-image: url(:/input_field_error.png);
        border: 1px solid red;
        border-radius: 3px;
        color: rgb(255, 255, 255);
    """
    )
    
def error_2(component) -> None:
    """
    Set the default_1 style sheet for a QLineEdit or QComboBox widget.

    Args:
        component (Union[QLineEdit, QComboBox]): The widget to set the style sheet for.
    """
    component.setStyleSheet(
    """
    border: 1px solid red;
    border-radius: 3px;
    color: rgb(255, 255, 255);
    """
    )