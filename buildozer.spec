[app]
title = Ghost PRO
package.name = ghostmessenger
package.domain = org.ghost.pro
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 2.2

# Принудительно жирные требования для стабильности
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,urllib3,certifi,openssl,hostpython3,sqlite3

orientation = portrait
# Целимся в Android 14/15/16
android.api = 34
# Минималка — Android 10
android.minapi = 29
android.ndk = 25b
# Полный набор архитектур
android.archs = arm64-v8a, armeabi-v7a

# Разрешения для работы и уведомлений
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, POST_NOTIFICATIONS
android.manifest.uses_cleartext_traffic = True
android.accept_sdk_license = True

# Черная заставка Ghost
android.presplash_color = #000000
presplash.filename = 
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
