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
        response = session.get('https://m.facebook.com/login/')

        # Parsing HTML menggunakan BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Temukan form login
        login_form = soup.find('form', {'method': 'post'})

        if login_form:
            # Temukan kotak email dan masukkan email
            email_input = login_form.find('input', {'type': 'email'})
            email_id = email_input['name']

            # Temukan kotak sandi dan masukkan sandi
            pass_input = login_form.find('input', {'type': 'password'})
            pass_id = pass_input['name']

            # Kirim data login
            login_data = {email_id: email, pass_id: password}
            response = session.post('https://m.facebook.com/login/', data=login_data)

            # Periksa apakah login berhasil
            if 'home.php' in response.url:
                print("Login Successful")
            else:
                print("Login Failed")
        else:
            print("Login form not found")

    except FileNotFoundError:
        print(f"{fg('red_1')}File 'akun.txt' not found.{attr('reset')}")
    except ValueError:
        print(f"{fg('red_1')}Invalid format in 'akun.txt'. Make sure email and password are separated by a comma.{attr('reset')}")
    except Exception as e:
        print(f"{fg('red_1')}Failed to execute script: {e}{attr('reset')}")

FacebookLogin()
