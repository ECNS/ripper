from tqdm import tqdm
import time
import urllib.request
import os

save_dir = 'exports'
file = 'list.txt'
links = []

try:
    f = open(file, 'r').read()
    print(f'The file {file} has been opened.')
except FileNotFoundError:
    f = open(file, 'w').close()
    print(f'No file with the name {file} exists so one has been created')

unformatted = f.split('\n')

count = 0
for x in unformatted:
    if not x.find('https://'):
        links.append(x)

links = list(dict.fromkeys(links))

print('List formatted for download')

count = 0
pbar = tqdm(range(0, len(links)))
for x in pbar:
    name = links[x].split('/')
    pbar.set_description("Processing %s" % name[-1])
    try:
        urllib.request.urlretrieve(links[x], f'{save_dir}/{name[-1]}')
    except FileNotFoundError:
        os.mkdir(save_dir)
        urllib.request.urlretrieve(links[x], f'{save_dir}/{name[-1]}')

