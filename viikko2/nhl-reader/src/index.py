import requests
from player import Player

class PlayerReader:
    def __init__(self, site):
        self.players = requests.get(site).json()
            
class PlayerStats:
    def __init__(self, stats):
        self.players = [Player(dict) for dict in stats.players]
    
    def top_scorers_by_nationality(self, nationality):
        print(f"Players from {nationality} \n")
        return filter(lambda player: player.nationality == nationality, self.players)


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()