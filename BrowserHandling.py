import cv2
from selenium import webdriver
import time
import datetime
import os
import ChessOpening


def start_browser(pgn_string, half_moves_amount, start_time):
    # pgn_file_path = os.path.join(os.getcwd(), "ECO PGN", "eco.pgn")
    # chess_openings = ChessOpening.load_chess_openings(pgn_file_path)
    # chess_opening = chess_openings[1463]

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

    # sleep until start time
    time.sleep((start_time - datetime.datetime.now()).total_seconds())

    # start iterating over moves
    time.sleep(2.5)
    for i in range(0, half_moves_amount):
        start_time = datetime.datetime.now()
        next_button.click()
        time.sleep(max(2.5 - (datetime.datetime.now() - start_time).total_seconds(), 0))

    time.sleep(5)
    driver.close()






