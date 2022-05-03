from PIL import ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import *
import logging
import PIL.Image
import urllib.request
import io
import os


logging.basicConfig(level=logging.DEBUG,
                    filename="log.log",
                    filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")

top = Tk()

if not os.path.isdir('exports/'):
    logging.info('creating directory \'exports/\'')
    os.mkdir('exports/')


def error_popup(error):
    if error is None:
        logging.error('Unknown error')
        messagebox.showerror(f'Error Code : Unknown', 'Unknown error contact dev')
        return

    if error == 'FILE01':
        messagebox.showerror(f'Error Code : {error}', 'No links in file')
        logging.error('No links in file')
        return


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = askopenfilename(
        initialdir=os.getcwd(),
        title='Open a file',
        filetypes=filetypes)

    f = open(filename, 'r').read()

    try:
        unformatted_list = f.split(split_point.get())
    except ValueError:
        unformatted_list = f.split('\n')

    unformatted_list = list(dict.fromkeys(unformatted_list))

    if unformatted_list == ['']:
        error_popup('FILE01')

    for i in unformatted_list:
        if not i.find('https://'):
            lb1.insert(0, i)


def onselect(evt):
    if lb1.size() == 0:
        return
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    raw_data = urllib.request.urlopen(value).read()

    image = PIL.Image.open(io.BytesIO(raw_data))

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
    pic.grid(row=4, column=1, columnspan=4, pady=5, padx=5)


def auto_download():
    while lb1.size() != 0:
        sv_f1(True)


def sv_f1(auto):

    if auto:
        lb1.select_set(0)

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

# Section 0
lb1 = Listbox(top, width=50, height=30, selectmode=SINGLE)
lb1.bind('<<ListboxSelect>>', onselect)
lb1.grid(column=0, row=0, padx=5, pady=5, rowspan=35)

imp_btn = Button(top, text='Import List', width=45, command=select_file)
imp_btn.grid(row=36, column=0, padx=5, pady=5)

# Section 1
split_point_text = Label(top, text='Set split point : ')
split_point_text.grid(row=0, column=1, padx=5, pady=5)

split_point = Entry(top, width=30)
split_point.grid(row=0, column=2, padx=5, pady=5, columnspan=3)

start_btn = Button(top, text='Automatic Download', width=40, command=auto_download)
start_btn.grid(row=1, column=1, padx=5, pady=5, columnspan=4)

save_one_btn = Button(top, text='Save Folder 1', width=17, command=lambda: sv_f1(False))
save_one_btn.grid(row=2, column=1, columnspan=2)

save_two_btn = Button(top, text='Save Folder 2', width=17, command=sv_f2)
save_two_btn.grid(row=2, column=3, columnspan=2)

del_btn = Button(top, text='Skip', width=40, command=skip)
del_btn.grid(row=3, column=1, columnspan=4)

pic = Label(top)
pic.grid(row=4, column=1, columnspan=4, pady=5, padx=5)

top.mainloop()
