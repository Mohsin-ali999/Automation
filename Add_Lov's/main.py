from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
url = ""
driver.get(url)
driver.maximize_window()

#Login section
try:
    WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.TAG_NAME,"body"))
    )
    print("Page loaded sucessfully now initializing Login")
    user_id = driver.find_element(By.XPATH,'//*[@id="PersonIDTextBox"]').send_keys('')
    password = driver.find_element(By.XPATH,'//*[@id="PasswordTextBox"]').send_keys('')
    radio_select = driver.find_element(By.XPATH,'//*[@id="LDAP"]').click()
    login = driver.find_element(By.XPATH,'//*[@id="LoginButton"]').click()
    print("Login Successful")

    print("Checking now the Customer Biometric")
    # cust_Bio = driver.find_elements(By.CLASS_NAME, "vertical-navs")
    # child_elements = cust_Bio.find_elements(By.XPATH, './*')

    # for element in child_elements:
    #     print(element)
    driver.implicitly_wait(3)
    cust_Bio = driver.find_element(By.XPATH,'//*[@id="mainMaster"]/div[2]/div[2]/div/div/div[2]/div/ul')
    items = cust_Bio.find_elements(By.TAG_NAME,"li")
    for list_item in items:
        text = list_item.text
        print(text)

except TimeoutError:
    print("The page didn't responded please check the URL")


  