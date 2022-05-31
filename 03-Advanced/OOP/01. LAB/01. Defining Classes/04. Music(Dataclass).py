from dataclasses import dataclass


@dataclass
class Music:
    title: str
    artist: str
    lyrics: str

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return f'{self.lyrics}'


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())