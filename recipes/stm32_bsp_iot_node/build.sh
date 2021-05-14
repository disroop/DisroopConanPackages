conan install -pr:h ../../.profiles/arm-m4-debug -pr:b default -if install --build=missing .
conan build -bf install .   
CMake command: cmake -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE="conan_toolchain.cmake" -DCMAKE_INSTALL_PREFIX="/home/michel/projects/DisroopConanPackages/recipes/stm32_bsp_Iot_node/install/package" "/home/michel/projects/DisroopConanPackages/recipes/stm32_bsp_Iot_node"

conan create -pr:h ../../.profiles/arm-m4-debug -pr:b default --build=missing .
