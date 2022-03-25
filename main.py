from tqdm import tqdm
from datetime import date
import time
import urllib.request
import os

save_dir = 'exports'
file = 'list.txt'
links = []
split = '\n'

try:
    f = open(file, 'r').read()
    print(f'The file {file} has been opened.')
except FileNotFoundError:
    f = open(file, 'w').close()
    exit(f'No file with the name {file} exists so one has been created')


unformatted = f.split(split)

count = 0
for x in unformatted:
    if not x.find('https://'):
        links.append(x)

if not links:
    time.sleep(0.1)
    exit(f'No links in {file}, add links to download them.')

links = list(dict.fromkeys(links))

time.sleep(1)
print('List formatted for download')
time.sleep(1)

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

print('All files downloaded')

export_file = open(f'{save_dir}/{file}', 'a')

for x in list

file = open(file, 'w').write('')

exit(f'All links cleared from {file}')
