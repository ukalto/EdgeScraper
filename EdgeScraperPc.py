import time

from random_word import RandomWords
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, NoSuchWindowException
from datetime import date
import requests

r = RandomWords()
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument("--headless=new")
edge_options.add_argument("start-maximized")
edge_options.add_argument("user-data-dir=C:\\Users\\XYZ\\AppData\\Local\\Microsoft\\Edge\\User Data 1")
edge_options.add_argument("profile-directory=Default")
edge_browser = webdriver.Edge(options=edge_options)
edge_browser.get("https://www.bing.com/")


def already_finished_today():
    today = date.today().strftime("%Y-%m-%d")
    f = open("C:\\Users\\XYZ\\Desktop\\EdgeScraper\\tracking.txt").read().split("\n")
    for i in f:
        if i == today:
            return False
    return True


def check_gained_points():
    while True:
        try:
            time.sleep(2)
            edge_browser.find_element('xpath', '//*[@id="id_rh"]').click()
            edge_browser.switch_to.frame("bepfm")
            fp, sp = edge_browser.find_element('xpath', '//*[@id="modern-flyout"]/div/div[5]/div/div/div[1]/div/div').text.split('/')
            edge_browser.switch_to.default_content()
            return fp != sp
        except (NoSuchElementException, ElementNotInteractableException):
            continue


def main():
    try:
        if already_finished_today():
            while check_gained_points():
                try:
                    rw = r.get_random_word()
                    search_bar = edge_browser.find_element('xpath', '//*[@id="sb_form_q"]')
                    search_bar.clear()
                    search_bar.send_keys(rw)
                    search_bar.submit()
                    print(f"done {edge_browser.current_url}")
                except (NoSuchElementException, ElementNotInteractableException):
                    print("error")
            edge_browser.quit()
    except (requests.ConnectionError, requests.Timeout):
        print("Internet is off")
    except NoSuchWindowException:
        print("Browser was closed")
    except KeyboardInterrupt:
        print("Program was interrupted")


if __name__ == '__main__':
    main()
