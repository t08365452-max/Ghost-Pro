[app]
title = Ghost PRO
package.name = ghostpro
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Минимум требований, чтобы 100% собралось
requirements = python3,kivy==2.2.1,pyjnius,android

orientation = portrait
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
