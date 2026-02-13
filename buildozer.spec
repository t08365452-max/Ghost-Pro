[app]
title = Ghost PRO
package.name = ghostmessenger
package.domain = org.ghost.pro
source.dir = .
# Убедись, что html и js включены в список!
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.3

# Возвращаем зависимости для работы Firebase
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,urllib3

orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
