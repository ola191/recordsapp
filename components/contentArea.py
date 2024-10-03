from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QDockWidget
from PySide6.QtCore import Qt

class ContentArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        self.dock1 = QDockWidget("Dock 1", self)
        self.dock1.setWidget(QLabel("Dock 1 Content"))
        self.dock2 = QDockWidget("Dock 2", self)
        self.dock2.setWidget(QLabel("Dock 2 Content"))
        self.dock3 = QDockWidget("Dock 3", self)
        self.dock3.setWidget(QLabel("Dock 3 Content"))

        self.layout.addWidget(self.dock1)
        self.layout.addWidget(self.dock2)
        self.layout.addWidget(self.dock3)
        
        self.dock2.hide()
        self.dock3.hide()
        
        self.setLayout(self.layout)
        
    def changeDock(self, dockName):
        self.dock1.hide()
        self.dock2.hide()
        self.dock3.hide()

        if dockName == "dock1":
            self.dock1.show()
        elif dockName == "dock2":
            self.dock2.show()
        elif dockName == "dock3":
            self.dock3.show()