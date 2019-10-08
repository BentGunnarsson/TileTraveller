"""
Inner most list take the form [N, E, S, W] 
where 1 means he can go in a given direction and 0 means he cant.
Inside the list there are 3 major lists each representing values according to what x is
inside those major list there are further more 3 more list that each represent values according to what y is  

Comments above list are to mark where on the picture each list is
"""
                                           #x = 1                                        #x = 2
                              #y = 1       #y = 2        #y = 3           #y = 1         #y = 2       #y = 3
possible_moves_list = [   [ [1, 0, 0, 0, 0], [1, 1, 1, 0, 1], [0, 1, 1, 0, 0] ], [ [1, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 1, 1] ],

                                    #x = 3
                      #y = 1        #y = 2        #y = 3
                [ [1, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 0, 1, 1, 0] ]   ]

def possible_moves(x_index, y_index):
    """
    Takes two integers representing position and return which direction the player can move
    """
    possiblities_str = 'You can travel: '
    #First number in inner most list that represents wether we can travel north and etc.+
    if possible_moves_list[x_index][y_index][0]:
        possiblities_str += '(N)orth or '
    if possible_moves_list[x_index][y_index][1]:
        possiblities_str += '(E)ast or '
    if possible_moves_list[x_index][y_index][2]:
        possiblities_str += '(S)outh or '
    if possible_moves_list[x_index][y_index][3]:
        possiblities_str += '(W)est or '
    #Remove ' or ' and add a dot at the end of the string    
    return possiblities_str[:-4] + '.'

def lever_check(x_index, y_index):
    if possible_moves_list[x_index][y_index][4]:
        user_input = input('Pull a lever (y/n): ').lower()
        return user_input == 'y'
    else:
        return False


def input_checker(user_input):
    """
    User_input is a string representing direction
    Function returns True(as 1) if user can go in that direction and False (as 0) otherwise
    """
    if user_input == 'n':
        return possible_moves_list[x_index][y_index][0]
    if user_input == 'e':
        return possible_moves_list[x_index][y_index][1]
    if user_input == 's':
        return possible_moves_list[x_index][y_index][2]
    if user_input == 'w':
        return possible_moves_list[x_index][y_index][3]
    else:
        return 0

#We start counting at 0 in python, at 1,1 on the picture we are talking about index 0, 0 in the list
x_index, y_index = 0, 0
coins = 0

while True:
    print(possible_moves(x_index, y_index))
    while True:
        user_input = input('Direction: ').lower()
        if input_checker(user_input):
            if user_input == 'n':
                y_index += 1
            elif user_input == 'e':
                x_index += 1
            elif user_input == 's':
                y_index -= 1
            else:
                x_index -= 1
            if lever_check(x_index, y_index):
                coins += 1
                print('You recieved 1 coin, your total is now {}.'.format(coins))
            break
        print('Not a valid direction!')
    #We win
    if x_index == 2 and y_index == 0:   #equal to 3, 1 on the picture
        print('Victory!')
        break
