[app]
title = Ghost PRO
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

requirements = python3,kivy==2.2.1,kivymd,requests,cryptography,urllib3,certifi,pyrebase4,pyjnius

icon.filename = icon.png
orientation = portrait

# ПРИНУДИТЕЛЬНО СТАВИМ СТАБИЛЬНУЮ ВЕРСИЮ
android.api = 33
android.build_tools_version = 33.0.0
android.ndk = 25b

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, POST_NOTIFICATIONS
android.meta_data = com.google.gms.google-services = @string/google_services_json
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
