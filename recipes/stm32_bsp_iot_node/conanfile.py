import os

from conans import ConanFile, CMake
from conan.tools.cmake import CMake
from conans.errors import ConanInvalidConfiguration

project_version = os.getenv("PROJECT_VERSION", "snapshot")
project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")

class Stm32BspIotNode(ConanFile):
    name = "stm32_bsp_iot_node"
    url = "todo add url"
    version = "1.1.7"
    license = "MIT"
    description = "BSP definition for STM32 Iot Node devoce"
    generators =  "CMakeDeps","CMakeToolchain"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "src/*",
    options = {"irq_spi_interface_prio":"ANY"}
    default_options = {"irq_spi_interface_prio":"0"}

    def configure(self):
        self.options["stm32_hal_l4"].device="STM32L475xx"
        self.options["stm32_hal_l4"].hal_module_enabled=True
        self.options["stm32_hal_l4"].hal_cortex_module_enabled=True
        self.options["stm32_hal_l4"].hal_dfsdm_module_enabled=True
        self.options["stm32_hal_l4"].hal_spi_module_enabled=True
        self.options["stm32_hal_l4"].hal_dma_module_enabled=True
        self.options["stm32_hal_l4"].hal_flash_module_enabled=True
        self.options["stm32_hal_l4"].hal_gpio_module_enabled=True
        self.options["stm32_hal_l4"].hal_i2c_module_enabled=True
        self.options["stm32_hal_l4"].hal_pwr_module_enabled=True
        self.options["stm32_hal_l4"].hal_qspi_module_enabled=True
        self.options["stm32_hal_l4"].hal_rcc_module_enabled=True
        self.options["stm32_hal_l4"].hal_uart_module_enabled=True
        self.options["stm32_hal_l4"].hal_rng_module_enabled=True
        self.options["stm32_hal_l4"].hal_rtc_module_enabled=True
        self.options["stm32_hal_l4"].hal_tim_module_enabled=True
    
    def requirements(self):
        self.requires(f"stm32_hal_l4/1.13.0@{project_username}/{project_channel}")

    def package(self):
        self.copy("*.h", src=f"src", dst = "include", keep_path = True)
        self.copy("*.a",  src = "src/B-L475E-IOT01", dst = "lib", keep_path = False)

    def package_info(self):
        self.cpp_info.libs.append("stm32bspiotnode")
        self.cpp_info.defines=[f"SPI_INTERFACE_PRIO={self.options.irq_spi_interface_prio}"]


    def build(self):
        if self.settings.arch == "armv7":
            cmake = CMake(self)
            cmake.configure()
            cmake.build()
        else:
            raise ConanInvalidConfiguration("Only armv7 builds are supported")
