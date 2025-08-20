# Tic-Tac-Toe Game (PyQt5)

A simple **Tic-Tac-Toe (XOX)** game built with **Python** and **PyQt5** as part of a self-improvement exercise (2022).  
This is a desktop GUI game where two players can take turns to play.

---

## Features

- **Two-player game (local)**
- **Clear GUI with PyQt5**
- **Restart button to reset the board**
- **Automatic turn display ("X's turn" / "O's turn")**
- **Winner and draw detection**

---

## Requirements

- **Python 3.6+**
- **PyQt5**

Install dependencies using pip:
```bash
pip install PyQt5
```

---

## How to Run

1. Clone or download the project:
```bash
git clone https://github.com/Brkberber/Tic-Tac-Toe-Game.git
cd Tic-Tac-Toe-Game
```

2. Make sure the following files are in the same folder:
   - `main.py` (game logic)
   - `xox.py` (auto-generated PyQt5 UI file)

3. Run the game:
```bash
python main.py
```

---

## Gameplay

- **X always starts first.**
- Players take turns clicking buttons.
- The game announces **who wins** or if it's a **draw**.
- The **Restart button** clears the board.

---

## File Structure

```
Tic-Tac-Toe-Game/
│
├── main.py       # Main game window and logic
├── xox.py        # PyQt5 UI file (auto-generated from Qt Designer)
└── README.md     # Project documentation
```

---

## Future Improvements

- Add AI player mode (single-player vs computer)
- Better UI styling and animations
- Keep score between rounds

---

## License

This project is open-source and free to use for learning purposes.
