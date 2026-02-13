[app]
title = Ghost PRO
package.name = ghostmessenger
package.domain = org.ghost.pro
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.9

# Добавили библиотеки для работы с SSL и уведомлениями
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,urllib3,certifi,chardet,idna

orientation = portrait
# API 34 — база для Android 14/15/16
android.api = 34
android.minapi = 29
android.ndk = 25b
# Поддержка всех современных ядер
android.archs = arm64-v8a, armeabi-v7a

# РАЗРЕШЕНИЯ (Интернет + Уведомления)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, POST_NOTIFICATIONS, WAKE_LOCK

# Чтобы приложение не падало при запросах к Firebase
android.manifest.uses_cleartext_traffic = True
android.accept_sdk_license = True
android.presplash_color = #000000
presplash.filename = 
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
