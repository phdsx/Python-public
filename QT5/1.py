import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        QToolTip.setFont(QFont('微软雅黑',10))
        self.setToolTip('')


        btn=QPushButton('退出',self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('退出程序')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        '''

        self.setGeometry(330,170,600,400)
        self.setWindowTitle("第一个程序")
        self.setWindowIcon(QIcon('1.png'))
        self.show()

    def closeEvent(self, event):

        reply=QMessageBox.question(self,'消息',"确认退出？",QMessageBox.Yes|QMessageBox.Mo,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Example()

    sys.exit(app.exec_())