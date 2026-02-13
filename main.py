import os
import certifi
from kivy.app import App
from kivy.utils import platform
from kivy.clock import Clock

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
        Clock.schedule_once(self.launch_web, 0.5)
        return None

    @run_on_ui_thread
    def launch_web(self, dt):
        try:
            self.webview = WebView(Activity)
            s = self.webview.getSettings()
            s.setJavaScriptEnabled(True)
            s.setDomStorageEnabled(True)
            s.setAllowFileAccess(True)
            self.webview.setWebViewClient(WebViewClient())
            self.interface = JSInterface(self.on_js_call)
            self.webview.addJavascriptInterface(self.interface, "Kivy")
            self.webview.loadUrl("file:///android_asset/index.html")
            Activity.setContentView(self.webview)
        except Exception as e:
            print(f"STAY_ALIVE_ERROR: {e}")

    def on_js_call(self, action, data):
        print(f"JS_SIGNAL: {action} {data}")

if __name__ == "__main__":
    GhostPRO().run()
