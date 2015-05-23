import tkinter as tk
import algorithm.sudokuAlgorithm
import pprint

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SQUARE_SIZE = 3
SQUARE_OF_SQUARE_SIZE = 3


class MainWindow:

    def __init__(self):
        #self.root = tk.Tk()
        self.app = Application()
        self.app.master.title("SUDOKU")
        self.app.master.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.app.master.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.app.mainloop()


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.sudoku_algorithm = algorithm.sudokuAlgorithm.SudokuAlgorithm(algorithm.sudokuAlgorithm.DEFAULT)

    def create_widgets(self):

        self.update_button = tk.Button(self, text="Update", fg="black", command=self.update)
        self.update_button.grid(row=1, column=1)

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.quit)
        self.QUIT.grid(row=1, column=2)

        self.print = tk.Button(self, text="print", fg="green", command=self.debug)
        self.print.grid(row=1, column=3)

        self.nine_square = list()
        for r in range(0, SQUARE_SIZE):
            self.nine_square.append([])
            for c in range(0, SQUARE_SIZE):
                self.nine_square[r].append(NineBoxSquare(self, r+2, c+1))

    def update(self):
        numbers = self.get_numbers()
        for row, row_items in enumerate(numbers):
            for column, column_items in enumerate(row_items):
                if numbers[row][column] == '':
                    numbers[row][column] = 0
                else:
                    numbers[row][column] = int(numbers[row][column])
        self.sudoku_algorithm.set_numbers(numbers)
        for row, row_items in enumerate(self.sudoku_algorithm.get_calculated_numbers()):
            for column, possible_numbers in enumerate(row_items):
                square_row = row // 3
                square_column = column // 3
                self.nine_square[square_row][square_column].set_possible_numbers(possible_numbers, row % 3, column % 3)

    def get_number(self, row=0, column=0):
        square_row = row // 3
        square_column = column // 3
        number = self.nine_square[square_row][square_column].get_value(row % 3, column % 3)
        return number

    def get_numbers(self):
        numbers = []
        for row in range(SQUARE_SIZE * SQUARE_OF_SQUARE_SIZE):
            number_row = []
            for column in range(SQUARE_SIZE * SQUARE_OF_SQUARE_SIZE):
                number_row.append(self.get_number(row, column))
            numbers.append(number_row)
        return numbers

    def debug(self):
        pprint.pprint(self.sudoku_algorithm.get_numbers())
        pprint.pprint(self.sudoku_algorithm.get_calculated_numbers())
        pass

class NumberBox(tk.Entry):

    ALLOWED_CHARS = "123456789"

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.old_string = ''
        self.number = tk.StringVar()
        self["textvariable"] = self.number
        self.number.trace('w', lambda nm, idx, mode, var=self.number: self.validate(var))
        self.create_popup_menu()
        self.bind("<Button-3>", self.popup)
        self.possible_numbers = list()

    def popup(self, event):
        self.aMenu.post(event.x_root, event.y_root)

    def get_old_string(self):
        return self.old_string

    def validate(self, text):
        if len(text.get()) == 0:
            self.old_string = text.get()
        elif len(text.get()) == 1:
            if text.get() in self.ALLOWED_CHARS:
                self.old_string = text.get()
            else:
                text.set(self.old_string)
        else:
            text.set(self.old_string)

    def get_number(self):
        return self.number.get()

    def set_number(self, value=0):
        return self.number.set(value)

    def set_possible_numbers(self, numbers=[]):
        self.aMenu.destroy()
        self.possible_numbers = numbers
        self.aMenu = tk.Menu(self, tearoff=0)
        if isinstance(self.possible_numbers, list):
            solutions = [str(i) for i in self.possible_numbers]
            self.aMenu.add_command(label="".join(solutions), command=self.hello)

    def get_possible_numbers(self):
        return self.possible_numbers

    @staticmethod
    def hello():
        pass

    def create_popup_menu(self):
        self.aMenu = tk.Menu(self, tearoff=0)


class NineBoxSquare:

    def __init__(self, master=None, row=0, column=0):
        self.frame = tk.Frame(master, bd=4)
        self.frame['relief'] = 'sunken'
        self.number = list()
        for r in range(0, SQUARE_OF_SQUARE_SIZE):
            self.number.append([])
            for c in range(0, SQUARE_OF_SQUARE_SIZE):
                number_box = NumberBox(self.frame, width=3, justify='center', font=("Purisa", 16))
                number_box.grid(row=r+1, column=c+1)
                self.number[r].append(number_box)
        self.frame.grid(row=row, column=column)

    def get_value(self, row=0, column=0):
        return self.number[row][column].get_number()

    def set_value(self, value=0, row=0, column=0):
        self.number[row][column].set_number(value)

    def set_possible_numbers(self, numbers=[], row=0, column=0):
        self.number[row][column].set_possible_numbers(numbers)

    def get_possible_numbers(self, row=0, column=0):
        return self.number[row][column].get_possible_numbers()

