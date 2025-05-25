from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget,QTableWidgetItem

import sys
from studentGrup import*

app = QtWidgets.QApplication([])
win = uic.loadUi("студенты.ui")

Gr = Grup()
Gr.read_data_from_file("text.txt")
Gr.sort_by_fam()
print("!!!", Gr.count)


data = []
data.append(('Заполнить', 'QTableWidget'))
data.append(('с данными', 'в Python'))
data.append(('очень', 'просто'))
win.tableWidget.setRowCount(Gr.count)


def btnLoadTable():
    #print(1111)
    row = 0
    for x in Gr.A:
        print(2)
       
        win.tableWidget.setItem(row, 0, QTableWidgetItem(Gr.A[x].fam+' '+Gr.A[x].name+' '+Gr.A[x].otchestvo))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(Gr.A[x].year))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(Gr.A[x].city))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(Gr.A[x].sb_inf))
        win.tableWidget.setItem(row, 4, QTableWidgetItem(Gr.A[x].sb_math)) 
        row += 1
    
 
    #print(2222)

    
win.pushButton.clicked.connect(btnLoadTable)


win.show()
sys.exit(app.exec())
