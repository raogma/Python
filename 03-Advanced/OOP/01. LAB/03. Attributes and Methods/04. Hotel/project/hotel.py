class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: object):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        self.search_room(room_number).take_room(people)

    def free_room(self, room_number):
        self.search_room(room_number).free_room()

    def search_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room

    def status(self):
        guests = 0
        free = []
        taken = []
        for room in self.rooms:
            guests += room.guests
            if room.is_taken:
                taken.append(room.number)
            else:
                free.append(room.number)
        return f"""Hotel {self.name} has {guests} total guests
Free rooms: {", ".join(map(str, free))}
Taken rooms: {", ".join(map(str, taken))}"""
