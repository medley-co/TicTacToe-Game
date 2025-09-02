# Tic-Tac-Toe Game (Python)

A strategic twist on the classic Tic-Tac-Toe game, built in Python. Players place pieces of varying sizes on a 3×3 grid, trying to outsmart their opponent. Larger pieces can cover smaller ones, adding strategy and depth. Align three of your symbols—O or X—to win, or face a stalemate.

---

## Features

- Two-player game (O vs X) on a 3×3 grid
- Pieces have different sizes; larger pieces can cover smaller ones
- Automatic win detection (rows, columns, diagonals)
- Stalemate detection when no valid moves remain
- Console-based, simple user interface with clear prompts

---

## Requirements

- Python 3.8+

---

## Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/medley-co/TicTacToe-Game.git
cd tictactoe
```

Run the game:

```bash
python tictactoe.py
```

## How to Play

1. The board is displayed with rows and columns numbered 1–3.
2. Each player has a set of numbered pieces (1–6 by default).
3. Enter your move in the format: ```row col size```
   Example: 1 3 2 places a piece of size 2 in row 1, column 3.
6. Type h anytime to display the help message.
7. The game continues until one player aligns three symbols or a stalemate occurs.
8. After the game, you can choose to play again by typing y.

## Example Board

```yaml
O has: 1, 2, 3, 4, 5, 6
X has: 1, 2, 3, 4, 5, 6

   1  2  3
  ---------
1|   |   |   |
  ---------
2|   |   |   |
  ---------
3|   |   |   |
  ---------
```

## License
This project is licensed under the MIT license.
```sql
MIT License

Copyright (c) 2025 [medley-co]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
