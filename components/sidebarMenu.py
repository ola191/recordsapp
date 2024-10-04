import subprocess
import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox, QSpacerItem, QSizePolicy, QHBoxLayout, QLabel
from PySide6.QtCore import Signal, QSize, Qt
from PySide6.QtGui import QIcon, QFont

class SidebarMenu(QWidget):
    
    changeDockRequested = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        
        self.setStyleSheet("""
            QWidget {
            }
            QPushButton {
                text-align: left;
                background: transparent;
            }
            QIcon {
                padding: 0 10px;
            }
        """)

        self.btn_dashboard = self.createButton("Dashboard", "./icons/dashboard.png")
        self.btn_dashboard.setStyleSheet("""
            QPushButton {
                background: rgba(0, 0, 0, 0.2);
            }
        """)
        self.btn_analyze = self.createButton("Analyze Recordings", "./icons/analyzing.png")
        self.btn_edit = self.createButton("Edit Recordings", "./icons/editing.png")
        self.btn_settings = self.createButton("Settings", "./icons/settings.png")
        self.btn_profile = self.createButton("Profile", "./icons/profile.png")
        
        self.layout.addWidget(self.btn_dashboard)
        self.layout.addWidget(self.btn_analyze)
        self.layout.addWidget(self.btn_edit)
        self.layout.addWidget(self.btn_settings)
        self.layout.addWidget(self.btn_profile)
        
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        self.setLayout(self.layout)

        self.btn_dashboard.clicked.connect(lambda: self.changeDockRequested.emit("dock1"))
        self.btn_analyze.clicked.connect(lambda: self.changeDockRequested.emit("dock2"))
        self.btn_edit.clicked.connect(lambda: self.changeDockRequested.emit("dock3"))
        self.btn_settings.clicked.connect(lambda: self.changeDockRequested.emit("dock4"))
        self.btn_profile.clicked.connect(lambda: self.changeDockRequested.emit("dock5"))
        
        self.buttons = [self.btn_dashboard, self.btn_analyze, self.btn_edit, self.btn_settings, self.btn_profile]
        
    def createButton(self, text, iconPath):
        button = QPushButton()
        button.setStyleSheet("""
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.1);
            }
        """)
        button.setFont(QFont("Arial", 24))
        # button.setLayoutDirection(Qt.RightToRight)
        icon = QIcon(iconPath)
        iconLabel = QLabel()
        iconLabel.setPixmap(icon.pixmap(24, 24))
        iconLabel.setFixedSize(24, 24)

        textLabel = QLabel(text)
        
        layout = QHBoxLayout()
        
        layout.setSpacing(10)
        
        layout.addWidget(iconLabel)
        layout.addWidget(textLabel)
        
        button.setLayout(layout)
        
        button.clicked.connect(lambda: self.changeButtonColor(button))
        
        return button
    
    
    def changeButtonColor(self, clicked_button):
        for button in self.buttons:
            button.setStyleSheet("background: transparent;")

        clicked_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
if __name__ == "__main__":
    subprocess.Popen([sys.executable, './main.py'])