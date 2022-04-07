import time
import winsound
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()    # Maximizing the window
driver.implicitly_wait(5)   # Waits until the element is present


def availability_check():
    """
     This function takes a user defined restaurant url as input
        Returns:
            if it's busy , in this case it will keep checking until
            it's available
            if it's Open , in this case it will make a beep sound
            if it's Closed
    """
    driver.get(input("Enter the Desired restaurant url : "))  # Takes the user url
    busy = True
    repeat = None
    while busy:
        # Checks if the restaurant is busy
        if driver.find_element(By.XPATH, '//*[@class="col-4 f-15-m rest-status"]').text == "Busy":
            driver.refresh()
            time.sleep(10)
            if repeat != 0:
                print("The Restaurant is Busy")
                repeat = 0
        # Checks if the restaurant is Closed
        if driver.find_element(By.XPATH, '//*[@class="col-4 f-15-m rest-status"]').text == "Closed":
            print("The Restaurant is Closed")
            break
        # Checks if the restaurant is Opened/available
        if driver.find_element(By.XPATH, '//*[@class="col-4 f-15-m rest-status"]').text == "OPEN":
            busy = False
            duration = 3000  # milliseconds
            freq = 500  # Hz
            winsound.Beep(freq, duration)  # Beep sound with a specific frequency and duration
            print("You can order now,The Restaurant service is available")


if __name__ == '__main__':
    availability_check()
