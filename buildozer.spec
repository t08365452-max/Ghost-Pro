[app]
title = Ghost PRO
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Строго фиксируем версии для стабильности на GitHub
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,cryptography==38.0.4,urllib3,certifi,pyrebase4,pyjnius,openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, VIBRATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
icon.filename = icon.png

# Связь с Firebase
android.meta_data = com.google.gms.google-services = @string/google_services_json

[buildozer]
log_level = 2
warn_on_root = 1
