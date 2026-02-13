import json
from kivy.app import App
from kivy.utils import platform

# Если мы на Android, настраиваем WebView
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

class GhostPRO(App):
    def build(self):
        if platform == 'android':
            self.create_webview()
        return None

    @run_on_ui_thread
    def create_webview(self):
        self.webview = WebView(Activity)
        self.webview.getSettings().setJavaScriptEnabled(True)
        self.webview.getSettings().setDomStorageEnabled(True) # Важно для JS
        self.webview.setWebViewClient(WebViewClient())
        
        # Подключаем твой интерфейс из index.html
        self.interface = JSInterface(self.on_python_call)
        self.webview.addJavascriptInterface(self.interface, "Kivy")
        
        # Загружаем локальный index.html
        self.webview.loadUrl("file:///android_asset/index.html")
        Activity.setContentView(self.webview)

    def on_python_call(self, action, data_json):
        # Тут будет обработка логина/регистрации из твоего HTML
        print(f"Action: {action}, Data: {data_json}")

if __name__ == "__main__":
    GhostPRO().run()
