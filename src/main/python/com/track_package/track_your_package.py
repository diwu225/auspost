from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def track_a_parcel():
    browser= webdriver.Firefox()
    browser.get("https://auspost.com.au/mypost/track/search")
    tracking_number_field= browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div/input")
    tracking_number_field.click()
    tracking_number_field.send_keys("11111111111111")
    track_button= browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div/button")
    track_button.click()

track_a_parcel()