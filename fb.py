import requests
from bs4 import BeautifulSoup

# URL login mobile Facebook
login_url = 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8'

# Baca informasi email dan password dari file akun.txt
with open('akun.txt', 'r') as file:
    email, password = file.readline().strip().split(',')

# Data yang diperlukan untuk login
data = {
    'email': email,
    'pass': password
}

# Buat sesi HTTP menggunakan requests
session = requests.Session()

# Kirimkan permintaan POST untuk login
response = session.post(login_url, data=data)

# Periksa apakah login berhasil
if 'Logout' in response.text:
    print("Login berhasil!")
else:
    print("Login gagal.")
