[app]
title = Ghost PRO
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Самый стабильный набор библиотек
requirements = python3,kivy==2.2.1,requests,pyrebase4,cryptography,pyjnius,android,openssl

orientation = portrait
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# ЭТО ВАЖНО: Принимаем лицензии автоматически
android.accept_sdk_license = True

icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
