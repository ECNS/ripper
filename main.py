from tqdm import tqdm
from datetime import date
import time
import urllib.request
import os

today = date.today()
save_dir = 'exports'
file = 'list.txt'
links = []
split = '\n'


def open_file(import_file, split_point):
    try:
        f = open(import_file, 'r').read()
        print(f'The file {import_file} has been opened.')
    except FileNotFoundError:
        f = open(import_file, 'w').close()
        # exit(f'No file with the name {import_file} exists so one has been created')

    unformatted_list = f.split(split_point)

    for i in unformatted_list:
        if not i.find('https://'):
            links.append(i)

    if not links:
        time.sleep(0.1)
        # exit(f'No links in {file}, add links to download them.')

    return list(dict.fromkeys(links))
#
# time.sleep(1)
#
# pbar = tqdm(range(0, len(links)))
# for x in pbar:
#     name = links[x].split('/')
#     pbar.set_description("Processing %s" % name[-1])
#     try:
#         urllib.request.urlretrieve(links[x], f'{save_dir}/{name[-1]}')
#     except FileNotFoundError:
#         os.mkdir(save_dir)
#         urllib.request.urlretrieve(links[x], f'{save_dir}/{name[-1]}')
#
# print('All files downloaded')
#
#
# export_file = open(f'{save_dir}/{today.strftime("%d-%m-%y")}.txt', 'a')
#
#
# for x in links:
#     export_file.write(f'{x}\n')
#
# export_file.close()
#
# file = open(file, 'w')
# file.write('')
# file.close()
#
# exit(f'All links cleared from {file.name}')
