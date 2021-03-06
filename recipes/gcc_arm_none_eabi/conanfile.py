import os
from conans import ConanFile, tools

class GccArmNoneEabi(ConanFile):
    name = "gcc_arm_none_eabi"
    version = "10.2.0"
    user = "disroop"
    channel = "release"
    settings = "os"

    # Implement source() and build() as usual
    def source(self):
        if self.settings.os == "Linux":
            tools.download("https://disroopartifacts.jfrog.io/artifactory/thirdparty-generic-local/gcc-arm-none-eabi-10-2020-q4-major-x86_64-linux.tar.bz2", "arm-gcc.tar.bz2", md5="8312c4c91799885f222f663fc81f9a31")
            self.run("mkdir toolchain && tar -xvjf arm-gcc.tar.bz2 -C toolchain --strip-components=1")
        elif tools.is_apple_os(self.settings.os):
            tools.download("https://developer.arm.com/-/media/Files/downloads/gnu-rm/10-2020q4/gcc-arm-none-eabi-10-2020-q4-major-mac.tar.bz2?revision=48a4e09a-eb5a-4eb8-8b11-d65d7e6370ff&la=en&hash=8AACA5F787C5360D2C3C50647C52D44BCDA1F73F", "arm-gcc.tar.bz2", md5="e588d21be5a0cc9caa60938d2422b058")
            self.run("mkdir toolchain && tar -xvjf arm-gcc.tar.bz2 -C toolchain --strip-components=1")


    def package(self):
        # Copy all the required files for your toolchain
        self.copy("*", dst="", src="toolchain")

    def package_info(self):
        bin_folder = os.path.join(self.package_folder, "bin")
        self.env_info.AR = os.path.join(bin_folder, "arm-none-eabi-ar")
        self.env_info.OBJCOPY = os.path.join(bin_folder, "arm-none-eabi-objcopy")
        self.env_info.OBJDUMP = os.path.join(bin_folder, "arm-none-eabi-objdump")
        self.env_info.SIZE = os.path.join(bin_folder, "arm-none-eabi-size")
        self.env_info.CC = os.path.join(bin_folder, "arm-none-eabi-gcc")
        self.env_info.CXX = os.path.join(bin_folder, "arm-none-eabi-g++")
        self.env_info.CONAN_CMAKE_CC = os.path.join(bin_folder, "arm-none-eabi-gcc")
        self.env_info.CONAN_CMAKE_CXX = os.path.join(bin_folder, "arm-none-eabi-g++")
        self.env_info.CONAN_CMAKE_SYSTEM_NAME = "Generic"
        self.env_info.LD =  os.path.join(bin_folder, "arm-none-eabi-ld")
        self.env_info.DEBUGGER =  os.path.join(bin_folder, "arm-none-eabi-gdb")
        self.env_info.OBJCOPY =  os.path.join(bin_folder, "arm-none-eabi-objcopy")
        self.env_info.OBJDUMP =  os.path.join(bin_folder, "arm-none-eabi-objdump")
        self.env_info.SIZE =  os.path.join(bin_folder, "arm-none-eabi-size")
        self.env_info.CPPFILT =  os.path.join(bin_folder, "arm-none-eabi-c++filt")
        self.env_info.SYSROOT = self.package_folder
        self.env_info.CMAKE_TRY_COMPILE_TARGET_TYPE = "STATIC_LIBRARY"
