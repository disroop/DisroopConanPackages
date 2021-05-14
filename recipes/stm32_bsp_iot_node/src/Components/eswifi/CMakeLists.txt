set(LIBRARY_NAME stm32bspiotnodeeswifi)

set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/es_wifi_conf.h
${CMAKE_CURRENT_LIST_DIR}/es_wifi.c
${CMAKE_CURRENT_LIST_DIR}/es_wifi.h
${CMAKE_CURRENT_LIST_DIR}/es_wifi_io.c
${CMAKE_CURRENT_LIST_DIR}/es_wifi_io.h
${CMAKE_CURRENT_LIST_DIR}/wifi.c
${CMAKE_CURRENT_LIST_DIR}/wifi.h)

add_library(${LIBRARY_NAME} OBJECT ${SOURCES})
target_include_directories(${LIBRARY_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(${LIBRARY_NAME} PUBLIC stm32_hal_l4::stm32_hal_l4)
set(DEFINES -DSPI_INTERFACE_PRIO=${CONAN_OPT_IRQ_SPI_INTERFACE_PRIO})
target_compile_definitions(${LIBRARY_NAME} PUBLIC ${DEFINES})
