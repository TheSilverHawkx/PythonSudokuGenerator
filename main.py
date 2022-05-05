import sudoku
import gui

game_window = gui.GameWindow()
sudoku_table = sudoku.Table(3)

sudoku_table.new_game('easy')

game_window.root.mainloop()

