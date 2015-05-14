import tkinter as tk

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

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
        self.old_string = ''
        self.number = tk.StringVar()
        self["textvariable"] = self.number
        self.number.trace('w', lambda nm, idx, mode, var=self.number: self.validate(var))
        self.create_popup_menu()
        self.bind("<Button-3>", self.popup)

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
        return int(self.number.get())

    @staticmethod
    def hello():
        print("hello!")

    def create_popup_menu(self):
        self.aMenu = tk.Menu(self, tearoff=0)
        self.aMenu.add_command(label="Undo", command=self.hello)


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
        self.frame.grid(row=row, column=column)
