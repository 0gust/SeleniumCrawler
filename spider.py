from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

url = "https://ww3.readopm.com/"
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get(url)

""" chapter_locator = driver.find_elements(By.CSS_SELECTOR, ".no-border-x > tr > td:nth-child(1)")
for chapter in chapter_locator:
  print(chapter.text) """

""" date_locator = driver.find_elements(By.CSS_SELECTOR, ".no-border-x > tr > td:nth-child(2)")
for date in date_locator:  
  print(date.text) """

link_locator = driver.find_elements(By.XPATH, "//tbody/tr/td[3]/div/a")
for link in link_locator:
  print (link.get_attribute("href"))