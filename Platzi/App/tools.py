def get_population(data):
	dict = {
		'2022':int(data['2022 Population']),
		'2020':int(data['2020 Population']),
		'2015':int(data['2015 Population']),
		'2010':int(data['2010 Population']),
		'2000':int(data['2000 Population']),
		'1990':int(data['1990 Population']),
		'1980':int(data['1980 Population']),
		'1970':int(data['1970 Population'])
		}
	return dict.keys(), dict.values()

def pop_by_country(data,country):
	result = list(filter(lambda item: item['Country'] == country,data))
	return result