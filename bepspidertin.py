from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from csv import writer

url = "https://time.d74.it/login"
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get(url)

usertim = driver.find_element(By.NAME,"email")
passtim = driver.find_element(by.NAME, "password")
search = driver.find_element(By.NAME, "search")
customer = "IACCIO"

usertim.send_keys("ye00_tinbroker")
passtim.send_keys("}Ub3t9ke6=")
search = send_keys(customer)



polizza_f = driver.find_element(By.XPATH, "//*[@id='kt_content_container']/div/div[1]/div/div/div/div[1]/div/div/div[1]/div")

print(polizza_f)


