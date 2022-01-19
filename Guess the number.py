import random

guess = int(input('Enter the number from 1 - 50 to guess: '))

number = random.randint(1, 50)
print(number)
while guess != number:
    if guess > number:
        guess = int(input('Загаданное число меньше: '))
    elif guess < number:
            guess = int(input('Загаданное число больше: '))
print(f'Вы угадали загаданное число {number}')
