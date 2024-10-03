import subprocess
import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal

class SidebarMenu(QWidget):
    
    changeDockRequested = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_analyze = QPushButton("Analyze Recordings")
        self.btn_edit = QPushButton("Edit Recordings")
        self.btn_settings = QPushButton("Settings")
        self.btn_profile = QPushButton("Profile")
        
        self.layout.addWidget(self.btn_dashboard)
        self.layout.addWidget(self.btn_analyze)
        self.layout.addWidget(self.btn_edit)
        self.layout.addWidget(self.btn_settings)
        self.layout.addWidget(self.btn_profile)
        
        self.setLayout(self.layout)

        self.btn_dashboard.clicked.connect(lambda: self.changeDockRequested.emit("dock1"))
        self.btn_analyze.clicked.connect(lambda: self.changeDockRequested.emit("dock2"))
        self.btn_edit.clicked.connect(lambda: self.changeDockRequested.emit("dock3"))
        self.btn_settings.clicked.connect(lambda: self.changeDockRequested.emit("dock4"))
        self.btn_profile.clicked.connect(lambda: self.changeDockRequested.emit("dock5"))
        
if __name__ == "__main__":
    subprocess.Popen([sys.executable, './main.py'])