from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from csv import writer

url = "https://ww3.readopm.com/"
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(url)

chapter_locator = driver.find_elements(By.CSS_SELECTOR, ".no-border-x > tr > td:nth-child(1)")
date_locator = driver.find_elements(By.CSS_SELECTOR, ".no-border-x > tr > td:nth-child(2)")
link_locator = driver.find_elements(By.XPATH, "//tbody/tr/td[3]/div/a")

with open ('opm.csv', 'w', encoding='utf8', newline='') as f:
  thewriter = writer(f)
  header = ['Chapter name', 'Release date', 'Chapter link']
  thewriter.writerow(header)
  
  for row in range(len(chapter_locator)):
    info = [chapter_locator[row].text, date_locator[row].text, link_locator[row].get_attribute("href")]
    thewriter.writerow(info)