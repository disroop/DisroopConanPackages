import os

from conans import ConanFile
from conan.tools.cmake import CMake

project_version = os.getenv("PROJECT_VERSION", "snapshot")
project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")


class Stm32Runtimel475(ConanFile):
    name = "stm32_runtime_l475_vtg"
    url = "todo add url"
    version = "0.1.0"
    channel = f"{project_channel}"
    user = f"{project_username}"
    license = "MIT"
    description = "This is the runtime setup of CMSIS devices provided by stm"
    generators =  "CMakeDeps","CMakeToolchain"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt","src/*","FindPlatform.cmake"

    def requirements(self):
        self.requires(f"stm32_cmsis_device_l4/1.7.1@{project_username}/{project_channel}")

    def package(self):
        self.copy("*.ld",  src="src", dst="include", keep_path=False)
        self.copy("*.a",  src="src", dst="lib", keep_path=False)
        self.copy("FindPlatform.cmake",  src=".", dst=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs.append(f"stm32_runtime_l475_vtg")
        self.cpp_info.defines.append("STM32L475xx")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
