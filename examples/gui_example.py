from pythontools.gui import gui

app = gui.App()
dialog = gui.Dialog("Example Gui", 480, 270)
dialog.show()
app.setSysExitOperationToAppExit()