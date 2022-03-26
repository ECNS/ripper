
links = []


def open_file(import_file, split_point):
    try:
        f = open(import_file, 'r').read()
    except FileNotFoundError:
        f = open(import_file, 'w').close()
        # exit(f'No file with the name {import_file} exists so one has been created')

    unformatted_list = f.split(split_point)

    for i in unformatted_list:
        if not i.find('https://'):
            links.append(i)

    return list(dict.fromkeys(links))
