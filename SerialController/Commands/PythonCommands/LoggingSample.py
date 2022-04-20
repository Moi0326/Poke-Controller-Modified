#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button
from Commands.PythonCommandBase import PythonCommand
from Commands.PythonCommandBase import ImageProcPythonCommand
from logging import getLogger, DEBUG, NullHandler


# ログ出力のサンプル
class LoggingSample(ImageProcPythonCommand):
    NAME = 'ログ出力のサンプル'

    def __init__(self, cam):
        super().__init__(cam)
        self.logger = getLogger(__name__)
        self.logger.addHandler(NullHandler())
        self.logger.propagate = True

    def do(self):
        self.logger.debug("DEBUG")
        self.logger.info("INFO")
        self.logger.warning("WARNING")
        self.logger.error("ERROR")
        self.logger.critical("CRITICAL")
