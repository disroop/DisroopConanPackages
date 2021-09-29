cmake_minimum_required(VERSION 3.16)

project(STM32_HAL_L4 C)
set(CMAKE_C_STANDARD 99)

set(LIBRARY_NAME stm32_hal_l4)
set(STM_HAL_DIR ${CMAKE_CURRENT_LIST_DIR}/hal_driver)

find_package(stm32_cmsis_core REQUIRED)
find_package(stm32_cmsis_device_l4 REQUIRED)

set(SOURCES 
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_adc_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_adc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_can.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_comp.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_cortex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_crc_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_crc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_cryp_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_cryp.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dac_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dac.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dcmi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dfsdm_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dfsdm.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dma_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dma.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dma2d.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_dsi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_exti.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_firewall.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_flash_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_flash_ramfunc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_flash.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_gfxmmu.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_gpio.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_hash_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_hash.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_hcd.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_i2c_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_i2c.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_irda.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_iwdg.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_lcd.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_lptim.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_ltdc_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_ltdc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_mmc_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_mmc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_nand.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_nor.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_opamp_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_opamp.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_ospi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_pcd_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_pcd.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_pka.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_pssi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_pwr_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_pwr.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_qspi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_rcc_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_rcc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_rng_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_rng.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_rtc_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_rtc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_sai_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_sai.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_sd_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_sd.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_smartcard_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_smartcard.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_smbus_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_smbus.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_spi_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_spi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_sram.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_swpmi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_tim_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_tim.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_tsc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_uart_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_uart.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_usart_ex.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_usart.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal_wwdg.c
    ${STM_HAL_DIR}/Src/stm32l4xx_hal.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_adc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_comp.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_crc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_crs.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_dac.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_dma.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_dma2d.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_exti.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_fmc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_gpio.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_i2c.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_lptim.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_lpuart.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_opamp.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_pka.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_pwr.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_rcc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_rng.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_rtc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_sdmmc.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_spi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_swpmi.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_tim.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_usart.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_usb.c
    ${STM_HAL_DIR}/Src/stm32l4xx_ll_utils.c)
# set defines
set(DEFINES)
set(DEFINES -DEXTERNAL_SAI1_CLOCK_VALUE=${CONAN_OPT_EXTERNAL_SAI1_CLOCK_VALUE} ${DEFINES}) 
set(DEFINES -DEXTERNAL_SAI2_CLOCK_VALUE=${CONAN_OPT_EXTERNAL_SAI2_CLOCK_VALUE} ${DEFINES}) 
set(DEFINES -DHSE_STARTUP_TIMEOUT=${CONAN_OPT_HSE_STARTUP_TIMEOUT}  ${DEFINES}) 
set(DEFINES -DHSE_VALUE=${CONAN_OPT_HSE_VALUE}                      ${DEFINES}) 
set(DEFINES -DHSI_VALUE=${CONAN_OPT_HSI_VALUE}                      ${DEFINES}) 
set(DEFINES -DLSE_STARTUP_TIMEOUT=${CONAN_OPT_LSE_STARTUP_TIMEOUT}  ${DEFINES}) 
set(DEFINES -DLSE_VALUE=${CONAN_OPT_LSE_VALUE}                      ${DEFINES}) 
set(DEFINES -DLSI_VALUE=${CONAN_OPT_LSI_VALUE}                      ${DEFINES}) 
set(DEFINES -DMSI_VALUE=${CONAN_OPT_MSI_VALUE}                      ${DEFINES}) 
set(DEFINES -DTICK_INT_PRIORITY=${CONAN_OPT_TICK_INT_PRIORITY}      ${DEFINES}) 
set(DEFINES -DVDD_VALUE=${CONAN_OPT_VDD_VALUE}                      ${DEFINES}) 
if(${CONAN_OPT_HAL_ADC_MODULE_ENABLED})
    set(DEFINES HAL_ADC_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_CORTEX_MODULE_ENABLED})
    set(DEFINES HAL_CORTEX_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_FLASH_MODULE_ENABLED})
    set(DEFINES HAL_FLASH_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_GPIO_MODULE_ENABLED})
    set(DEFINES HAL_GPIO_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_MODULE_ENABLED})
    set(DEFINES HAL_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_NAND_MODULE_ENABLED})
    set(DEFINES HAL_NAND_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_NOR_MODULE_ENABLED})
    set(DEFINES HAL_NOR_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_CAN_LEGACY_MODULE_ENABLED})
    set(DEFINES HAL_CAN_LEGACY_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_CAN_MODULE_ENABLED})
    set(DEFINES HAL_CAN_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_COMP_MODULE_ENABLED})
    set(DEFINES HAL_COMP_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_CRC_MODULE_ENABLED})
    set(DEFINES HAL_CRC_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_CRYP_MODULE_ENABLED})
    set(DEFINES HAL_CRYP_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_DAC_MODULE_ENABLED})
    set(DEFINES HAL_DAC_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_DFSDM_MODULE_ENABLED})
    set(DEFINES HAL_DFSDM_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_DMA_MODULE_ENABLED})
    set(DEFINES HAL_DMA_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_RTC_MODULE_ENABLED})
    set(DEFINES HAL_RTC_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_PWR_MODULE_ENABLED})
    set(DEFINES HAL_PWR_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_RCC_MODULE_ENABLED})
    set(DEFINES HAL_RCC_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_HCD_MODULE_ENABLED})
    set(DEFINES HAL_HCD_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_I2C_MODULE_ENABLED})
    set(DEFINES HAL_I2C_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_IRDA_MODULE_ENABLED})
    set(DEFINES HAL_IRDA_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_IWDG_MODULE_ENABLED})
    set(DEFINES HAL_IWDG_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_LCD_MODULE_ENABLED})
    set(DEFINES HAL_LCD_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_LPTIM_MODULE_ENABLED})
    set(DEFINES HAL_LPTIM_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_OPAMP_MODULE_ENABLED})
    set(DEFINES HAL_OPAMP_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_PCD_MODULE_ENABLED})
    set(DEFINES HAL_PCD_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_QSPI_MODULE_ENABLED})
    set(DEFINES HAL_QSPI_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_SAI_MODULE_ENABLED})
    set(DEFINES HAL_SAI_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_SD_MODULE_ENABLED})
    set(DEFINES HAL_SD_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_SMARTCARD_MODULE_ENABLED})
    set(DEFINES HAL_SMARTCARD_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_SMBUS_MODULE_ENABLED})
    set(DEFINES HAL_SMBUS_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_SPI_MODULE_ENABLED})
    set(DEFINES HAL_SPI_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_SRAM_MODULE_ENABLED})
    set(DEFINES HAL_SRAM_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_SWPMI_MODULE_ENABLED})
    set(DEFINES HAL_SWPMI_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_TIM_MODULE_ENABLED})
    set(DEFINES HAL_TIM_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_TSC_MODULE_ENABLED})
    set(DEFINES HAL_TSC_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_UART_MODULE_ENABLED})
    set(DEFINES HAL_UART_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_USART_MODULE_ENABLED})
    set(DEFINES HAL_USART_MODULE_ENABLED ${DEFINES}) 
