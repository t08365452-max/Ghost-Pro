[app]
title = Ghost PRO
package.name = ghostpro
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Только база. Чем меньше тут слов, тем быстрее соберется.
requirements = python3,kivy==2.2.1,requests,pyrebase4,pyjnius,android

orientation = portrait
android.permissions = INTERNET
android.api = 33
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
