# pip install random-word
# pip install selenium
# find edge-profile with "edge://version/"
# create copy of "User Data" profile if it doesn't work
import time

from random_word import RandomWords
from selenium import webdriver
from datetime import date

r = RandomWords()
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument("--headless=new")
edge_options.add_argument("start-maximized")
edge_options.add_argument("user-data-dir=C:\\Users\\XYZ\\AppData\\Local\\Microsoft\\Edge\\User Data 1")
edge_options.add_argument("profile-directory=Profile")
edge_browser = webdriver.Edge(options=edge_options)
edge_browser.get("https://www.bing.com/")


def start_up():
    today = date.today()
    f = open("C:\\Users\\XYZ\\Desktop\\EdgeScraper\\tracking.txt", "r")
    for i in f:
        if i == today.__str__():
            return False
    f.close()
    f = open("C:\\Users\\XYZ\\Desktop\\EdgeScraper\\tracking.txt", "a")
    f.write("\n" + today.__str__())
    f.close()
    return True


def check_gained_points():
    time.sleep(2)
    edge_browser.find_element('xpath', '//*[@id="id_rh"]').click()
    edge_browser.switch_to.frame("bepfm")
    fp, sp = edge_browser.find_element('xpath', '//*[@id="modern-flyout"]/div/div[5]/div/div/div[1]/div/div').text.split('/')
    edge_browser.switch_to.default_content()
    return fp != sp


if __name__ == '__main__':
    if start_up():
        while check_gained_points():
            try:
                rw = r.get_random_word()
                search_bar = edge_browser.find_element('xpath', '//*[@id="sb_form_q"]')
                search_bar.clear()
                search_bar.send_keys(rw)
                search_bar.submit()
                print(f"done {edge_browser.current_url}")
            except:
                print("error")
    edge_browser.quit()
