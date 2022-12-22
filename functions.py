import fileinput
from functools import lru_cache


@lru_cache
def load_file():
    res = []
    for line in fileinput.input(['all_stocks_5yr.csv']):
        res.append(line.strip('\n'))
    return res


def filter_func(value: str, data):
    res = []
    value = ''.join(value)

    column = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    if value in column:
        value = column.index(value)
    data.sort(key=lambda row: row[value])

    for i in data:
        res.append(i)
    return res


def limit_func(num, data):
    return data[:num]


def sort_func(method, data):
    res = []
    if method is False:
        return data
    else:
        data.sort(key=lambda x: x[6])
        for i in data:
            res.append(i)
        return res


def sort_revers(method, data):
    if method == 'asc':
        return sorted(data, reverse=True)
    elif method == 'desc':
        return sorted(data, reverse=False)


@lru_cache
def get_date(name, date):
    res = []
    for line in fileinput.input(['all_stocks_5yr.csv']):
        if name in line and date in line:
            res.append(line)
    return res


def write_file(value, res):
    with open(value, "w") as f:
        for item in res:
            res = str(item).split(',')
            f.write(f"{res[0]} | {res[1]} | {res[2]} | {res[3]} | {res[4]} | {res[5]} | {res[6]}\n")



