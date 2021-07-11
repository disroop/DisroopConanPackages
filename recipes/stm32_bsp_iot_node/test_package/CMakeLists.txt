# Set the minimum version of CMake that can be used
# To find the cmake version run
# $ cmake --version

cmake_minimum_required(VERSION 3.16 FATAL_ERROR)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
#Include Conan

include(${CMAKE_CURRENT_BINARY_DIR}/conan_toolchain.cmake)
# Set the project name
project(test C)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_C_STANDARD 99)

add_subdirectory(src)

