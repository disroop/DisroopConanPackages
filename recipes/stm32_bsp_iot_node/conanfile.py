import os

from conans import ConanFile, CMake, tools
from conan.tools.cmake import CMake, CMakeDeps

project_version = os.getenv("PROJECT_VERSION", "snapshot")
project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")

class Stm32BspIotNode(ConanFile):
    name = "stm32_bsp_Iot_node"
    url = "todo add url"
    version = "1.1.7"
    license = "MIT"
    description = "BSP definition for STM32 Iot Node devoce"
    generators =  "CMakeDeps","CMakeToolchain","cmake_vars"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "src/*",
    
    def configure(self):
        self.options["stm32_hal_l4"].device="STM32L475xx"
        self.options["stm32_hal_l4"].hal_module_enabled=True
        self.options["stm32_hal_l4"].hal_cortex_module_enabled=True
        self.options["stm32_hal_l4"].hal_dfsdm_module_enabled=True
        #self.options["stm32_hal_l4"].hal_spi_module_enabled=True
        self.options["stm32_hal_l4"].hal_dma_module_enabled=True
        self.options["stm32_hal_l4"].hal_flash_module_enabled=True
        self.options["stm32_hal_l4"].hal_gpio_module_enabled=True
        self.options["stm32_hal_l4"].hal_i2c_module_enabled=True
        self.options["stm32_hal_l4"].hal_pwr_module_enabled=True
        self.options["stm32_hal_l4"].hal_qspi_module_enabled=True
        self.options["stm32_hal_l4"].hal_rcc_module_enabled=True
        self.options["stm32_hal_l4"].hal_uart_module_enabled=True

    
    def requirements(self):
        self.requires(f"stm32_hal_l4/1.13.0@{project_username}/{project_channel}")
        self.requires(f"stm32_runtime_l475/{project_version}@{project_username}/{project_channel}")


    def package(self):
        self.copy("*.h", src = f"{self.source_folder}/hal_driver/Inc",
                  dst = "include", excludes = "*template.h", keep_path = False)
        self.copy("*.h", src = f"{self.source_folder}/hal_driver/Inc/Legacy",
                  dst = "include/Legacy", excludes = "*template.h", keep_path = False)
        self.copy("*.h", src = f"{self.source_folder}/include",
                  dst = "include", excludes = "*template.h", keep_path = False)
        self.copy("*.a",  src = "lib", dst = "lib", keep_path = False)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
