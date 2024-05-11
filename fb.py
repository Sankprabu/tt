import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colored import fg, attr

def FacebookLogin():
    try:
        # Baca email dan password dari file akun.txt
        with open('akun.txt', 'r') as file:
            email, password = file.readline().strip().split(',')

        # Inisialisasi WebDriver dengan Firefox
        driver = webdriver.Firefox()

        # Buka halaman login Facebook Mobile
        driver.get('https://m.facebook.com/login/')

        # Temukan kotak email dan masukkan email
        email_box = driver.find_element_by_name('email')
        email_box.send_keys(email)

        # Temukan kotak sandi dan masukkan sandi
        pass_box = driver.find_element_by_name('pass')
        pass_box.send_keys(password)

        # Klik tombol login
        login_button = driver.find_element_by_name('login')
        login_button.click()

        # Tunggu beberapa saat untuk proses login
        time.sleep(5)

        # Periksa apakah login berhasil dengan melihat URL
        if "login_attempt" not in driver.current_url:
            print("Login Successful")
        else:
            print("Login Failed")

        # Tutup browser
        driver.quit()

    except FileNotFoundError:
        print(f"{fg('red_1')}File 'akun.txt' not found.{attr('reset')}")
    except ValueError:
        print(f"{fg('red_1')}Invalid format in 'akun.txt'. Make sure email and password are separated by a comma.{attr('reset')}")
    except Exception as e:
        print(f"{fg('red_1')}Failed to execute script: {e}{attr('reset')}")

FacebookLogin()
