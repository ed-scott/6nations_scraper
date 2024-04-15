from dotenv import load_dotenv
import os
import undetected_chromedriver as uc
import time 
from selenium.webdriver.common.by import By
load_dotenv()

email_input_id = os.getenv("EMAIL")
password_input_id = os.getenv("PASSWORD")
sign_in_url = "https://account.sixnationsrugby.com/en/sign-in"

# Setup headless browser
chromeOptions = uc.ChromeOptions() 
chromeOptions.headless = True
driver = uc.Chrome(use_subprocess=True, options=chromeOptions) 
driver.get(sign_in_url)
time.sleep(3) # To let the login page load.

# Send username and password into various boxes
uname = driver.find_element(By.ID, ":R1ial9ltsrqla:") 
uname.send_keys(email_input_id)
pword = driver.find_element(By.ID, "password")
pword.send_keys(password_input_id)
button = driver.find_element(By.ID, ":R4ial9ltsrqla:")
button.click()
time.sleep(3)
driver_logs = driver.get_log("driver")
browser_logs = driver.get_log("browser")

#find the button-play button and click it
driver.get("https://fantasy.sixnationsrugby.com/")
time.sleep(3)
button_play = driver.find_element(By.XPATH("//button-play")).get_attribute("innerHTML")
button_play.click()
time.sleep(5)

# Get the first match in question
driver.get("https://fantasy.sixnationsrugby.com/m6n/#/game/play/me")

time.sleep(5)