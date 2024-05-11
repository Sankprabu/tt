import json
import requests

def get_user_agent():
    try:
        with open('juragan.json', 'r') as file:
            data = json.load(file)
            return data.get('user_agent', '')
    except FileNotFoundError:
        print("File 'juragan.json' not found.")
        return ''
    except Exception as e:
        print(f"Failed to read user agent: {e}")
        return ''

def FacebookLogin():
    try:
        user_agent = get_user_agent()

        if not user_agent:
            print("User-Agent not found. Make sure 'juragan.json' contains the user agent.")
            return

        # Baca email dan password dari file akun.txt
        with open('akun.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            email, password = line.strip().split(',')
            # URL untuk mengirim permintaan login
            login_url = 'https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&amp;lwv=100'

            # Data yang akan dikirimkan dalam permintaan POST
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

            # Header dengan User-Agent
            headers = {
                'User-Agent': user_agent
            }

            # Kirim permintaan POST untuk login
            response = requests.post(login_url, data=data, headers=headers)

            # Periksa apakah berhasil login dengan memeriksa URL setelah login
            if response.status_code == 200:
                if 'c_user' in response.cookies.get_dict():
                    print(f"Login Successful for email: {email}")
                else:
                    print(f"Login Failed: Invalid credentials for email: {email}")
            else:
                print(f"Login Failed: Server error for email: {email}")

    except FileNotFoundError:
        print("File 'akun.txt' not found.")
    except ValueError:
        print("Invalid format in 'akun.txt'. Make sure email and password are separated by a comma.")
    except Exception as e:
        print(f"Failed to execute script: {e}")

FacebookLogin()
