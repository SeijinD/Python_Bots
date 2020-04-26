from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from time import sleep

def main():
    driver = webdriver.Firefox(executable_path="C:\\Python\\Tools\\geckodriver.exe")

    while True:
        driver.get("https://facebook.com")
        sleep(7)

        print("Type Email: ")
        email = input()
        input_email = driver.find_element_by_id("email")
        for character in email:
                input_email.send_keys(character)
                sleep(0.05)
        
        print("Type password: ")
        password = input() 
        input_password = driver.find_element_by_id("pass")
        for character in password:
                input_password.send_keys(character)
                sleep(0.05)

        # Click Login Button
        driver.find_element_by_id("u_0_b").click()
        sleep(5)
        print("It's OK!")
        break

        # Code For Search:
        # print("Type search: ")
        # search = input()
        # input_search = driver.find_element_by_xpath("")       
        # for character in search:
        #         input_search.send_keys(character)
        #         sleep(0.05)
        # input_search.send_keys(Keys.ENTER)
        # print("Searcing...")
        # sleep(5)
        # print("It's finished!")
        # break 

    number_post = 1
    # Loop Start Like
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[6]/div/div/div["+str(number_post)+"]/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div[2]/div/span[1]/div/div/a").click()
                                        # /html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[6]/div/div/div[3]                   /div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/form/div/div[2]/div/div[2]/div/span[1]/div/div/a
            sleep(3)
            print("Like It!")
            number_post += 1
        except:
            continue

if __name__=="__main__":
    main()