endif()
if(${CONAN_OPT_HAL_WWDG_MODULE_ENABLED})
    set(DEFINES HAL_WWDG_MODULE_ENABLED ${DEFINES}) 
endif()

if(${CONAN_OPT_INSTRUCTION_CACHE_ENABLE})
    set(DEFINES INSTRUCTION_CACHE_ENABLE=1 ${DEFINES}) 
else()
    set(DEFINES INSTRUCTION_CACHE_ENABLE=0 ${DEFINES})
endif()
if(${CONAN_OPT_PREFETCH_ENABLE})
    set(DEFINES PREFETCH_ENABLE=1 ${DEFINES}) 
else()
    set(DEFINES PREFETCH_ENABLE=0 ${DEFINES})
endif()
if(${CONAN_OPT_USE_FULL_ASSERT})
    set(DEFINES USE_FULL_ASSERT=1 ${DEFINES}) 
else()
    set(DEFINES USE_FULL_ASSERT=0 ${DEFINES})
endif()
if(${CONAN_OPT_USE_RTOS})
    set(DEFINES USE_RTOS=1 ${DEFINES}) 
else()
    set(DEFINES USE_RTOS=0 ${DEFINES})
endif()
if(${CONAN_OPT_USE_SPI_CRC})
    set(DEFINES USE_SPI_CRC=1 ${DEFINES}) 
else()
    set(DEFINES USE_SPI_CRC=0 ${DEFINES})
endif()
string(REPLACE XX
       xx CONAN_OPT_DEVICE_MAN 
       ${CONAN_OPT_DEVICE})

set(DEFINES ${CONAN_OPT_DEVICE_MAN} ${DEFINES})

if(${CMAKE_CROSSCOMPILING})
    add_library(${LIBRARY_NAME} STATIC ${SOURCES})
    target_link_libraries(${LIBRARY_NAME} PRIVATE stm32_cmsis_core::stm32_cmsis_core stm32_cmsis_device_l4::stm32_cmsis_device_l4)
    target_include_directories(${LIBRARY_NAME} PUBLIC ${STM_HAL_DIR}/Inc ${CMAKE_CURRENT_LIST_DIR}/include)
    target_compile_definitions(${LIBRARY_NAME} PUBLIC ${DEFINES})
endif()
