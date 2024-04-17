from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

def logout():
    browser = webdriver.Firefox()
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

