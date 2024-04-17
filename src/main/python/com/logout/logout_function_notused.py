from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait



browser = webdriver.Firefox()
browser.get("https://auspost.com.au")
#browser.find_element(By.ID, "lm480318-706350").click()
# Find the element to hover over
login_menu_hover_element = browser.find_element(By.ID, "skha480318-706350")

# Create an ActionChains object
action = ActionChains(browser)

# Move the mouse to hover over the element
action.move_to_element(login_menu_hover_element).perform()

#click on Mypost to take user to login page
button_move_to_loginpage = browser.find_element(By.ID,"login-options-0-476994-402204").click()

#applying wait to load the webpage completely
wait = WebDriverWait(browser, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "username")))
#Enter username
username = browser.find_element(By.NAME, "username").send_keys("diwakar225@gmail.com")

#Enter password
password = browser.find_element(By.NAME, "password").send_keys("Melbourne123@")

browser.get("https://auspost.com.au/mypost/dashboard/")

# Find the element to hover over
global_account_button = browser.find_element(By.ID, "global-account-btn")

# Create an ActionChains object
action = ActionChains(browser)

# Move the mouse to hover over the element
action.move_to_element(global_account_button).perform()

# click Logout
logout_button = browser.find_element(By.ID, "mypost-logout-link-desktop").click()

browser.close()


