from .signature import Signature
from .package import Package
from pathlib import Path


class Runner:
    def __init__(self):
        pass

    def create_all(self, conan_packages, configurations):
        config_counter = 0
        for config in configurations:
            config_counter = config_counter + 1;
            print(f"CONFIG {config_counter}")
            for package in conan_packages:
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

    def export_all(self, conan_packages):
        for package in conan_packages:
            package.export()
