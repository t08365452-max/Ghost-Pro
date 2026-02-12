import json
import pyrebase
from kivy.app import App
from kivy.uix.webview import WebView
from cryptography.fernet import Fernet

# Твои данные из конфига
firebase_config = {
    "apiKey": "AIzaSyAbiRCuR9egtHKg0FNzzBdL9dNqPqpPLNk",
    "authDomain": "ghost-pro-5aa22.firebaseapp.com",
    "projectId": "ghost-pro-5aa22",
    "storageBucket": "ghost-pro-5aa22.firebasestorage.app",
    "messagingSenderId": "332879455079",
    "appId": "1:332879455079:android:15c36642c62d13e0dd05c2",
    "databaseURL": "https://ghost-pro-5aa22-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
cipher = Fernet(b'6fL3_F5_E8v1pXz7_m-90U5IF-ri8GYQ_ABCDE123456=')

class GhostPRO(App):
    def build(self):
        self.view = WebView(url="index.html")
        return self.view

    def on_python_call(self, action, data_json):
        data = json.loads(data_json)
        try:
            if action == 'register':
                user = auth.create_user_with_email_and_password(data['e'], data['p'])
                auth.send_email_verification(user['idToken'])
                self.view.execute_js("log('REG_OK: Код подтверждения отправлен!')")

            elif action == 'login':
                user = auth.sign_in_with_email_and_password(data['e'], data['p'])
                info = auth.get_account_info(user['idToken'])
                if info['users'][0]['emailVerified']:
                    self.view.execute_js("set_view('chat'); log('ВХОД ВЫПОЛНЕН')")
                else:
                    self.view.execute_js("log('ERR: Подтвердите почту!', '#ffae00')")

            elif action == 'send_msg':
                enc = cipher.encrypt(data.encode()).decode()
                db.child("messages").push({"m": enc})
                self.view.execute_js("log('Пакет зашифрован.')")

        except Exception as e:
            msg = str(e).replace("'", "").replace('"', "")
            self.view.execute_js(f"log('ERROR: {msg[:40]}...', '#f00')")

if __name__ == "__main__":
    GhostPRO().run()
