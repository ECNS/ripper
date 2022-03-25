import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from main import open_file

links = []
split = '\n'

top = Tk()
lb1 = Listbox(top, width=50, height=30)


def select_file():

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = askopenfilename(
        initialdir=os.getcwd(),
        title='Open a file',
        filetypes=filetypes)

    count = 0
    for x in open_file(filename, split):
        name = x.split('/')
        lb1.insert(count, name[-1])
        links.append(x)


lb1.grid(column=0, row=0, padx=5, pady=5)

imp_button = Button(top, text='Import List', width=45, padx=5, command=select_file)
imp_button.grid(row=1, column=0, padx=5, pady=5)
top.mainloop()
