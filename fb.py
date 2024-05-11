import time
import requests
from bs4 import BeautifulSoup
from colored import fg, attr

def FacebookLogin():
    try:
        # Baca email dan password dari file akun.txt
        with open('akun.txt', 'r') as file:
            email, password = file.readline().strip().split(',')

        # Membuat sesi HTTP
        session = requests.Session()

        # Membuka halaman login Facebook Mobile
        response = session.get('https://m.facebook.com/')
        print(f"{fg('yellow_1')}Facebook Mobile Opened!{attr('reset')}")

        # Parsing HTML menggunakan BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Temukan kotak email dan masukkan email
        email_input = soup.find('input', {'type': 'email'})
        email_id = email_input['id']
        login_data = {email_id: email}

        # Temukan kotak sandi dan masukkan sandi
        pass_input = soup.find('input', {'type': 'password'})
        pass_id = pass_input['id']
        login_data[pass_id] = password

        # Temukan tombol login dan kirim data login
        form = soup.find('form', {'method': 'post'})
        login_url = form['action']
        response = session.post(login_url, data=login_data)

        # Periksa apakah login berhasil
        if 'home.php' in response.url:
            print("Login Successful")
        else:
            print("Login Failed")

    except FileNotFoundError:
        print(f"{fg('red_1')}File 'akun.txt' not found.{attr('reset')}")
    except ValueError:
        print(f"{fg('red_1')}Invalid format in 'akun.txt'. Make sure email and password are separated by a comma.{attr('reset')}")
    except Exception as e:
        print(f"{fg('red_1')}Failed to execute script: {e}{attr('reset')}")

FacebookLogin()
