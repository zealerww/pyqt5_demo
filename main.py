#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: 
Author: wuwei.wison
Time: 2019-11-13
"""

from __future__ import print_function
from __future__ import absolute_import
import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QStatusBar
from PyQt5 import QtGui
from form import Ui_Form
import pkgutil


# important
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")
icon_file = os.path.join(base_path, 'source/app.ico')
print(icon_file)
class BasicForm(QWidget, Ui_Form):
    def __init__(self):
        super(BasicForm, self).__init__()
        self.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('创建文件夹')
        self.main_widget = BasicForm()
        self.setCentralWidget(self.main_widget)
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.setWindowIcon(QtGui.QIcon(icon_file))
        self.resize(500, 500)

        self.main_widget.select_dir.clicked.connect(self.task)

    def task(self):
        self.status_bar.showMessage('')

        parent_dir_path = QFileDialog().getExistingDirectory(caption='选择文件夹')

        if parent_dir_path:
            try:
                text = self.main_widget.textEdit.toPlainText()
                name_list = text.split('\n')
                for name in name_list:
                    if name:
                        dir_path = os.path.join(parent_dir_path, name)
                        os.mkdir(dir_path)
                self.status_bar.showMessage('创建成功！')
            except Exception as e:
                print(e)
                self.status_bar.showMessage('创建失败!文件夹是否存在或是否有权限?')
        else:
            self.status_bar.showMessage('未选择文件夹!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

