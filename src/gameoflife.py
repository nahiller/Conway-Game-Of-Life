from enum import Enum
from itertools import chain, count

class CellState(Enum): 
    DEAD = 1
    ALIVE = 2

def next_generation_status(cell_state, number_of_alive_neighbors):
    return CellState.ALIVE if number_of_alive_neighbors == 3  or cell_state == CellState.ALIVE and number_of_alive_neighbors == 2 else CellState.DEAD
    
def generate_signal_for_a_cell(cell):
    return [(x, y)
        for x in list(range(cell[0] - 1, cell[0] + 2))
        for y in list(range(cell[1] - 1, cell[1] + 2))
        if(x, y) != cell
    ]

def generate_signal_for_cells(alive_cells): 
    return list(chain(*map(generate_signal_for_a_cell, alive_cells)))

def count_live_neighbors(signals):
    return {signal: signals.count(signal) for signal in signals}

def compute_next_generation(alive_cells):
    signals = count_live_neighbors(generate_signal_for_cells(alive_cells))
    return [cell for cell in signals 
        if next_generation_status(CellState.ALIVE if cell in alive_cells else CellState.DEAD, signals[cell]) == CellState.ALIVE]

def get_bounds(cells):
    x_values = [cell[0] for cell in cells]
    y_values = [cell[1] for cell in cells]
    return [(min(x_values) - 10, min(y_values) - 10), (max(x_values) + 10, max(y_values) + 10)] if bool(cells) else [(0, 0), (100, 100)]