#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from scipy import interpolate as inp
import pylab as lab

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "grafenzí"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        #self.lbl = tk.Label(self, text="cus svete")
        #self.lbl.pack()

        self.fileFrame = tk.LabelFrame(self, text="Soubor")
        self.fileFrame.pack(padx=5, pady=5)

        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack(anchor=tk.W)
        self.fileBtn = tk.Button(self.fileFrame, text="...")
        self.fileBtn.pack(anchor=tk.E)

        self.dataformatVar = tk.StringVar(value="RADEK")
        self.radkyRbtn = tk.Radiobutton(self.fileFrame, text="Data jsou v řádcích", variable=self.dataformatVar, value="RADEK")
        self.radkyRbtn.pack(anchor=tk.W)
        self.sloupceRbtn = tk.Radiobutton(self.fileFrame, text="Data jsou ve sloupcích", variable=self.dataformatVar, value="SLOUPEC")
        self.sloupceRbtn.pack(anchor=tk.W)

        self.grafFrame = tk.LabelFrame(self, text="Parametry grafu")
        self.grafFrame.pack(padx=5, pady=5)

        tk.Label(self.grafFrame, text="Titulek").grid(row=0, column=0)
        self.titleEntry = MyEntry(self.grafFrame)
        self.titleEntry.grid(row=0,column=1)
        tk.Label(self.grafFrame, text="Popisek X").grid(row=1, column=0)
        self.xlabelEntry = MyEntry(self.grafFrame)
        self.xlabelEntry.grid(row=1,column=1)
        tk.Label(self.grafFrame, text="Popisek Y").grid(row=2, column=0)
        self.ylabelEntry = MyEntry(self.grafFrame)
        self.ylabelEntry.grid(row=2,column=1)
        tk.Label(self.grafFrame, text="Mřížka").grid(row=3, column=0)
        self.gridChck = tk.Checkbutton(self.grafFrame)
        self.gridChck.grid(row=3, column=1, sticky="w")


        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
