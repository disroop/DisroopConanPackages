from conans import ConanFile
from conans import tools
from conan.tools.cmake import CMake, CMakeDeps
import os


project_version = os.getenv("PROJECT_VERSION", "snapshot")
project_username = os.getenv("CONAN_USERNAME", "disroop")
project_channel = os.getenv("CONAN_CHANNEL", "development")
class Stm32BspIotNodeTest(ConanFile):
    name = "test_cmake_vars"
    version = f"{project_version}"
    license = "closed"
    url = "TODO"
    default_channel = f"{project_channel}"
    default_user = f"{project_username}"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps","CMakeToolchain"
    exports_sources = "src/*", "CMakeLists.txt"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        
    def test(self):
        if tools.cross_building(self.settings):
            bin_path = os.path.join("src", "test")
            if not os.path.isfile(bin_path):
                raise FileNotFoundError(bin_path)