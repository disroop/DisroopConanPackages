import os
import sys
import traceback
from contextlib import contextmanager
from tools.disroopbuildhelper import run, chdir


if __name__ == '__main__':
    with chdir(os.path.dirname(os.path.realpath(__file__))):
        run(f'conan export cmake_vars')
        run(f'conan export gcc_arm_none_eabi')
        run(f'conan export stm32_cmsis_core')
        run(f'conan export stm32_cmsis_device_l4')
        run(f'conan export stm32_hal_l4')
    
    
        run(f'conan create stm32_cmsis_core --build=missing')
        run(f'conan create stm32_hal_l4 --build=missing')
        run(f"conan create stm32_cmsis_device_wb  -pr=./.profiles/gcc-arm-none-eabi-9")
    
