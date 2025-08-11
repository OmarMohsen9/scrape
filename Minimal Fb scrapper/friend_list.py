import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#import time
# Set up WebDriver
driver: WebDriver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#login
driver.get('https://www.facebook.com/')
z: WebElement = driver.find_element(by=By.ID,value='email')
z.send_keys('xxx@gmail.com') #enter scrapper email address
z: WebElement = driver.find_element(by=By.ID,value='pass')
z.send_keys('xxx')  #enter scrapper password
z: WebElement = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
z.click()
#time.sleep(30)

# Input friend list url of the profile you want to scrape example: https://www.facebook.com/zuck/friends
driver.get('xxx')

# Scroll to load more content (adjust the range depending on the content size)
for _ in range(15):  # Scroll 15 times, adjust as necessary
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to load


# Find profile links with both IDs and handlers
profile_links = driver.find_elements(by=By.XPATH,value="//a[contains(@href, 'profile.php?id=') or contains(@href, '/')]")

# Use a set to automatically handle duplicates
urls = set()

# Extract URLs
for link in profile_links:
    url = link.get_attribute('href')
    urls.add(url)

# Save to CSV
with open('profile_urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for url in sorted(urls):
        writer.writerow([url])


# Close the browser
driver.quit()
