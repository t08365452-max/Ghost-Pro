[app]
# (str) Title of your application
title = Ghost PRO
# (str) Package name
package.name = ghost_messenger_secure
# (str) Package domain
package.domain = org.ghost
# (str) Source code where the main.py lives
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# ВАЖНО: Список библиотек оптимизирован для сборки на GitHub
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,cryptography==38.0.4,pyjnius,pyrebase4,openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, VIBRATE

# Настройки SDK/NDK для 2026 года
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# Иконка (файл icon.png должен быть в репозитории!)
icon.filename = icon.png

# Связь с Firebase
android.meta_data = com.google.gms.google-services = @string/google_services_json

[buildozer]
log_level = 2
warn_on_root = 1
