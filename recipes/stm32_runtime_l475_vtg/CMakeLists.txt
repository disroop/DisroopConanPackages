cmake_minimum_required(VERSION 3.16)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
include(${CMAKE_CURRENT_BINARY_DIR}/conan_toolchain.cmake)

project(STM_RUNTIME_L475 C ASM)

set(CMAKE_C_STANDARD 99)

find_package(stm32_cmsis_device_l4 REQUIRED)

add_subdirectory(src)




