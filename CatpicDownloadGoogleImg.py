import undetected_chromedriver as uc
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib

driver_path = "C:/Users/jeger/grams/Cats/chromedriver-win64/chromedriver.exe"

options = uc.ChromeOptions()
# options.add_argument("--user-data-dir=/Users/a970/Library/Application Support/Google/Chrome/Default")
# options.add_argument("--disable-extensions")
# options.add_argument('--disable-application-cache')
# options.add_argument('--disable-gpu')
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-setuid-sandbox")
# options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--headless")

driver = uc.Chrome(options=options, version_main=122)
#driver.minimize_window()

cat_list =[
    "orange",
    "black",
    "persian",
    "tabby",
    "tux",
    "blue",
    "calico"
]

cat_adj = [
    "cute",
    "mean",
    "baby",
    "sad",
    "happy"
]

for color in cat_list:
    for mood in cat_adj:
        url = "https://www.google.com/search?sca_esv=3020367edbd259b4&rlz=1C1CHBF_enUS867US867&sxsrf=ACQVn0-YG9BgqCPxXhaawjrJRCHVrofnUA:1708894359521&q={0}+cat+{1}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwij6IfKr8eEAxUlrYkEHVTtB3AQ0pQJegQIDBAB&biw=1920&bih=953".format(color,mood)

        driver.get(url)

        prev_height = -1
        max_scrolls = 5
        scroll_count = 0

        while scroll_count < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  # give some time for new results to load
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == prev_height:
                break
            prev_height = new_height
            scroll_count += 1


        time.sleep(5)
        img_results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//img[contains(@class, 'Q4LuWd')]")))
        #img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")

        img_urls = []

        for img in img_results:
            img_urls.append(img.get_attribute('src'))

        folderPath = "C:/Users/jeger/grams/Cats/Pics/"

        print(len(img_urls))

        for i in range(30):
            try:
                urllib.request.urlretrieve(str(img_urls[i]), folderPath + "cat_{0}_{1}_{2}.jpg".format(color, mood, i))
            except:
                continue

driver.quit()