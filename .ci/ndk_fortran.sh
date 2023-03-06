#!/bin/bash

cd ..

SCRIPT_PATH=$(dirname $(realpath -s $0))

echo "Working dir: $SCRIPT_PATH"

ANDROID_NDK_VERSION_LEGACY="21e"
ANDROID_HOME="LEGACY_NDK"

TARGET_OS="linux"

ANDROID_NDK_HOME_LEGACY="$ANDROID_HOME/android-ndk-legacy"
ANDROID_NDK_FOLDER_LEGACY="$ANDROID_HOME/android-ndk-r$ANDROID_NDK_VERSION_LEGACY"
ANDROID_NDK_ARCHIVE_LEGACY="$ANDROID_HOME/android-ndk-r$ANDROID_NDK_VERSION_LEGACY-$TARGET_OS-x86_64.zip"

ANDROID_NDK_GFORTRAN_ARCHIVE_ARM64="$ANDROID_HOME/gcc-arm64-linux-x86_64.tar.bz2"
ANDROID_NDK_GFORTRAN_ARCHIVE_ARM="$ANDROID_HOME/gcc-arm-linux-x86_64.tar.bz2"

ANDROID_NDK_DL_URL_LEGACY="https://dl.google.com/android/repository/android-ndk-r$ANDROID_NDK_VERSION_LEGACY-linux-x86_64.zip"

echo "downloading ndk-r$ANDROID_NDK_VERSION_LEGACY"
curl --location --progress-bar --continue-at - "$ANDROID_NDK_DL_URL_LEGACY" --output "$ANDROID_NDK_ARCHIVE_LEGACY"
echo "download_android_ndk_gfortran"
curl --location --progress-bar --continue-at - \
"https://github.com/mzakharo/android-gfortran/releases/download/r21e/gcc-arm64-linux-x86_64.tar.bz2" --output "$ANDROID_NDK_GFORTRAN_ARCHIVE_ARM64"
curl --location --progress-bar --continue-at - \
"https://github.com/mzakharo/android-gfortran/releases/download/r21e/gcc-arm-linux-x86_64.tar.bz2" --output "$ANDROID_NDK_GFORTRAN_ARCHIVE_ARM"

echo "extract_android_ndk_legacy:"
mkdir -p "$ANDROID_NDK_FOLDER_LEGACY" \
&& unzip -q "$ANDROID_NDK_ARCHIVE_LEGACY" -d "$ANDROID_HOME" \
&& mv "$ANDROID_NDK_FOLDER_LEGACY" "$ANDROID_NDK_HOME_LEGACY" \
&& rm -f "$ANDROID_NDK_ARCHIVE_LEGACY"

echo "extract_android_ndk_gfortran:"
rm -rf "$ANDROID_NDK_HOME_LEGACY/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/" \
&& mkdir "$ANDROID_NDK_HOME_LEGACY/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/" \
&& tar -xf "$ANDROID_NDK_GFORTRAN_ARCHIVE_ARM64" -C "$ANDROID_NDK_HOME_LEGACY/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/" --strip-components 1 \
&& rm -f "$ANDROID_NDK_GFORTRAN_ARCHIVE_ARM64" \
&& rm -rf "$ANDROID_NDK_HOME_LEGACY/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/" \
&& mkdir "$ANDROID_NDK_HOME_LEGACY/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/" \
&& tar -xf "$ANDROID_NDK_GFORTRAN_ARCHIVE_ARM" -C "$ANDROID_NDK_HOME_LEGACY/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/" --strip-components 1 \
&& rm -f "$ANDROID_NDK_GFORTRAN_ARCHIVE_ARM"
