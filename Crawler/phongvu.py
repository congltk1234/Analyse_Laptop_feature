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




csv_columns = ['Product','Price','Brand','Core','RAM','ScrSize','GraphicCard','Drive_Type','Capacity','OperSystem','Weight','Madein', 'Since','Shop','URL']
browser = webdriver.Chrome(executable_path="chromedriver.exe")
links = ['https://phongvu.vn/apple-scat.01-N004-03', 'https://phongvu.vn/laptop-macbook-scat.01-N001?sellerCategoryId=01-N001&page=1','https://phongvu.vn/laptop-macbook-scat.01-N001?sellerCategoryId=01-N001&page=2','https://phongvu.vn/laptop-macbook-scat.01-N001?sellerCategoryId=01-N001&page=3']

product_links=[]
for url in links: 
    browser.get(url)
    sleep(3)
    a = browser.find_elements_by_xpath('//*[@class="css-cbrxda"]')  # Vị trí chứa đường dẫn sản phẩm
    for i in a:
        link=i.get_attribute("href")   # Lấy đường dẫn và thêm vào list  
        product_links.append(link)

for link in product_links:
    browser.get(link)
    try:   
        ram=browser.find_element_by_xpath('//*[@id="__next"]/div[4]/div/div/div[4]/div[2]/div[2]/div[10]/div[2]').text
        ram = re.sub(r'x', '*', ram[:6])
        ram = re.findall(r'(\d.*\d)',ram)
        scr = browser.find_element_by_xpath('//*[@id="__next"]/div[4]/div/div/div[4]/div[2]/div[2]/div[11]/div[2]').text
        scr = re.findall(r'(.*")',scr)
        capacity=browser.find_element_by_xpath('//*[@id="__next"]/div[4]/div/div/div[4]/div[2]/div[2]/div[12]/div[2]').text
        
        weight = browser.find_element_by_xpath('//*[@id="__next"]/div[4]/div/div/div[4]/div[2]/div[2]/div[21]/div[2]').text
        if 'TB' in capacity:
            capacity = 1000*convert(capacity)
        else:
            capacity = convert(capacity[:6])
        brand = browser.find_element_by_xpath('//*[@id="__next"]/div[4]/div/div/div[4]/div[2]/div[2]/div[1]/div[2]').text
        if 'APPLE' in brand:
            opsys = 'Mac OS'
            brand = 'Apple'
        else:
            opsys = 'Window'
        data = {
                "Product" : browser.find_element_by_xpath('//*[@class="css-4kh4rf"]').text,
                "Price" : convert(browser.find_element_by_xpath('//*[@class="css-awj0nj"]').text),
                "Brand" : brand,
                "Core" : browser.find_element_by_xpath('//*[@id="__next"]/div[4]/div/div/div[4]/div[2]/div[2]/div[8]/div[2]').text,
                "RAM" : eval(ram.pop()),
                "ScrSize" : scr.pop(),
                "GraphicCard" : browser.find_element_by_xpath('//*[@id="__next"]/div[4]/div/div/div[4]/div[2]/div[2]/div[9]/div[2]').text,
                "Drive_Type" : 'SDD',
                "Capacity" : capacity,
                "OperSystem" : opsys,
                "Weight" : re.sub(r'(?: kg)','',weight),
                "Madein" : "",
                "Since" : "",
                "Shop": 'Phongvu',
                "URL":link,
                } 
        with open('data.csv', "a", encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writerow(data)
    except:
        pass

browser.close()