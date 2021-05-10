set(LIBRARY_NAME stm32bspiotnodelis3mdl)

set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/lis3mdl.c
${CMAKE_CURRENT_LIST_DIR}/lis3mdl.h)

add_library(${LIBRARY_NAME} OBJECT ${SOURCES})
target_link_directories(${LIBRARY_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR})