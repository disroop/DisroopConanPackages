cmake_minimum_required(VERSION 3.16)
include(${CMAKE_CURRENT_BINARY_DIR}/cmake_vars.cmake)
include(${CMAKE_CURRENT_BINARY_DIR}/conan_toolchain.cmake)
project(STM_BSP_IOT_NODE C ASM)

set(CMAKE_C_STANDARD 99)

find_package(stm32_hal_l4 REQUIRED)
#if(${CMAKE_SYSTEM_NAME} STREQUAL "Generic")
    add_subdirectory(src)
#endif()
