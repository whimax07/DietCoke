import sys
import ast
import ColourPalletSuportingClasses
from PyQt5.QtWidgets import (QWidget, QApplication, QSlider,
                             QGridLayout, QLineEdit, QLabel,
                             QFrame)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class ColourPallet2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.col = QColor(0, 84, 154)

        red = QLabel('Red')
        green = QLabel('Green')
        blue = QLabel('Blue')
        hue = QLabel('Hue')
        saturation = QLabel('Saturation')
        luminace = QLabel('Luminace')

        self.redSlider = QSlider()
        self.redSlider.setSingleStep(1)
        self.redSlider.setMaximum(255)
        self.redSlider.valueChanged.connect(self.rgb1SlidersChanged)
        self.greenSlider = QSlider()
        self.greenSlider.setSingleStep(1)
        self.greenSlider.setMaximum(255)
        self.greenSlider.valueChanged.connect(self.rgb1SlidersChanged)
        self.blueSlider = QSlider()
        self.blueSlider.setSingleStep(1)
        self.blueSlider.setMaximum(255)
        self.blueSlider.valueChanged.connect(self.rgb1SlidersChanged)

        self.hueSlider = QSlider()
        self.hueSlider.setSingleStep(1)
        self.hueSlider.setMaximum(359)
        self.hueSlider.valueChanged.connect(self.hslSliderChanged)
        self.saturationSlider = QSlider()
        self.saturationSlider.setSingleStep(1)
        self.saturationSlider.setMaximum(255)
        self.saturationSlider.valueChanged.connect(self.hslSliderChanged)
        self.luminaceSlider = QSlider()
        self.luminaceSlider.setSingleStep(1)
        self.luminaceSlider.setMaximum(255)
        self.luminaceSlider.valueChanged.connect(self.hslSliderChanged)

        grid1 = QGridLayout()
        grid1.setHorizontalSpacing(10)
        grid1.setContentsMargins(0, 0, 0, 0)
        for i in range(6):
            grid1.setColumnStretch(i, 1)
            grid1.setColumnMinimumWidth(i, 50)
            grid1.setRowMinimumHeight(i, 10)

        grid1.addWidget(red, 0, 0, alignment=Qt.AlignCenter)
        grid1.addWidget(self.redSlider, 1, 0, alignment=Qt.AlignCenter)
        grid1.addWidget(green, 0, 1, alignment=Qt.AlignCenter)
        grid1.addWidget(self.greenSlider, 1, 1, alignment=Qt.AlignCenter)
        grid1.addWidget(blue, 0, 2, alignment=Qt.AlignCenter)
        grid1.addWidget(self.blueSlider, 1, 2, alignment=Qt.AlignCenter)

        grid1.addWidget(hue, 0, 3, alignment=Qt.AlignCenter)
        grid1.addWidget(self.hueSlider, 1, 3, alignment=Qt.AlignCenter)
        grid1.addWidget(saturation, 0, 4, alignment=Qt.AlignCenter)
        grid1.addWidget(self.saturationSlider, 1, 4, alignment=Qt.AlignCenter)
        grid1.addWidget(luminace, 0, 5, alignment=Qt.AlignCenter)
        grid1.addWidget(self.luminaceSlider, 1, 5, alignment=Qt.AlignCenter)

        rgb1_ = QLabel('rgb')
        rgb255_ = QLabel('RGB')
        hex_ = QLabel('Hex')
        hsl_ = QLabel('hsl')

        self.rgb1Edit = QLineEdit()
        self.rgb1Edit.editingFinished.connect(self.rg1EditChanged)
        self.rgb255Edit = QLineEdit()
        self.rgb255Edit.editingFinished.connect(self.rgb255EditChanged)
        self.hexEdit = QLineEdit()
        self.hexEdit.editingFinished.connect(self.hexEditChanged)
        self.hslEdit = QLineEdit()
        self.hslEdit.editingFinished.connect(self.hslEditChanged)

        grid2 = QGridLayout()
        grid2.setVerticalSpacing(2)
        grid2.setHorizontalSpacing(20)
        grid2.setContentsMargins(0, 0, 0, 0)

        grid2.addWidget(rgb1_, 0, 0)
        grid2.addWidget(rgb255_, 0, 1)
        grid2.addWidget(hex_, 0, 2)
        grid2.addWidget(hsl_, 0, 3)

        grid2.addWidget(self.rgb1Edit, 1, 0)
        grid2.addWidget(self.rgb255Edit, 1, 1)
        grid2.addWidget(self.hexEdit, 1, 2)
        grid2.addWidget(self.hslEdit, 1, 3)

        self.square = QFrame(self)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        grid = QGridLayout()
        grid.addLayout(grid1, 0, 0)
        grid.addLayout(grid2, 1, 0)
        grid.addWidget(self.square, 2, 0)
        for i in (0, 2):
            grid.setRowStretch(i, 1)
        grid.setVerticalSpacing(10)

        self.setLayout(grid)

        self.setEverything()
        self.setGeometry(400, 400, 500, 400)
        self.setWindowTitle('Colour Pallet 2')
        self.show()

    def rg1EditChanged(self):
        rgb1 = ast.literal_eval(self.rgb1Edit.text())
        rgb255 = [round(i * 255) for i in rgb1]
        self.col.setRgb(*rgb255)
        self.setEverything()

    def rgb255EditChanged(self):
        rgb255 = ast.literal_eval(self.rgb255Edit.text())
        self.col.setRgb(*rgb255)
        self.setEverything()

    def hexEditChanged(self):
        self.col.setNamedColor(self.hexEdit.text())
        self.setEverything()

    def hslEditChanged(self):
        hsl = ast.literal_eval(self.hslEdit.text())
        self.col.setHsl(*hsl)
        self.setEverything()

    def rgb1SlidersChanged(self):
        self.col.setRgb(self.redSlider.value(), self.greenSlider.value(),
                        self.blueSlider.value())
        self.setEverything()

    def hslSliderChanged(self):
        self.col.setHsl(self.hueSlider.value(), self.saturationSlider.value(),
                        self.luminaceSlider.value())
        self.setEverything()

    def setEverything(self):
        hsl = self.col.getHsl()[0:3]
        Hex = self.col.name()
        rgb255 = self.col.getRgb()[0:3]
        rgb1 = [i/255 for i in rgb255][0:3]

        self.BlockSignals(True)
        self.hslEdit.setText(str(hsl))
        self.hexEdit.setText(Hex)
        self.rgb255Edit.setText(str(rgb255))
        self.rgb1Edit.setText(str(rgb1))

        self.redSlider.setValue(rgb255[0])
        self.greenSlider.setValue(rgb255[1])
        self.blueSlider.setValue(rgb255[2])

        self.hueSlider.setValue(hsl[0])
        self.saturationSlider.setValue(hsl[1])
        self.luminaceSlider.setValue(hsl[2])

        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())
        self.BlockSignals(False)

    def BlockSignals(self, state):
        self.hslEdit.blockSignals(state)
        self.hexEdit.blockSignals(state)
        self.rgb255Edit.blockSignals(state)
        self.rgb1Edit.blockSignals(state)
        self.redSlider.blockSignals(state)
        self.greenSlider.blockSignals(state)
        self.blueSlider.blockSignals(state)
        self.hueSlider.blockSignals(state)
        self.saturationSlider.blockSignals(state)
        self.luminaceSlider.blockSignals(state)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    colPal = ColourPallet2()
    sys.exit(app.exec_())
