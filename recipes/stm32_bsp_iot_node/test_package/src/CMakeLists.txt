set(APP_NAME test)


find_package(stm32_bsp_iot_node REQUIRED)

set(LINKER_SCRIPT ${CMAKE_CURRENT_LIST_DIR}/linker/STM32L475VGTx_FlASH.ld)

add_executable(${APP_NAME} ${CMAKE_CURRENT_LIST_DIR}/main.cpp)

target_link_libraries(${APP_NAME} PRIVATE stm32_bsp_iot_node::stm32_bsp_iot_node )
set_target_properties(${TARGET_NAME} PROPERTIES LINK_DEPENDS ${LINKER_SCRIPT})
target_link_options(${APP_NAME} PRIVATE -Xlinker -Map=${APP_NAME}.map)