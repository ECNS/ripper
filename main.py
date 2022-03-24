import urllib.request

file = 'list.txt'
links = []

try:
    f = open(file, 'r').read()
except FileNotFoundError:
    f = open(file, 'w').close()
    print(f'No file with the name {file} exists so one has been created')

unformatted = f.split('\n')


count = 0
for x in unformatted:
    if not x.find('https://'):
        links.append(x)

links = list(dict.fromkeys(links))


for x in links:
    name = x.split('/')
    urllib.request.urlretrieve(x, f'exports/{name[-1]}')
