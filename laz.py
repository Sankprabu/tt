import json
import random
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

# URL login mobile Facebook
facebook_mobile_login_url = 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8'

# Path to your JSON file containing user-agents
user_agents_file = 'juragan.json'

# Check if juragan.json is empty or does not exist
if not os.path.exists(user_agents_file) or os.path.getsize(user_agents_file) == 0:
    # Generate random user-agent
    user_agent = UserAgent().random
else:
    # Read user-agents from JSON file
    with open(user_agents_file, 'r') as file:
        user_agents_data = json.load(file)
    
    # Randomly select a user-agent from the manual list
    user_agent = random.choice(user_agents_data['manual'])

# Set Chrome options with the chosen user-agent
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')

# Initialize Chrome WebDriver with the custom user-agent
driver = webdriver.Chrome(options=chrome_options)

# Open Facebook login page
driver.get(facebook_mobile_login_url)

# Your further automation steps can be added here, such as finding elements and interacting with them.
# For example:
# username_field = driver.find_element_by_name('email')
# password_field = driver.find_element_by_name('pass')
# login_button = driver.find_element_by_name('login')
# username_field.send_keys("your_facebook_username")
# password_field.send_keys("your_facebook_password")
# login_button.click()

# Don't forget to close the WebDriver after you finish
# driver.quit()
