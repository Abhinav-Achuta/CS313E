class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        win_percentage = self.wins/(self.wins+self.losses)
        return win_percentage
    
    # TODO: Define print_standing()
    def print_standing(self):
        win_percentage = self.get_win_percentage()
        print(f"Win percentage: {win_percentage:.2f}")
        if win_percentage > 0.5:
            print(f"Congratulations, Team {self.name} has a winning average!")
        else:
            print(f"Team {self.name} has a losing average.")


if __name__ == "__main__":
    team = Team()
   
    user_name = input()
    user_wins = int(input())
    user_losses = int(input())
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing()