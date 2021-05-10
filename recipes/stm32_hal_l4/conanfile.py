import os

from conans import ConanFile, CMake, tools

hal_version = "1.13.0"


project_version = os.getenv("PROJECT_VERSION", "snapshot")
project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")

class Stm32HalL4(ConanFile):
    name = "stm32_hal_l4"
    url = "todo add url"
    version = f"{hal_version}"
    license = "MIT"
    description = "HAL_defined for STM32"
    generators = "cmake", "cmake_vars",
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "include/*.h",
    options = {"device": ["STM32L476xx","STM32L475xx"],
               "hal_module_enabled": [True, False],
               "hal_adc_module_enabled": [True, False],
               "hal_can_module_enabled": [True, False],
               "hal_can_legacy_module_enabled": [True, False],
               "hal_comp_module_enabled": [True, False],
               "hal_cortex_module_enabled": [True, False],
               "hal_crc_module_enabled": [True, False],
               "hal_cryp_module_enabled": [True, False],
               "hal_dac_module_enabled": [True, False],
               "hal_dfsdm_module_enabled": [True, False],
               "hal_dma_module_enabled": [True, False],
               "hal_flash_module_enabled": [True, False],
               "hal_nand_module_enabled": [True, False],
               "hal_nor_module_enabled": [True, False],
               "hal_sram_module_enabled": [True, False],
               "hal_gpio_module_enabled": [True, False],
               "hal_i2c_module_enabled": [True, False],
               "hal_iwdg_module_enabled": [True, False],
               "hal_lcd_module_enabled": [True, False],
               "hal_lptim_module_enabled": [True, False],
               "hal_opamp_module_enabled": [True, False],
               "hal_pwr_module_enabled": [True, False],
               "hal_qspi_module_enabled": [True, False],
               "hal_rcc_module_enabled": [True, False],
               "hal_rng_module_enabled": [True, False],
               "hal_rtc_module_enabled": [True, False],
               "hal_sai_module_enabled": [True, False],
               "hal_sd_module_enabled": [True, False],
               "hal_smbus_module_enabled": [True, False],
               "hal_spi_module_enabled": [True, False],
               "hal_swpmi_module_enabled": [True, False],
               "hal_tim_module_enabled": [True, False],
               "hal_tsc_module_enabled": [True, False],
               "hal_uart_module_enabled": [True, False],
               "hal_usart_module_enabled": [True, False],
               "hal_irda_module_enabled": [True, False],
               "hal_smartcard_module_enabled": [True, False],
               "hal_wwdg_module_enabled": [True, False],
               "hal_pcd_module_enabled": [True, False],
               "hal_hcd_module_enabled": [True, False],
               "hse_value": "ANY",
               "hse_startup_timeout": "ANY",
               "msi_value": "ANY",
               "hsi_value": "ANY",
               "lsi_value": "ANY",
               "lse_value": "ANY",
               "lse_startup_timeout": "ANY",
               "external_sai1_clock_value": "ANY",
               "external_sai2_clock_value": "ANY",
               "vdd_value": "ANY",
               "tick_int_priority": "ANY",
               "use_rtos": [True, False],
               "prefetch_enable": [True, False],
               "instruction_cache_enable": [True, False],
               "data_cache_enable": [True, False],
               "use_full_assert": [True, False],
               "use_spi_crc": [True, False]
               }

    default_options = {
        "device": "STM32L476xx",
        "hal_module_enabled": True,
        "hal_adc_module_enabled": False,
        "hal_can_module_enabled": False,
        "hal_can_legacy_module_enabled": False,
        "hal_comp_module_enabled": False,
        "hal_cortex_module_enabled": True,
        "hal_crc_module_enabled": False,
        "hal_cryp_module_enabled": False,
        "hal_dac_module_enabled": False,
        "hal_dfsdm_module_enabled": False,
        "hal_dma_module_enabled": False,
        "hal_flash_module_enabled": True,
        "hal_nand_module_enabled": False,
        "hal_nor_module_enabled": False,
        "hal_sram_module_enabled": False,
        "hal_gpio_module_enabled": True,
        "hal_i2c_module_enabled": False,
        "hal_iwdg_module_enabled": False,
        "hal_lcd_module_enabled": False,
        "hal_lptim_module_enabled": False,
        "hal_opamp_module_enabled": False,
        "hal_pwr_module_enabled": True,
        "hal_qspi_module_enabled": False,
        "hal_rcc_module_enabled": True,
        "hal_rng_module_enabled": False,
        "hal_rtc_module_enabled": False,
        "hal_sai_module_enabled": False,
        "hal_sd_module_enabled": False,
        "hal_smbus_module_enabled": False,
        "hal_spi_module_enabled": False,
        "hal_swpmi_module_enabled": False,
        "hal_tim_module_enabled": False,
        "hal_tsc_module_enabled": False,
        "hal_uart_module_enabled": False,
        "hal_usart_module_enabled": False,
        "hal_irda_module_enabled": False,
        "hal_smartcard_module_enabled": False,
        "hal_wwdg_module_enabled": False,
        "hal_pcd_module_enabled": False,
        "hal_hcd_module_enabled": False,
        "hse_value": "8000000",
        "hse_startup_timeout": "100",
        "msi_value": "4000000",
        "hsi_value": "16000000",
        "lsi_value": "32000",
        "lse_value": "32768",
        "lse_startup_timeout": "5000",
        "external_sai1_clock_value": "48000",
        "external_sai2_clock_value": "48000",
        "vdd_value": "3300",
        "tick_int_priority": "0x0f",
        "use_rtos": False,
        "prefetch_enable": False,
        "instruction_cache_enable": True,
        "data_cache_enable": True,
        "use_full_assert": False,
        "use_spi_crc": True,
    }

    def requirements(self):
        self.requires(f"cmake_vars/1.0.0@{project_username}/{project_channel}",private=True)
        self.requires(
            f"stm32_cmsis_core/5.6.0_cm4@{project_username}/{project_channel}")
        self.requires(
            f"stm32_cmsis_device_l4/1.7.1@{project_username}/{project_channel}")

    def source(self):
        git = tools.Git(folder=f"{self.source_folder}/hal_driver")
        git.clone("https://github.com/STMicroelectronics/stm32l4xx_hal_driver.git",
                  branch=f"v{hal_version}", shallow=True)

    def package(self):
        self.copy("*.h", src = f"{self.source_folder}/hal_driver/Inc",
                  dst = "include", excludes = "*template.h", keep_path = False)
        self.copy("*.h", src = f"{self.source_folder}/hal_driver/Inc/Legacy",
                  dst = "include/Legacy", excludes = "*template.h", keep_path = False)
        self.copy("*.h", src = f"{self.source_folder}/include",
                  dst = "include", excludes = "*template.h", keep_path = False)
        self.copy("*.a",  src = "lib", dst = "lib", keep_path = False)

    def package_info(self):
        self.cpp_info.libs.append(f"{self.name}")
        for option, optionstr in self.options.items():
            if option.endswith("_enabled") and optionstr == "True":
                self.cpp_info.defines.append(f"{option.upper()}")
            if option == "use_full_assert":
                self.cpp_info.defines.append("USE_FULL_ASSERT")
            if option.endswith("_enable"):
                if optionstr == "True":
                    self.cpp_info.defines.append(f"{optionstr.upper()}=1")
                else:
                    self.cpp_info.defines.append(f"{optionstr.upper()}=0")
            if option == "use_rtos":
                if optionstr == "True":
                    self.cpp_info.defines.append(f"USE_RTOS=1")
                else:
                    self.cpp_info.defines.append(f"USE_RTOS=0")
            if option == "use_spi_crc":
                if optionstr == "True":
                    self.cpp_info.defines.append(f"USE_SPI_CRC=1")
                else:
                    self.cpp_info.defines.append(f"USE_SPI_CRC=0")
            if option.endswith("_value"):
                self.cpp_info.defines.append(f"{optionstr.upper()}={optionstr}")
            if option == "device":
                self.cpp_info.defines.append(f"{optionstr}")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
