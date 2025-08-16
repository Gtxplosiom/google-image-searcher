from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow
from PyQt6.QtGui import QIcon
import sys
from modules import image_searcher

class WindowOverlay(QMainWindow):
    def __init__(self, image):
        super().__init__()
        self.image = image

        # overlay the image (screenshot) in the entire screen
        # baga pareho han win + shift + s
        # para ma selectan han area
        # this needs to be toplevel

    def select_area(self):
        image_area = ""
        return image_area

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mode = 0

        self.tray_icon = QSystemTrayIcon(QIcon('assets/default.ico'), parent=self.app)
        self.tray_icon.setToolTip('Click to change mode: image search, reverse image search')

        # populating menu
        self.menu = QMenu()
        self.close_option = self.menu.addAction('Close')

        # signal koneksiyon
        self.tray_icon.activated.connect(self.search)
        self.close_option.triggered.connect(self.close_app)

        self.tray_icon.setContextMenu(self.menu)

    def run_app(self):
        self.tray_icon.show()
        self.app.exec()

    def close_app(self):
        self.app.exit()

    def search(self):
        # 0 = reverse image search
        # 1 = image search
        if self.mode == 0:
            image = self.screenshot()

            window_overlay = WindowOverlay()
            image_area = window_overlay.select_area()

            links = image_searcher.reverse_image(image_area)
            self.show_results(links)
        else:
            query = self.search_prompt
            links = image_searcher.image_search(query)
            self.show_results(links)
    
    def search_prompt(self):
        query = ""
        return query

    def show_results(self, links):
        # idk what to do here yet
        pass
    
    def screenshot(self):
        image = ""
        return image

main_app = MainApp()
main_app.run_app()

# TODO: implement keyboard shortcuts