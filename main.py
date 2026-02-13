import os
import certifi
from kivy.app import App
from kivy.utils import platform
from kivy.clock import Clock

# Без этого Firebase на Android 14+ вылетает
os.environ['SSL_CERT_FILE'] = certifi.where()

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
        # Запуск через 0.5 сек для стабильности
        Clock.schedule_once(self.create_webview, 0.5)
        return None

    @run_on_ui_thread
    def create_webview(self, dt):
        try:
            self.webview = WebView(Activity)
            s = self.webview.getSettings()
            s.setJavaScriptEnabled(True)
            s.setDomStorageEnabled(True)
            s.setAllowFileAccess(True)
            s.setDatabaseEnabled(True)
            
            self.webview.setWebViewClient(WebViewClient())
            
            self.interface = JSInterface(self.on_js_call)
            self.webview.addJavascriptInterface(self.interface, "Kivy")
            
            self.webview.loadUrl("file:///android_asset/index.html")
            Activity.setContentView(self.webview)
        except Exception as e:
            print(f"FATAL: {e}")

    def on_js_call(self, action, data):
        print(f"GHOST_DATA: {action} {data}")

if __name__ == "__main__":
    GhostPRO().run()
