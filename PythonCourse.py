import module4

while True:
    module4.TicTacToe.Play()
    again = input("Play again? (y/any)")
    if again.upper() != "Y":
        break