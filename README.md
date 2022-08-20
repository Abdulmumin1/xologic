# xologic

a tic tac toe game logic to check the win on a game board!

## Usage

```python

from xologic import Logic

game_logic = Logic(board_size=3)

# update the board

game_logic.board[0] = 'x'
game_logic.board[3] = 'o'

#check if there is a win

win = game_logic.check()
print(f"{win['winner']} wins")
# if you create a custom board

win = game_logic.check(custom_board, board_size)
```
