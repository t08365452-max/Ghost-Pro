[app]
title = Ghost PRO
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Оставляем только самое необходимое. 
# pyrebase4 сам возьмет нужные зависимости внутри себя.
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,pyrebase4,pyjnius

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, VIBRATE

# Настройки для стабильности
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

icon.filename = icon.png
android.meta_data = com.google.gms.google-services = @string/google_services_json

[buildozer]
log_level = 2
warn_on_root = 1
