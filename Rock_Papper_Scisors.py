import random

variants = {
    'R': 1,
    'P': 2,
    'S': 3
}
proceed = True
while proceed:

    choice, weight = random.choice(list(variants.items()))
    
    selection = str.upper(input('Select R, P, S: '))
    if variants[selection] > variants[choice]:
        print(f'You Won. My choice was {choice}!')

    elif variants[selection] == variants[choice]:
        print(f'Equal. My choice was {choice}!')

    else:
        print(f'You lost. My choice was {choice}!')

    proceed = input('Want to play more? [y/n]').lower() == 'y'

