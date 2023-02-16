def palindromo(word):
	word = word.replace(' ','')
	word = word.lower()
	wordinv = word[::-1]
	if word == wordinv:
		return True
	else:
		return False

def run():
	word = input('Escribe una palabra: ')
	pali = palindromo(word)
	if pali == True:
		print('Es palindromo')
	else:
		print('No es palindromo')


if __name__ == '__main__':
	run()

