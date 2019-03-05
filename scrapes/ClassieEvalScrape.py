import re
import credentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def login(site, userElement, passwordElement, submitElement):
    driver.get(site)
    username = driver.find_element_by_id(userElement)
    password = driver.find_element_by_id(passwordElement)
    username.send_keys(credentials.username)
    password.send_keys(credentials.password)
    submitBtn = driver.find_element_by_class_name(submitElement)
    submitBtn.click()
    
def departmentSearch(department):
    searchBox = driver.find_element_by_id("SearchKeyword")
    searchBox.send_keys(department)
    searchBox.submit()

def scrapeTeacherReviews():


options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install())
login("https://classie-evals.stonybrook.edu", "username", "password", "login-button");
departmentSearch("cse")
driver.quit()
