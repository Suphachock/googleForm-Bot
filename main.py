import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://forms.gle/yMNuPnUAbnbE1SYM8")
wait = WebDriverWait(driver, 10)

# Loop for 100 times
for _ in range(100):
    time.sleep(0.5)
    driver.refresh()

    # ========================================================================================
    options = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[1]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[2]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[3]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[4]'
    ]
    q1 = random.choice(options)
    option_field = wait.until(EC.element_to_be_clickable((By.XPATH, q1)))
    option_field.click()

    # ========================================================================================
    options2 = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]'
    ]
    q2 = random.choice(options2)
    option_field2 = wait.until(EC.element_to_be_clickable((By.XPATH, q2)))
    option_field2.click()

    # ========================================================================================
    first_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    first_field.send_keys("John Doe")

    #  ================================== ปุ่มส่ง ===============================================
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')))
    submit_button.click()

