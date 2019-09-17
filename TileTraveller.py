print(1)

# User starts in (1,1) only being able to move (N)orth
# def tile_placement (x,y)
# if y = 1 the user can only move (N)orth
# if y = 2 the user can move (S)outh
# if x = 1 and y != 1 the user can move right

# (1,1)     N           PAR.2
# (1,2)     N S E
# (1,3)       S E

# (2,1)     N           PAR.2
# (2,2)       S   W     PAR.1
# (2,3)         E W

# (3,1)     N           PAR.2
# (3,2)     N S
# (3,3)       S   W     PAR.1


# Print out "You can travel", available_direction
# Moving N or S raises the Y value by 1 or reduces it by 1
# Moving E or W raises the X value by 1 or reduces it by 1

# The player is victorious if the (x,y) is (3,3)
