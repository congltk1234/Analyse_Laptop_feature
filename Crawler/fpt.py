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
url = 'https://fptshop.com.vn/may-tinh-xach-tay?sort=ban-chay-nhat&trang=10'


browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get(url)

links = browser.find_elements_by_xpath('//*[@class="cdt-product__info"]/h3/a')  # Vị trí chứa đường dẫn sản phẩm
for i in links:
    link=i.get_attribute("href")   # Lấy đường dẫn và thêm vào list
    product_links.append(link)
sleep(10)

csv_columns = ['Product','Price','Brand','Core','RAM','ScrSize','GraphicCard','Drive_Type','Capacity','OperSystem','Weight','Madein', 'Since','Shop','URL']

with open('data.csv', "a", encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=csv_columns)
    writer.writeheader()

for link in product_links:
    browser.get(link)
    try:
        if len(browser.find_elements_by_xpath ('//*[@class="st-pd-table"]/tbody/tr')) == 10 :
            scr=browser.find_element_by_xpath('//*[@class="st-pd-table"]/tbody/tr[3]/td[2]/span').text
            ram=browser.find_element_by_xpath('//*[@class="st-pd-table"]/tbody/tr[2]/td[2]/span').text
            capacity=convert(browser.find_element_by_xpath('//*[@class="st-pd-table"]/tbody/tr[5]/td[2]/span').text)
            if capacity <10:
                capacity = 1000
            brand = browser.find_element_by_xpath('//*[@id="root"]/main/div/div[1]/div[1]/div/ol/li[3]/a').text
            if 'Apple' in brand:
                opsys = 'Mac OS'
            else:
                opsys = 'Window'

            data = {
                "Product" : browser.find_element_by_xpath('//*[@class="st-name"]').text,
                "Price" : convert(browser.find_element_by_xpath('//*[@class="st-price-main"]').text),
                "Brand" : brand,
                "Core" : browser.find_element_by_xpath('//*[@class="st-pd-table"]/tbody/tr[1]/td[2]/span').text,
                "RAM" : convert(ram[:2]),
                "ScrSize" : scr[:4],
                "GraphicCard" : browser.find_element_by_xpath('//*[@class="st-pd-table"]/tbody/tr[4]/td[2]/span').text,
                "Drive_Type" : "SDD",
                "Capacity" : capacity,
                "OperSystem" : opsys,
                "Weight" : browser.find_element_by_xpath('//*[@class="st-pd-table"]/tbody/tr[7]/td[2]/span').text,
                "Madein" : browser.find_element_by_xpath('//*[@class="st-pd-table"]/tbody/tr[9]/td[2]/span').text,
                "Since" : browser.find_element_by_xpath('//*[@class="st-pd-table"]/tbody/tr[10]/td[2]/span').text,
                "Shop": 'FPTShop',
                "URL":link,
                } 
            with open('data.csv', "a", encoding="utf8") as f:
                writer = csv.DictWriter(f, fieldnames=csv_columns)
                writer.writerow(data)
                
        else:
            pass
    except:
        pass
browser.close()