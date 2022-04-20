import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrollbarhelper import ScrollbarHelper
import cv2
import os
import sys
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsg
from logging import StreamHandler, getLogger, DEBUG, NullHandler, INFO, WARNING, ERROR
import subprocess
import platform

from pygubu.widgets.scrollbarhelper import ScrollbarHelper

import Settings
import Utility as util
from Camera import Camera
from CommandLoader import CommandLoader
from Commands import McuCommandBase, PythonCommandBase, Sender
import PokeConLogger
from Commands.Keys import KeyPress
from GuiAssets import CaptureArea, ControllerGUI
from Keyboard import SwitchKeyboardController
from Menubar import PokeController_Menubar

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "assets/MainUI.ui"


class MainApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('main_window', master)

        self.var_canera_id = None
        self.is_show_realtime = None
        self.var_camera_name_from_dll = None
        self.var_fps = None
        self.var_communication_port = None
        self.is_show_serial = None
        self.var_show_size = None
        self.var_python_command_name = None
        self.var_mcu_command_name = None
        builder.import_variables(self, ['var_canera_id', 'is_show_realtime', 'var_camera_name_from_dll', 'var_fps',
                                        'var_communication_port', 'is_show_serial', 'var_show_size',
                                        'var_python_command_name', 'var_mcu_command_name'])

        builder.connect_callbacks(self)
        # ログ機能の生成
        self.logger = getLogger(__name__)
        self.logger.addHandler(NullHandler())
        # self.logger.setLevel(DEBUG)
        self.logger.propagate = True

        # load settings file
        # self.loadSettings()

    def run(self):
        self.mainwindow.mainloop()

    def open_camera(self):
        pass

    def save_capture(self):
        pass

    def set_camera_id(self, event=None):
        self.logger.debug(self.var_camera_name_from_dll.get())
        pass

    def applyFps(self, event=None):
        print(self.var_fps.get())
        pass

    def connect_communication_port(self):
        pass

    def applyWindowSize(self, event=None):
        pass

    def reload_commands(self):
        pass

    def start_assigned_command(self):
        pass

    def pause_running_script(self):
        pass


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, _logger, level):
        self.logger = _logger
        self.level = level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.level, line.rstrip())

    def flush(self):
        pass


if __name__ == '__main__':
    logger = PokeConLogger.root_logger()
    sys.stdout = StreamToLogger(logger, INFO)
    sys.stderr = StreamToLogger(logger, ERROR)
    root = tk.Tk()
    app = MainApp(root)
    app.run()
