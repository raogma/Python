from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = System._hardware
        p = PowerHardware(name, capacity, memory)
        hardware.append(p)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = System._hardware
        h = HeavyHardware(name, capacity, memory)
        hardware.append(h)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System._hardware
        software = System._software
        h = [x for x in hardware if x.name == hardware_name]
        if not h:
            return "Hardware does not exist"
        h = h[0]
        s = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            h.install(s)
        except Exception:
            return "Software cannot be installed"
        software.append(s)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System._hardware
        software = System._software
        h = [x for x in hardware if x.name == hardware_name]
        if not h:
            return "Hardware does not exist"
        h = h[0]
        s = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            h.install(s)
        except Exception:
            return "Software cannot be installed"
        software.append(s)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System._hardware
        software = System._software
        h = [x for x in hardware if x.name == hardware_name]
        s = [x for x in software if x.name == software_name]
        if h:
            if s:
                h, s = h[0], s[0]
                h.uninstall(s)
                software.remove(s)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        hardware = System._hardware
        software = System._software
        return f'''System Analysis
Hardware Components: {len(hardware)}
Software Components: {len(software)}
Total Operational Memory: {int(sum([x.memory_consumption for x in software]))} / {int(sum([x.memory for x in hardware]))}
Total Capacity Taken: {int(sum([x.capacity_consumption for x in software]))} / {int(sum([x.capacity for x in hardware]))}'''

    @staticmethod
    def system_split():
        res = ''
        hardware = System._hardware
        software = System._software
        for h in hardware:
            res += f'''Hardware Component - {h.name}
Express Software Components: {len([x for x in h.software_components if x.type=='Express'])}
Light Software Components: {len([x for x in h.software_components if x.type=='Light'])}
Memory Usage: {int(sum([x.memory_consumption for x in h.software_components]))} / {int(h.memory)}
Capacity Usage: {int(sum([x.capacity_consumption for x in h.software_components]))} / {int(h.capacity)}
Type: {h.type}\n'''
            names = ", ".join([x.name for x in h.software_components])
            res += f'Software Components: {names if names else None}'
        return res
