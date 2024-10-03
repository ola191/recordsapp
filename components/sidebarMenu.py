from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal

class SidebarMenu(QWidget):
    
    changeDockRequested = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        self.button1 = QPushButton("Dashboard")
        self.button2 = QPushButton("Settings")
        self.button3 = QPushButton("Profile")
        
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        
        self.setLayout(self.layout)

        self.button1.clicked.connect(lambda: self.changeDockRequested.emit("dock1"))
        self.button2.clicked.connect(lambda: self.changeDockRequested.emit("dock2"))
        self.button3.clicked.connect(lambda: self.changeDockRequested.emit("dock3"))