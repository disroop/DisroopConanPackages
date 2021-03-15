import os

from conans import ConanFile, CMake, tools

device_version = "1.8.0"
project_version = os.getenv("PROJECT_VERSION", "snapshot")
project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")


class Stm32CmsisDeviceL4(ConanFile):
    name = "stm32_cmsis_device_wb"
    url = "todo add url"
    version = f"{device_version}"
    channel = f"{project_channel}"
    user = f"{project_username}"
    license = "MIT"
    description = "This is the runtime setup of CMSIS devices provided by stm"
    generators = "virtualenv", "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt"
    options = {
        "STM32WB": [True, False],
        "USE_HAL_DRIVER": [True, False],
        "STM32WB55_DEVICE": [
            "STM32WB55xx",
            "STM32WB5Mxx",
            "STM32WB50xx",
            "STM32WB35xx",
            "STM32WB30xx",
            "STM32WB15xx",
            "STM32WB10xx",
        ],
        # todo
        # "hse_value": "ANY",  # (32000000UL) /*!< Value of the External oscillator in Hz */
        # "msi_value": "ANY",  # (4000000UL) /*!< Value of the Internal oscillator in Hz*/
        # "hsi_value": "ANY",  # (16000000UL) /*!< Value of the Internal oscillator in Hz*/
        # "lsi_value": "ANY",  # (32000UL)       /*!< Value of LSI in Hz*/
        # "lse_value": "ANY",  # (32768UL)    /*!< Value of LSE in Hz*/
        # USER_VECT_TAB_ADDRESS
        #     VECT_TAB_SRAM
        # VECT_TAB_BASE_ADDRESS
        #     VECT_TAB_OFFSET
    }
    _cmake = None

    def requirements(self):
        self.requires(f"stm32_cmsis_core/5.6.0_cm4@{project_username}/{project_channel}")

    def source(self):
        git = tools.Git(folder=self.source_folder)
        git.clone("https://github.com/STMicroelectronics/cmsis_device_wb.git", branch=f"v{device_version}",
                  shallow=True)

    def package(self):
        self.copy("*.h", src="Include", dst="include", keep_path=False)
        # self.copy("stm32l476xx.h", src="Include", dst="include", keep_path=False)
        # self.copy("system_stm32l4xx.h", src="Include", dst="include", keep_path=False)
        # self.copy("*.a", src="lib", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.arch == "x86_64":
            self.cpp_info.libs.append(f"{self.name}")
        self.cpp_info.defines.append("STM32WB55xx")

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        self._cmake.definitions["STM32WB"] = self.options.STM32WB
        self._cmake.definitions["USE_HAL_DRIVER"] = not self.options.USE_HAL_DRIVER
        self._cmake.definitions["STM32WB55_DEVICE"] = not self.options.STM32WB55_DEVICE
        # self._cmake.configure(build_folder=self._build_subfolder)
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.configure()
        cmake.build()
