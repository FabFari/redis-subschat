from PyQt4 import QtCore, QtGui
from settings import r
import threading

pubsub = None
ui = None

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# The Main Window class, the UI of the application
class Ui_MainWindow(object):
	# To setup the User interface main window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Redis Web-Chat"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 467, 371, 71))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 510, 98, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 521, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 10, 101, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 10, 98, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 50, 521, 401))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(640, 460, 141, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 50, 221, 21))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 80, 221, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 110, 221, 22))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 140, 221, 22))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 170, 221, 22))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 200, 221, 22))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 230, 221, 22))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_8 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 260, 221, 22))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox_9 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 410, 221, 22))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_10 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(20, 290, 221, 22))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.checkBox_11 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(20, 320, 221, 22))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.checkBox_12 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(20, 350, 221, 22))
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.checkBox_13 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(20, 380, 221, 22))
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 496, 211, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 466, 201, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_2.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.textEdit.raise_()
        self.comboBox.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.checkBox_7.raise_()
        self.checkBox_8.raise_()
        self.checkBox_9.raise_()
        self.checkBox_10.raise_()
        self.checkBox_11.raise_()
        self.checkBox_12.raise_()
        self.checkBox_13.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
	# To setup the labels and to register the handlers 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Send", None))
        self.label.setText(_translate("MainWindow", "Channels", None))
        self.label_2.setText(_translate("MainWindow", "Multi-Tematic Web-Chat", None))
        self.pushButton_2.setText(_translate("MainWindow", "Stop", None))
        self.pushButton_3.setText(_translate("MainWindow", "Start", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sport", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Movies", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "TV Shows", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Music", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "Economics", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "Politics", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "Books", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "Pets", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "Travel", None))
        self.comboBox.setItemText(9, _translate("MainWindow", "Cooking", None))
        self.comboBox.setItemText(10, _translate("MainWindow", "Gaming", None))
        self.comboBox.setItemText(11, _translate("MainWindow", "Fitness", None))
        self.comboBox.setItemText(12, _translate("MainWindow", "Misc", None))
        self.checkBox.setText(_translate("MainWindow", "Sport", None))
        self.checkBox_2.setText(_translate("MainWindow", "Movies", None))
        self.checkBox_3.setText(_translate("MainWindow", "TV Shows", None))
        self.checkBox_4.setText(_translate("MainWindow", "Music", None))
        self.checkBox_5.setText(_translate("MainWindow", "Economics", None))
        self.checkBox_6.setText(_translate("MainWindow", "Politics", None))
        self.checkBox_7.setText(_translate("MainWindow", "Books", None))
        self.checkBox_8.setText(_translate("MainWindow", "Pets", None))
        self.checkBox_9.setText(_translate("MainWindow", "Misc", None))
        self.checkBox_10.setText(_translate("MainWindow", "Travel", None))
        self.checkBox_11.setText(_translate("MainWindow", "Cooking", None))
        self.checkBox_12.setText(_translate("MainWindow", "Gaming", None))
        self.checkBox_13.setText(_translate("MainWindow", "Fitness", None))
        self.label_3.setText(_translate("MainWindow", "Username", None))
        # Disable the button needed only when the session is started
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.textEdit.setReadOnly(True)
        # Set handlers of the application buttons
        self.pushButton.clicked.connect(on_send)
        self.pushButton_2.clicked.connect(on_stop)
        self.pushButton_3.clicked.connect(on_start)

# The handler of the message receiving system: 
# it's job is to push the received message into the textEdit
def mess_handler(message):
	QtCore.QMetaObject.invokeMethod(ui.textEdit, "append", QtCore.Q_ARG(str,str(message['data'])+'\n'))

# The handler of the start button: it has to setup the chat session and
# start the concurrent thread handling the receiving system.
def on_start():
	global pubsub
	global ui
	
	# We create a new instance of the object to interact with the
	# Redis Pub/Sub sub-system
	pubsub = r.pubsub()	
	
	# Disable Widgets and manage subscriptions
	ui.pushButton_3.setEnabled(False)
	ui.lineEdit.setEnabled(False)
	ui.checkBox.setEnabled(False)
	if ui.checkBox.isChecked():
		pubsub.subscribe(**{str(ui.checkBox.text()): mess_handler})
	ui.checkBox_2.setEnabled(False)
	if ui.checkBox_2.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_2.text()): mess_handler})
	ui.checkBox_3.setEnabled(False)
	if ui.checkBox_3.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_3.text()): mess_handler})
	ui.checkBox_4.setEnabled(False)
	if ui.checkBox_4.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_4.text()): mess_handler})
	ui.checkBox_5.setEnabled(False)
	if ui.checkBox_5.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_5.text()): mess_handler})
	ui.checkBox_6.setEnabled(False)
	if ui.checkBox_6.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_6.text()): mess_handler})
	ui.checkBox_7.setEnabled(False)
	if ui.checkBox_7.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_7.text()): mess_handler})
	ui.checkBox_8.setEnabled(False)
	if ui.checkBox_8.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_8.text()): mess_handler})
	ui.checkBox_9.setEnabled(False)
	if ui.checkBox_9.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_9.text()): mess_handler})
	ui.checkBox_10.setEnabled(False)
	if ui.checkBox_10.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_10.text()): mess_handler})
	ui.checkBox_11.setEnabled(False)
	if ui.checkBox_11.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_11.text()): mess_handler})
	ui.checkBox_12.setEnabled(False)
	if ui.checkBox_12.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_12.text()): mess_handler})
	ui.checkBox_13.setEnabled(False)
	if ui.checkBox_13.isChecked():
		pubsub.subscribe(**{str(ui.checkBox_13.text()): mess_handler})
	# Enable the buttons stop and send
	ui.pushButton.setEnabled(True)
	ui.pushButton_2.setEnabled(True)
	
	# To start the message receiving thread
	thread = pubsub.run_in_thread(sleep_time=0.001)

# The handler of the stop button: it has to stop close the channel to
# interact with the Redis Pub/Sub sub-system
def on_stop():
	global pubsub
	global ui
	
	# Disable Widgets and manage subscriptions
	ui.pushButton_3.setEnabled(True)
	ui.lineEdit.setEnabled(True)
	ui.checkBox.setEnabled(True)
	ui.checkBox_2.setEnabled(True)
	ui.checkBox_3.setEnabled(True)
	ui.checkBox_4.setEnabled(True)
	ui.checkBox_5.setEnabled(True)
	ui.checkBox_6.setEnabled(True)
	ui.checkBox_7.setEnabled(True)
	ui.checkBox_8.setEnabled(True)
	ui.checkBox_9.setEnabled(True)
	ui.checkBox_10.setEnabled(True)
	ui.checkBox_11.setEnabled(True)
	ui.checkBox_12.setEnabled(True)
	ui.checkBox_13.setEnabled(True)
		
	# Enable Buttons
	ui.pushButton.setEnabled(False)
	ui.pushButton_2.setEnabled(False)
    
    # Close the Pub/Sub channel
	pubsub.close()

# The handler of the send button: it has to read the content of the
# message and push it to the proper channel, using the pubsub object
def on_send():
	msg = str(ui.textEdit_2.toPlainText())
	# Check if the message is not empty
	if len(msg) > 0:
		usrname = str(ui.lineEdit.text())
		channel = str(ui.comboBox.currentText())
		ui.textEdit_2.clear()
		message = '%s [%s]: %s' % (usrname, channel, msg)
		# Publish the message into the Pub/Sub sub-system
		r.publish(channel, message)
	

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
