from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import base64
import urllib.parse

# Initialize the Chrome driver
driver = webdriver.Chrome()

# URL of the webpage
url = "https://astro-charts.com/tools/birth_chart/?name=Sabrina+Shields&location=Baltimore%2C+Maryland%2C+United+States&geo_pk=595&date=1987-11-24+9-17&place=Baltimore%2C+Maryland%2C+United+States&newchart=ctrue&month=11&day=24&year=1987&hour=09&min=17&timeRadio=am"

# Navigate to the desired webpage
driver.get(url)

# Maximize the window (to ensure all elements are visible)
driver.maximize_window()

# Extract the name from the URL
parsed_url = urllib.parse.urlparse(url)
parsed_qs = urllib.parse.parse_qs(parsed_url.query)
name = parsed_qs.get('name', [None])[0]

# Ensure the name is not None and remove special characters for file naming
if name:
    sanitized_name = ''.join(e for e in name if e.isalnum())
else:
    sanitized_name = "Unknown"

# Wait for the user command to take a screenshot
input("Press Enter when you are ready to take a screenshot...")

# Save the content as a PNG
screenshot_name = f'ChartPage_{sanitized_name}.png'
driver.save_screenshot(screenshot_name)

# Close the browser
driver.quit()

print(f"PNG saved as {screenshot_name}")

