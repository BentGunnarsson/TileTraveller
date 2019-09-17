# User starts in (1,1) only being able to move (N)orth
x, y = 1, 1

def displacement(user_input):
    if user_input == 'n':
        return x+1, y+0
    if user_input == 's':
        return x-1, y+0
    if user_input == 'e':
        return x+0, y+1
    if user_input == 'w':
        return x+0, y-1



"""
while True:
    direction = input('Direction: ').lower
    if direction == 'e' or direction == 'w' or direction == 'n' or direction == 's':
        break
    else:
        print('Not a valid direction!')
"""

# if y = 1 the user can only move (N)orth
# if y = 2 the user can move (S)outh
# if x = 1 and y != 1 the user can move right

# (1,1)     N           PAR.2
while True:
    if (x == 1 and y == 1) or (x == 2 and y == 1) or (x == 3 and y == 1):
        print("You can travel: (N)orth.")
        while True:
            direction = input('Direction: ').lower
            if direction == 'n':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    # (1,2)     N S E
    elif x == 1 and y == 2:
        print("You can travel: (N)orth, (S)outh or (E)ast.")
        while True:
            direction = input('Direction: ').lower
            if direction == 'e' or direction == 'n' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)
    # (1,3)       S E
    elif x == 1 and y == 3:
        print("You can travel: (S)outh or (E)ast.")
        while True:
            direction = input('Direction: ').lower
            if direction == 'e' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    # (2,1)     N           PAR.2 
    # (2,2)       S   W 
    elif x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")
        while True:
            direction = input('Direction: ').lower
            if direction == 'w' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)
    # (2,3)         E W
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
        while True:
            direction = input('Direction: ').lower
            if direction == 'e' or direction == 'w':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    # (3,1)     N           PAR.2
    # (3,2)     N S
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
        while True:
            direction = input('Direction: ').lower
            if direction == 'e' or direction == 'w' or direction == 'n' or direction == 's':
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)
    # (3,3)       VICTORY
    elif x == 3 and y == 3:
        print("Victory!")
        break


# Print out "You can travel", available_direction
# Moving N or S raises the Y value by 1 or reduces it by 1
# Moving E or W raises the X value by 1 or reduces it by 1

# The player is victorious if the (x,y) is (3,3)
