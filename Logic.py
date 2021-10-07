class TicTacToe:
    def __init__(self):
        self.grid = {"7":' ',"8":' ',"9":' ',
                    "4":' ',"5":' ',"6":' ',
                    "1":' ',"2":' ',"3":' '}
        self.winning_moves = [["7","8","9"],
                             ["4","5","6"],
                             ["1","2","3"],
                             ["7","4","1"],
                             ["8","5","2"],
                             ["9","6","3"],
                             ["7","5","3"],
                             ["9","5","1"]]
    def display_grid(self):
        print("\n")
        print("\t  {}  |  {}   |  {}".format(self.grid["7"], self.grid["8"], self.grid["9"]))
        print("\t     |      |")
        print('\t_____|______|_____')
        print("\t     |      |")
        print("\t  {}  |  {}   |  {}".format(self.grid["4"], self.grid["5"], self.grid["6"]))
        print('\t_____|______|_____')
        print("\t     |      |")
        print("\t  {}  |  {}   |  {}".format(self.grid["1"], self.grid["2"], self.grid["3"]))
        print("\t     |      |")
        print("\n")
    def game_over(self,turn):
        gg = False
        for i in self.winning_moves:
            if self.grid[i[0]] == self.grid[i[1]] == self.grid[i[2]] == turn:
                gg = True
        return gg
    def game(self):
        turn = "X"
        count = 0
        over = False
        for i in range(0,9):
            self.display_grid()
            if over:
                break
            print("{}'s Turn".format(turn))
            u_in = input("Enter pos to fill : ")
            if self.grid[u_in] == " ":
                self.grid[u_in] = turn
                count = count + 1
            else:
                print("Not Empty")
                continue
            if count>=4:
                if self.game_over(turn):
                    over = True
                    print("CONGRATS {} WINS".format(turn))
            if count == 9:
                print("ITS A DRAW")
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
ttt = TicTacToe()
ttt.game()
