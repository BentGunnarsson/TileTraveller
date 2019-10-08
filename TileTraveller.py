#https://github.com/BentGunnarsson/TileTraveller
import random
# User starts in (1,1) with 0 coins
x, y = 1, 1
coin_count = 0
valid_moves = 0
def random_move():
    direction_list = ["n","e","s","w"]
    direction = random.choice(direction_list)
    print("Direction:", direction)
    return direction

def random_answer():
    yes_or_no_list = ["y","n"]
    answer = random.choice(yes_or_no_list)
    return answer

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

def pull_lever(coins):
    #answer = input("Pull a lever (y/n): ")
    answer = random_answer()
    print("Pull a lever (y/n):",answer)
    if answer == "y":
        coins += 1
        print("You received 1 coin, your total is now "+str(coins)+".")
    return coins

seed = input("Input seed: ")
random.seed(a=seed, version=2)

#While loop runs until we win
while True:
    if (x == 1 and y == 1) or (x == 2 and y == 1):
        
        while True:
            print("You can travel: (N)orth.")
            #direction = input('Direction: ').lower()
            direction = random_move()
            if direction == 'n':
                valid_moves += 1
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 1 and y == 2:
        coin_count = pull_lever(coin_count)
        while True:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            #direction = input('Direction: ').lower()
            direction = random_move()
            if direction == 'e' or direction == 'n' or direction == 's':
                valid_moves += 1
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 1 and y == 3:
        while True:
            print("You can travel: (E)ast or (S)outh.")
            #direction = input('Direction: ').lower()
            direction = random_move()
            print("Direction:", direction)
            if direction == 'e' or direction == 's':
                valid_moves += 1
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 2 and y == 2:
        coin_count = pull_lever(coin_count)
        while True:
            print("You can travel: (S)outh or (W)est.")
            #direction = input('Direction: ').lower()
            direction = random_move()
            if direction == 'w' or direction == 's':
                valid_moves += 1
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 2 and y == 3:
        coin_count = pull_lever(coin_count)
        while True:
            print("You can travel: (E)ast or (W)est.")
            #direction = input('Direction: ').lower()
            direction = random_move()
            if direction == 'e' or direction == 'w':
                valid_moves += 1
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)

    elif x == 3 and y == 2:
        coin_count = pull_lever(coin_count)
        while True:
            print("You can travel: (N)orth or (S)outh.")
            #direction = input('Direction: ').lower()
            direction = random_move()
            if direction == 'n' or direction == 's':
                valid_moves += 1
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)
    
    elif x == 3 and y == 3:
        while True:
            print("You can travel: (S)outh or (W)est.")
            #direction = input('Direction: ').lower()
            direction = random_move()
            if direction == 'w' or direction == 's':
                valid_moves += 1
                break
            else:
                print('Not a valid direction!')
        x, y = displacement(direction)
    # (3,1)       VICTORY so we break
    elif x == 3 and y == 1:
        print("Victory! Total coins "+str(coin_count)+". Valid moves",valid_moves)
        again = input("Play again (y/n): ")
        if again == "y":
            coin_count = 0
            valid_moves = 0
            x ,y = 1, 1
        else:
            break