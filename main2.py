import time
import serial
import sys
import numpy as np
import pyqtgraph as pg
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

ardData = serial.Serial("/dev/ttyUSB0", 115200)
time.sleep(2)

x = []
y1 = []
y2 = []


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("My Application")
window.setGeometry(100, 100, 800, 600)
layout = QVBoxLayout(window)


# graphWidget =pg.PlotWidget()
# layout.addWidget(graphWidget)
# plotSin=graphWidget.plot(x,y1,pen=pg.mkPen('r',width=1))
# # plotCos=graphWidget.plot(x,y2,pen=pg.mkPen('g',width=1))
# graphWidget.setYRange(-1.25,1.25)


def updatePlot():
    global x, y1, y2
    cmd = 'send'
    cmd = cmd + '\r'
    ardData.write(cmd.encode())
    print("called")
    while len(x) < 50 or len(y1) < 50 or len(y2) < 50:
        while ardData.inWaiting() == 0:
            pass
        data = ardData.readline()
        data = str(data, "utf-8")
        data = data.replace("\r\n", "")
        data1 = data.split(" ")
        x.append(float(data1[0]))
        y1.append(float(data1[1]))
        y2.append(float(data1[2]))

    # print(x)
    # print(y1)
    # print(y2)

    plotSin.setData(x, y1)
    # plotCos.setData(x, y2)

    print("Data Updated")

    x = []
    y1 = []
    y2 = []


graphWidget = pg.PlotWidget()
layout.addWidget(graphWidget)
plotSin = graphWidget.plot(x, y1, pen=pg.mkPen("r", width=1))
# plotCos=graphWidget.plot(x,y2,pen=pg.mkPen('g',width=1))
graphWidget.setYRange(-2, 2)


timer = QTimer()
timer.timeout.connect(updatePlot)
timer.start(5000)


window.setLayout(layout)
window.show()
sys.exit(app.exec())
