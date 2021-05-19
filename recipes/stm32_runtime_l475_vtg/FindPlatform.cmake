cmake_minimum_required(VERSION 3.16)

set(PLATFORM_FOUND TRUE)

set(FLASH_SCRIPT "flash.jLink")

function(create_jlinkflash_script TARGET_NAME)
    add_custom_target(
        create-flash-script ALL
        DEPENDS ${TARGET_NAME}
        COMMAND echo "erase" > ${FLASH_SCRIPT}
        COMMAND echo "loadfile  ${TARGET_NAME}.hex" >> ${FLASH_SCRIPT}
        COMMAND echo "r" >> ${FLASH_SCRIPT}
        COMMAND echo "qc" >> ${FLASH_SCRIPT}
        WORKING_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
    )
endfunction(create_jlinkflash_script)

function(add_flash_step)
    if(NOT DEFINED $ENV{JLINK_SERVER})
        add_custom_target(
            flash-hex
            DEPENDS create-flash-script
            COMMAND JLinkExe -IP $ENV{JLINK_SERVER} -Speed 4000 -Device STM32L475VG -si SWD -CommanderScript ${FLASH_SCRIPT} -Log flash.log -ExitOnError 1
            WORKING_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
        )
    else()
        message(INFO No JLinkServer IP is set. No flash step added.)
    endif()
endfunction(add_flash_step)

function(setup_runtime TARGET_NAME LINKER_FILE LINKER_FLAGS)
    target_link_options(${TARGET_NAME} PUBLIC ${LINKER_FLAGS} -T ${LINKER_FILE} -Xlinker -Map=${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${FILENAME}.map)

    add_custom_command(TARGET ${TARGET_NAME} POST_BUILD
        COMMAND $ENV{OBJCOPY} -O ihex ${FILENAME} ${FILENAME}.hex
        COMMAND $ENV{OBJCOPY} -O binary ${FILENAME} ${FILENAME}.bin
        WORKING_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
        COMMENT "Create Target-Application")
endfunction(setup_runtime)

function(target_setup_runtime TARGET_NAME)
    setup_runtime(${TARGET_NAME} "STM32L475VGTx_FLASH.ld" "")
    create_jlinkflash_script(${TARGET_NAME})
    add_flash_step()
endfunction(target_setup_runtime)