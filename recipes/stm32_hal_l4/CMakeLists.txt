PROJECT(stm32wb55_runtime C)
cmake_minimum_required(VERSION 3.16)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)

project(STM32_HAL_L4 C)

set(CMAKE_C_STANDARD 99)

conan_basic_setup()

set(LIBRARY_NAME ${CONAN_PACKAGE_NAME})
set(STM_HAL_DIR ${CMAKE_CURRENT_LIST_DIR}/hal_driver)

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

if(${CMAKE_SYSTEM_NAME} STREQUAL "Generic")
    add_library(${LIBRARY_NAME} STATIC ${SOURCES})
    target_include_directories(${LIBRARY_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR}/include ${STM_HAL_DIR}/Inc ${CONAN_INCLUDE_DIRS})
    target_compile_definitions(${LIBRARY_NAME} PUBLIC ${CONAN_DEFINES})
endif()
