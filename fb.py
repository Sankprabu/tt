import json
import requests
import logging
import time

# Configure logging
logging.basicConfig(filename='login.log', level=logging.ERROR)

def get_user_agent():
    try:
        with open('juragan.json', 'r') as file:
            data = json.load(file)
            return data.get('user_agent', '')
    except FileNotFoundError:
        logging.error("File 'juragan.json' not found.")
        return ''
    except Exception as e:
        logging.error(f"Failed to read user agent: {e}")
        return ''

def FacebookLogin():
    try:
        user_agent = get_user_agent()

        if not user_agent:
            logging.error("User-Agent not found. Make sure 'juragan.json' contains the user agent.")
            return

        with open('akun.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            email, password = line.strip().split(',')
            login_url = 'https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&amp;lwv=100'

            data = {
                'email': email,
                'pass': password,
                'lsd': 'AVro0WNYaCM',
                'jazoest': '2919',
                'm_ts': '1715444401',
                'li': 'sZo_ZhwFPCPV8wmk39pZ8cFq',
                'try_number': '0',
                'unrecognized_tries': '0'
            }

            headers = {
                'User-Agent': user_agent
            }

            response = requests.post(login_url, data=data, headers=headers)

            if response.status_code == 200:
                if 'c_user' in response.cookies.get_dict():
                    logging.info(f"Login Successful for email: {email}")
                else:
                    logging.error(f"Login Failed: Invalid credentials for email: {email}")
            else:
                logging.error(f"Login Failed: Server error for email: {email}")
            
            # Introduce a delay between login attempts
            time.sleep(1)

    except FileNotFoundError:
        logging.error("File 'akun.txt' not found.")
    except ValueError:
        logging.error("Invalid format in 'akun.txt'. Make sure email and password are separated by a comma.")
    except Exception as e:
        logging.error(f"Failed to execute script: {e}")

FacebookLogin()
