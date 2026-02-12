[app]
# (str) Title of your application
title = Ghost PRO

# (str) Package name (из твоего google-services.json)
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
requirements = python3,kivy==2.2.1,kivymd,requests,cryptography,urllib3,certifi,pyrebase4,pyjnius

# (str) Icon of the application
icon.filename = icon.png

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, POST_NOTIFICATIONS

# (int) Target Android API
android.api = 33

# (str) Android NDK version to use
android.ndk = 25b

# --- КРИТИЧЕСКИЙ ФИКС ДЛЯ AIDL ---
# Принудительно используем стабильные инструменты вместо версии 36.1
android.build_tools_version = 33.0.0

# (list) Android meta-data (для твоего google-services.json)
android.meta_data = com.google.gms.google-services = @string/google_services_json

# (str) The Android arch to build for
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
# (int) Log level (2 = debug для отлова всех косяков)
log_level = 2

warn_on_root = 1
