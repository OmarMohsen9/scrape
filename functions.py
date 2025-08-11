from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_and_launch_chrome(wait):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(wait)
    return driver


def web_goto(driver,url):
    driver.get(url)
    return driver


def verify_title(drivers,title):
    ar_title = drivers.find_element(By.CSS_SELECTOR, 'div.page-title h2, h1, h2, h3, h4, h5, h6')
    print(ar_title.text)
    if ar_title.text == title:
        print("Pass Title check")
    else:
        print("Fail Title check")


def setup_select_tab(drivers,title):
    webelement = drivers.find_element(by=By.CLASS_NAME,value='level0')
    webelement.click()
    verify_title(drivers,title)
    webelement = drivers.find_element(by=By.XPATH,value='//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/select/option[2]')
    webelement.click()
    return drivers


def scrape_list(drivers,title):
    setup_select_tab(drivers,title)
    product_list = []
    unord_list = drivers.find_element(by=By.XPATH, value='//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul') #enter unordered list
    list_items = unord_list.find_elements(by=By.TAG_NAME, value='li') # find all elements in unordered list
    for i in list_items:
        a_tag = i.find_element(by=By.TAG_NAME, value='a')
        items = a_tag.get_attribute('title')
        if items != '':
            product_list.append(items)
    return product_list


def check_prices(drivers):
    webelement = drivers.find_element(by=By.ID, value='product-price-1')
    mobile_inlist_price=webelement.text
    webelement = drivers.find_element(by=By.XPATH, value='//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[3]/div/h2/a')
    webelement.click()
    webelement= drivers.find_element(by=By.CSS_SELECTOR, value='span.price')
    mobile_inpage_price = webelement.text
    if mobile_inlist_price == mobile_inpage_price:
        print("Same Price")
    else:
        print("different Price")
    return drivers
