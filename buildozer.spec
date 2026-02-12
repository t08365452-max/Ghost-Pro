[app]
title = Ghost PRO
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Упрощенный список для стабильной сборки
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,pyrebase4,pyjnius,openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
icon.filename = icon.png
android.meta_data = com.google.gms.google-services = @string/google_services_json

[buildozer]
log_level = 2
warn_on_root = 1
