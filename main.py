# pip install random-word
# pip install selenium
# find edge-profile with "edge://version/"
# create copy of "User Data" profile if it doesn't work

from random_word import RandomWords
from selenium import webdriver

r = RandomWords()

if __name__ == '__main__':
    edge_options = webdriver.EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("start-maximized")
    edge_options.add_argument("user-data-dir=C:\\Users\\XYZ\\AppData\\Local\\Microsoft\\Edge\\User Data 1")
    edge_options.add_argument("profile-directory=Profile")
    edgeBrowser = webdriver.Edge(options=edge_options)
    edgeBrowser.get("https://www.bing.com/")

    for i in range(20):
        try:
            rw = r.get_random_word()
            search_bar = edgeBrowser.find_element('xpath', '//*[@id="sb_form_q"]')
            search_bar.clear()
            search_bar.send_keys(rw)
            search_bar.submit()
            print(f"done {edgeBrowser.current_url}")
        except:
            print("error")
    edgeBrowser.quit()
