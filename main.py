import json
from kivy.app import App
from kivy.utils import platform
from kivy.clock import Clock

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
        # Задержка 0.2 сек убирает конфликт при инициализации окна
        Clock.schedule_once(self.init_app, 0.2)
        return None

    def init_app(self, dt):
        self.create_webview()

    @run_on_ui_thread
    def create_webview(self):
        try:
            self.webview = WebView(Activity)
            self.webview.getSettings().setJavaScriptEnabled(True)
            self.webview.getSettings().setDomStorageEnabled(True)
            self.webview.setWebViewClient(WebViewClient())
            
            # Связь с JS: Kivy.send_to_python(action, data)
            self.interface = JSInterface(self.on_python_call)
            self.webview.addJavascriptInterface(self.interface, "Kivy")
            
            # Загрузка твоего HTML из папки assets
            self.webview.loadUrl("file:///android_asset/index.html")
            Activity.setContentView(self.webview)
        except Exception as e:
            print(f"REPORT_ERROR: {e}")

    def on_python_call(self, action, data_json):
        # Ловим данные от кнопок регистрация/логин из index.html
        print(f"Action: {action}, Data: {data_json}")

if __name__ == "__main__":
    GhostPRO().run()
