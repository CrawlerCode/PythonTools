from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import sys, base64


class App(object):

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyleSheet("QMainWindow { border: 1px solid #242424; }")

    def setIcon(self, b64):
        icon = QtGui.QIcon()
        pm = QtGui.QPixmap()
        pm.loadFromData(base64.b64decode(b64))
        icon.addPixmap(pm)
        self.app.setWindowIcon(icon)
        return self

    def setDarkStyle(self):
        css = """
            QMainWindow { 
                background-color: #363636;
            }

            QDialog { 
                background-color: #363636;
            }

            QLineEdit { 
                background-color: #363636; 
                color: #c2c2c2;
            }

            QPlainTextEdit {
                background-color: #363636; 
                color: #c2c2c2;
            }

            QListWidget {
                background-color: #363636;
                color: #c2c2c2;
            }

            QLabel {
                color: #c2c2c2;
            }

            QMenuBar {
                background-color: #141414;
                color: #c2c2c2;
            }

            QMenuBar::item::selected  {
                background-color: #3b3b3b;
            }

            QPushButton {
                background-color: #141414;
                color: #c2c2c2;
            }

            QPushButton::hover {
                background-color: #242424;
            }

            """
        self.app.setStyleSheet(css)
        return self

    def onClipboardChanged(self, function):
        self.app.clipboard().dataChanged.connect(lambda: function(self.getClipboard()))

    def setClipboard(self, text=None, files=None):
        data = QtCore.QMimeData()
        if text is not None:
            data.setText(text)
        if files is not None:
            urls = []
            for f in files:
                urls.append(QtCore.QUrl.fromLocalFile(f))
            data.setUrls(urls)
        self.app.clipboard().setMimeData(data)

    def getClipboard(self):
        return self.app.clipboard().text()

    def setSysExitOperationToAppExit(self):
        sys.exit(self.app.exec_())


class Onject:

    def __init__(self, window):
        self.window = window
        self.styles = []

    def setPosition(self, x, y):
        self.obj.move(x, y)
        return self

    def setSize(self, width, height):
        self.obj.setFixedSize(width, height)
        return self

    def setFont(self, name="Time", size=10, bold=False):
        self.obj.setFont(QtGui.QFont("Time", size, QtGui.QFont.Normal if bold is False else QtGui.QFont.Bold))
        return self

    def setColor(self, color):
        self.styles.append("color:" + color)
        self.obj.setStyleSheet(type(self.obj).__name__ + "{" + ";".join(self.styles) + "}")
        return self

    def setBackgroundColor(self, color):
        self.styles.append("background-color:" + color)
        self.obj.setStyleSheet(type(self.obj).__name__ + "{" + ";".join(self.styles) + "}")
        return self

    def setBorderRadius(self, radius):
        self.styles.append("border-radius:" + radius)
        self.obj.setStyleSheet(type(self.obj).__name__ + "{" + ";".join(self.styles) + "}")
        return self

    def setEnabled(self, bool):
        self.obj.setEnabled(bool)

    def hasFocus(self):
        return self.obj.hasFocus()


class TextEdit(Onject):

    def __init__(self, window):
        super(TextEdit, self).__init__(window)
        self.obj = QtWidgets.QPlainTextEdit(window.window)

    def setText(self, text):
        self.obj.insertPlainText(text)
        return self

    def getText(self):
        return self.obj.toPlainText()


class EditLine(Onject):

    def __init__(self, window):
        super(EditLine, self).__init__(window)
        self.obj = QtWidgets.QLineEdit(window.window)

    def setToPasswordField(self):
        self.obj.setEchoMode(QtWidgets.QLineEdit.Password)
        return self

    def setReadOnly(self, bool):
        self.obj.setReadOnly(bool)
        return self

    def setPlaceholderText(self, text):
        self.obj.setPlaceholderText(text)
        return self

    def setText(self, text):
        self.obj.setText(text)
        return self

    def onChange(self, on_change):
        self.obj.textChanged.connect(on_change)
        return self

    def onEnter(self, on_enter):
        self.obj.returnPressed.connect(on_enter)
        return self

    def getText(self):
        return self.obj.text()


class Label(Onject):

    def __init__(self, window):
        super(Label, self).__init__(window)
        self.obj = QtWidgets.QLabel(window.window)

    def setText(self, text):
        self.obj.setText(text)
        return self

    def getText(self):
        return self.obj.text()


class Button(Onject):

    def __init__(self, text, window):
        super(Button, self).__init__(window)
        self.obj = QtWidgets.QPushButton(text, window.window)

    def onClick(self, on_click):
        self.obj.clicked.connect(on_click)
        return self


