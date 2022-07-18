
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://stackoverflow.com/")


print(driver.title)
search = driver.find_element_by_ID("s")
search.send_keys("home")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main")))

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
except:
    print("loading failed.")
    driver.quit()

driver.quit()
