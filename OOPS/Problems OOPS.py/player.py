class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def player_info(self):
        Player.player_count += 1
        print(f"Player name : {self.name} \nPlayer level : {self.level}")
    
    @classmethod
    def counting(cls):
        print(f"Total player count : {cls.player_count}")

p1 = Player("Rohit Sharma", 10)
p1.player_info()
p2 = Player("Virat Kohli", 10)
p2.player_info()
p3 = Player("Surya", 8)
p3.player_info()
Player.counting()