"""
	Python GIST Uploader
	By Roy Portas
"""

import requests
import json

# GUI Stuff
from PySide import QtGui
from gui import Ui_MainWindow as main
from linkDisplay import Ui_Dialog as popupUI
import sys


class Popup(QtGui.QWidget):
	def __init__(self, text):
		QtGui.QWidget.__init__(self)
		self.ui = popupUI()
		self.ui.setupUi(self)
		self.ui.textEdit.setText(text)
		self.ui.okButton.clicked.connect(self.quit)

	def quit(self):
		self.close()

class GistUploader(QtGui.QMainWindow):
	def __init__(self):
		super(GistUploader, self).__init__()
		self.ui = main()
		self.ui.setupUi(self)
		self.ui.actionUpload.triggered.connect(self.getDataAndUpload)
		self.ui.actionDisplay_Last_URL.triggered.connect(self.displayURL)
		self.ui.actionOpen.triggered.connect(self.openFile)
		self.ui.actionSave.triggered.connect(self.saveFile)
		self.ui.textEdit.setTabStopWidth(20)
		self.url = None

		self.show()

	def displayURL(self):
		self.popupWin = Popup(self.url)
		self.popupWin.show()

	def openFile(self):
		fname, other = QtGui.QFileDialog.getOpenFileName(self, "Open file")
		try:
			with open(fname, 'r') as f:
				self.ui.textEdit.setPlainText(f.read())
		except:
			print("Error: Failed to open file")

	def saveFile(self):
		fname, other = QtGui.QFileDialog.getSaveFileName(self, "Save file")
		try:
			with open(fname, 'w') as f:
				text = self.ui.textEdit.toPlainText()
				f.write(text)
		except:
			print('Error: Failed to save file')

	def getDataAndUpload(self):
		text = self.ui.textEdit.toPlainText()
		name = self.ui.titleEdit.text()
		desc = self.ui.descEdit.text()
		ext = self.ui.extBox.currentText()
		name = name + ext
		self.url = uploadGist(desc, text, name)
		self.popupWin = Popup(self.url)
		self.popupWin.show()

def uploadGist(desc, content, name):
	payload = {"description":desc, "public":0, "files":{name:{"content":content}}}
	jsonPayload = json.dumps(payload)
	r = requests.post("https://api.github.com/gists", data=jsonPayload)
	response = r.json()
	return response.get('html_url')


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	guploader = GistUploader()
	sys.exit(app.exec_())