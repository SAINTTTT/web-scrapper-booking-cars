from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
url = ""
driver.get(url)
sleep(13)
""" soup = BeautifulSoup(driver.page_source, 'html.parser')
s = soup.find('div', class_='sc-b0eaf57-15 esCopK')
content = s.find_all('price') """

prices = driver.find_elements(By.CLASS_NAME, "price")
for price in prices:
    print(price.text)
driver.quit()