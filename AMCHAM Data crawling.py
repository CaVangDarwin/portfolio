from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

options = webdriver.ChromeOptions()

prefs = {'download.default_directory': r'C:\Users\Savvycom\Desktop\haha'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options)

driver.get('https://accthailand.chambermaster.com/Login/?ReturnUrl=%2fmic%2fmembers%2flogin')

username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'UserName'))
)

username_input.send_keys('Enter provided username')

password_input = driver.find_element(By.ID, 'Password')
password_input.send_keys('Enter pasword')

login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @name='Submit' and @value='Sign In' and contains(@class, 'button') and contains(@class, 'basicBtn')]")
login_button.click()
time.sleep(10) 

WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'directorySearchForm')))

vcf_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.vcf')]")
for link in vcf_links:
    vcf_url = link.get_attribute("href")
    vcf_filename = os.path.basename(vcf_url)
    print(f"Downloading file: {vcf_filename}")
    driver.get(vcf_url)
    time.sleep(1)  

driver.quit()
