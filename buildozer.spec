[app]
title = Ghost PRO
package.name = ghostpro
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Минимальный набор для стабильности на старте
requirements = python3,kivy==2.2.1,pyjnius,android

orientation = portrait
# API 34 идеально для Android 15
android.api = 34
android.minapi = 24
android.ndk = 25b
# Убираем все старое, оставляем только 64-бит для S24
android.archs = arm64-v8a
android.accept_sdk_license = True
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
