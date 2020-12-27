import random
names = open('D:/Projects/Python/password-generator/names.txt', 'r')
def generate(length):
    password = ''
    for x in range(length):
        password += random.choice(names)
    file.write(password)
    file.write('\n')
def start():
    amount = 100 * 100
    length = 5
    for x in range(amount):
        generate(length)
start()
