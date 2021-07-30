from selenium import webdriver
import time
import datetime


def start_browser(pgn_string, half_moves_amount, start_time):
    driver = webdriver.Chrome("chromedriver.exe")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.get("http://lichess.org/paste")
    time.sleep(1)

    search_field = driver.find_element_by_id("form3-pgn")
    search_field.send_keys(pgn_string)
    search_field.submit()

    time.sleep(1)

    toggle_button = driver.find_element_by_class_name("switch")
    toggle_button.click()

    next_button = driver.find_element_by_xpath("/html/body/div/main/div[3]/div[2]/button[3]")

    time.sleep((start_time - datetime.datetime.now()).total_seconds())

    time.sleep(2.5)

    for i in range(0, half_moves_amount):
        start_time = datetime.datetime.now()
        next_button.click()
        time.sleep(max(2.5 - (datetime.datetime.now() - start_time).total_seconds(), 0))

    time.sleep(5)# 5 default
    driver.quit()






