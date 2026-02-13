import json
import pyrebase
from kivy.app import App
from kivy.utils import platform
from cryptography.fernet import Fernet

if platform == 'android':
    from android.runnable import run_on_ui_thread
    from jnius import autoclass, PythonJavaClass, java_method
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    Activity = autoclass('org.kivy.android.PythonActivity').mActivity

    # Мост между JS и Python
    class JSBridge(PythonJavaClass):
        __javainterfaces__ = ['org/kivy/android/PythonActivity$JSInterface'] # Зависит от версии, но чаще просто кастомный интерфейс
        __javacontext__ = 'app'

        def __init__(self, callback):
            super().__init__()
            self.callback = callback

        @java_method('(Ljava/lang/String;Ljava/lang/String;)V')
        def send_to_python(self, action, data):
            self.callback(action, data)
else:
    def run_on_ui_thread(f): return f

# Твой конфиг Firebase
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
        self.webview.getSettings().setDomStorageEnabled(True)
        self.webview.setWebViewClient(WebViewClient())
        
        # Создаем мост, чтобы Kivy.send_to_python работал
        # В твоем JS это вызывается как Kivy.send_to_python
        # Мы регистрируем объект под именем "Kivy"
        # Для простоты в Android WebView используем стандартный addJavascriptInterface
        class WebInterface(PythonJavaClass):
            __javainterfaces__ = ['java/lang/Object']
            def __init__(self, app):
                self.app = app
            @java_method('(Ljava/lang/String;Ljava/lang/String;)V')
            def send_to_python(self, action, data):
                self.app.on_python_call(action, data)

        self.webview.addJavascriptInterface(WebInterface(self), "Kivy")
        self.webview.loadUrl("file:///android_asset/index.html")
        Activity.setContentView(self.webview)

    def on_python_call(self, action, data_json):
        try:
            data = json.loads(data_json)
            if action == 'reg':
                user = auth.create_user_with_email_and_password(data['e'], data['p'])
                auth.send_email_verification(user['idToken'])
            # ... остальная логика регистрации/входа
        except Exception as e:
            print(f"Bridge Error: {e}")

if __name__ == "__main__":
    GhostPRO().run()
