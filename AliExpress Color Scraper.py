from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Selenium webdriver
url = 'https://www.aliexpress.us/item/3256805502243536.html?spm=a2g0o.productlist.main.65.73529bae8V0vI7&algo_pvid=78de5aec-e178-4d02-bda7-f46b31696825&algo_exp_id=78de5aec-e178-4d02-bda7-f46b31696825-32&pdp_npi=4%40dis%21USD%2118.61%216.14%21%21%21135.61%21%21%40210321b416982969230891825ec064%2112000034016161690%21sea%21US%211706421191%21AC&curPageLogUid=v4MZ0bDgoS36'
options = webdriver.ChromeOptions()
options.add_argument('--headless')  
driver = webdriver.Chrome(options=options)
driver.get(url)

# Scroll down to load reviews 
for _ in range(5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

# Find and scrape the reviews
reviews = driver.find_elements(By.CLASS_NAME, 'ae-evaluateList-card-content')

if reviews:
    for review in reviews:
        print(review.text)

# Close the browser
driver.quit()
