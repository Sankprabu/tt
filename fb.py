import requests

def FacebookLogin():
    try:
        # Baca email dan password dari file akun.txt
        with open('akun.txt', 'r') as file:
            email, password = file.readline().strip().split(',')

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

        # Kirim permintaan POST untuk login
        response = requests.post(login_url, data=data)

        # Periksa apakah berhasil login dengan memeriksa URL setelah login
        if response.status_code == 200:
            if 'c_user' in response.cookies.get_dict():
                print("Login Successful")
            else:
                print("Login Failed: Invalid credentials")
        else:
            print("Login Failed: Server error")

    except FileNotFoundError:
        print("File 'akun.txt' not found.")
    except ValueError:
        print("Invalid format in 'akun.txt'. Make sure email and password are separated by a comma.")
    except Exception as e:
        print(f"Failed to execute script: {e}")

FacebookLogin()
