from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import re
from time import sleep

def main():
    driver = webdriver.Firefox(executable_path="C:\\Python\\Tools\\geckodriver.exe")
    wait = WebDriverWait(driver, 10)

    while True:
        driver.get("https://play.typeracer.com")
        # driver.get("https://play.typeracer.com/?rt=27w907vmm3")

        sleep(5)
        while True:
            try:
                #Ctrl+Alt+I = Multi , Ctrl+Alt+O = Single , Ctrl+Alt+P = With Friends
                print("1->Multi , 2->Single , 3->With Friends , 4->Exit")
                anwser_1 = input()
                if anwser_1 == "1":
                    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL+Keys.ALT+'i')
                    break
                elif anwser_1 == "2":
                    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL+Keys.ALT+'o')
                    break
                elif anwser_1 == "3":
                    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL+Keys.ALT+'p')
                    break
                elif anwser_1 == "4":
                    driver.quit()
                    print("Exit!")
            except:
                continue

        sleep(5)
        if anwser_1 == "1":    
            sleep(10)  
            try: 
                path = '//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div'
                element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
                get_words = element.get_attribute('innerHTML')
                get_words = re.sub('<[^>]+>', '', get_words)
            except TimeoutException:
                print("Loading took too much time!")

            print(get_words)

            input_words = driver.find_element_by_class_name("txtInput")

            for character in get_words:
                input_words.send_keys(character)
                sleep(0.103)
            
        elif anwser_1 == "2":
            try: 
                path = '//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div'
                element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
                get_words = element.get_attribute('innerHTML')
                get_words = re.sub('<[^>]+>', '', get_words)
            except TimeoutException:
                print("Loading took too much time!")

            print(get_words)

            input_words = driver.find_element_by_class_name("txtInput")

            for character in get_words:
                input_words.send_keys(character)
                sleep(0.103)

        elif anwser_1 == "3":
            print("If you want to join race, type ok!")
            anwser_2 = input()
            if anwser_2 == "ok":
                driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL+Keys.ALT+'k')
                sleep(15)
                try: 
                    path = '//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div'
                    element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
                    get_words = element.get_attribute('innerHTML')
                    get_words = re.sub('<[^>]+>', '', get_words)
                except TimeoutException:
                    print("Loading took too much time!")

                print(get_words)

                input_words = driver.find_element_by_class_name("txtInput")

                for character in get_words:
                    input_words.send_keys(character)
                    sleep(0.105)
            
        print("Continiun...")
        sleep(10)
      
if __name__=="__main__":
    main()