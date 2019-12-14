from pythontools.webbot import webbot
import time

# Google Chrome
browser = webbot.WebBot().Chrome(chromedriver="chromedriver.exe")
# Firefox
browser.get("https://www.google.com/")
browser = webbot.WebBot().Firefox(geckodriver="geckodriver.exe")

browser.input('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input', "what is python?")
browser.click('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')

time.sleep(10)

browser.close()
