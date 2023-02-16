import random

def run():
	winner = random.randint(1,100)
	number = int(input('Type a number between 1 and 100: '))
	tof = True
	count = 0
	while tof:
		count += 1
		if winner > number:
			number = int(input('Type a larger number: '))
		elif winner < number:
			number = int(input('Type a smaller number: '))
		elif winner == number:
			print('Congratulations! The correct number is ' + str(winner))
			print('You needed ' + str(count) + ' attempts to guess the number')
			tof = False
			break
			
if __name__ == '__main__':
	run()