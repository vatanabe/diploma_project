import sys 
from PySide.QtCore import QUrl, QSize
from PySide.QtGui import QApplication, QMainWindow, QWidget
from PySide.QtWebKit import QWebView


class Browser(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.web_view = QWebView()
        self.setCentralWidget(self.web_view)

        self.web_view.loadFinished.connect(self._load_finished)

    def _load_finished(self):
        frame = self.web_view.page().mainFrame()
        self.web_view.page().setViewportSize(frame.contentsSize())
        self.resize(frame.contentsSize())
        html_data = frame.toHtml()


if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    browser = Browser() 
    r = QUrl("http://127.0.0.1:5000/1")
    browser.web_view.load(r)
    browser.showMaximized()
    app.exec_()