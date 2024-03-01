import undetected_chromedriver as uc
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib

options = uc.ChromeOptions()
driver = uc.Chrome(options=options, version_main=122)
maxPage = 76

for page in range(26,maxPage):
    url = "https://www.petfinder.com/search/cats-for-adoption/us/fl/tampa/?page={}".format(page)

    driver.get(url)

    prev_height = -1
    max_scrolls = 1
    scroll_count = 0

    while scroll_count < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # give some time for new results to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height
        scroll_count += 1


    time.sleep(2)
    img_results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//img[contains(@class, 'petCard-media-img')]")))
    #img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")

    img_urls = []

    for img in img_results:
        img_urls.append(img.get_attribute('src'))

    folderPath = "C:/Users/jeger/grams/Cats/Pics/"

    print(len(img_urls))

    for i in range(50):
        try:
            urllib.request.urlretrieve(str(img_urls[i]), folderPath + "cat_{0}_{1}.jpg".format(page, i))
        except:
            continue

driver.quit()