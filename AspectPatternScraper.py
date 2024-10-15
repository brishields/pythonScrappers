from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import base64
from urllib.parse import urlparse, parse_qs

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the desired webpage
url = "https://astro-charts.com/tools/birth_chart/?name=Sabrina+Shields&location=Baltimore%2C+Maryland%2C+United+States&geo_pk=595&date=1987-11-24+9-17&place=Baltimore%2C+Maryland%2C+United+States&newchart=ctrue&month=11&day=24&year=1987&hour=09&min=17&timeRadio=am"
driver.get(url)

# Extract name from the URL
parsed_url = urlparse(url)
parsed_qs = parse_qs(parsed_url.query)
name = parsed_qs.get("name", [None])[0]
if name:
    name = ''.join(name.split())  # Removing spaces

# List of IDs 
id_list = []
i = 0
while True:
    try:
        driver.find_element(By.ID, f"ap_{i}")
        id_list.append(f"ap_{i}")
        i += 1
    except:
        break

base_url = "https://astro-charts.com"

# Loop through each ID and save its content
for idx, element_id in enumerate(id_list):
    # Locate the div element by the current ID in the loop
    div_element = driver.find_element(By.ID, element_id)

    # Extract the direct SVG child of the current div
    svg_element = div_element.find_element(By.TAG_NAME, "svg")

    # Find all image tags inside the SVG
    image_elements = svg_element.find_elements(By.TAG_NAME, "image")

    # For each image tag, replace the href with the actual image data
    for img in image_elements:
        img_url = img.get_attribute("xlink:href") or img.get_attribute("href")
        
        # Check if the img_url is a relative path, and if so, prepend the base_url
        if not img_url.startswith('http'):
            img_url = base_url + img_url

        response = requests.get(img_url)
        if img_url.endswith('.svg'):
            base64_img = base64.b64encode(response.content).decode('utf-8')
            img_data = f"data:image/svg+xml;base64,{base64_img}"
        else:
            base64_img = base64.b64encode(response.content).decode('utf-8')
            img_data = f"data:image/png;base64,{base64_img}"
        
        # Setting the attribute
        driver.execute_script(f'arguments[0].setAttributeNS("http://www.w3.org/1999/xlink", "xlink:href", "{img_data}")', img)

    # Now get the SVG's outerHTML after the changes
    svg_content = svg_element.get_attribute('outerHTML')

    # Construct the filename based on the ID index
    filename = f"AspectPattern_{name}_{idx}.svg"

    # Save the SVG content to a file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)

    print(f"SVG saved as {filename}")

# Close the browser
driver.quit()
