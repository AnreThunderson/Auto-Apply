from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

#Type your Linkedin login informations here.
ACCOUNT_EMAIL = "henry.patrick.anderson@gmail.com"
ACCOUNT_PASSWORD = "henfart123"
PHONE_NUMBER = "8018099253"

#Change drive path area with yours path
driver = webdriver.Chrome(executable_path=r'C:\projects\chromedriver_win32\chromedriver.exe')


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3293222578&f_AL=true&keywords=")

driver.find_element(By.LINK_TEXT, "Sign in").click()

time.sleep(5)

email_field = driver.find_element(By.ID,"username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID,"password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

search_result_elements = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

for element in search_result_elements:
    try:
        time.sleep(10)
        element.click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()

        time.sleep(1)
        submit_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        if submit_btn.text == "Submit application":
            submit_btn.click()
    

        else:
            time.sleep(1)
            dismiss_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            dismiss_btn.click()

            time.sleep(1)
            discard_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal--layer-confirmation "
                                                              ".artdeco-modal__actionbar--confirm-dialog "
                                                              ".artdeco-button--primary")
            discard_btn.click()   

      

    except NoSuchElementException as e:
        pass

driver.quit()