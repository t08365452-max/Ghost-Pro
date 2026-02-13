[app]
title = Ghost PRO
package.name = ghostmessenger
package.domain = org.ghost.pro
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.6

# Библиотеки для работы сети и Firebase
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,urllib3

orientation = portrait
# API 33 оптимален для Android 15 и старых версий
android.api = 33
android.minapi = 21
android.ndk = 25b

# ВАЖНО: Поддержка и 64-бит (S24), и 32-бит (старые ядра)
android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True
android.manifest.launch_mode = standard

# Убираем белый экран при загрузке
android.presplash_color = #000000
presplash.filename = 
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
