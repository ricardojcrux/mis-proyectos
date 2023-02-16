import tools, charts, read

def run():
	data = read.read_csv('data.csv')
	country = input('Type Country: ')
	result = tools.pop_by_country(data,country)

	if len(result) > 0: 
		country = result[0]
		keys, values = tools.get_population(country)
		final = list(zip(keys,values))
		result = {keys: values for keys,values in final}
		charts.bar_chart(keys,values)
	return result

if __name__ == '__main__':
	print(run())