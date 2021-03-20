cmake_minimum_required(VERSION 3.16)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)

project(STM_CMSIS_DEVICE_L4 C ASM)

set(CMAKE_C_STANDARD 99)

conan_basic_setup()

set(LIBRARY_NAME ${CONAN_PACKAGE_NAME})
set(CORE_DEVICE_DIR ${CMAKE_CURRENT_BINARY_DIR})

if(${CMAKE_SYSTEM_NAME} STREQUAL "Generic")
    if (CMAKE_C_COMPILER_ID STREQUAL "GNU")
        set(STARTUP_FILE "${CORE_DEVICE_DIR}/Source/Templates/gcc/startup_stm32l476xx.s")
        
    elseif (CMAKE_C_COMPILER_ID STREQUAL "IAR")
        set(STARTUP_FILE "${CORE_DEVICE_DIR}/Source/Templates/iar/startup_stm32l476xx.s")
    else()
        message(FATAL_ERROR "Unsupported Compiler")
    endif()
    message(INFO " STARTUP_FILE: ${STARTUP_FILE}")
    
    set(SOURCES 
            ${STARTUP_FILE}
            ${CORE_DEVICE_DIR}/Source/Templates/system_stm32l4xx.c)
    
    add_library(${LIBRARY_NAME} STATIC ${SOURCES})
    target_include_directories(${LIBRARY_NAME} PUBLIC ${CORE_DEVICE_DIR}/Include)
    target_compile_definitions(${LIBRARY_NAME} PUBLIC STM32L476xx)
endif()
