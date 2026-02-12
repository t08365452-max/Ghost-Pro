[app]
# (str) Title of your application
title = Ghost PRO

# (str) Package name
package.name = ghost_messenger_secure

# (str) Package domain (needed for android packaging)
package.domain = org.ghost

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,html,js,json

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# Фиксируем версии, чтобы GitHub Actions не падал из-за несовместимости
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,cryptography==38.0.4,urllib3,certifi,pyrebase4,pyjnius,openssl

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, VIBRATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = 

# (list) Android architectures to build for
android.archs = armeabi-v7a, arm64-v8a

# (str) Icon of the application
icon.filename = icon.png

# (str) XML file for Google Services (Firebase)
android.meta_data = com.google.gms.google-services = @string/google_services_json

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = NO, 1 = YES)
warn_on_root = 1
