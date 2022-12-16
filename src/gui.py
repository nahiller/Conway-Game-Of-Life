import PySimpleGUI as sg    
import gameoflife


class GUI:
    def __init__(self, cells):
        self.previous_cells = []
        self.cells = cells
        self.bounds = gameoflife.get_bounds(self.cells)

        layout = [
            [sg.Graph(canvas_size=(600, 600), 
            graph_bottom_left = (self.bounds[0][1] * 10, self.bounds[1][0] * 10), 
            graph_top_right = (self.bounds[1][1] * 10, self.bounds[0][0] * 10), background_color='black', key='graph')],
            [sg.Button("Start")]]     

        self.window = sg.Window("Conway's Game of Life", layout, finalize=True)  
        self.graph = self.window['graph'] 

    def create_live_cells_on_grid(self):
        self.displayed_cells = [self.graph.DrawRectangle((cell[1] * 10, cell[0] * 10), 
            (cell[1] * 10 + 10, cell[0] * 10 + 10),
            fill_color = 'white', line_color = 'grey') for cell in self.cells]

    def start_GUI(self):
        start = False

        while bool(self.cells) is True or set(self.cells) is not set(self.previous_cells):  
            event, values = self.window.read(timeout=500)  

            if event == sg.WIN_CLOSED:      
                break 

            elif start:
                self.graph.erase()
                self.previous_cells = self.cells
                self.cells = gameoflife.compute_next_generation(self.cells)
                self.displayed_cells = self.create_live_cells_on_grid()

            elif event == 'Start':
                start = True
        
        if bool(self.cells) is True or set(self.cells) is not set(self.previous_cells):
            event = self.window.read()
                       