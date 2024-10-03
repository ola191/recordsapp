import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from components.contentArea import ContentArea
from components.sidebarMenu import SidebarMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Dashboard of sound records")
        self.setMinimumSize(1280,720)
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout(self.centralWidget)

        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        self.setDockNestingEnabled(True)
        
        self.sidebarMenu = SidebarMenu(self)
        self.contentArea = ContentArea(self)
        
        self.layout.addWidget(self.sidebarMenu)
        self.layout.addWidget(self.contentArea)
        
        self.sidebarMenu.changeDockRequested.connect(self.contentArea.changeDock)
        
    def resizeEvent(self, event):
        width = self.width()
        height = self.height()

        self.sidebarMenu.setFixedWidth(width * 0.2)
        self.contentArea.setFixedWidth(width * 0.8)
        
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())