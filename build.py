import os
import sys
import traceback
from contextlib import contextmanager


def run(cmd, assert_error=False):
    print("*********** Running: %s" % cmd)
    ret = os.system(cmd)
    if ret == 0 and assert_error:
        raise Exception("Command unexpectedly succeeded: %s" % cmd)
    if ret != 0 and not assert_error:
        raise Exception("Failed command: %s" % cmd)


@contextmanager
def chdir(path):
    current_path = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(current_path)


def execute(function):
    try:
        function()
    except:
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    run(f'conan export cmake_vars')
    run(f'conan export gcc_arm_none_eabi')
    run(f'conan export stm32_cmsis_core')
    run(f'conan export stm32_cmsis_device_l4')
    run(f'conan export stm32_hal_l4')
    run(f'conan create stm32_cmsis_core --build=missing')
    run(f'conan create stm32_hal_l4 --build=missing')
