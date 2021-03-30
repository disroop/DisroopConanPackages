from .signature import Signature
from .package import Package
from pathlib import Path


class Runner:

    def __init__(self,root_path, signature=Signature()):
        self.packages = self._get_all_packages(root_path,signature=Signature())

    def create_all(self, configurations):
        for config in configurations:
            print("#######################################\n"
                  "########### create packages ###########\n"
                  f"# host profile:  {config.hostprofile}\n"
                  f"# build profile: {config.buildprofile}\n"
                  f"# host settings: {config.hostsettings}\n"
                  f"# includes:      {config.includes}\n"
                  f"# excludes:      {config.excludes}\n"
                  "#######################################\n")
            for package in self.packages:
                if package.is_withing_scope(config):
                    package.create(config)

    # relative_path = path.absolute()
    # eprint(package.pattern)

    # package_signature = get_package_signature()
    # package_pattern=f'{package_signature.name}/{package_signature.version}@{package_signature.user}/{package_signature.channel}'
    ### conan_command_line.create(package.path,test_build_folder=f'/tmp/{package.pattern}/tbf')
    # TODO:profiles_names =HOST, profiles_build=build
    # conan_command_line.authenticate()
    # conan_command_line.remote_add()
    # conan_command_line.upload(package_pattern)
    # print(f'SUCCESS: {package_pattern}')

    def _get_all_packages(self, root_path, signature=Signature()):
        conan_packages = []
        for path in Path(root_path).rglob('conanfile.py'):
            path = str(path.absolute())
            if "test_package" not in path:
                conan_packages.append(Package(signature, path))
        return conan_packages

    def export_all(self):
        for package in self.packages:
            package.export()

    def get_all_sources(self):
        print(
            "#######################################\n"
            "########### download sources ##########\n"
            "#######################################\n")
        for package in self.packages:
            package.source()

    def remove_all_sources(self):
        text = ()
        print("#######################################\n"
              "########### remove sources ############\n"
              "#######################################\n")
        for package in self.packages:
            package.source_remove()
