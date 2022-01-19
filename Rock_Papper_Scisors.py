import random

variants = {
    'R': 1,
    'P': 2,
    'S': 3
}
proceed = True
while proceed:

    choice, weight = random.choice(list(variants.items()))
    print(choice)
    selection = input('Select R, P, S: ')
    if variants[selection] > variants[choice]:
        print('You Won')

    elif variants[selection] == variants[choice]:
        print('Equal')

    else:
        print('You lost')

    proceed = input('Want to play more? [y/n]').lower() == 'y'

