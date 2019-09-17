# User starts in (1,1) only being able to move (N)orth
x, y = 1, 1

def displacement(user_input):
    if user_input == 'n':
        return 1, 0
    if user_input == 's':
        return -1, 0
    if user_input == 'e':
        return 0, 1
    if user_input == 'w':
        return 0, -1

def can_move(n):
    n == 'n':
"""        
while True:
    direction = input('Direction: ').lower
    if direction == 'e' or direction == 'w' or directio == 'n' or direction == 's':
        break
    else:
        print('Not a valid direction!')
"""

# if y = 1 the user can only move (N)orth
# if y = 2 the user can move (S)outh
# if x = 1 and y != 1 the user can move right

# (1,1)     N           PAR.2
if x,y == 1,1 or x,y == 2,1 or x,y == 3,1:
    print("You can travel: (N)orth.")
# (1,2)     N S E
if x,y == 1,2:
    print("You can travel: (N)orth, (S)outh or (E)ast.")
# (1,3)       S E
if x,y == 1,3:
    print("You can travel: (S)outh or (E)ast.")

# (2,1)     N           PAR.2 
# (2,2)       S   W 
if x,y == 2,2:
    print("You can travel: (S)outh or (W)est.")
# (2,3)         E W
if x,y == 2,3:
    print("You can travel: (E)ast or (W)est.")

# (3,1)     N           PAR.2
# (3,2)     N S
if x,y == 3,2:
    print("You can travel: (N)orth or (S)outh.")
# (3,3)       VICTORY
if x,y == 3,3:
    print("Victory!")


# Print out "You can travel", available_direction
# Moving N or S raises the Y value by 1 or reduces it by 1
# Moving E or W raises the X value by 1 or reduces it by 1

# The player is victorious if the (x,y) is (3,3)
