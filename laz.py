from selenium import webdriver

# URL login mobile Facebook
facebook_mobile_login_url = 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8'

# Baca email dan password dari file akun.txt
with open('akun.txt', 'r') as file:
    credentials = file.readline().strip().split(',')  # Membaca satu baris, memisahkan email dan password dengan koma
    email = credentials[0]  # Mengambil email
    password = credentials[1]  # Mengambil password

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize Chrome WebDriver with ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Facebook login page
driver.get(facebook_mobile_login_url)

# Find username and password fields and login button
username_field = driver.find_element_by_name('email')
password_field = driver.find_element_by_name('pass')
login_button = driver.find_element_by_name('login')

# Input username and password
username_field.send_keys(email)
password_field.send_keys(password)

# Click login button
login_button.click()

# Wait for the login process to complete
driver.implicitly_wait(10)

# Check if login was successful
if 'm.facebook.com' in driver.current_url:
    print("Login berhasil!")
else:
    print("Gagal login.")

# Your further automation steps can be added here, such as navigating to other pages or interacting with elements.
# For example:
# driver.get('https://m.facebook.com/your_desired_page')

# Don't forget to close the WebDriver after you finish
# driver.quit()
