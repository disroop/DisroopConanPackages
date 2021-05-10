set(LIBRARY_NAME stm32bspiotnodelsm6dsl)

set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/lsm6dsl.c
${CMAKE_CURRENT_LIST_DIR}/lsm6dsl.h)

add_library(${LIBRARY_NAME} OBJECT ${SOURCES})
target_link_directories(${LIBRARY_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR})