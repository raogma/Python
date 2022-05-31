class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player: object):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name):
        searched_player = [x for x in self.players if x.name == player_name]
        if searched_player:
            searched_player = searched_player[0]
            self.players.remove(searched_player)
            return searched_player
        return f"Player {player_name} not found"
