import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        lista = []
        for row in reader:
            iterable = zip(header,row)
            dict_country = {key: value for key,value in iterable}
            lista.append(dict_country)
    return lista