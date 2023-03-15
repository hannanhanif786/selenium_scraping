from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

path = 'chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.yellowpages.ca/')

whatwho = driver.find_element(By.ID, 'whatwho')
whatwho.send_keys('Restaurants')

where = driver.find_element(By.ID, 'where')
where.send_keys('Range Road Ottawa ON')

search = driver.find_element(By.NAME,'search_button')
search.click()
time.sleep(3)

filename = "yellowpagedata.csv"
# with open(filename, 'w') as csvfile: 
#     csvwriter = csv.writer(csvfile)
#     fields = ['name', 'address', 'website', 'phone_no']
#     writer = csv.DictWriter(csvfile, fieldnames = fields) 
#     writer.writeheader() 

containers = driver.find_elements(By.CLASS_NAME, 'listing__content__wrapper')
resturant_names = []
for container in containers:
    try:
        name = container.find_element(By.TAG_NAME, 'h3').text
        print("name :",name)
        under_resturant = container.find_element(By.PARTIAL_LINK_TEXT, name)
        under_resturant.click()
        print("Done")
        resturant_name = driver.find_element(By.TAG_NAME,'h1').text
        # resturant_address = driver.find_element(By.TAG_NAME,'itemprop').text
        resturant_website = driver.find_element(By.PARTIAL_LINK_TEXT, 'Website').get_attribute('href')
        resturant_phone = driver.find_element(By.CSS_SELECTOR, 'li.mlr__submenu__item').text
        print('name :', resturant_name, ', address : ', ', website_url : ', resturant_website, ', phone : ',resturant_phone)
        # writer.writerow({'name': resturant_name, 'address': 'address', 'website':resturant_website, 'phone_no':resturant_phone})
        # csvfile.close()
        driver.back()
        print("Ok")
    except Exception as e:
        print("Exception : ",e)
        break

driver.quit()