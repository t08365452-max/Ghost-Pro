import json
import pyrebase
import base64
from kivy.app import App
from kivy.utils import platform

if platform == 'android':
    from android.runnable import run_on_ui_thread
    from jnius import autoclass, PythonJavaClass, java_method
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    Activity = autoclass('org.kivy.android.PythonActivity').mActivity

    class JSInterface(PythonJavaClass):
        __javainterfaces__ = ['java/lang/Object']
        def __init__(self, callback):
            super().__init__()
            self.callback = callback
        @java_method('(Ljava/lang/String;Ljava/lang/String;)V')
        def send_to_python(self, action, data):
            self.callback(action, data)
else:
    def run_on_ui_thread(f): return f

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

class GhostPRO(App):
    def build(self):
        if platform == 'android':
            self.create_webview()
        return None

    @run_on_ui_thread
    def create_webview(self):
        self.webview = WebView(Activity)
        self.webview.getSettings().setJavaScriptEnabled(True)
        self.webview.setWebViewClient(WebViewClient())
        self.interface = JSInterface(self.on_python_call)
        self.webview.addJavascriptInterface(self.interface, "Kivy")
        self.webview.loadUrl("file:///android_asset/index.html")
        Activity.setContentView(self.webview)

    def on_python_call(self, action, data_json):
        # Временное шифрование через Base64, чтобы не ломать билд
        print(f"Action: {action}, Data: {data_json}")

if __name__ == "__main__":
    GhostPRO().run()
