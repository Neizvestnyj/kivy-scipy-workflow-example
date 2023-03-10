## Workflow example for `scipy`

`src` - folder with test application

`.ci/ndk_fortran.py` - that script download android-gfortran archives from [mzakharo repository](https://github.com/mzakharo/android-gfortran/releases), 
download `ndk-r21e`, extract all folders and copy with replace **arm-linux-androideabi-4.9** and **aarch64-linux-android-4.9** content in the folders to **android-ndk-r21e/toolchains**

`.github/workflows/android.yml` - uses [ArtemSBulgakov buildozer-action](https://github.com/ArtemSBulgakov/buildozer-action)
