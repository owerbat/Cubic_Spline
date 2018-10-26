from tkinter import *
import console
from tkinter import messagebox
from random import randint


def x_check(x, number, x_entries):
    for j in range(number):
        if x == x_entries[j].get():
            return False
    return True


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.x_entries = []
        self.y_entries = []
        self.x_labels = []
        self.y_labels = []

        for i in range(8):
            lx = Label(self, text='x'+str(i))
            lx.grid(row=i, column=0)
            self.x_labels.append(lx)

            ex = Entry(self)
            ex.grid(row=i, column=1)
            self.x_entries.append(ex)

            ly = Label(self, text='y' + str(i))
            ly.grid(row=i, column=2)
            self.y_labels.append(ly)

            ey = Entry(self)
            ey.grid(row=i, column=3)
            self.y_entries.append(ey)

        self.x_entries[0].insert(0, '0')
        self.y_entries[0].insert(0, '0')
        self.x_entries[1].insert(0, '1')
        self.y_entries[1].insert(0, '1')
        self.x_entries[2].insert(0, '2')
        self.y_entries[2].insert(0, '-1')
        self.x_entries[3].insert(0, '3')
        self.y_entries[3].insert(0, '0')

        self.random_button = Button(self, text='Random', command=self.randomize)
        self.random_button.grid(row=8, column=1)

        self.spline_button = Button(self, text='Get spline', command=self.solve)
        self.spline_button.grid(row=8, column=3)

    def randomize(self):
        numbers = []
        for i in range(8):
            self.x_entries[i].delete(0, END)
            self.y_entries[i].delete(0, END)
            x_rand = str(randint(-20, 20))
            y_rand = str(randint(-20, 20))
            self.x_entries[i].insert(0, x_rand)
            self.y_entries[i].insert(0, y_rand)
            numbers.append(x_rand)

        for i in range(8):
            if not x_check(self.x_entries[i].get(), i, self.x_entries):
                while self.x_entries[i].get() in numbers:
                    self.x_entries[i].delete(0, END)
                    self.x_entries[i].insert(0, str(randint(-20, 20)))

    def solve(self):
        try:
            file = open('dots.txt', 'w', encoding='utf-8')
        except FileNotFoundError:
            print("Dots file is nor founded")
            exit(2)

        for i in range(8):
            x = self.x_entries[i].get()
            y = self.y_entries[i].get()
            if x != '' and y != '':
                if x_check(x, i, self.x_entries):
                    file.write(x + ' ' + y + '\n')
                else:
                    messagebox.showinfo('Error', 'All points must have different x')
                    raise ValueError

        file.close()

        console.main()


root = Tk()
root.title("Cubic Spline")
root.geometry("300x300")
app = Application(root)
root.mainloop()
