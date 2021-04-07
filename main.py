import cv2
from selenium import webdriver
import time


driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("https://lichess.org/paste")



search_field = driver.find_element_by_id("form3-pgn")

search_field.send_keys("""[White "King's Indian"]
[Black "5.Nf3"]

1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Nf3""")

search_field.submit()

time.sleep(2)
toggle_button = driver.find_element_by_class_name("switch")
toggle_button.click()

for i in range(0, 5):
    next_button = driver.find_element_by_xpath("/html/body/div/main/div[3]/div[2]/button[3]")
    time.sleep(2.5)
    next_button.click()


print("ende")

