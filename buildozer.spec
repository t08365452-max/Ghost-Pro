[app]
title = Ghost PRO
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Фикс зависимостей: добавил openssl для cryptography и зафиксировал версии
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,cryptography==38.0.4,urllib3,certifi,pyrebase4,pyjnius,openssl

icon.filename = icon.png
orientation = portrait
fullscreen = 0

# Разрешения
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, VIBRATE

# Стабильные настройки для GitHub Actions
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

# Firebase конфиг
android.meta_data = com.google.gms.google-services = @string/google_services_json

[buildozer]
log_level = 2
warn_on_root = 1
