from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import subprocess

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.laptopsdirect.co.uk/ct/laptops-and-netbooks/laptops"
driver.get(url)
# driver.implicitly_wait(10)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

products = soup.find_all('div', class_="OfferBox")

with open('file.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Information', 'Availability'])

    for product in products:
        print("------------------------------------------")

        product_name = product.find('a', class_="offerboxtitle").text
        print(product_name)

        product_price = product.find('span', class_="offerprice").text.strip()
        print(f'{product_price}')

        product_information = []
        product_info = product.find('div', class_="productInfo").find('ul').find_all('li')
        for i in product_info:
            product_information.append(i.text.strip())
            print(i.text)

        product_availability = product.find('span', class_="stockText").find('span').text
        print(product_availability)

        writer.writerow([product_name, product_price, ', '.join(product_information), product_availability])

# Close the webdriver
driver.quit()

subprocess.run(["python", "PROD_SD_05_DISPLAY.py"], check=True)
