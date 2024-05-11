from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your webdriver
webdriver_path = '/path/to/chromedriver'

# URL login mobile Facebook
facebook_mobile_login_url = 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8'

# URL persetujuan GDPR Facebook
facebook_gdpr_consent_url = 'https://www.facebook.com/privacy/consent/gdp/?params%5Bapp_id%5D=1477455072510375&params%5Bdisplay%5D=%22popup%22&params%5Bdomain%5D=%22member.lazada.co.id%22&params%5Bfallback_redirect_uri%5D=%22https%3A%5C%2F%5C%2Fmember.lazada.co.id%5C%2Fuser%5C%2Flogin%22&params%5Bkid_directed_site%5D=false&params%5Blogger_id%5D=%22f8b3fe6beea9385ff%22&params%5Bnext%5D=%22read%22&params%5Bredirect_uri%5D=%22https%3A%5C%2F%5C%2Fstaticxx.facebook.com%5C%2Fx%5C%2Fconnect%5C%2Fxd_arbiter%5C%2F%3Fversion%3D46%23cb%3Df2d86afce2329c4cb%26domain%3Dmember.lazada.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%5Cu00253A%5Cu00252F%5Cu00252Fmember.lazada.co.id%5Cu00252Ff4b86e37557f11a34%26relation%3Dopener%26frame%3Dfe964710e45e37596%22&params%5Bresponse_type%5D=%22token%2Csigned_request%2Cgraph_domain%22&params%5Breturn_scopes%5D=true&params%5Bscope%5D=%5B%22email%22%5D&params%5Bsdk%5D=%22joey%22&params%5Bsteps%5D=%7B%22read%22%3A%5B%22email%22%2C%22baseline%22%2C%22public_profile%22%5D%7D&params%5Btp%5D=%22unspecified%22&params%5Bcui_gk%5D=%22%5BPASS%5D%3Alogin_platformization_joey%2Clogin_platformization_read%22&params%5Bis_limited_login_shim%5D=false&source=gdp_delegated'

# URL login Lazada dengan Facebook
lazada_login_url = 'https://member.lazada.co.id/user/login'

# Data akun Facebook
with open('akun.txt', 'r') as file:
    email, password = file.readline().strip().split()

# Start a new instance of Chrome browser
driver = webdriver.Chrome(webdriver_path)

try:
    # Login to Facebook
    driver.get(facebook_mobile_login_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'm_login_email')))
    email_field = driver.find_element_by_id('m_login_email')
    password_field = driver.find_element_by_id('m_login_password')
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.submit()

    # Wait for login to complete
    WebDriverWait(driver, 10).until(EC.url_contains("home.php"))

    print("Login to Facebook successful!")

    # Continue to Facebook GDPR consent
    driver.get(facebook_gdpr_consent_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'platformDialogForm')))
    continue_button = driver.find_element_by_xpath('//button[@name="__CONFIRM__"]')
    continue_button.click()

    # Wait for consent form to disappear
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.ID, 'platformDialogForm')))

    print("Consent accepted successfully!")

    # Continue to Lazada login page
    driver.get(lazada_login_url)

    # Wait for Lazada login form to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-form')))

    # Input your Lazada credentials if necessary
    # lazada_email_field = driver.find_element_by_id('login-email')
    # lazada_password_field = driver.find_element_by_id('login-password')
    # lazada_email_field.send_keys(lazada_email)
    # lazada_password_field.send_keys(lazada_password)
    # lazada_password_field.submit()

    print("Login to Lazada with Facebook successful!")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
