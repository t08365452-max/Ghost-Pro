[app]

# (str) Title of your application
title = Ghost PRO

# (str) Package name (строго по твоему JSON)
package.name = ghost_messenger_secure

# (str) Package domain
package.domain = org.ghost

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,html,js,json

# (str) Application version
version = 1.0

# (list) Application requirements
# pyrebase4 нужен для связи с Firebase и регистрации по почте
requirements = python3,kivy==2.2.1,kivymd,requests,cryptography,urllib3,certifi,pyrebase4,pyjnius

# (str) Icon of the application (твоя новая аватарка)
icon.filename = icon.png

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, VIBRATE

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (list) Android meta-data (обязательно для работы google-services.json)
android.meta_data = com.google.gms.google-services = @string/google_services_json

# (list) Android additionnal libraries (для шифрования)
android.add_libs_armeabi = libcrypto.so, libssl.so

# (str) The Android arch to build for
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
# (int) Log level (2 = подробный вывод для отлова ошибок)
log_level = 2

warn_on_root = 1

