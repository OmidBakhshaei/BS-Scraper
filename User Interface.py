import os
import webbrowser
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """Create the UI."""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 75)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.get_data)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_data(self):
        """Connect the code to the "دانلود" pushbutton."""
        def get_game_s_url(team):
            """Return the link that contains the game which the user is looking for.

            Args:
                team (str): The team which the user wants to download its game

            Returns:
                str: the link which contains the video of the game
            """
            # reads the html page
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html)
            # returns a list of all links in the HTML tagged with href
            for a in soup.find_all('a', href=True):
                # finds the links which are dedicated to the selected team's games
                if team in a['href'] and "خلاصه" in a['href']:
                    new_url = url+a['href']
                    return new_url

        def IRI_to_Ascii(link):
            """Convert a URL containing non-ascii characters(IRI) to a plain ASCII.

            Args:
                link (str): link to convert

            Returns:
                str: ASCII link
            """
            iri = quote(link.split("/")[-1])
            url_without_iri = link.split("/")[:-1]
            converted_url = "/".join(url_without_iri) + "/" + iri
            return converted_url

        def get_video_s_url():
            """Extract and return the download's url from the game's url."""
            html = urllib.request.urlopen(IRI_to_Ascii(get_game_s_url(team)))
            soup = BeautifulSoup(html)
            for a in soup.find_all('a', href=True):
                if ".mp4" in a['href']:
                    get_video_s_url = a['href']
            return get_video_s_url

        def download_video():
            """Create a folder on user's desktop and save the video in the created folder."""
            desktop = os.path.join(os.path.join(
                os.environ['USERPROFILE']), 'Desktop')
            newpath = os.path.join(desktop, "Varzesh3")
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            filename_and_path = os.path.join(newpath, f"{team}.mp4")
            urllib.request.urlretrieve(get_video_s_url(), filename_and_path)

        url = "https://video.varzesh3.com"
        team = self.lineEdit.text()
        download_video()

    def retranslateUi(self, MainWindow):
        """Translate to Farsi."""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "دانلود کننده‌ی آخرین بازی تیم‌های فوتبال"))
        self.pushButton.setText(_translate("MainWindow", "دانلود"))
        self.lineEdit.setText(_translate("MainWindow", "لیورپول"))
        self.label.setText(_translate(
            "MainWindow", "نام تیم مورد نظر را وارد کنید:"))

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
