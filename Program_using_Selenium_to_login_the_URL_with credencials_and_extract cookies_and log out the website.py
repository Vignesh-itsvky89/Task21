import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
paths = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
username = driver.find_element(By.ID,"user-name")
time.sleep(4)
username.click()
time.sleep(2)
username.send_keys("standard_user")
time.sleep(4)
password = driver.find_element(By.ID, "password")
password.click()
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)
time.sleep(2)
mycookies = driver.get_cookies()
print("Cookies created before login:",len(mycookies))
print("Cookies created before login", mycookies)
login = driver.find_element(By.ID, "login-button")
login.click()
mycookies = driver.get_cookies()
print("Cookies created after login:",len(mycookies))
print("Cookies created after login", mycookies)
button = driver.find_element(By.ID, "react-burger-menu-btn")
button.click()
time.sleep(3)
driver.find_element(By.ID, 'logout_sidebar_link').click()