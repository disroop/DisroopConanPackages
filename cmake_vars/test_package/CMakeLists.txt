# Set the minimum version of CMake that can be used
# To find the cmake version run
# $ cmake --version

cmake_minimum_required(VERSION 3.16 FATAL_ERROR)
#Include Conan
include(${CMAKE_CURRENT_BINARY_DIR}/conan_env_toolchain.cmake)
include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
# Set the project name
project(test CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_C_STANDARD 99)

conan_basic_setup()


if(CONAN_OPT_SIMULATOR)
    add_executable(${PROJECT_NAME} ${CMAKE_CURRENT_LIST_DIR}/main_sim.cpp)
else()
    add_executable(${PROJECT_NAME} ${CMAKE_CURRENT_LIST_DIR}/main.cpp)
endif()