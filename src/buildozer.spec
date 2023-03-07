[app]

title = Test applications

package.name = test_app

package.domain = org.kivy.test

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = kivy==master, scipy

orientation = portrait, landscape, portrait-reverse, landscape-reverse

osx.python_version = 3

osx.kivy_version = 2.1.0

fullscreen = 0

android.api = 33

android.minapi = 21

android.ndk = 25b

android.accept_sdk_license = True

android.enable_androidx = True

android.logcat_filters = *:S python:D

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

p4a.branch = develop

p4a.bootstrap = sdl2


#
# iOS specific
#

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

ios.codesign.allowed = false


[buildozer]

log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
