import json
import pyrebase
from kivy.app import App
from kivy.utils import platform
from cryptography.fernet import Fernet

# Настройка WebView для Android
if platform == 'android':
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    Activity = autoclass('org.kivy.android.PythonActivity').mActivity
else:
    Activity = None

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
        self.webview = None
        if platform == 'android':
            self.create_webview()
        return None

    @run_on_ui_thread
    def create_webview(self):
        self.webview = WebView(Activity)
        self.webview.getSettings().setJavaScriptEnabled(True)
        self.webview.getSettings().setDomStorageEnabled(True) # Чтобы JS работал четко
        self.webview.setWebViewClient(WebViewClient())
        # Загрузка твоего index.html
        self.webview.loadUrl("file:///android_asset/index.html")
        Activity.setContentView(self.webview)

    @run_on_ui_thread
    def run_js(self, code):
        """Метод для отправки команд в твой HTML"""
        if self.webview:
            self.webview.evaluateJavascript(code, None)

    def on_python_call(self, action, data_json):
        try:
            data = json.loads(data_json)
            if action == 'reg':
                user = auth.create_user_with_email_and_password(data['e'], data['p'])
                auth.send_email_verification(user['idToken'])
                self.run_js("log('REG_SUCCESS: Проверь почту!')")
            
            elif action == 'login':
                user = auth.sign_in_with_email_and_password(data['e'], data['p'])
                info = auth.get_account_info(user['idToken'])
                if info['users'][0]['emailVerified']:
                    self.run_js("set_view('chat'); log('Вход выполнен!')")
                else:
                    self.run_js("log('ERR: Подтвердите Email!')")
                    
        except Exception as e:
            self.run_js(f"log('SYSTEM_ERROR: {str(e)}')")

if __name__ == "__main__":
    GhostPRO().run()
