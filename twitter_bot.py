from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from time import sleep

def main():
    driver = webdriver.Firefox(executable_path="C:\\Python\\Tools\\geckodriver.exe")

    while True:
        driver.get("https://twitter.com/login")
        sleep(7)

        print("Type Email: ")
        email = input()
        input_email = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
        for character in email:
                input_email.send_keys(character)
                sleep(0.05)
        
        print("Type password: ")
        password = input() 
        input_password = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
        for character in password:
                input_password.send_keys(character)
                sleep(0.05)

        # Click Login Button
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div").click()
        sleep(5)
        print("It's OK!")

        print("Type search: ")
        search = input()
        input_search = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")       
        for character in search:
                input_search.send_keys(character)
                sleep(0.05)
        input_search.send_keys(Keys.ENTER)
        print("Searcing...")
        sleep(5)
        print("It's finished!")
        break 

    number_post = 1
    the_page_source = driver.page_source

    # Error with Like.

    # Find Like
    for i in range (1,10,1):
        if the_page_source.find(driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div["+str(i)+"]"+"]/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div/div/svg")):
            print(i)
            number_post = i
            break
        else:
            print(i)
            continue
   
   # Start Loop Like
    while True:
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div["+str(number_post)+"]/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div/div/svg").click()
        sleep(2)
        print("Like It!")
        number_post += 1

if __name__=="__main__":
    main()