class ListWidget(Onject):

    def __init__(self, window):
        super(ListWidget, self).__init__(window)
        self.obj = QtWidgets.QListWidget(window.window)
        self.obj.setContextMenuPolicy(Qt.CustomContextMenu)

    def setContextMenu(self, actions, openOnylIfItemSelected=True):
        def rightMenuShow():
            if openOnylIfItemSelected is False or self.getSelectedItem() is not None:
                menu = QtWidgets.QMenu(self.obj)
                for action in actions:
                    menu.addAction(action)
                menu.exec_(QtGui.QCursor.pos())

        self.obj.customContextMenuRequested[QtCore.QPoint].connect(rightMenuShow)
        return self

    def createContextMenuAction(self, name, function):
        return QtWidgets.QAction(name, self.obj, triggered=function)

    def addItem(self, text, icon=None, toolTip=None):
        item = QtWidgets.QListWidgetItem(text)
        item.text()
        if icon is not None:
            item.setIcon(icon)
        if toolTip is not None:
            item.setToolTip(toolTip)
        item.toolTip()
        self.obj.addItem(item)
        return self

    def removeItem(self, text, toolTip=None):
        for i in range(self.obj.count()):
            item = self.obj.item(i)
            if item.text() == text and (toolTip is None or item.toolTip() == toolTip):
                self.obj.takeItem(i)

    def getSelectedItem(self):
        try:
            return self.obj.selectedItems()[0].text()
        except:
            return None

    def setAcceptDrops(self, bool):
        self.obj.setAcceptDrops(bool)
        return self

    def onFileDragEvent(self, function):
        def dragMoveEvent(event):
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.CopyAction)
                event.accept()
            else:
                event.ignore()

        self.obj.dragMoveEvent = dragMoveEvent

        def dragEnterEvent(event):
            if event.mimeData().hasUrls:
                event.accept()
            else:
                event.ignore()

        self.obj.dragEnterEvent = dragEnterEvent

        def dropEvent(event):
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.CopyAction)
                event.accept()
                files = []
                for url in event.mimeData().urls():
                    files.append(str(url.toLocalFile()))
                function(files)
            else:
                event.ignore()

        self.obj.dropEvent = dropEvent
        return self

    def onDoubleClick(self, on_double_click):
        self.obj.itemDoubleClicked.connect(on_double_click)
        return self


class MenuBar:

    def __init__(self, window):
        self.window = window
        self.obj = window.window.menuBar()
        self.menues = {}
        self.on_clicks = {}

    def addMenu(self, name):
        menu = self.obj.addMenu(name)
        self.menues[name] = menu

        def triggered(e):
            _name = name + "." + e.text()
            if _name in self.on_clicks:
                self.on_clicks[_name]()

        menu.triggered[QtWidgets.QAction].connect(triggered)
        return self

    def addAction(self, menu, name, shortcut=None, on_click=None):
        action = QtWidgets.QAction(name, self.window.window)
        if shortcut is not None:
            action.setShortcut(shortcut)
        self.menues[menu].addAction(action)
        if on_click is not None:
            self.on_clicks[menu + "." + name] = on_click
        return self


class Window(object):

    def __init__(self, title, width, height):
        self.window = QtWidgets.QDialog(None)
        self.window.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.window.setWindowTitle(title)
        self.window.setFixedSize(width, height)

    def setPosition(self, x, y):
        self.window.move(x, y)
        return self
    
    def onClose(self, on_close):
        self.window.closeEvent = on_close
        return self

    def setTitle(self, title):
        self.window.setWindowTitle(title)
        return self

    def setAcceptDrops(self, bool):
        self.window.setAcceptDrops(bool)
        return self

    def setEnabled(self, bool):
        self.window.setEnabled(bool)

    def onKeyPress(self, function):
        def keyPressEvent(event):
            function(event.key())

        self.window.keyPressEvent = keyPressEvent
        return self

    def openFileDialog(self, name, file="", validFiles="All Files (*)"):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, name, file, validFiles, options=options)
        if fileName:
            return fileName
        return None

    def saveFileDialog(self, name, file="", validFiles="All Files (*)"):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self.window, name, file, validFiles, options=options)
        if fileName:
            return fileName
        return None

    def show(self):
        self.window.show()
        return self

    def hide(self):
        self.window.hide()
        return self

    def close(self):
        self.window.close()
        return self

class MainWindow(Window):

    def __init__(self, title, width, height):
        self.window = QtWidgets.QMainWindow(None)
        self.window.setWindowTitle(title)
        self.window.setFixedSize(width, height)

    def showMessage(self, text, duration=3000, color=None):
        self.window.statusBar().showMessage(text, duration)
        if color is not None:
            self.window.statusBar().setStyleSheet("QStatusBar { color: " + color + " }")
        return self

class SystemTray:

    def __init__(self, window):
        self.window = window
        self.tray = QtWidgets.QSystemTrayIcon(window.window)
        self.tray.setIcon(window.window.style().standardIcon(QtWidgets.QStyle.SP_ComputerIcon))

    def setIcon(self, b64):
        icon = QtGui.QIcon()
        pm = QtGui.QPixmap()
        pm.loadFromData(base64.b64decode(b64))
        icon.addPixmap(pm)
        self.tray.setIcon(icon)
        return self

    def setContextMenu(self, actions):
        menu = QtWidgets.QMenu()
        for action in actions:
            menu.addAction(action)
        self.tray.setContextMenu(menu)
        return self

    def createContextMenuAction(self, name, function):
        return QtWidgets.QAction(name, self.tray, triggered=function)

    def show(self):
        self.tray.show()
        return self

    def showMessage(self, title, message, duration=3000):
        self.tray.showMessage(title, message, QtWidgets.QSystemTrayIcon.Information, duration)
        return self