from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to your webdriver, e.g., chromedriver
webdriver_path = '/path/to/your/webdriver'

# Read email and password from a file
with open('akun.txt', 'r') as file:
    credentials = file.readline().strip().split()
    email = credentials[0]
    password = credentials[1]

# Start a new instance of Chrome browser
driver = webdriver.Chrome(webdriver_path)

# Open Facebook login page
driver.get('https://www.facebook.com')

# Wait for some time to let the page load
time.sleep(2)

# Find the email and password fields and enter your credentials
email_field = driver.find_element_by_id('email')
email_field.send_keys(email)

password_field = driver.find_element_by_id('pass')
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for some time to let the login process
time.sleep(5)

# Check if login was successful
if "home.php" in driver.current_url:
    print("Login to Facebook successful!")
    
    # Continue to Lazada login page
    driver.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=1477455072510375&kid_directed_site=0&app_id=1477455072510375&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.11%2Fdialog%2Foauth%3Fapp_id%3D1477455072510375%26cbt%3D1715363432845%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2aed753a3d6f5314%2526domain%253Dmember.lazada.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmember.lazada.co.id%25252Ff455cdd05777642bc%2526relation%253Dopener%26client_id%3D1477455072510375%26display%3Dpopup%26domain%3Dmember.lazada.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmember.lazada.co.id%252Fuser%252Flogin%26locale%3Den_US%26logger_id%3Dfc5b2ad95fff8efb5%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9efb38263a128539%2526domain%253Dmember.lazada.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmember.lazada.co.id%25252Ff455cdd05777642bc%2526relation%253Dopener%2526frame%253Dfcd9c12aff8026050%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.11%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9efb38263a128539%26domain%3Dmember.lazada.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmember.lazada.co.id%252Ff455cdd05777642bc%26relation%3Dopener%26frame%3Dfcd9c12aff8026050%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=id_ID&pl_dbl=0')
    time.sleep(2)
    
    # Check if login to Lazada with Facebook was successful
    if "dialog/oauth" in driver.current_url:
        print("Continue to Lazada login page successful!")
        # You need to locate and click the button to continue with Facebook login in Lazada page
        continue_facebook_button = driver.find_element_by_css_selector('button[name="login"]')
        continue_facebook_button.click()
        
        # Wait for some time to let the login process to Lazada with Facebook
        time.sleep(5)
        
        # Check if login to Lazada with Facebook was successful
        if "member.lazada.co.id/user/index" in driver.current_url:
            print("Login to Lazada with Facebook successful!")
        else:
            print("Login to Lazada with Facebook failed!")
    else:
        print("Continue to Lazada login page failed!")
else:
    print("Login to Facebook failed!")

# Close the browser
driver.quit()
