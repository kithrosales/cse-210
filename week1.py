# Author: Kith Rosales


# Application
class TicTacToe:
    def __init__(self) -> None:
        self.running = True
        self.turn = ['X', 'O']
        self.flag = 0
        self.grid = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]

    def check_rows(self):
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2]:
            return self.grid[0][0]
        elif self.grid[1][0] == self.grid[1][1] == self.grid[1][2]:
            return self.grid[1][0]
        elif self.grid[2][0] == self.grid[2][1] == self.grid[2][2]:
            return self.grid[2][0]
        else:
            return None
    
    def check_columns(self):
        if self.grid[0][0] == self.grid[1][0] == self.grid[2][0]:
            return self.grid[0][0]
        elif self.grid[0][1] == self.grid[1][1] == self.grid[2][1]:
            return self.grid[1][0]
        elif self.grid[0][2] == self.grid[1][2] == self.grid[2][2]:
            return self.grid[2][0]
        else:
            return None
    
    def check_diagonals(self):
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return self.grid[0][0]
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return self.grid[1][0]
        else:
            return None

    def move(self, i):
        self.grid[int(i/3)][int(i%3)] = self.get_current_turn

        if self.check_rows() is not None:
            self.running = False

        if self.check_columns() is not None:
            self.running = False

        if self.check_diagonals() is not None:
            self.running = False
            
        self.flag = self.flag + 1
        if self.flag == 9:
            self.running = False

    @property
    def get_current_turn(self):
        return self.turn[self.flag % 2]

    def display(self):
        print(f"{self.grid[0][0]}|{self.grid[0][1]}|{self.grid[0][2]}")
        print("-+-+-")
        print(f"{self.grid[1][0]}|{self.grid[1][1]}|{self.grid[1][2]}")
        print("-+-+-")
        print(f"{self.grid[2][0]}|{self.grid[2][1]}|{self.grid[2][2]}")
        
        print("")


# Main Function
def main(game: TicTacToe):
    while game.running:
        game.display()
        print(f"{game.get_current_turn}'s turn to choose a square (1-9): ", end='')
        move = int(input(''))
        if(game.flag == 8):
            break
        game.move(move - 1)
    
    print("\n\n-+-+-")
    game.display()
    print("Good game. Thanks for playing!")


if __name__ == "__main__":
    game = TicTacToe()
    main(game)