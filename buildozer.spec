[app]
title = Ghost PRO
package.name = ghostmessenger
package.domain = org.ghost.pro
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.8

requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,urllib3

orientation = portrait
android.api = 33
android.minapi = 21
android.ndk = 25b
# Поддержка всех процессоров сразу
android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True
# Чёрная заставка вместо логотипа Kivy
android.presplash_color = #000000
presplash.filename = 
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
