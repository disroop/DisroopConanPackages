import os

from conans import ConanFile, CMake, tools

device_version="1.7.1"
project_version = os.getenv("PROJECT_VERSION", "snapshot")
project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")


class Stm32CmsisDeviceL4(ConanFile):
    name = "stm32_cmsis_device_l4"
    url = "todo add url"
    version = f"{device_version}"
    channel = f"{project_channel}"
    user = f"{project_username}"
    license = "MIT"
    description = "This is the runtime setup of CMSIS devices provided by stm"
    generators = "virtualenv", "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt"

    def requirements(self):
        self.requires(f"stm32_cmsis_core/5.6.0_cm4@{project_username}/{project_channel}")

    def source(self):
        git=tools.Git(folder=self.source_folder)
        git.clone("https://github.com/STMicroelectronics/cmsis_device_l4.git", branch=f"v{device_version}", shallow=True)

    def package(self):
        self.copy("*.h", src="Include", dst="include", keep_path=False)

    def build(self):
        pass
    
    def package_id(self):
        self.info.header_only()