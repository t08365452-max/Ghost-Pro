import os
import certifi
from kivy.app import App
from kivy.utils import platform
from kivy.clock import Clock

# Фикс SSL для всех версий Android
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
        # Даем системе время на инициализацию Python-библиотек
        Clock.schedule_once(self.launch_web, 0.5)
        return None

    @run_on_ui_thread
    def launch_web(self, dt):
        try:
            self.webview = WebView(Activity)
            settings = self.webview.getSettings()
            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setAllowFileAccess(True)
            settings.setDatabaseEnabled(True)
            settings.setMixedContentMode(0) # MIXED_CONTENT_ALWAYS_ALLOW
            
            self.webview.setWebViewClient(WebViewClient())
            
            self.interface = JSInterface(self.on_js_call)
            self.webview.addJavascriptInterface(self.interface, "Kivy")
            
            self.webview.loadUrl("file:///android_asset/index.html")
            Activity.setContentView(self.webview)
        except Exception as e:
            # Если упадет — увидишь в логах GitHub
            print(f"FATAL_ERROR_STAY_ALIVE: {e}")

    def on_js_call(self, action, data):
        print(f"GHOST_INBOUND: {action} -> {data}")

if __name__ == "__main__":
    GhostPRO().run()
