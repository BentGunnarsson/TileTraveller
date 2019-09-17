#https://github.com/BentGunnarsson/TileTraveller

# User starts in (1,1)
x, y = 1, 1

def displacement(user_input):
    """
    user_input: String representing direction
    Returns changed x and y depending on which direction
    """
    if user_input == 'n':
        return x+0, y+1
    if user_input == 's':
        return x+0, y-1
    if user_input == 'e':
        return x+1, y+0
    if user_input == 'w':
        return x-1, y-0

#While loop runs until we win
while True:
    if (x == 1 and y == 1) or (x == 2 and y == 1):
        print("You can travel: (N)orth.")
        while True:
            direction = input('Direction: ').lower()
            if direction == 'n':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        while True:
            direction = input('Direction: ').lower()
            if direction == 'e' or direction == 'n' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
        while True:
            direction = input('Direction: ').lower()
            if direction == 'e' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")
        while True:
            direction = input('Direction: ').lower()
            if direction == 'w' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
        while True:
            direction = input('Direction: ').lower()
            if direction == 'e' or direction == 'w':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
        while True:
            direction = input('Direction: ').lower()
            if direction == 'e' or direction == 'w' or direction == 'n' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)
    
    elif x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")
        while True:
            direction = input('Direction: ').lower()
            if direction == 'w' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)
    # (3,1)       VICTORY so we break
    elif x == 3 and y == 1:
        print("Victory!")
        break