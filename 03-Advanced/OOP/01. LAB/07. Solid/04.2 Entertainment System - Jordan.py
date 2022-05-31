class Connector:
    def connect(self, other): ...


class PowerMixin:
    ...


class HDMIConnector:
    ...


class RCAConnector:
    ...


class EthernetConnector:
    ...


class PowerConnector:
    ...


class Television(PowerMixin, Connector):
    def __init__(self):
        self.rca = RCAConnector()
        self.hdmi = HDMIConnector()
        self.ethernet = EthernetConnector()


class DVDPlayer(PowerMixin, Connector):
    def __init__(self):
        self.hdmi = HDMIConnector()


class GameConsole(PowerMixin, Connector):
    def __init__(self):
        self.hdmi = HDMIConnector()
        self.ethernet = EthernetConnector()


class Router(PowerMixin, Connector):
    def __init__(self):
        self.ethernet = EthernetConnector()


tv = Television()
game_console = GameConsole()

tv.hdmi.connect(game_console.hdmi)
