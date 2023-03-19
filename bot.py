from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv
try:
    date_to_Book=input("Enter the date you want to work and book :- ")
    month_to_book=input("Enter the present month in number :- ")
    family=input("Enter the Family name : - ")
    Firstname=input("Enter the First name : - ")
    Email_address=input("Enter the Email address : - ")
    phone_no=input("Enter the Phone no : - ")
    number_of_applicant=input("Enter the no of applicant (Number only) : - ")
    Purpose_of_travel=input("Enter the Purpose of travel : - ")
    Date_of_travel=input("Enter the Date of travel : - ")
    chrome_options =webdriver.ChromeOptions()
    s=Service(ChromeDriverManager().install())
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=s,options=chrome_options)
    wait=WebDriverWait(driver, 60)
    url='https://coubic.com/Embassy-of-Japan/948169/express?selected_slot=37243046'
    driver.get(url)

    # driver.execute_script("arguments[0].click();", date)
    slot_availability=False
    time_slots=['08:30-09:30','09:30-10:30']
    while(slot_availability==False):
        add_date = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='BooksTextButton_BooksTextButton__Gwq_G']")))
        add_date=driver.find_element(By.XPATH,"//button[@class='BooksTextButton_BooksTextButton__Gwq_G']")
        driver.execute_script("arguments[0].click();", add_date)
        time.sleep(10)
        date= wait.until(EC.element_to_be_clickable((By.XPATH,f"//button[@value='2022-{month_to_book}-{date_to_Book}']")))
        date=driver.find_element(By.XPATH,f"//button[@value='2022-{month_to_book}-{date_to_Book}']").click()
        driver.find_element(By.XPATH,f"//button[@value='2022-{month_to_book}-{date_to_Book}']").click()
        try:
         occupied=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='OutlineLabel_OutlineLabel__Q9Z6O BooksSelectTimeEvent_BooksSelectTimeEvent__Label__TBhi2 BooksSelectTimeEvent_isSoldOut__EnCbg']")))
         occupied1=driver.find_elements(By.XPATH,"//span[@class='OutlineLabel_OutlineLabel__Q9Z6O BooksSelectTimeEvent_BooksSelectTimeEvent__Label__TBhi2 BooksSelectTimeEvent_isSoldOut__EnCbg']")
        except:
            pass
        i=0
        while(i<2):
            occupied=occupied1[i] 
            if occupied:
                if(i==1):
                    driver.get(url)
                    
                pass
            else:
                slot_availability=True
                button_date_confirmation=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Add this date and time')]")))
                button_date_confirmation=driver.find_element(By.XPATH,"//button[contains(text(),'Add this date and time')]")
                driver.execute_script("arguments[0].click();", button_date_confirmation)
                input_boxes=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name]")))
                input_boxes=driver.find_elements(By.XPATH,"//input[@name]")
                family_box=input_boxes[0].send_keys(family)
                First_name_box=input_boxes[1].send_keys(Firstname)
                Email_address_box=input_boxes[2].send_keys(Email_address)
                phone_no_box=input_boxes[3].send_keys(phone_no)
                number_of_applicant_box=input_boxes[4].send_keys(number_of_applicant)
                Date_of_travel_box=input_boxes[5].send_keys(Date_of_travel)
                Purpose_of_travel_box=input_boxes[6].send_keys(Purpose_of_travel)
                Button_proceed_to_confirmation=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Proceed to confirmation')]")))
                Button_proceed_to_confirmation=driver.find_element(By.XPATH,"//button[contains(text(),'Proceed to confirmation')]")
                driver.execute_script("arguments[0].click();", Button_proceed_to_confirmation)
                Button_reserve=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Reserve')]")))
                Button_reserve=driver.find_element(By.XPATH,"//button[contains(text(),'Reserve')]")
                driver.execute_script("arguments[0].click();", Button_reserve)
                print(f"The appoint has been booked for date {date_to_Book} of time {time_slots[i]} ")
            i=i+1
except:
    print("Some problem  occurs run again or contact developer")
