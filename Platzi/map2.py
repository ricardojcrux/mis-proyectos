items=[
	{
	'producto' :'camisa',
	'price': 100
	},
	{
	'producto' :'pantalones',
	'price': 300
	},
	{
	'producto' :'shorts',
	'price': 200
	}
]

prices = [100,300,200]
print(prices)

prices = list(map(lambda item: item['price'],items))
print(prices)

def taxes(item):
	new_item = item.copy()
	new_item['taxes'] = new_item['price'] * .19
	return new_item

new_items = list(map(taxes,items))
print(new_items)
print(items)

