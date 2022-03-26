import gc
import os
import urllib.request
from tkinter import *
from tkinter.filedialog import askopenfilename
from main import open_file
from PIL import ImageTk, Image
from time import sleep
import io


links = []
split = '\n'


top = Tk()

if not os.path.isdir('exports/'):
    os.mkdir('exports/')


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
        lb1.insert(count, x)
        links.append(x)


def onselect(evt,):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    raw_data = urllib.request.urlopen(value).read()

    image = Image.open(io.BytesIO(raw_data))

    if image.width > 400:
        factor = image.width / 400
        image_h = int(image.height / factor)
        image_w = int(image.width / factor)
        image = image.resize((image_w, image_h))

    if image.height > 500:
        factor = image.height / 400
        image_h = int(image.height / factor)
        image_w = int(image.width / factor)
        image = image.resize((image_w, image_h))

    image = ImageTk.PhotoImage(image)
    pic.config(image=image)
    pic.image = image
    pic.grid(row=3, column=1, columnspan=2, pady=5, padx=5)


def auto_download_start():
    sleep(0.5)
    auto_download()


def auto_download():
    lb1.selection_clear(0, END)
    lb1.select_set(0)
    link = lb1.get(lb1.curselection())
    name = link.split('/')
    name = name[-1]
    try:
        urllib.request.urlretrieve(link, f'exports/{name}')
    except FileNotFoundError:
        os.mkdir('exports/')
        urllib.request.urlretrieve(link, f'exports/{name}')
    lb1.delete(0)
    auto_download_start()


def sv_f1():
    link = lb1.get(lb1.curselection())
    name = link.split('/')
    name = name[-1]
    try:
        urllib.request.urlretrieve(link, f'exports/1/{name}')
    except FileNotFoundError:
        os.mkdir('exports/1/')
        urllib.request.urlretrieve(link, f'exports/1/{name}')
    lb1.delete(lb1.curselection())
    lb1.selection_clear(0, END)
    lb1.select_set(0)
    lb1.event_generate("<<ListboxSelect>>")


def sv_f2():
    link = lb1.get(lb1.curselection())
    name = link.split('/')
    name = name[-1]
    try:
        urllib.request.urlretrieve(link, f'exports/2/{name}')
    except FileNotFoundError:
        os.mkdir('exports/2/')
        urllib.request.urlretrieve(link, f'exports/2/{name}')
    lb1.delete(lb1.curselection())
    lb1.selection_clear(0, END)
    lb1.select_set(0)
    lb1.event_generate("<<ListboxSelect>>")


def skip():
    lb1.delete(lb1.curselection())
    lb1.selection_clear(0, END)
    lb1.select_set(0)
    lb1.event_generate("<<ListboxSelect>>")


top.title('Ripper')

lb1 = Listbox(top, width=50, height=30, selectmode=SINGLE)
lb1.bind('<<ListboxSelect>>', onselect)
lb1.grid(column=0, row=0, padx=5, pady=5, rowspan=35)

imp_btn = Button(top, text='Import List', width=45, command=select_file)
imp_btn.grid(row=36, column=0, padx=5, pady=5)

start_btn = Button(top, text='Automatic Download', width=40, command=auto_download)
start_btn.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

save_one_btn = Button(top, text='Save Folder 1', width=17, command=sv_f1)
save_one_btn.grid(row=1, column=1)

save_two_btn = Button(top, text='Save Folder 2', width=17, command=sv_f2)
save_two_btn.grid(row=1, column=2)

del_btn = Button(top, text='Skip', width=40, command=skip)
del_btn.grid(row=2, column=1, columnspan=2)

pic = Label(top, text='')
pic.grid(row=3, column=1, columnspan=2, pady=5, padx=5)

top.mainloop()
