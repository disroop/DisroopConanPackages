if (CMAKE_C_COMPILER_ID STREQUAL "GNU")
    set(STARTUP_FILE ${CMAKE_CURRENT_LIST_DIR}/gcc/startup_stm32l476xx.s)
    
elseif (CMAKE_C_COMPILER_ID STREQUAL "IAR")
    set(STARTUP_FILE ${CMAKE_CURRENT_LIST_DIR}/iar/startup_stm32l476xx.s)
else()
    message(FATAL_ERROR "Unsupported Compiler")
endif()
message(INFO " STARTUP_FILE: ${STARTUP_FILE}")

set(SOURCES 
        ${STARTUP_FILE}
        ${CMAKE_CURRENT_LIST_DIR}/system_stm32l4xx.c)

add_library(${LIBRARY_NAME} STATIC ${SOURCES})
target_include_directories(${LIBRARY_NAME} PUBLIC ${CORE_DEVICE_DIR}/Include)
target_link_libraries(${LIBRARY_NAME} PRIVATE stm32_cmsis_device_l4::stm32_cmsis_device_l4)