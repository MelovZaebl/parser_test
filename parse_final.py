from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = r"C:\Users\Melov\Desktop\parse\parse shkola\chromedriver.exe"
logs = open('log.txt', 'w', encoding='UTF-8')
links = []
ads = []
ads_info = []
driver = webdriver.Chrome(executable_path=path)
driver.get("https://youla.ru/login")

user_number = input('Введите номер ')
login_number = driver.find_element_by_name('phone')
login_number.send_keys(user_number)
login_number.send_keys(Keys.ENTER)

user_code = input('Введите код ')
login_code = driver.find_element_by_class_name('sc-oTaid')
login_code.send_keys(user_code)

time.sleep(2)

driver.get('https://youla.ru/sochi/rabota')

ads = driver.find_elements_by_xpath("//li[@class='product_item']//a")

for ad in ads:
    url = ad.get_attribute('href')
    link = {
        'href': url
    }
    links.append(link)

wait = WebDriverWait(driver, 5)

for button in links:
    driver.get(button['href'])
    # title = driver.find_element_by_class_name('sc-fznZeY').text
    # desc = driver.find_element_by_class_name('sc-fzowVh').text
    title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'sc-fznZeY'))).text
    desc = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'sc-fzowVh'))).text
    driver.find_element_by_class_name('dInOnW').click()
    time.sleep(2)
    phone = driver.find_element_by_partial_link_text('+7').text
    ads_info.append({
        'title': title,
        'desc': desc,
        'phone': phone,
    })
    for ad_info in ads_info:
        print(f'{ad_info["title"]}\n{ad_info["desc"]}\n{ad_info["phone"]}\n\n----------------------------------------------------------\n\n')
        logs.write(f'{ad_info["title"]}\n{ad_info["desc"]}\n{ad_info["phone"]}\n\n----------------------------------------------------------\n\n')
logs.close()