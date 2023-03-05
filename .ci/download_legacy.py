import requests
import tarfile
from pathlib import Path
import os
from zipfile import ZipFile
import shutil

current_path = Path(__file__).parent.absolute()


def recursive_overwrite(src: str, dest: str, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore,
                                    )
    else:
        shutil.copyfile(src, dest)


def download_and_extract(url: str, file: str):
    """
    :param url: download url
    :param file: where to save the file and under what name
    :return:
    """

    print(f'Start downloading {url}')

    with open(file, 'wb') as f:
        r = requests.get(url, stream=True)
        size = r.headers['Content-length']
        print(f'File size: {size}')
        for chunk in r.raw.stream(1024, decode_content=False):
            if chunk:
                f.write(chunk)
                f.flush()

    print(f'Starting extraction of {file}')

    output = os.path.dirname(file)

    _, ext = os.path.splitext(file)

    if ext == '.bz2':
        tar = tarfile.open(file, f"r:bz2")
        tar.extractall(output)
        tar.close()
        arch_name = tar.name
    elif ext == '.zip':
        with ZipFile(file, 'r') as zip_file:
            zip_file.extractall(output)
            arch_name = zip_file.filename
    else:
        raise AttributeError

    print(arch_name, 'extracted to', output)


arm32_url = "https://github.com/mzakharo/android-gfortran/releases/download/r21e/gcc-arm-linux-x86_64.tar.bz2"
arm64_url = "https://github.com/mzakharo/android-gfortran/releases/download/r21e/gcc-arm64-linux-x86_64.tar.bz2"
ndk21e_url = "https://dl.google.com/android/repository/android-ndk-r21e-linux-x86_64.zip"

if __name__ == '__main__':
    LEGACY_NDK = os.path.join(str(current_path.parent), 'LEGACY_NDK')
    print(f'LEGACY_NDK: {LEGACY_NDK}')

    if not os.path.exists(LEGACY_NDK):
        os.makedirs(LEGACY_NDK)
        print(f'Created {LEGACY_NDK}')

    arm32_archive = os.path.join(LEGACY_NDK, 'arm32.tar.bz2')
    arm64_archive = os.path.join(LEGACY_NDK, 'arm64.tar.bz2')
    ndk_archive = os.path.join(LEGACY_NDK, 'ndk21e.zip')

    arm32_folder = os.path.join(LEGACY_NDK, "arm-linux-androideabi-4.9")
    arm64_folder = os.path.join(LEGACY_NDK, "aarch64-linux-android-4.9")
    ndk_folder = os.path.join(LEGACY_NDK, "android-ndk-r21e")

    toolchains = os.path.join(ndk_folder, 'toolchains')
    print(toolchains)

    buildozer_ndk_armeabi = os.path.join(toolchains, "arm-linux-androideabi-4.9", "prebuilt", "linux-x86_64")
    buildozer_ndk_arm64 = os.path.join(toolchains, "aarch64-linux-android-4.9", "prebuilt", "linux-x86_64")

    download_and_extract(arm32_url, arm32_archive)
    download_and_extract(arm64_url, arm64_archive)
    download_and_extract(ndk21e_url, ndk_archive)

    print(f'Copy {arm32_folder} to {buildozer_ndk_armeabi}')
    recursive_overwrite(arm32_folder, buildozer_ndk_armeabi)
    print(f'Copy {arm64_folder} to {buildozer_ndk_arm64}')
    recursive_overwrite(arm64_folder, buildozer_ndk_arm64)
