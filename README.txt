Type paver game in the terminal
Follow game with the cells you want to be alive at the start of the game
Each cell should be a string of a tuple consisting of two integers separated by a comma

Example to create a block:
paver game '(0, 0)' '(0, 1)' '(1, 0)' '(1, 1)'

Example to create glider:
paver game '(1, 1)' '(2, 2)' '(0, 3)' '(1, 3)' '(2, 3)'

Example to create penta-oscillator:
paver game '(0, 0)' '(0, 1)' '(-1, 2)' '(1, 2)' '(0, 3)' '(0, 4)' '(0, 5)' '(0, 6)' '(-1, 7)' '(1, 7)' '(0, 8)' '(0, 9)'