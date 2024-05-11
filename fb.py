import requests
from bs4 import BeautifulSoup

def login_to_facebook(email, password):
    # URL login mobile Facebook
    login_url = 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8'

    # Buat sesi HTTP menggunakan requests
    session = requests.Session()

    # Kirimkan permintaan GET untuk mendapatkan halaman login
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Temukan form login
    form = soup.find('form')

    # Temukan input untuk email dan password
    email_input = form.find('input', {'name': 'email'})
    password_input = form.find('input', {'name': 'pass'})
    login_button = form.find('button', {'type': 'submit'})

    # Set nilai email dan password
    email_input['value'] = email
    password_input['value'] = password

    # Kirimkan permintaan POST untuk login
    response = session.post(login_url, data={email_input['name']: email, password_input['name']: password})

    # Periksa apakah login berhasil
    if 'Logout' in response.text:
        print("Login berhasil!")
    else:
        print("Login gagal. Silakan periksa kembali email dan password Anda.")

# Baca informasi email dan password dari file akun.txt
with open('akun.txt', 'r') as file:
    email, password = file.readline().strip().split(',')

# Panggil fungsi login
login_to_facebook(email, password)
