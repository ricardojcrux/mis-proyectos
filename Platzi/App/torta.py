import tools, charts, read

def porc():
    continent = input('Type a Continent: ')
    data = read.read_csv('data.csv')
    data = list(filter(lambda item:item['Continent'] == continent,data))
    countries = list(map(lambda x:x['Country'],data))
    porc = list(map(lambda x:x['World Population Percentage'],data))
    charts.pie_chart(countries,porc)

if __name__ == '__main__':
    porc()