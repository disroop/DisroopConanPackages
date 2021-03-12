import os
from conans import ConanFile, CMake, tools

core_version="5.6.0_cm4"
project_username = os.getenv("CONAN_USERNAME")
project_channel = os.getenv("CONAN_CHANNEL")


class Stm32CmsisCore(ConanFile):
    name = "stm32_cmsis_core"
    url = "todo add url"
    version = f"{core_version}"
    channel = f"{project_channel}"
    user = f"{project_username}"
    license = "MIT"
    description = "Minimal CMSIS Core"

    def source(self):
        git=tools.Git(folder=self.source_folder)
        git.clone("https://github.com/STMicroelectronics/cmsis_core.git", branch=f"v{core_version}", shallow=True)

    def package(self):
        self.copy("*.h", src="Core/Include", dst="include", keep_path=False)

    def build(self):
        pass

    def package_id(self):
        self.info.header_only()