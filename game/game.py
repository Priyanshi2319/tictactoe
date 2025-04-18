from game.board import Board
from game.player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_player_index = 0
        
# Game class handles the drama between X and O 

    def setup_players(self):
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        self.players = [Player(name1, 'X'), Player(name2, 'O')]

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        self.setup_players()
        self.board.print_board()

        while True:
            player = self.players[self.current_player_index]
            print(f"{player.name}'s turn ({player.symbol})")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            if not self.board.place_move(row, col, player.symbol):
                print("Invalid move. Try again.")
                continue

            self.board.print_board()

            if self.board.check_winner(player.symbol):
                print(f"🎉 {player.name} wins!")
                break
            if self.board.is_full():
                print("It's a draw!")
                break

            self.switch_player()
