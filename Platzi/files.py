file = open('./text.txt')
print(file.read())
file.close()

file = open('./text.txt')
for i in file:
    print(i)
file.close()

with open('./text.txt','r+') as file:
    for i in file:
        print(i)
    file.write('\nEscribamos nuevas cosas')
