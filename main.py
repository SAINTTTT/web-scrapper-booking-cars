from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
import os

chrome_service = Service(ChromeDriverManager().install())

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(service=chrome_service,options=options)
url = os.getenv("BOOKING_URL")
driver.get(url)
sleep(13)
""" soup = BeautifulSoup(driver.page_source, 'html.parser')
s = soup.find('div', class_='sc-b0eaf57-15 esCopK')
content = s.find_all('price') """

prices = driver.find_elements(By.CLASS_NAME, "price")
names = driver.find_elements(By.CLASS_NAME, "sc-b0eaf57-12.kviJWz")

PRICE_THRESHOLD = 1000
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
message = ""

print(TOKEN)

for i in range(len(names)):
    #print(f"{names[i].text}: ${prices[i].text}")
    value = int(prices[i].text.split()[1].replace(".", "")) 
    if value < PRICE_THRESHOLD:
        message += f"{names[i].text}: ${prices[i].text} \n"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {
    "chat_id": CHAT_ID,
    "text": message 
}
        
response = requests.post(url, data=params)
print(response.status_code)
print(response.json())


driver.quit()
