import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG,
                    filename="log_sort.log",
                    filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")

final_dir = 'sorts/'
if not os.path.isdir(final_dir):
    logging.info(f'creating directory \'{final_dir}\'')
    os.mkdir(final_dir)

target_dir = 'exports/1/'
files = os.listdir(target_dir)

tags = []
for x in files:
    tag = x.split('_')
    tag = tag[0]
    tags.append(tag)

catagorized = {}
for i in tags:
    catagorized[i] = []

for i in catagorized:
    try:
        os.mkdir(f'{final_dir}{i}/')
        logging.info(f'creating directory \'{i}/\'')
    except FileExistsError:
        logging.info(f'directory exists \'{i}/\'')
    for x in files:
        if not x.find(i):
            try:
                shutil.move(target_dir + x, final_dir + i)
                logging.info(f'moved file {i}')
            except shutil.Error:
                os.remove(target_dir + x)
                logging.info(f'file {i} already exists, deleting')
