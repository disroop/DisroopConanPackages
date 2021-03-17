from conans import ConanFile, CMake
from conans import tools
import os


project_version = os.getenv("PROJECT_VERSION")
project_username = os.getenv("CONAN_USERNAME")
project_channel = os.getenv("CONAN_CHANNEL")

class CmakeVarsGeneratorTest(ConanFile):
    name = "test_cmake_vars"
    version = f"{project_version}"
    license = "closed"
    url = "TODO"
    default_channel = f"{project_channel}"
    default_user = f"{project_username}"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_vars"
    exports_sources = "src/*", "CMakeLists.txt", "test/*"
    options = {"simulator": [True, False],
    }
    default_options = {"simulator": False,
    }
    

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        
    def package_info(self):
        self.cpp_info.libs.append(f"{self.name}") 
    
    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join("bin", "test")
            self.run(bin_path, run_environment=True)