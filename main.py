from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon
import sys

app = QApplication(sys.argv)

tray_icon = QSystemTrayIcon(QIcon('assets/default.ico'), parent=app)
tray_icon.setToolTip('Click to change mode: image search, reverse image search')
tray_icon.show()

app.exec()

# TODO: implement keyboard shortcuts