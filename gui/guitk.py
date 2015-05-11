import tkinter as tk

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "SOLVE"
        self.hi_there.grid(row=1, column=1)

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.quit)
        self.QUIT.grid(row=1, column=2)

        self.nine_square = []
        for r in range(2, 5):
            for c in range(1, 4):
                self.nine_square.append(NineBoxSquare(self, r, c))


class MainWindow():

    def __init__(self):
        #self.root = tk.Tk()
        self.app = Application()
        self.app.master.title("SUDOKU")
        self.app.master.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.app.master.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.app.mainloop()


class NumberBox(tk.Entry):

    ALLOWED_CHARS = "123456789"

    def __init__(self, master=None, cnf={}, **kw):

        super().__init__(master, cnf, **kw)
        self.number = tk.StringVar()


    def validate(self, text=''):
        new_value = self.get()
        if len(new_value) > 1:
            pass
        print("validating")


class NineBoxSquare():

    def __init__(self, master=None, row=0, column=0):
        self.frame = tk.Frame(master, bd=4)
        self.frame['relief'] = 'sunken'
        self.number = []
        for r in range(1, 4):
            for c in range(1, 4):
                number_box = NumberBox(self.frame, width=3, justify='center', font=("Purisa", 16))
                number_box.grid(row=r, column=c)
                self.number.append(number_box)
                vcmd = (self.register(self.number[-1].validate))
        self.frame.grid(row=row, column=column)
