from random_word import RandomWords
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, NoSuchWindowException
from datetime import date
import requests

r = RandomWords()
mobile_emulation = {
    "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"
}
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument("--headless=new")
edge_options.add_argument("start-maximized")
edge_options.add_experimental_option("mobileEmulation", mobile_emulation)
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
            edge_browser.get("https://rewards.bing.com/status/")
            edge_browser.find_element('xpath', '//*[@id="earn-report-pointsbreakdown"]/span/ng-transclude').click()
            fp, sp = edge_browser.find_element('xpath', '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]') \
                .text.replace(" ", "").split('/')
            edge_browser.get("https://www.bing.com/")
            return fp != sp
        except (NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Couldn't find element {e}")
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
                except (NoSuchElementException, ElementNotInteractableException) as e:
                    print(f"error {e}")
            edge_browser.quit()
    except (requests.ConnectionError, requests.Timeout):
        print("Internet is off")
    except NoSuchWindowException:
        print("Browser was closed")
    except KeyboardInterrupt:
        print("Program was interrupted")


if __name__ == '__main__':
    main()
