class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: object):
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: object):
        if software in self.software_components:
            self.software_components.remove(software)

