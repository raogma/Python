class PowerMixin:
    def plug_in_power(self):
        self.power.connect_to_power_outlet(self)


class HDMIConnector:
    def connect_via_hdmi_cable(self, device): pass


class RCAConnector:
    def connect_via_rca_cable(self, device): pass


class EthernetConnector:
    def connect_via_ethernet_cable(self, device): pass


class PowerConnector:
    def connect_to_power_outlet(self, device): pass


class Television(PowerMixin):
    def __init__(self):
        self.rca = RCAConnector()
        self.hdmi = HDMIConnector()
        self.ethernet = EthernetConnector()

    def connect_to_dvd(self, dvd_player):
        self.rca.connect_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.hdmi.connect_via_hdmi_cable(game_console)

    def connect_to_router(self, router):
        self.ethernet.connect_via_ethernet_cable(router)


class DVDPlayer(PowerMixin):
    def __init__(self):
        self.hdmi = HDMIConnector()

    def connect_to_tv(self, television):
        self.hdmi.connect_via_hdmi_cable(television)


class GameConsole(PowerMixin):
    def __init__(self):
        self.hdmi = HDMIConnector()
        self.ethernet = EthernetConnector()

    def connect_to_tv(self, television):
        self.hdmi.connect_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.ethernet.connect_via_ethernet_cable(router)


class Router(PowerMixin):
    def __init__(self):
        self.ethernet = EthernetConnector()

    def connect_to_tv(self, television):
        self.ethernet.connect_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.ethernet.connect_via_ethernet_cable(game_console)
