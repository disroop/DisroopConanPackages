import json


from .signature import Signature
from .buildersettings import BuilderSettings

class ConfigReader:
    def __init__(self, path):
        self.path = path
        self._configurations = [BuilderSettings()]
        self._signature = Signature()

    def read(self):
        with open(self.path) as json_file:
            data = json.load(json_file)
            if 'version' in data:
                self._signature.version = data['version']
            if 'user' in data:
                self._signature.user = data['user']
            if 'channel' in data:
                self._signature.channel = data['channel']
            if 'config' in data:
                self._configurations = []
                for p in data['config']:
                    configuration = BuilderSettings()
                    if 'hostprofile' in p:
                        configuration.host_profile = p['hostprofile']
                    if 'buildprofile' in p:
                        configuration.build_profile = p['buildprofile']
                    if 'hostsettings' in p:
                        configuration.host_settings = p['hostsettings']
                    if 'excludes' in p:
                        configuration.excludes = p['excludes']
                    if 'includes' in p:
                        configuration.includes = p['includes']
                    self._configurations.append(configuration)

    def get_configurations(self):
        return self._configurations

    def get_signature(self):
        return self._signature
