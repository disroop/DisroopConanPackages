import os
from conans import ConanFile, load
from conans.model import Generator

class cmake_vars(Generator):

    def __init__(self, conanfile):
        self.conanfile = conanfile
        self.toolchainfile=""
        self._deps_build_info = conanfile.deps_cpp_info
        self._deps_env_info = conanfile.deps_env_info
        self._env_info = conanfile.env_info
        self._deps_user_info = conanfile.deps_user_info

    def append(self, key,value):
        if value == "TRUE" or value == "FALSE":
            self.toolchainfile += f'set({key} {value})\n';
        else:
            self.toolchainfile += f'set({key} "{value}")\n';

    def append_header(self, Title):
        self.toolchainfile += f"#####################################################\n";
        self.toolchainfile += f"### {Title}\n";
        self.toolchainfile += f"#####################################################\n";

    def publish_env(self,environment):
        for key in environment:
            if key != "PATH":
                self.append(key,environment[key])

    def publish_options(self, options):
        for key in options.fields:
            optionstr = "CONAN_OPT_"+str(key)
            valuestr = str(options.get_safe(f"{key}"))
            self.append(optionstr.upper(),valuestr.upper())

    @property
    def filename(self):
        return "cmake_vars.cmake"

    @property
    def content(self):
        self.append_header("Conan Environment Variables")
        self.publish_env(self.conanfile.env)
        self.append_header("Conan Options")
        self.publish_options(self.conanfile.options)
        return self.toolchainfile;

class CmakeVarExport(ConanFile):
     name = "cmake_vars"
     version = "1.0.0"
     url = "TODO"
     description = "This is a toolchain generator which exports environment variables and options from a conanfile."
     license = "MIT"