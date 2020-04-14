import os, shutil

USERNAME = "CrawlerCode"
PASSWORD = ""

os.system('python setup.py sdist')
os.system('twine check .\dist\*')
os.system("twine upload --repository-url https://upload.pypi.org/legacy/ -u " + USERNAME + " -p " + PASSWORD + " .\dist\*")
shutil.rmtree("CrawlerCodePythonTools.egg-info", ignore_errors=True)
shutil.rmtree("CrawlerCodePythonTools_Gui.egg-info", ignore_errors=True)
shutil.rmtree("CrawlerCodePythonTools_WebBot.egg-info", ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)