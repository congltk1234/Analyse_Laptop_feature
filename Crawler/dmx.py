from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import csv
# Options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")


import re
#text_after = re.sub(regex_search_term, regex_replacement, text_before)
def convert(value):
    value = re.sub(r'\D', "",value)
    return int(value)



product_links = []
url = 'https://www.dienmayxanh.com/laptop#c=44&o=9&pi=10'


browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get(url)

links = browser.find_elements_by_xpath('//*[@class="main-contain"]')  # Vị trí chứa đường dẫn sản phẩm
for i in links:
    link=i.get_attribute("href")   # Lấy đường dẫn và thêm vào list
    product_links.append(link)
sleep(20)

csv_columns = ['Product','Price','Brand','Core','RAM','ScrSize','GraphicCard','Drive_Type','Capacity','OperSystem','Weight','Madein', 'Since','Shop','URL']


for link in product_links:
    browser.get(link)
    click_button = driver.find_element_by_xpath('//div[@class="ng-star-inserted"]//button[@class="text-center btn btn-link"]')
    click_button.click()
    time.sleep(5)
    try:   
        ram=convert(browser.find_element_by_xpath('//*[@class="parameter"]/ul/li[2]/div/span[1]').text)
        scr = browser.find_element_by_xpath('//*[@class="parameter"]/ul/li[4]/div/span[1]').text
        capacity=browser.find_element_by_xpath('//*[@class="parameter"]/ul/li[3]/div/span').text
        weight = re.sub(r'(?:Dài.* - Rộng.*Nặng )',"",browser.find_element_by_xpath('//*[@class="parameter"]/ul/li[10]/div/span').text)
        if 'TB' in capacity:
            capacity = 1000
        else:
            capacity = convert(capacity[:6])
        brand = browser.find_element_by_xpath('/html/body/section[1]/ul/li[2]/a').text
        if 'MacBook' in brand:
            opsys = 'Mac OS'
        else:
            opsys = 'Window'
                
        data = {
                "Product" : browser.find_element_by_xpath('/html/body/section[1]/h1').text,
                "Price" : convert(browser.find_element_by_xpath('//*[@class="giamsoc-ol-price"]').text),
                "Brand" : brand[7:],
                "Core" : browser.find_element_by_xpath('//*[@class="parameter"]/ul/li[1]/div').text,
                "RAM" : ram,
                "ScrSize" : re.sub(r'(?: ")', '', scr[:4]),
                "GraphicCard" : browser.find_element_by_xpath('//*[@class="parameter"]/ul/li[5]/div/span[2]').text,
                "Drive_Type" : 'SDD',
                "Capacity" : capacity,
                "OperSystem" : opsys,
                "Weight" : re.sub(r'(?: kg)','',weight),
                "Madein" : "",
                "Since" : browser.find_element_by_xpath('//*[@class="parameter"]/ul/li[11]/div/span').text,
                "Shop": 'Dienmayxanh',
                "URL":link,
                } 
        with open('data.csv', "a", encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writerow(data)
    except:
        pass


browser.close()