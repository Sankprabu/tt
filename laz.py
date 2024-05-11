import getpass
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from colored import fg, attr

def FacebookLogin():
    try:
        # Baca email dan password dari file akun.txt
        with open('akun.txt', 'r') as file:
            email, password = file.readline().strip().split(',')

        # Initialize WebDriver
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # Opening Facebook.
        driver.get('https://www.facebook.com/')
        print(f"{fg('yellow_1')}Facebook Opened!{attr('reset')}")
        
        # Entering Email and Password
        username_box = driver.find_element(By.ID, 'email')
        username_box.send_keys(email)
        print(f"{fg('yellow_1')}Email entered{attr('reset')}")

        password_box = driver.find_element(By.ID, 'pass')
        password_box.send_keys(password)
        print(f"{fg('yellow_1')}Password entered{attr('reset')}")

        # Pressing The Login Button
        login_button = driver.find_element(By.ID, 'loginbutton')
        login_button.click()

        print("Done")
        input(f"{fg('green_1')}Press anything to quit{attr('reset')}")
        driver.quit()
        print(f"{fg('green_1')}Finished{attr('reset')}")

    except FileNotFoundError:
        print(f"{fg('red_1')}File 'akun.txt' not found.{attr('reset')}")
    except ValueError:
        print(f"{fg('red_1')}Invalid format in 'akun.txt'. Make sure email and password are separated by a comma.{attr('reset')}")
    except NoSuchElementException as e:
        print(f"{fg('red_1')}Failed to find element: {e}{attr('reset')}")
    except Exception as e:
        print(f"{fg('red_1')}Failed to execute script: {e}{attr('reset')}")

FacebookLogin()
