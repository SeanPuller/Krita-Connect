from PyQt5.QtWidgets import *
from PyQt5 import Qt, QtCore

#this is for development autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *

class krita_connect(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Krita Connect")
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)
        
        exampleButton = QPushButton("Connect to ComfyUI", mainWidget)
        exampleButton.clicked.connect(self.popup)
        
        displayLabel = QLabel("Not Connected", mainWidget)
        displayLabel.setAlignment(Qt.AlignCenter)
        


        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(exampleButton)
        mainWidget.layout().addWidget(displayLabel)        
        mainWidget.layout().setAlignment(QtCore.Qt.AlignTop)

        
    def popup(self):
              QMessageBox.information(QWidget(), "Docker Example", "This example button works")
              
    def canvasChanged(self, canvas):
        pass