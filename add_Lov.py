from libraries import *
from passwords import *
import pdb

#Initialize the webdriver and install according to the system
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
url = ""
driver.get(url)
driver.maximize_window()

#Encoded password used
u_name = encoded_password(user_name)
pwd = encoded_password(password)
deco_uname = decoded_password(u_name)
deco_pwd = decoded_password(pwd)
deco_uname = instances(deco_uname)
deco_pwd = instances(deco_pwd)

#Values added to Admin-Panel
data_value = 'Retailer_type_lov'
display_value = 'Retailer_type_lov'
description = "Lov's added for search filter in retailer management page"
existense = 0

#Login Section
try:
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'mat-typography'))
    )
    user_name = driver.find_element(By.XPATH,'//*[@id="mat-input-0"]').send_keys(deco_uname)
    passw = driver.find_element(By.XPATH,'//*[@id="mat-input-1"]').send_keys(deco_pwd)
    button = driver.find_element(By.XPATH,'/html/body/app-root/app-account-layout/div/app-login/form/div/div/div/div/div/div[2]/div/button').click()
    print("Page Login successful")

except:
    print("Page Login Unsuccessful")

#Perform action through Xpath
driver.implicitly_wait(5)
adm_btn = driver.find_element(By.XPATH,'//*[@id="navbarCollapse"]/div/div/div[1]/a[1]').click()
lov_btn = driver.find_element(By.XPATH,'//*[@id="mat-menu-panel-0"]/div/div[4]/div/button').click()
lov_btn1 = driver.find_element(By.XPATH,"//mat-icon[contains(text(), 'chevron_right')]").click()
add_btn = driver.find_element(By.XPATH,"//mat-icon[contains(text(),'add')]").click()
lov_list = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/app-lov-add/mat-dialog-content/form/div/div/div/div/mat-form-field[1]/div").click()
element = driver.find_element(By.XPATH, '//*[@id="mat-option-125"]/span')
# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView(true);", element)
element.click()

input_datav = driver.find_element(By.XPATH,'//*[@id="mat-input-3"]')
input_dispv = driver.find_element(By.XPATH,'//*[@id="mat-input-4"]')
input_desc = driver.find_element(By.XPATH,'//*[@id="mat-input-5"]')

input_datav.send_keys(data_value)
input_dispv.send_keys(display_value)
input_desc.send_keys(description)

save_btn = driver.find_element(By.XPATH,"//mat-icon[contains(text(),'save')]")
save_btn.click()

#Incase of duplicate values
try:
    message = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "ajs-message"), "IS ALREADY EXIST.")
    )
    if message:
        existense = existense + 1

except Exception as e:
    print("No visible alert message was captured or it disappeared too quickly.")


if existense > 0:
    reponses = []
    new_questions = [
        "Enter new Data Value to insert",
        "Enter new Display Value to insert",
        "Enter new Description"]
            
    for question in new_questions:
        reponse = input(question + " ")
        reponses.append(reponse)
    
    data_value = reponses[0]
    display_value = reponses[1] 
    description = reponses[2]

    input_datav.clear() ; input_datav.send_keys(data_value)
    input_dispv.clear() ; input_dispv.send_keys(display_value)
    input_desc.clear() ; input_desc.send_keys(description)
    save_btn.click()



    
# driver.quit()