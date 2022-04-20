#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button
from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
import tkinter as tk


class SubWindow(ImageProcPythonCommand, tk.Frame):
    NAME = 'TopLevelかんたんにするやつ'

    def __init__(self, cam, master=None):
        super().__init__(cam, master)
        self.cam = cam
        self.master = master
        self.sub_window = None
        self.sample_checkbox = None

    def do(self):
        if self.master is not None:
            self.sub_window = tk.Toplevel()

        self.sample_checkbox = tk.Checkbutton(self.sub_window, text="Sampleです")
        self.sample_checkbox.pack()
