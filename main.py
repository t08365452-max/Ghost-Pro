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
    # Заглушка, чтобы код не вылетал на ПК
    class WebView:
        def __init__(self, **kwargs): pass

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
        # На Android мы создаем нативный WebView
        if platform == 'android':
            self.create_webview()
        return None # Интерфейс будет поверх окна Kivy

    @run_on_ui_thread
    def create_webview(self):
        webview = WebView(Activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.setWebViewClient(WebViewClient())
        # Загружаем твой index.html из папки приложения
        webview.loadUrl("file:///android_asset/index.html")
        Activity.setContentView(webview)

    # Твоя логика обработки вызовов из JS остается без изменений
    def on_python_call(self, action, data_json):
        try:
            data = json.loads(data_json)
            if action == 'reg':
                user = auth.create_user_with_email_and_password(data['e'], data['p'])
                auth.send_email_verification(user['idToken'])
                db.child("users").child(user['localId']).set({"status": "user"})
                print("REG_SUCCESS")
            # ... и так далее (весь твой остальной код)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    GhostPRO().run()
