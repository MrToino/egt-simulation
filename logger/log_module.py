"""
Project: EGT-Sim

Filename: log_module.py
Description: defines the log management module
"""

import logging as log


class EGTLogger(log.Logger):
    def __init__(self, filename: str = '..\\logs\\log.log'):
        super().__init__(filename)

        """Initializes the logger object"""
        self.logger = log.getLogger(filename)
        self.filename = filename

    def basicConfig(self, level=log.DEBUG, filemode='a', log_format="%(levelname)s [%(asctime)s] %(message)s"):
        log.basicConfig(filename=self.filename, level=level, format=log_format, filemode=filemode)


