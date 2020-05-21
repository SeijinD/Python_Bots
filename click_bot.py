from selenium import webdriver
import sys
from time import sleep
import time

def main():
    driver = webdriver.Firefox(executable_path="C:\\Python\\Tools\\geckodriver.exe")

    driver.get("https://clickspeedtest.com")
    sleep(7)

    t_end = time.time() + 60 * 5
    try:
        while time.time() < t_end:
            driver.find_element_by_id("clicker").click()
            sleep(0.001)
    except:
        print("It's OK!")


if __name__=="__main__":
    main()