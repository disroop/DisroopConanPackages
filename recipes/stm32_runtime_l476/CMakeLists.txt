cmake_minimum_required(VERSION 3.16)
include(${CMAKE_CURRENT_BINARY_DIR}/conan_toolchain.cmake)

project(STM_RUNTIME_L476 C ASM)

set(CMAKE_C_STANDARD 99)

find_package(stm32_cmsis_device_l4 REQUIRED)

set(LIBRARY_NAME ${CONAN_PACKAGE_NAME})
set(CORE_DEVICE_DIR ${CMAKE_CURRENT_BINARY_DIR})


add_subdirectory(src)
