import random

def new_password():
	mayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	number = ['0','1','2','3','4','5','6','7','8','9']
	chart = ['#','/','.',':',';','=']

	caracter = mayus + minus + number + chart
	password = []

	for i in range(18):
		c_random = random.choice(caracter)
		password.append(c_random)

	password = ''.join(password)
	return password

def run():
	password = new_password()
	print('Tu nueva contraseña es: ' + password)

if __name__ == '__main__':
	run()