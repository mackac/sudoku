__author__ = 'Maciej'

DEFAULT = [[0] * 9 for i in range(9)]

class SudokuAlgorithm:
    def __init__(self, numbers=DEFAULT):
        self.numbers = numbers
        self.possible_numbers = None
        self.calculated = None

    def set_numbers(self, numbers):
        self.numbers = numbers

    def get_calculated_numbers(self):
        return self.calculated

    def get_possible_numbers(self):
        return self.possible_numbers

    def calculate_possible_numbers(self):
        calculated_numbers = None

        return calculated_numbers

    def calculate_for_one_field(self, row=0, column=0):
        possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        possible_numbers = self.square_check(possible_numbers, row, column)
        return possible_numbers

    def square_check(self, possible_numbers, row=0, column=0):
        start_row = row - row % 3
        start_column = column - column % 3
        square = list(zip(*(list(zip(*self.numbers[start_row:start_row+3])))[start_column:start_column+3]))
        for row in square:
            for one_element in row:
                possible_numbers.remove(one_element)
        return possible_numbers

    def vertical_check(self, possible_numbers, column=0):
        for i in self.numbers:
            possible_numbers.remove(i[column])
        return possible_numbers

    def horizontal_check(self, possible_numbers, row=0):
        for i in self.numbers[row]:
            possible_numbers.remove(i)
        return possible_numbers

SudokuAlgorithm(DEFAULT)
