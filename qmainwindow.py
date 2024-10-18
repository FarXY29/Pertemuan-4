# MENGGUNAKAN QMainWindow
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()
# Label = QLabel("Label", window) #Cara 1
label = QLabel(window)            #Cara 2
label.setText("Label1")
label.move(200,0)

# button = QPushButton("MyButton", window) #Cara 1
button = QPushButton(window)               #cara 2
button.setText("Button1")

window.show()
app.exec_()