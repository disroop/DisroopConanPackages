set(LIBRARY_NAME stm32bspiotnodelps22hb)

set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/lps22hb.c
${CMAKE_CURRENT_LIST_DIR}/lps22hb.h)

add_library(${LIBRARY_NAME} OBJECT ${SOURCES})
target_link_directories(${LIBRARY_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR})