import sys 
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("WindowTitle")
        self.setMinimumSize(1280,720)
        
    def resizeEvent(self, event):
        size = event.size()
        width = self.width()
        height = self.height()

        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())