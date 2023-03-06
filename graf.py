import pylab as pl
from numpy import pi
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Application(tk.Tk):
    name = "graf"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.entryLoad = tk.Entry(self, text="Cesta", width=50)
        self.entryLoad.insert(0, "Není vybrána cesta.")
        self.entryLoad.pack()

        self.btnLoad = tk.Button(self, text="Vybrat soubor", command=self.load, width=50)
        self.btnLoad.pack()

        self.btnMake = tk.Button(self, text="Vykreslit", command=self.make, width=50)
        self.btnMake.pack()

        self.btnQuit = tk.Button(self, text="Quit", command=self.quit, width=50)
        self.btnQuit.pack()

    def make(self, event=None):
        hodnoty_x = []
        hodnoty_y = []      
        self.filename = self.entryLoad.get()
        try:
            with open(self.filename, "r") as f:
                while line := f.readline():
                    x, y = line.split()
                    hodnoty_x.append(float(x))
                    hodnoty_y.append(float(y))
                pl.plot(hodnoty_x, hodnoty_y)
                pl.grid()
                pl.show()
        except:
            messagebox.showwarning("Chyba!", "Nejdříve vyberte soubor!")

    def load(self, event=None):
        self.filename = filedialog.askopenfilename()
        print(self.filename)
        self.entryLoad.delete (0, tk.END)
        self.entryLoad.insert(0, self.filename)
    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()
