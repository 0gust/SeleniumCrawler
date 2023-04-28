from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from csv import writer

url = "https://secure.fattureincloud.it/situation"

service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get(url)

userfat = driver.find_element(By.XPATH, "")
driver.find_element(By.id, "FattureeDocumenti").click()
driver.find_element(By.id, "Fatture").click()
driver.find_element(By.id, "new-doc-button").click()
