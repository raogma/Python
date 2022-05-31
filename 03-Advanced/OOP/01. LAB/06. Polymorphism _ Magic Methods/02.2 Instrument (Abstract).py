from abc import ABC, abstractmethod


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


start_playing = lambda instrument: instrument.play()
