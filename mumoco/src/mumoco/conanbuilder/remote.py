class Remote:
    def __init__(self, name, url, verify_ssl=True, priority=0, force=False):
        self._name = name
        self._url = url
        self._verify_ssl = True
        self._priority = priority
        self._force = False

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def verify_ssl(self):
        return self._verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, val):
        self._verify_ssl = val

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, val):
        self._priority = val

    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, val):
        self._force = val
