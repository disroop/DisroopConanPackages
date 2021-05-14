set(LIBRARY_NAME stm32bspiotnode)
set(SOURCES
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_accelero.c
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_accelero.h
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_gyro.c
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_gyro.h
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_hsensor.c
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_hsensor.h
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_magneto.c
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_magneto.h
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_psensor.c
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_psensor.h
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_qspi.c
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_qspi.h
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_tsensor.c
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01_tsensor.h
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01.c
${CMAKE_CURRENT_LIST_DIR}/stm32l475e_iot01.h)

add_library(${LIBRARY_NAME} STATIC ${SOURCES} 
    $<TARGET_OBJECTS:stm32bspiotnodehts221>
    $<TARGET_OBJECTS:stm32bspiotnodelis3mdl>
    $<TARGET_OBJECTS:stm32bspiotnodelps22hb>
    $<TARGET_OBJECTS:stm32bspiotnodelsm6dsl>)

target_link_libraries(${LIBRARY_NAME} PRIVATE stm32_hal_l4::stm32_hal_l4)