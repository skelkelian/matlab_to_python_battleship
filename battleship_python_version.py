# battleship
# enhancements: play sound after player wins, god mode difficulty, keep hitting until miss

# imports
from random import *

# functions
def pretty_print_list(matrix):
    for row in range(0, len(matrix)):
        print(matrix[row])
        for col in range(0, len(matrix)-1):
            pass

# display directions
print('If you want to play against a computer type 1 \nIf you want to play against a friend type 2\n')

# have them pick gamemode
gameMode = int(input('Enter who you would like to play against a computer(1) or a friend(2): '))
while gameMode != 1 and gameMode != 2:
    gameMode = int(input('Please select either 1 or 2: '))

# run code depending on which gamemode chosen
if int(gameMode) == 1:
    # display rules for computer mode
    print('\nYou have chose to play against a computer. \nTake turns choosing points on the computers 10x10 board \nin hopes of hitting a part of the ship. \nIf you hit every part of the ship it will be sunk and \nyou will continue picking points until you sink all ships. \nThe first player to sink all opponent ships wins. \n\nGoodluck, Have fun! \n\n')

    # ask for difficulty
    gameDifficulty = int(input('Enter what level computer you would like to play against, easy(1), pro(2) or god(3): '))
    while gameDifficulty != 1 and gameDifficulty != 2 and gameDifficulty != 3:
        gameDifficulty = int(input('Please select either 1, 2 or 3: '))

    # player 1 picking points

    # create primary board for player 1
    PB1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # carrier

    # horizontal or vertical axis
    CA1 = int(input('Specify whether you would like your carrier to be horizontal(1) or vertical(2): '))  # carrier axis player one
    while CA1 != 1 and CA1 != 2:
        CA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for carrier
    CR1 = int(input('Specify what row you would like to place the carrier: '))  # carrier row player one
    while CR1 != 1 and CR1 != 2 and CR1 != 3 and CR1 != 4 and CR1 != 5 and CR1 != 6 and CR1 != 7 and CR1 != 8 and CR1 != 9 and CR1 != 10:
        CR1 = int(input('Please select a number between 1-10: '))
    CC1 = int(input('Specify what column you would like to place the carrier: '))  # carrier column player one
    while CC1 != 1 and CC1 != 2 and CC1 != 3 and CC1 != 4 and CC1 != 5 and CC1 != 6 and CC1 != 7 and CC1 != 8 and CC1 != 9 and CC1 != 10:
        CC1 = int(input('Please select a number between 1-10: '))

    # verify that the ship will fit and place points
    if CA1 == 1:
        while CC1 > 6 or CC1 <= 0 or CC1 % 1 != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            CR1 = int(input('Try a row integer that is between 1 and 6: '))
            CC1 = int(input('Try a column integer that is between 1 and 6: '))
        PB1[CR1 - 1][CC1 - 1] = 5
        PB1[CR1 - 1][CC1] = 5
        PB1[CR1 - 1][CC1 + 1] = 5
        PB1[CR1 - 1][CC1 + 2] = 5
        PB1[CR1 - 1][CC1 + 3] = 5
    else:
        while CR1 > 6 or CR1 <= 0 or CR1 % 1 != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            CR1 = int(input('Try a row integer that is between 1 and 6: '))
            CC1 = int(input('Try a column integer that is between 1 and 6: '))
        PB1[CR1 - 1][CC1 - 1] = 5
        PB1[CR1][CC1 - 1] = 5
        PB1[CR1 + 1][CC1 - 1] = 5
        PB1[CR1 + 2][CC1 - 1] = 5
        PB1[CR1 + 3][CC1 - 1] = 5

    # this was the function I made in matlab idk if we will keep it
    # place rest of points
    # PB1 = placing_carrier_points(PB1, CA1, CR1, CC1)

    # display board
    pretty_print_list(PB1)
    print('Your carrier has been placed \n\n')

    # battleship

    # horizontal or vertical axis
    BA1 = int(input('Specify whether you would like your battleship to be horizontal(1) or vertical(2): '))  # battleship axis player one
    while BA1 != 1 and BA1 != 2:
        BA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for battleship
    BR1 = int(input('Specify what row you would like to place the battleship: ')) # battleship row player one
    while BR1 != 1 and BR1 != 2 and BR1 != 3 and BR1 != 4 and BR1 != 5 and BR1 != 6 and BR1 != 7 and BR1 != 8 and BR1 != 9 and BR1 != 10:
        BR1 = int(input('Please select a number between 1-10: '))
    BC1 = int(input('Specify what column you would like to place the battleship: ')) # battleship column player one
    while BC1 != 1 and BC1 != 2 and BC1 != 3 and BC1 != 4 and BC1 != 5 and BC1 != 6 and BC1 != 7 and BC1 != 8 and BC1 != 9 and BC1 != 10:
        BC1 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if BA1 == 1:
        while BC1 > 7 or BC1 <= 0 or BC1 % 1 != 0 or PB1[BR1 - 1][BC1 - 1] != 0 or PB1[BR1 - 1][BC1] != 0 or PB1[BR1 - 1][BC1 + 1] != 0 or PB1[BR1 - 1][BC1 + 2] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            BR1 = int(input('Try a row integer that is between 1 and 7: '))
            BC1 = int(input('Try a column integer that is between 1 and 7: '))
        PB1[BR1 - 1][BC1 - 1] = 4
        PB1[BR1 - 1][BC1] = 4
        PB1[BR1 - 1][BC1 + 1] = 4
        PB1[BR1 - 1][BC1 + 2] = 4
    else:
        while BR1 > 7 or BR1 <= 0 or BR1 % 1 != 0 or PB1[BR1 - 1][BC1 - 1] != 0 or PB1[BR1][BC1 - 1] != 0 or PB1[BR1 + 1][BC1 - 1] != 0 or PB1[BR1 + 2][BC1 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            BR1 = int(input('Try a row integer that is between 1 and 7: '))
            BC1 = int(input('Try a column integer that is between 1 and 7: '))
        PB1[BR1 - 1][BC1 - 1] = 4
        PB1[BR1][BC1 - 1] = 4
        PB1[BR1 + 1][BC1 - 1] = 4
        PB1[BR1 + 2][BC1 - 1] = 4

    # display the board
    pretty_print_list(PB1)
    print('Your battleship has been placed \n\n')

    # destroyer

    # horizontal or vertical axis
    DA1 = int(input('Specify whether you would like your destroyer to be horizontal(1) or vertical(2): '))  # destroyer axis player one
    while DA1 != 1 and DA1 != 2:
        DA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for destroyer
    DR1 = int(input('Specify what row you would like to place the destroyer: ')) # destroyer row player one
    while DR1 != 1 and DR1 != 2 and DR1 != 3 and DR1 != 4 and DR1 != 5 and DR1 != 6 and DR1 != 7 and DR1 != 8 and DR1 != 9 and DR1 != 10:
        DR1 = int(input('Please select a number between 1-10: '))
    DC1 = int(input('Specify what column you would like to place the destroyer: ')) # destroyer column player one
    while DC1 != 1 and DC1 != 2 and DC1 != 3 and DC1 != 4 and DC1 != 5 and DC1 != 6 and DC1 != 7 and DC1 != 8 and DC1 != 9 and DC1 != 10:
        DC1 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if DA1 == 1:
        while DC1 > 8 or DC1 < 0 or DC1 % 1 != 0 or PB1[DR1 - 1][DC1 - 1] != 0 or PB1[DR1 - 1][DC1] != 0 or PB1[DR1 - 1][DC1 + 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            DR1 = int(input('Try a row integer that is between 1 and 8: '))
            DC1 = int(input('Try a column integer that is between 1 and 8: '))
        PB1[DR1 - 1][DC1 - 1] = 3
        PB1[DR1 - 1][DC1] = 3
        PB1[DR1 - 1][DC1 + 1] = 3
    else:
        while DR1 > 8 or DR1 < 0 or DR1 % 1 != 0 or PB1[DR1 - 1][DC1 - 1] != 0 or PB1[DR1][DC1 - 1] != 0 or PB1[DR1 + 1][DC1 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            DR1 = int(input('Try a row integer that is between 1 and 8: '))
            DC1 = int(input('Try a column integer that is between 1 and 8: '))
        PB1[DR1 - 1][DC1 - 1] = 3
        PB1[DR1][DC1 - 1] = 3
        PB1[DR1 + 1][DC1 - 1] = 3

    # display the board
    pretty_print_list(PB1)
    print('Your destroyer has been placed \n\n')

    # submarine

    # horizontal or vertical axis
    SA1 = int(input('Specify whether you would like your submarine to be horizontal(1) or vertical(2): ')) # submarine axis player one
    while SA1 != 1 and SA1 != 2:
        SA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for submarine
    SR1 = int(input('Specify what row you would like to place the submarine: ')) # submarine row player one
    while SR1 != 1 and SR1 != 2 and SR1 != 3 and SR1 != 4 and SR1 != 5 and SR1 != 6 and SR1 != 7 and SR1 != 8 and SR1 != 9 and SR1 != 10:
        SR1 = int(input('Please select a number between 1-10: '))
    SC1 = int(input('Specify what column you would like to place the submarine: ')) # submarine column player one
    while SC1 != 1 and SC1 != 2 and SC1 != 3 and SC1 != 4 and SC1 != 5 and SC1 != 6 and SC1 != 7 and SC1 != 8 and SC1 != 9 and SC1 != 10:
        SC1 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if SA1 == 1:
        while SC1 > 8 or SC1 < 0 or SC1 % 1 != 0 or PB1[SR1 - 1][SC1 - 1] != 0 or PB1[SR1 - 1][SC1] != 0 or PB1[SR1 - 1][SC1 + 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            SR1 = int(input('Try a row integer that is between 1 and 8: '))
            SC1 = int(input('Try a column integer that is between 1 and 8: '))
        PB1[SR1 - 1][SC1 - 1] = 1
        PB1[SR1 - 1][SC1] = 1
        PB1[SR1 - 1][SC1 + 1] = 1
    else:
        while SR1 > 8 or SR1 < 0 or SR1 % 1 != 0 or PB1[SR1 - 1][SC1 - 1] != 0 or PB1[SR1][SC1 - 1] != 0 or PB1[SR1 + 1][SC1 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            SR1 = int(input('Try a row integer that is between 1 and 8: '))
            SC1 = int(input('Try a column integer that is between 1 and 8: '))
        PB1[SR1 - 1][SC1 - 1] = 1
        PB1[SR1][SC1 - 1] = 1
        PB1[SR1 + 1][SC1 - 1] = 1

    # display the board
    pretty_print_list(PB1)
    print('Your submarine has been placed \n\n')

    # patrol boat

    # horizontal or vertical axis
    PA1 = int(input('Specify whether you would like your patrol boat to be horizontal(1) or vertical(2): ')) # patrol boat axis player one
    while PA1 != 1 and PA1 != 2:
        PA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for patrol boat
    PR1 = int(input('Specify what row you would like to place the patrol boat: '))  # patrol boat row player one
    while PR1 != 1 and PR1 != 2 and PR1 != 3 and PR1 != 4 and PR1 != 5 and PR1 != 6 and PR1 != 7 and PR1 != 8 and PR1 != 9 and PR1 != 10:
        PR1 = int(input('Please select a number between 1-10: '))
    PC1 = int(input('Specify what column you would like to place the patrol boat: '))  # patrol boat column player one
    while PC1 != 1 and PC1 != 2 and PC1 != 3 and PC1 != 4 and PC1 != 5 and PC1 != 6 and PC1 != 7 and PC1 != 8 and PC1 != 9 and PC1 != 10:
        PC1 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if PA1 == 1:
        while PC1 > 9 or PC1 < 0 or PC1 % 1 != 0 or PB1[PR1 - 1][PC1 - 1] != 0 or PB1[PR1 - 1][PC1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            PR1 = int(input('Try a row integer that is between 1 and 9: '))
            PC1 = int(input('Try a column integer that is between 1 and 9: '))
        PB1[PR1 - 1][PC1 - 1] = 2
        PB1[PR1 - 1][PC1] = 2
    else:
        while PR1 > 9 or PR1 < 0 or PR1 % 1 != 0 or PB1[PR1 - 1][PC1 - 1] != 0 or PB1[PR1][PC1 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            PR1 = int(input('Try a row integer that is between 1 and 9: '))
            PC1 = int(input('Try a column integer that is between 1 and 9: '))
        PB1[PR1 - 1][PC1 - 1] = 2
        PB1[PR1][PC1 - 1] = 2

    # display the board
    pretty_print_list(PB1)
    print('Your patrol boat has been placed \n\n')

    # computer picking points

    # create primary board for computer
    PB2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # carrier

    # horizontal or vertical axis
    CA2 = (randint(1, 2))  # carrier axis computer

    # have computer assign location for carrier
    CR2 = (randint(1, 10))
    CC2 = (randint(1, 10))

    # verify ship will fit
    if CA2 == 1:
        while CC2>6:
            CR2 = (randint(1, 6))
            CC2 = (randint(1, 6))
    else:
        while CR2>6:
            CR2 = (randint(1, 6))
            CC2 = (randint(1, 6))

    # autoplace the points
    if CA2 == 1:
        PB2[CR2 - 1][CC2 - 1] = 5
        PB2[CR2 - 1][CC2] = 5
        PB2[CR2 - 1][CC2 + 1] = 5
        PB2[CR2 - 1][CC2 + 2] = 5
        PB2[CR2 - 1][CC2 + 3] = 5
    else:
        PB2[CR2 - 1][CC2 - 1] = 5
        PB2[CR2][CC2 - 1] = 5
        PB2[CR2 + 1][CC2 - 1] = 5
        PB2[CR2 + 2][CC2 - 1] = 5
        PB2[CR2 + 3][CC2 - 1] = 5

    # battleship

    # horizontal or vertical axis
    BA2 = (randint(1, 2))

    # have computer assign location for battleship
    BR2 = (randint(1, 10))
    BC2 = (randint(1, 10))

    # verify ship will fit and place points
    if BA2 == 1:
        while BC2 > 7 or PB2[BR2 - 1][BC2 - 1] != 0 or PB2[BR2 - 1][BC2] != 0 or PB2[BR2 - 1][BC2 + 1] != 0 or PB2[BR2 - 1][BC2 + 2] != 0:
            BR2 = (randint(1, 7))
            BC2 = (randint(1, 7))
        PB2[BR2 - 1][BC2 - 1] = 4
        PB2[BR2 - 1][BC2] = 4
        PB2[BR2 - 1][BC2 + 1] = 4
        PB2[BR2 - 1][BC2 + 2] = 4
    else:
        while BR2 > 7 or PB2[BR2 - 1][BC2 - 1] != 0 or PB2[BR2][BC2 - 1] != 0 or PB2[BR2 + 1][BC2 - 1] != 0 or PB2[BR2 + 2][BC2 - 1] != 0:
            BR2 = (randint(1, 7))
            BC2 = (randint(1, 7))
        PB2[BR2 - 1][BC2 - 1] = 4
        PB2[BR2][BC2 - 1] = 4
        PB2[BR2 + 1][BC2 - 1] = 4
        PB2[BR2 + 2][BC2 - 1] = 4

    # destroyer

    # horizontal or vertical axis
    DA2 = (randint(1, 2))

    # have computer assign location for destroyer
    DR2 = (randint(1, 10))
    DC2 = (randint(1, 10))

    # verify ship will fit and place points
    if DA2 == 1:
        while DC2 > 8 or PB2[DR2 - 1][DC2 - 1] != 0 or PB2[DR2 - 1][DC2] != 0 or PB2[DR2 - 1][DC2 + 1] != 0:
            DR2 = (randint(1, 8))
            DC2 = (randint(1, 8))
        PB2[DR2 - 1][DC2 - 1] = 3
        PB2[DR2 - 1][DC2] = 3
        PB2[DR2 - 1][DC2 + 1] = 3
    else:
        while DR2>8 or PB2[DR2 - 1][DC2 - 1] != 0 or PB2[DR2][DC2 - 1] != 0 or PB2[DR2 + 1][DC2 - 1] != 0:
            DR2 = (randint(1, 8))
            DC2 = (randint(1, 8))
        PB2[DR2 - 1][DC2 - 1] = 3
        PB2[DR2][DC2 - 1] = 3
        PB2[DR2 + 1][DC2 - 1] = 3

    # submarine

    # horizontal or vertical axis
    SA2 = (randint(1, 2))

    # have computer assign location for submarine
    SR2 = (randint(1, 10))
    SC2 = (randint(1, 10))

    # verify ship will fit and place points
    if SA2 == 1:
        while SC2 > 8 or PB2[SR2 - 1][SC2 - 1] != 0 or PB2[SR2 - 1][SC2] != 0 or PB2[SR2 - 1][SC2 + 1] != 0:
            SR2 = (randint(1, 8))
            SC2 = (randint(1, 8))
        PB2[SR2 - 1][SC2 - 1] = 1
        PB2[SR2 - 1][SC2] = 1
        PB2[SR2 - 1][SC2 + 1] = 1
    else:
        while SR2 > 8 or PB2[SR2 - 1][SC2 - 1] != 0 or PB2[SR2][SC2 - 1] != 0 or PB2[SR2 + 1][SC2 - 1] != 0:
            SR2 = (randint(1, 8))
            SC2 = (randint(1, 8))
        PB2[SR2 - 1][SC2 - 1] = 1
        PB2[SR2][SC2 - 1] = 1
        PB2[SR2 + 1][SC2 - 1] = 1

    # patrol boat

    # horizontal or vertical axis
    PA2 = (randint(1, 2))

    # have computer assign location for patrol boat
    PR2 = (randint(1, 10))
    PC2 = (randint(1, 10))

    # verify ship will fit and place points
    if PA2 == 1:
        while PC2 > 9 or PB2[PR2 - 1][PC2 - 1] != 0 or PB2[PR2 - 1][PC2] != 0:
            PR2 = (randint(1, 9))
            PC2 = (randint(1, 9))
        PB2[PR2 - 1][PC2 - 1] = 2
        PB2[PR2 - 1][PC2] = 2
    else:
        while PR2 > 9 or PB2[PR2 - 1][PC2 - 1] != 0 or PB2[PR2][PC2 - 1] != 0:
            PR2 = (randint(1, 9))
            PC2 = (randint(1, 9))
        PB2[PR2 - 1][PC2 - 1] = 2
        PB2[PR2][PC2 - 1] = 2

    # create secondary board for player and computer
    SB1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    SB2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # create hit counter for each ship

    # list of hit counters
    HCA1 = [0, 0, 0, 0, 0]
    HCA2 = [0, 0, 0, 0, 0]
    # 5,4,3,2,1 (5 = carrier, 4 = battleship, 3 = destroyer, 2 = patrol boat, 1 = submarine)

    # create while loop so game continues until someone wins
    gameover = 0
    while gameover == 0:

        # player 1 picks a point
        print('\nIT IS YOUR TURN PLAYER 1\n\n')
        P1PR = int(input('Pick a row you think one of the opponents ship is on: '))  # player one point row
        while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:  # make sure it is valid point
            P1PR = int(input('Please select an integer between 1-10: '))
            P1PC = int(input('Pick a column you think one of the opponents ship is on: '))  # player one point column
        while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:  # make sure it is valid point
            P1PC = int(input('Please select an integer between 1-10: '))

        # verify that point hasn't been picked yet
        while SB1[P1PR - 1][P1PC - 1] != 0:  # if SB1 is not equal to 0 then point already picked
            print('\nYou have already picked that point\n\n')
            P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt user to pick again
            while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
                P1PR = int(input('Please select an integer between 1-10: '))
            P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
            while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
                P1PC = int(input('Please select an integer between 1-10: '))

        # if player hits a ship
        while PB2[P1PR - 1][P1PC - 1] == 1 or PB2[P1PR - 1][P1PC - 1] == 2 or PB2[P1PR - 1][P1PC - 1] == 3 or PB2[P1PR - 1][P1PC - 1] == 4 or PB2[P1PR - 1][P1PC - 1] == 5:  # If he picks a point and ship is there

            # check which ship it hit
            if PB2[P1PR - 1][P1PC - 1] == 1:  # I set the submarine points to one
                HCA2[4] = HCA2[4] + 1
                if HCA2[4] == 3:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe submarine has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')
            elif PB2[P1PR - 1][P1PC - 1] == 2:  # I set the patrol boat points to two
                HCA2[3] = HCA2[3] + 1
                if HCA2[3] == 2:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe patrol boat has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')
            elif PB2[P1PR - 1][P1PC - 1] == 3:  # I set the destroyer points to three
                HCA2[2] = HCA2[2] + 1
                if HCA2[2] == 3:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe destroyer has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')
            elif PB2[P1PR - 1][P1PC - 1] == 4:  # I set the battleship points to four
                HCA2[1] = HCA2[1] + 1
                if HCA2[1] == 4:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe battleship has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')
            elif PB2[P1PR - 1][P1PC - 1] == 5:  # I set the carrier point to five
                HCA2[0] = HCA2[0] + 1
                if HCA2[0] == 5:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe carrier has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')

            # if sum of hit counter list is 17, end the game
            if HCA2[0] + HCA2[1] + HCA2[2] + HCA2[3] + HCA2[4] == 17:
                gameover = 1
                # sound()
                print('\nCongratulations player 1! YOU WON! You now have bragging rights over your opponent for the rest of your life!\n\n')

            # if game is over, stop while loop
            if gameover == 1:
                break

            # prompt to keep choosing until a miss
            P1PR = int(input('Pick a row you think one of the opponents ship is on: '))
            while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
                P1PR = int(input('Please select an integer between 1-10: '))
            P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
            while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
                P1PC = int(input('Please select an integer between 1-10: '))

            # check if point has already been picked
            while SB1[P1PR - 1][P1PC - 1] != 0:  # if secondary point not equal to 0 then point already picked
                print('\nYou have already picked that point\n\n')
                P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt to pick again
                while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
                    P1PR = int(input('Please select an integer between 1-10: '))
                P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
                while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
                    P1PC = int(input('Please select an integer between 1-10: '))

        # if game is over, stop while loop
        if gameover == 1:
            break

        # if player misses a ship
        if PB2[P1PR - 1][P1PC - 1] == 0:  # if he picks a point and there is no ship

            # check if point has already been picked
            while SB1[P1PR - 1][P1PC - 1] != 0: # if the secondary point doesn't equal 0 then point already picked
                print('\nYou have already picked that point\n\n')
                P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt to pick again
                while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
                    P1PR = int(input('Please select an integer between 1-10: '))
                P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
                while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
                    P1PC = int(input('Please select an integer between 1-10: '))
            SB1[P1PR - 1][P1PC - 1] = -1  # set SB1 to -1 to show miss
            print('\nMISS!\n\n')
            pretty_print_list(SB1)

        # computer picking points

        # computer plays based off difficulty
        if gameDifficulty == 1:  # easy difficulty
            P2PR = (randint(1, 10))
            P2PC = (randint(1, 10))

            # check if point already picked
            while SB2[P2PR - 1][P2PC - 1] != 0:
                P2PR = (randint(1, 10))
                P2PC = (randint(1, 10))

            # if computer hits ship
            while PB1[P2PR - 1][P2PC - 1] == 1 or PB1[P2PR - 1][P2PC - 1] == 2 or PB1[P2PR - 1][P2PC - 1] == 3 or PB1[P2PR - 1][P2PC - 1] == 4 or PB1[P2PR - 1][P2PC - 1] == 5:

                # hit counter and sunk ship
                if PB1[P2PR - 1][P2PC - 1] == 1:
                    HCA1[4] = HCA1[4] + 1
                    if HCA1[4] == 3:  # if every point has been hit, ship is sunk
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your submarine\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 2:
                    HCA1[3] = HCA1[3] + 1
                    if HCA1[3] == 2:  # if every point has been hit, ship is sunk
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your patrol boat\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 3:
                    HCA1[2] = HCA1[2] + 1
                    if HCA1[2] == 3:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your destroyer\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 4:
                    HCA1[1] = HCA1[1] + 1
                    if HCA1[1] == 4:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your battleship\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1(P2PR,P2PC)==5:
                    HCA1[0] = HCA1[0] + 1
                    if HCA1[0] == 5:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your carrier\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')

                # if sum of hit counter list is 17, end the game
                if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
                    gameover = 1
                    print('\nComputer wins! Better luck next time!\n\n')

                # if game is over, stop while loop
                if gameover == 1:
                    break

                # prompt to choose until a miss
                P2PR = (randint(1, 10))
                P2PC = (randint(1, 10))

                # check if point has already been picked
                while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point doesn't equal 0 then computer already picked that point
                    P2PR = (randint(1, 10)) # prompt computer to pick again
                    P2PC = (randint(1, 10))

            # if game is over, stop while loop
            if gameover == 1:
                break

            # if computer misses a ship
            if PB1[P2PR - 1][P2PC - 1] == 0:  # if he picks point and there is no ship

                # check if point has already been picked
                while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point doesn't equal 0 then computer already picked that point
                    P2PR = (randint(1, 10))  # prompt computer to pick again
                    P2PC = (randint(1, 10))
                SB2[P2PR - 1][P2PC - 1] = -1  # set SB2 equal to -1 to show miss
                print('\nComputer missed your ships!\n\n')

        elif gameDifficulty == 2:  # pro difficulty (chooses points around it)
            P2PR = (randint(1, 10))
            P2PC = (randint(1, 10))

            # check if point already picked
            while SB2[P2PR - 1][P2PC - 1] != 0:
                P2PR = (randint(1, 10))  # prompt computer to pick again
                P2PC = (randint(1, 10))

            # if computer hits ship
            while PB1[P2PR - 1][P2PC - 1] == 1 or PB1[P2PR - 1][P2PC - 1] == 2 or PB1[P2PR - 1][P2PC - 1] == 3 or PB1[P2PR - 1][P2PC - 1] == 4 or PB1[P2PR - 1][P2PC - 1] == 5:

                # hit counter and sunk ship
                if PB1[P2PR - 1][P2PC - 1] == 1:
                    HCA1[4] = HCA1[4] + 1
                    if HCA1[4] == 3:  # if every point hit, ship is sunk
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your submarine\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')

                elif PB1[P2PR - 1][P2PC - 1] == 2:
                    HCA1[3] = HCA1[3] + 1
                    if HCA1[3] == 2:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your patrol boat\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1(P2PR,P2PC) == 3:
                    HCA1[2] = HCA1[2] + 1
                    if HCA1[2] == 3:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your destroyer\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 4:
                    HCA1[1] = HCA1[1] + 1
                    if HCA1[1] == 4:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your battleship\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 5:
                    HCA1[0] = HCA1[0] + 1
                    if HCA1[0] == 5:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer sunk your carrier\n\n')
                    else:
                        PB1[P2PR - 1][P2PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                        SB2[P2PR - 1][P2PC - 1] = 1  # sets player 1's secondary board to show a hit
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')

                # if sum of hit counter list is 17, end the game
                if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
                    gameover = 1
                    print('\nComputer wins! Better luck next time!\n\n')

                # if game is over, stop while loop
                if gameover == 1:
                    break

                # prompt to pick until miss
                while PB1[P2PR - 1][P2PC - 1] != 0:
                    RNG = (randint(1, 4))
                    if RNG == 1:
                        P2PC = P2PC + 1
                        while P2PC > 10:
                            P2PC = P2PC - 2
                            if P2PC > 10 or P2PC < 1:
                                P2PR = (randint(1, 10))
                                P2PC = (randint(1, 10))
                    elif RNG == 2:
                        P2PR = P2PR + 1
                        while P2PR > 10:
                            P2PR = P2PR - 2
                            if P2PR > 10 or P2PR < 1:
                                P2PR = (randint(1, 10))
                                P2PC = (randint(1, 10))
                    elif RNG == 3:
                        P2PR = P2PR - 1
                        while P2PR < 1:
                            P2PR = P2PR + 2
                            if P2PR > 10 or P2PR < 1:
                                P2PR = (randint(1, 10))
                                P2PC = (randint(1, 10))
                    elif RNG == 4:
                        P2PC = P2PC - 1
                        while P2PC < 1:
                            P2PC = P2PC + 2
                            if P2PC > 10 or P2PC < 1:
                                P2PR = (randint(1, 10))
                                P2PC = (randint(1, 10))

                # check if point already picked
                while SB2[P2PR - 1][P2PC - 1] != 0:  # if point already picked, just randomly pick
                    P2PR = (randint(1, 10))
                    P2PC = (randint(1, 10))

            # if sum of hit counter list is 17, end the game
            if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
                gameover = 1
                print('\nComputer wins! Better luck next time!\n\n')

            # if game is over, stop while loop
            if gameover == 1:
                break

            # if computer misses ship
            if PB1[P2PR - 1][P2PC - 1] == 0:  # if he picks point and there is no ship

                # check if point already picked
                while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point doesn't equal 0 then computer already picked that point
                    P2PR = (randint(1, 10))  # prompt computer to pick again
                    P2PC = (randint(1, 10))
                SB2[P2PR - 1][P2PC - 1] = -1  # set secondary board equal to -1 to show miss
                print('\nComputer missed your ships!\n\n')

        elif gameDifficulty == 3:  # god mode difficulty (insta kill)
            P2PR = (randint(1, 10))
            P2PC = (randint(1, 10))

            # check if point already picked
            while SB2[P2PR - 1][P2PC - 1] != 0:
                P2PR = (randint(1, 10))  # prompt computer to pick again
                P2PC = (randint(1, 10))

            # if computer hits ship
            while PB1[P2PR - 1][P2PC - 1] == 1 or PB1[P2PR - 1][P2PC - 1] == 2 or PB1[P2PR - 1][P2PC - 1] == 3 or PB1[P2PR - 1][P2PC - 1] == 4 or PB1[P2PR - 1][P2PC - 1] == 5:

                # set variable equal to ship that was hit
                ship_hit = PB1[P2PR - 1][P2PC - 1]

                # hit counter and sunk ship
                if PB1[P2PR - 1][P2PC - 1] == 1:
                    HCA1[4] = HCA1[4] + 1
                    if HCA1[4] == 3:  # if every point hit, ship is sunk
                        pretty_print_list(PB1)
                        print('\nComputer sunk your submarine\n\n')
                    else:
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 2:
                    HCA1[3] = HCA1[3] + 1
                    if HCA1[3] == 2:
                        pretty_print_list(PB1)
                        print('\nComputer sunk your patrol boat\n\n')
                    else:
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 3:
                    HCA1[2] = HCA1[2] + 1
                    if HCA1[2] == 3:
                        pretty_print_list(PB1)
                        print('\nComputer sunk your destroyer\n\n')
                    else:
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 4:
                    HCA1[1] = HCA1[1] + 1
                    if HCA1[1] == 4:
                        pretty_print_list(PB1)
                        print('\nComputer sunk your battleship\n\n')
                    else:
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')
                elif PB1[P2PR - 1][P2PC - 1] == 5:
                    HCA1[0] = HCA1[0] + 1
                    if HCA1[0] == 5:
                        pretty_print_list(PB1)
                        print('\nComputer sunk your carrier\n\n')
                    else:
                        pretty_print_list(PB1)
                        print('\nComputer got a hit\n\n')

                # change values of PB1 and SB2
                PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to show ship been hit
                SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to 1 to show hit

                # if sum of hit counter list is 17, end the game
                if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
                    gameover = 1
                print('\nComputer wins! Better luck next time!\n\n')

                # if game is over, stop while loop
                if gameover == 1:
                    break

                # insta kill ship
                for k in range(1, 11):
                    for h in range(1, 11):
                        if PB1[k - 1][h - 1] == ship_hit:
                            if ship_hit == 1:
                                HCA1[4] = HCA1[4] + 1
                                PB1[k - 1][h - 1] = 9
                                if HCA1[4] == 3:
                                    pretty_print_list(PB1)
                                    print('\nComputer sunk your submarine\n\n')
                                else:
                                    pretty_print_list(PB1)
                                    print('\nComputer got a hit\n\n')
                            elif ship_hit == 2:
                                HCA1[3] = HCA1[3] + 1
                                PB1[k - 1][h - 1] = 9
                                if HCA1[3] == 2:
                                    pretty_print_list(PB1)
                                    print('\nComputer sunk your patrol boat\n\n')
                                else:
                                    pretty_print_list(PB1)
                                    print('\nComputer got a hit\n\n')
                            elif ship_hit == 3:
                                HCA1[2] = HCA1[2] + 1
                                PB1[k - 1][h - 1] = 9
                                if HCA1[2] == 3:
                                    pretty_print_list(PB1)
                                    print('\nComputer sunk your destroyer\n\n')
                                else:
                                    pretty_print_list(PB1)
                                    print('\nComputer got a hit\n\n')
                            elif ship_hit == 4:
                                HCA1[1] = HCA1[1] + 1
                                PB1[k - 1][h - 1] = 9
                                if HCA1[1] == 4:
                                    pretty_print_list(PB1)
                                    print('\nComputer sunk your battleship\n\n')
                                else:
                                    pretty_print_list(PB1)
                                    print('\nComputer got a hit\n\n')
                            elif ship_hit == 5:
                                HCA1[0] = HCA1[0] + 1
                                PB1[k - 1][h - 1] = 9
                                if HCA1[0] == 5:
                                    pretty_print_list(PB1)
                                    print('\nComputer sunk your carrier\n\n')
                                else:
                                    pretty_print_list(PB1)
                                    print('\nComputer got a hit\n\n')
                        SB2[k - 1][h - 1] = 1 # makes sure insta kill is covered on SB2

                # prompt to pick until miss
                P2PR = (randint(1, 10))
                P2PC = (randint(1, 10))

                # check if point already picked
                while SB2[P2PR - 1][P2PC - 1] != 0:
                    P2PR = (randint(1, 10))
                    P2PC = (randint(1, 10))

            # if sum of hit counter list is 17, end the game
            if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
                gameover = 1
                print('\nComputer wins! Better luck next time!\n\n')

            # if game is over, stop while loop
            if gameover == 1:
                break

            # if computer misses ship
            if PB1[P2PR - 1][P2PC - 1] == 0:  # if he picks point and there is no ship

                # check if point already picked
                while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point does not equal 0 then point already picked
                    P2PR = (randint(1, 10))  # prompt computer to pick again
                    P2PC = (randint(1, 10))

                SB2[P2PR - 1][P2PC - 1] = -1  # set secondary board to -1 to show miss
                print('\nComputer missed your ships!\n\n')
else:
    # display rules for 2 player
    print('\nYou have chose to play against another player. \nTake turns choosing points on your opponents 10x10 board \nin hopes of hitting a part of the ship. \nIf you hit every part of the ship it will be sunk and \nyou will continue picking points until you sink all ships. \nThe first player to sink all opponent ships wins. \n\nGoodluck, Have fun! \n\n')

    # player 1 picking points

    # create primary board for player 1
    PB1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # carrier

    # horizontal or vertical axis
    CA1 = int(input('Specify whether you would like your carrier to be horizontal(1) or vertical(2): '))  # carrier axis player one
    while CA1 != 1 and CA1 != 2:
        CA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for carrier
    CR1 = int(input('Specify what row you would like to place the carrier: '))  # carrier row player one
    while CR1 != 1 and CR1 != 2 and CR1 != 3 and CR1 != 4 and CR1 != 5 and CR1 != 6 and CR1 != 7 and CR1 != 8 and CR1 != 9 and CR1 != 10:
        CR1 = int(input('Please select a number between 1-10: '))
    CC1 = int(input('Specify what column you would like to place the carrier: '))  # carrier column player one
    while CC1 != 1 and CC1 != 2 and CC1 != 3 and CC1 != 4 and CC1 != 5 and CC1 != 6 and CC1 != 7 and CC1 != 8 and CC1 != 9 and CC1 != 10:
        CC1 = int(input('Please select a number between 1-10: '))

    # verify that the ship will fit and place points
    if CA1 == 1:
        while CC1 > 6 or CC1 <= 0 or CC1 % 1 != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            CR1 = int(input('Try a row integer that is between 1 and 6: '))
            CC1 = int(input('Try a column integer that is between 1 and 6: '))
        PB1[CR1 - 1][CC1 - 1] = 5
        PB1[CR1 - 1][CC1] = 5
        PB1[CR1 - 1][CC1 + 1] = 5
        PB1[CR1 - 1][CC1 + 2] = 5
        PB1[CR1 - 1][CC1 + 3] = 5
    else:
        while CR1 > 6 or CR1 <= 0 or CR1 % 1 != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            CR1 = int(input('Try a row integer that is between 1 and 6: '))
            CC1 = int(input('Try a column integer that is between 1 and 6: '))
        PB1[CR1 - 1][CC1 - 1] = 5
        PB1[CR1][CC1 - 1] = 5
        PB1[CR1 + 1][CC1 - 1] = 5
        PB1[CR1 + 2][CC1 - 1] = 5
        PB1[CR1 + 3][CC1 - 1] = 5

    # display board after each ship placement
    pretty_print_list(PB1)
    print('Your carrier has been placed \n\n')

    # battleship

    # horizontal or vertical axis
    BA1 = int(input('Specify whether you would like your battleship to be horizontal(1) or vertical(2): '))  # battleship axis player one
    while BA1 != 1 and BA1 != 2:
        BA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for battleship
    BR1 = int(input('Specify what row you would like to place the battleship: ')) # battleship row player one
    while BR1 != 1 and BR1 != 2 and BR1 != 3 and BR1 != 4 and BR1 != 5 and BR1 != 6 and BR1 != 7 and BR1 != 8 and BR1 != 9 and BR1 != 10:
        BR1 = int(input('Please select a number between 1-10: '))
    BC1 = int(input('Specify what column you would like to place the battleship: ')) # battleship column player one
    while BC1 != 1 and BC1 != 2 and BC1 != 3 and BC1 != 4 and BC1 != 5 and BC1 != 6 and BC1 != 7 and BC1 != 8 and BC1 != 9 and BC1 != 10:
        BC1 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if BA1 == 1:
        while BC1 > 7 or BC1 <= 0 or BC1 % 1 != 0 or PB1[BR1 - 1][BC1 - 1] != 0 or PB1[BR1 - 1][BC1] != 0 or PB1[BR1 - 1][BC1 + 1] != 0 or PB1[BR1 - 1][BC1 + 2] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            BR1 = int(input('Try a row integer that is between 1 and 7: '))
            BC1 = int(input('Try a column integer that is between 1 and 7: '))
        PB1[BR1 - 1][BC1 - 1] = 4
        PB1[BR1 - 1][BC1] = 4
        PB1[BR1 - 1][BC1 + 1] = 4
        PB1[BR1 - 1][BC1 + 2] = 4
    else:
        while BR1 > 7 or BR1 <= 0 or BR1 % 1 != 0 or PB1[BR1 - 1][BC1 - 1] != 0 or PB1[BR1][BC1 - 1] != 0 or PB1[BR1 + 1][BC1 - 1] != 0 or PB1[BR1 + 2][BC1 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            BR1 = int(input('Try a row integer that is between 1 and 7: '))
            BC1 = int(input('Try a column integer that is between 1 and 7: '))
        PB1[BR1 - 1][BC1 - 1] = 4
        PB1[BR1][BC1 - 1] = 4
        PB1[BR1 + 1][BC1 - 1] = 4
        PB1[BR1 + 2][BC1 - 1] = 4

    # display the board
    pretty_print_list(PB1)
    print('Your battleship has been placed \n\n')

    # destroyer

    # horizontal or vertical axis
    DA1 = int(input('Specify whether you would like your destroyer to be horizontal(1) or vertical(2): '))  # destroyer axis player one
    while DA1 != 1 and DA1 != 2:
        DA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for destroyer
    DR1 = int(input('Specify what row you would like to place the destroyer: ')) # destroyer row player one
    while DR1 != 1 and DR1 != 2 and DR1 != 3 and DR1 != 4 and DR1 != 5 and DR1 != 6 and DR1 != 7 and DR1 != 8 and DR1 != 9 and DR1 != 10:
        DR1 = int(input('Please select a number between 1-10: '))
    DC1 = int(input('Specify what column you would like to place the destroyer: ')) # destroyer column player one
    while DC1 != 1 and DC1 != 2 and DC1 != 3 and DC1 != 4 and DC1 != 5 and DC1 != 6 and DC1 != 7 and DC1 != 8 and DC1 != 9 and DC1 != 10:
        DC1 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if DA1 == 1:
        while DC1 > 8 or DC1 < 0 or DC1 % 1 != 0 or PB1[DR1 - 1][DC1 - 1] != 0 or PB1[DR1 - 1][DC1] != 0 or PB1[DR1 - 1][DC1 + 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            DR1 = int(input('Try a row integer that is between 1 and 8: '))
            DC1 = int(input('Try a column integer that is between 1 and 8: '))
        PB1[DR1 - 1][DC1 - 1] = 3
        PB1[DR1 - 1][DC1] = 3
        PB1[DR1 - 1][DC1 + 1] = 3
    else:
        while DR1 > 8 or DR1 < 0 or DR1 % 1 != 0 or PB1[DR1 - 1][DC1 - 1] != 0 or PB1[DR1][DC1 - 1] != 0 or PB1[DR1 + 1][DC1 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            DR1 = int(input('Try a row integer that is between 1 and 8: '))
            DC1 = int(input('Try a column integer that is between 1 and 8: '))
        PB1[DR1 - 1][DC1 - 1] = 3
        PB1[DR1][DC1 - 1] = 3
        PB1[DR1 + 1][DC1 - 1] = 3

    # display the board
    pretty_print_list(PB1)
    print('Your destroyer has been placed \n\n')

    # submarine

    # horizontal or vertical axis
    SA1 = int(input('Specify whether you would like your submarine to be horizontal(1) or vertical(2): ')) # submarine axis player one
    while SA1 != 1 and SA1 != 2:
        SA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for submarine
    SR1 = int(input('Specify what row you would like to place the submarine: ')) # submarine row player one
    while SR1 != 1 and SR1 != 2 and SR1 != 3 and SR1 != 4 and SR1 != 5 and SR1 != 6 and SR1 != 7 and SR1 != 8 and SR1 != 9 and SR1 != 10:
        SR1 = int(input('Please select a number between 1-10: '))
    SC1 = int(input('Specify what column you would like to place the submarine: ')) # submarine column player one
    while SC1 != 1 and SC1 != 2 and SC1 != 3 and SC1 != 4 and SC1 != 5 and SC1 != 6 and SC1 != 7 and SC1 != 8 and SC1 != 9 and SC1 != 10:
        SC1 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if SA1 == 1:
        while SC1 > 8 or SC1 < 0 or SC1 % 1 != 0 or PB1[SR1 - 1][SC1 - 1] != 0 or PB1[SR1 - 1][SC1] != 0 or PB1[SR1 - 1][SC1 + 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            SR1 = int(input('Try a row integer that is between 1 and 8: '))
            SC1 = int(input('Try a column integer that is between 1 and 8: '))
        PB1[SR1 - 1][SC1 - 1] = 1
        PB1[SR1 - 1][SC1] = 1
        PB1[SR1 - 1][SC1 + 1] = 1
    else:
        while SR1 > 8 or SR1 < 0 or SR1 % 1 != 0 or PB1[SR1 - 1][SC1 - 1] != 0 or PB1[SR1][SC1 - 1] != 0 or PB1[SR1 + 1][SC1 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            SR1 = int(input('Try a row integer that is between 1 and 8: '))
            SC1 = int(input('Try a column integer that is between 1 and 8: '))
        PB1[SR1 - 1][SC1 - 1] = 1
        PB1[SR1][SC1 - 1] = 1
        PB1[SR1 + 1][SC1 - 1] = 1

    # display the board
    pretty_print_list(PB1)
    print('Your submarine has been placed \n\n')

    # patrol boat

    # horizontal or vertical axis
    PA1 = int(input('Specify whether you would like your patrol boat to be horizontal(1) or vertical(2): ')) # patrol boat axis player one
    while PA1 != 1 and PA1 != 2:
        PA1 = int(input('Please select either 1 or 2: '))

    # ask player 1 to assign location for patrol boat
    PR1 = int(input('Specify what row you would like to place the patrol boat: '))  # patrol boat row player one
    while PR1 != 1 and PR1 != 2 and PR1 != 3 and PR1 != 4 and PR1 != 5 and PR1 != 6 and PR1 != 7 and PR1 != 8 and PR1 != 9 and PR1 != 10:
        PR1 = int(input('Please select a number between 1-10: '))
    PC1 = int(input('Specify what column you would like to place the patrol boat: '))  # patrol boat column player one
    while PC1 != 1 and PC1 != 2 and PC1 != 3 and PC1 != 4 and PC1 != 5 and PC1 != 6 and PC1 != 7 and PC1 != 8 and PC1 != 9 and PC1 != 10:
        PC1 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if PA1 == 1:
        while PC1 > 9 or PC1 < 0 or PC1 % 1 != 0 or PB1[PR1 - 1][PC1 - 1] != 0 or PB1[PR1 - 1][PC1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            PR1 = int(input('Try a row integer that is between 1 and 9: '))
            PC1 = int(input('Try a column integer that is between 1 and 9: '))
        PB1[PR1 - 1][PC1 - 1] = 2
        PB1[PR1 - 1][PC1] = 2
    else:
        while PR1 > 9 or PR1 < 0 or PR1 % 1 != 0 or PB1[PR1 - 1][PC1 - 1] != 0 or PB1[PR1][PC1 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            PR1 = int(input('Try a row integer that is between 1 and 9: '))
            PC1 = int(input('Try a column integer that is between 1 and 9: '))
        PB1[PR1 - 1][PC1 - 1] = 2
        PB1[PR1][PC1 - 1] = 2

    # display the board
    pretty_print_list(PB1)
    print('Your patrol boat has been placed \n\n')

    # clear (clears the output)

    # switch to player 2 so he can pick ship placement
    print('Now that player 1 has finished placing his ships, it is your turn player 2!\n\n')

    # create primary board player 2
    PB2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # horizontal or vertical axis
    CA2 = int(input('Specify whether you would like your carrier to be horizontal(1) or vertical(2): '))  # carrier axis player two
    while CA2 != 1 and CA2 != 2:
        CA2 = int(input('Please select either 1 or 2: '))

    # ask player 2 to assign location for carrier
    CR2 = int(input('Specify what row you would like to place the carrier: '))  # carrier row player two
    while CR2 != 1 and CR2 != 2 and CR2 != 3 and CR2 != 4 and CR2 != 5 and CR2 != 6 and CR2 != 7 and CR2 != 8 and CR2 != 9 and CR2 != 10:
        CR2 = int(input('Please select a number between 1-10: '))
    CC2 = int(input('Specify what column you would like to place the carrier: '))  # carrier column player two
    while CC2 != 1 and CC2 != 2 and CC2 != 3 and CC2 != 4 and CC2 != 5 and CC2 != 6 and CC2 != 7 and CC2 != 8 and CC2 != 9 and CC2 != 10:
        CC2 = int(input('Please select a number between 1-10: '))

    # verify that the ship will fit and place points
    if CA2 == 1:
        while CC2 > 6 or CC2 <= 0 or CC2 % 1 != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            CR2 = int(input('Try a row integer that is between 1 and 6: '))
            CC2 = int(input('Try a column integer that is between 1 and 6: '))
        PB2[CR2 - 1][CC2 - 1] = 5
        PB2[CR2 - 1][CC2] = 5
        PB2[CR2 - 1][CC2 + 1] = 5
        PB2[CR2 - 1][CC2 + 2] = 5
        PB2[CR2 - 1][CC2 + 3] = 5
    else:
        while CR2 > 6 or CR2 <= 0 or CR2 % 1 != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            CR2 = int(input('Try a row integer that is between 1 and 6: '))
            CC2 = int(input('Try a column integer that is between 1 and 6: '))
        PB2[CR2 - 1][CC2 - 1] = 5
        PB2[CR2][CC2 - 1] = 5
        PB2[CR2 + 1][CC2 - 1] = 5
        PB2[CR2 + 2][CC2 - 1] = 5
        PB2[CR2 + 3][CC2 - 1] = 5

    # display board
    pretty_print_list(PB2)
    print('Your carrier has been placed \n\n')

    # battleship

    # horizontal or vertical axis
    BA2 = int(input('Specify whether you would like your battleship to be horizontal(1) or vertical(2): '))  # battleship axis player two
    while BA2 != 1 and BA2 != 2:
        BA2 = int(input('Please select either 1 or 2: '))

    # ask player 2 to assign location for battleship
    BR2 = int(input('Specify what row you would like to place the battleship: ')) # battleship row player two
    while BR2 != 1 and BR2 != 2 and BR2 != 3 and BR2 != 4 and BR2 != 5 and BR2 != 6 and BR2 != 7 and BR2 != 8 and BR2 != 9 and BR2 != 10:
        BR2 = int(input('Please select a number between 1-10: '))
    BC2 = int(input('Specify what column you would like to place the battleship: ')) # battleship column player two
    while BC2 != 1 and BC2 != 2 and BC2 != 3 and BC2 != 4 and BC2 != 5 and BC2 != 6 and BC2 != 7 and BC2 != 8 and BC2 != 9 and BC2 != 10:
        BC2 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if BA2 == 1:
        while BC2 > 7 or BC2 <= 0 or BC2 % 1 != 0 or PB2[BR2 - 1][BC2 - 1] != 0 or PB2[BR2 - 1][BC2] != 0 or PB2[BR2 - 1][BC2 + 1] != 0 or PB2[BR2 - 1][BC2 + 2] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            BR2 = int(input('Try a row integer that is between 1 and 7: '))
            BC2 = int(input('Try a column integer that is between 1 and 7: '))
        PB2[BR2 - 1][BC2 - 1] = 4
        PB2[BR2 - 1][BC2] = 4
        PB2[BR2 - 1][BC2 + 1] = 4
        PB2[BR2 - 1][BC2 + 2] = 4
    else:
        while BR2 > 7 or BR2 <= 0 or BR2 % 1 != 0 or PB2[BR2 - 1][BC2 - 1] != 0 or PB2[BR2][BC2 - 1] != 0 or PB2[BR2 + 1][BC2 - 1] != 0 or PB2[BR2 + 2][BC2 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            BR2 = int(input('Try a row integer that is between 1 and 7: '))
            BC2 = int(input('Try a column integer that is between 1 and 7: '))
        PB2[BR2 - 1][BC2 - 1] = 4
        PB2[BR2][BC2 - 1] = 4
        PB2[BR2 + 1][BC2 - 1] = 4
        PB2[BR2 + 2][BC2 - 1] = 4

    # display the board
    pretty_print_list(PB2)
    print('Your battleship has been placed \n\n')

    # destroyer

    # horizontal or vertical axis
    DA2 = int(input('Specify whether you would like your destroyer to be horizontal(1) or vertical(2): '))  # destroyer axis player two
    while DA2 != 1 and DA2 != 2:
        DA2 = int(input('Please select either 1 or 2: '))

    # ask player 2 to assign location for destroyer
    DR2 = int(input('Specify what row you would like to place the destroyer: '))  # destroyer row player two
    while DR2 != 1 and DR2 != 2 and DR2 != 3 and DR2 != 4 and DR2 != 5 and DR2 != 6 and DR2 != 7 and DR2 != 8 and DR2 != 9 and DR2 != 10:
        DR2 = int(input('Please select a number between 1-10: '))
    DC2 = int(input('Specify what column you would like to place the destroyer: '))  # destroyer column player two
    while DC2 != 1 and DC2 != 2 and DC2 != 3 and DC2 != 4 and DC2 != 5 and DC2 != 6 and DC2 != 7 and DC2 != 8 and DC2 != 9 and DC2 != 10:
        DC2 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if DA2 == 1:
        while DC2 > 8 or DC2 < 0 or DC2 % 1 != 0 or PB2[DR2 - 1][DC2 - 1] != 0 or PB2[DR2 - 1][DC2] != 0 or PB2[DR2 - 1][DC2 + 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            DR2 = int(input('Try a row integer that is between 1 and 8: '))
            DC2 = int(input('Try a column integer that is between 1 and 8: '))
        PB2[DR2 - 1][DC2 - 1] = 3
        PB2[DR2 - 1][DC2] = 3
        PB2[DR2 - 1][DC2 + 1] = 3
    else:
        while DR2 > 8 or DR2 < 0 or DR2 % 1 != 0 or PB2[DR2 - 1][DC2 - 1] != 0 or PB2[DR2][DC2 - 1] != 0 or PB2[DR2 + 1][DC2 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            DR2 = int(input('Try a row integer that is between 1 and 8: '))
            DC2 = int(input('Try a column integer that is between 1 and 8: '))
        PB2[DR2 - 1][DC2 - 1] = 3
        PB2[DR2][DC2 - 1] = 3
        PB2[DR2 + 1][DC2 - 1] = 3

    # display the board
    pretty_print_list(PB2)
    print('Your destroyer has been placed \n\n')

    # submarine

    # horizontal or vertical axis
    SA2 = int(input('Specify whether you would like your submarine to be horizontal(1) or vertical(2): '))  # submarine axis player two
    while SA2 != 1 and SA2 != 2:
        SA2 = int(input('Please select either 1 or 2: '))

    # ask player 2 to assign location for submarine
    SR2 = int(input('Specify what row you would like to place the submarine: '))  # submarine row player two
    while SR2 != 1 and SR2 != 2 and SR2 != 3 and SR2 != 4 and SR2 != 5 and SR2 != 6 and SR2 != 7 and SR2 != 8 and SR2 != 9 and SR2 != 10:
        SR2 = int(input('Please select a number between 1-10: '))
    SC2 = int(input('Specify what column you would like to place the submarine: '))  # submarine column player two
    while SC2 != 1 and SC2 != 2 and SC2 != 3 and SC2 != 4 and SC2 != 5 and SC2 != 6 and SC2 != 7 and SC2 != 8 and SC2 != 9 and SC2 != 10:
        SC2 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if SA2 == 1:
        while SC2 > 8 or SC2 < 0 or SC2 % 1 != 0 or PB2[SR2 - 1][SC2 - 1] != 0 or PB2[SR2 - 1][SC2] != 0 or PB2[SR2 - 1][SC2 + 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            SR2 = int(input('Try a row integer that is between 1 and 8: '))
            SC2 = int(input('Try a column integer that is between 1 and 8: '))
        PB2[SR2 - 1][SC2 - 1] = 1
        PB2[SR2 - 1][SC2] = 1
        PB2[SR2 - 1][SC2 + 1] = 1
    else:
        while SR2 > 8 or SR2 < 0 or SR2 % 1 != 0 or PB2[SR2 - 1][SC2 - 1] != 0 or PB2[SR2][SC2 - 1] != 0 or PB2[SR2 + 1][SC2 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            SR2 = int(input('Try a row integer that is between 1 and 8: '))
            SC2 = int(input('Try a column integer that is between 1 and 8: '))
        PB2[SR2 - 1][SC2 - 1] = 1
        PB2[SR2][SC2 - 1] = 1
        PB2[SR2 + 1][SC2 - 1] = 1

    # display the board
    pretty_print_list(PB2)
    print('Your submarine has been placed \n\n')

    # patrol boat

    # horizontal or vertical axis
    PA2 = int(input('Specify whether you would like your patrol boat to be horizontal(1) or vertical(2): ')) # patrol boat axis player two
    while PA2 != 1 and PA2 != 2:
        PA2 = int(input('Please select either 1 or 2: '))

    # ask player 2 to assign location for patrol boat
    PR2 = int(input('Specify what row you would like to place the patrol boat: '))  # patrol boat row player two
    while PR2 != 1 and PR2 != 2 and PR2 != 3 and PR2 != 4 and PR2 != 5 and PR2 != 6 and PR2 != 7 and PR2 != 8 and PR2 != 9 and PR2 != 10:
        PR2 = int(input('Please select a number between 1-10: '))
    PC2 = int(input('Specify what column you would like to place the patrol boat: '))  # patrol boat column player two
    while PC2 != 1 and PC2 != 2 and PC2 != 3 and PC2 != 4 and PC2 != 5 and PC2 != 6 and PC2 != 7 and PC2 != 8 and PC2 != 9 and PC2 != 10:
        PC2 = int(input('Please select a number between 1-10: '))

    # verify ship will fit and place points
    if PA2 == 1:
        while PC2 > 9 or PC2 < 0 or PC2 % 1 != 0 or PB2[PR2 - 1][PC2 - 1] != 0 or PB2[PR2 - 1][PC2] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            PR2 = int(input('Try a row integer that is between 1 and 9: '))
            PC2 = int(input('Try a column integer that is between 1 and 9: '))
        PB2[PR2 - 1][PC2 - 1] = 2
        PB2[PR2 - 1][PC2] = 2
    else:
        while PR2 > 9 or PR2 < 0 or PR2 % 1 != 0 or PB2[PR2 - 1][PC2 - 1] != 0 or PB2[PR2][PC2 - 1] != 0:
            print('\nThis ship cannot fit in the location you have chosen.\n\n')
            PR2 = int(input('Try a row integer that is between 1 and 9: '))
            PC2 = int(input('Try a column integer that is between 1 and 9: '))
        PB2[PR2 - 1][PC2 - 1] = 2
        PB2[PR2][PC2 - 1] = 2

    # display the board
    pretty_print_list(PB2)
    print('Your patrol boat has been placed \n\n')

    # clear (clears the output)

    # create secondary board for player 1 and 2
    SB1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    SB2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # create hit counter for each ship

    # list of hit counters
    HCA1 = [0, 0, 0, 0, 0]
    HCA2 = [0, 0, 0, 0, 0]
    # 5,4,3,2,1 (5 = carrier, 4 = battleship, 3 = destroyer, 2 = patrol boat, 1 = submarine)

    # create while loop so game continues until someone wins
    gameover = 0
    while gameover == 0:

        # player 1 picks a point
        print('\nIT IS YOUR TURN PLAYER 1\n\n')
        P1PR = int(input('Pick a row you think one of the opponents ship is on: '))  # player one point row
        while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:  # make sure it is valid point
            P1PR = int(input('Please select an integer between 1-10: '))
            P1PC = int(input('Pick a column you think one of the opponents ship is on: '))  # player one point column
        while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:  # make sure it is valid point
            P1PC = int(input('Please select an integer between 1-10: '))

        # verify that point hasn't been picked yet
        while SB1[P1PR - 1][P1PC - 1] != 0:  # if SB1 is not equal to 0 then point already picked
            print('\nYou have already picked that point\n\n')
            P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt user to pick again
            while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
                P1PR = int(input('Please select an integer between 1-10: '))
            P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
            while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
                P1PC = int(input('Please select an integer between 1-10: '))

        # if player hits a ship
        while PB2[P1PR - 1][P1PC - 1] == 1 or PB2[P1PR - 1][P1PC - 1] == 2 or PB2[P1PR - 1][P1PC - 1] == 3 or PB2[P1PR - 1][P1PC - 1] == 4 or PB2[P1PR - 1][P1PC - 1] == 5:  # If he picks a point and ship is there

            # check which ship it hit
            if PB2[P1PR - 1][P1PC - 1] == 1:  # I set the submarine points to one
                HCA2[4] = HCA2[4] + 1
                if HCA2[4] == 3:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe submarine has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')
            elif PB2[P1PR - 1][P1PC - 1] == 2:  # I set the patrol boat points to two
                HCA2[3] = HCA2[3] + 1
                if HCA2[3] == 2:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe patrol boat has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')
            elif PB2[P1PR - 1][P1PC - 1] == 3:  # I set the destroyer points to three
                HCA2[2] = HCA2[2] + 1
                if HCA2[2] == 3:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe destroyer has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')
            elif PB2[P1PR - 1][P1PC - 1] == 4:  # I set the battleship points to four
                HCA2[1] = HCA2[1] + 1
                if HCA2[1] == 4:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe battleship has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')
            elif PB2[P1PR - 1][P1PC - 1] == 5:  # I set the carrier point to five
                HCA2[0] = HCA2[0] + 1
                if HCA2[0] == 5:  # if every point has been hit, the ship is sunk
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nThe carrier has been sunk!\n\n')
                else:
                    PB2[P1PR - 1][P1PC - 1] = 9  # set the opponent's primary board to 9 to remove the ship
                    SB1[P1PR - 1][P1PC - 1] = 1  # sets player 1's secondary board to show a hit
                    pretty_print_list(SB1)
                    print('\nHIT\n\n')

            # if sum of hit counter list is 17, end the game
            if HCA2[0] + HCA2[1] + HCA2[2] + HCA2[3] + HCA2[4] == 17:
                gameover = 1
                # sound()
                print('\nCongratulations player 1! YOU WON! You now have bragging rights over player 2 for the rest of your life!\n\n')

            # if game is over, stop while loop
            if gameover == 1:
                break

            # prompt to keep choosing until a miss
            P1PR = int(input('Pick a row you think one of the opponents ship is on: '))
            while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
                P1PR = int(input('Please select an integer between 1-10: '))
            P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
            while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
                P1PC = int(input('Please select an integer between 1-10: '))

            # check if point has already been picked
            while SB1[P1PR - 1][P1PC - 1] != 0:  # if secondary point not equal to 0 then point already picked
                print('\nYou have already picked that point\n\n')
                P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt to pick again
                while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
                    P1PR = int(input('Please select an integer between 1-10: '))
                P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
                while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
                    P1PC = int(input('Please select an integer between 1-10: '))

        # if player misses a ship
        if PB2[P1PR - 1][P1PC - 1] == 0:  # if he picks a point and there is no ship

            # check if point has already been picked
            while SB1[P1PR - 1][P1PC - 1] != 0: # if the secondary point doesn't equal 0 then point already picked
                print('\nYou have already picked that point\n\n')
                P1PR = int(input('Pick a row you think one of the opponents ship is on: ')) # prompt to pick again
                while P1PR != 1 and P1PR != 2 and P1PR != 3 and P1PR != 4 and P1PR != 5 and P1PR != 6 and P1PR != 7 and P1PR != 8 and P1PR != 9 and P1PR != 10:
                    P1PR = int(input('Please select an integer between 1-10: '))
                P1PC = int(input('Pick a column you think one of the opponents ship is on: '))
                while P1PC != 1 and P1PC != 2 and P1PC != 3 and P1PC != 4 and P1PC != 5 and P1PC != 6 and P1PC != 7 and P1PC != 8 and P1PC != 9 and P1PC != 10:
                    P1PC = int(input('Please select an integer between 1-10: '))
            SB1[P1PR - 1][P1PC - 1] = -1  # set SB1 to -1 to show miss
            print('\nMISS!\n\n')
            pretty_print_list(SB1)

        # tell player 2 to pick a point
        if gameover == 1:
            break
        print('\nIT IS YOUR TURN PLAYER 2\n\n')
        P2PR = int(input('Pick a row you think one of the opponents ship is on: '))  # player two point row
        while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:  # make sure valid point
            P2PR = int(input('Please select an integer between 1-10: '))
        P2PC = int(input('Pick a column you think one of the opponents ship is on: '))  # player two point column
        while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:  # make sure valid point
            P2PC = int(input('Please select an integer between 1-10: '))

        # check if point already picked
        while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point not equal to 0 then he already picked that point
            print('\nYou have already picked that point\n\n')
            P2PR = int(input('Pick a row you think one of the opponents ship is on: '))  # prompt to pick again
            while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:
                P2PR = int(input('Please select an integer between 1-10: '))
            P2PC = int(input('Pick a column you think one of the opponents ship is on: '))
            while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:
                P2PC = int(input('Please select an integer between 1-10: '))

        # if player 2 hits ship
        while PB1[P2PR - 1][P2PC - 1] == 1 or PB1[P2PR - 1][P2PC - 1] == 2 or PB1[P2PR - 1][P2PC - 1] == 3 or PB1[P2PR - 1][P2PC - 1] == 4 or PB1[P2PR - 1][P2PC - 1] == 5:

            # hit counter and sunk ship
            if PB1[P2PR - 1][P2PC - 1] == 1:
                HCA1[4] = HCA1[4] + 1
                if HCA1[4] == 3:  # if every point has been hit, ship is sunk
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 sunk player 1 submarine \n\n')
                else:
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 got a hit\n\n')
            elif PB1[P2PR - 1][P2PC - 1] == 2:
                HCA1[3] = HCA1[3] + 1
                if HCA1[3] == 2:  # if every point has been hit, ship is sunk
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 sunk player 1 patrol boat\n\n')
                else:
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 got a hit\n\n')
            elif PB1[P2PR - 1][P2PC - 1] == 3:
                HCA1[2] = HCA1[2] + 1
                if HCA1[2] == 3:
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 sunk player 1 destroyer\n\n')
                else:
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 got a hit\n\n')
            elif PB1[P2PR - 1][P2PC - 1] == 4:
                HCA1[1] = HCA1[1] + 1
                if HCA1[1] == 4:
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 sunk player 1 battleship\n\n')
                else:
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 got a hit\n\n')
            elif PB1(P2PR,P2PC)==5:
                HCA1[0] = HCA1[0] + 1
                if HCA1[0] == 5:
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 sunk player 1 carrier\n\n')
                else:
                    PB1[P2PR - 1][P2PC - 1] = 9  # set opponent's primary board to 9 to remove ship
                    SB2[P2PR - 1][P2PC - 1] = 1  # set player 1's secondary board to show hit
                    pretty_print_list(PB1)
                    print('\nPlayer 2 got a hit\n\n')

            # if sum of hit counter list is 17, end the game
            if HCA1[0] + HCA1[1] + HCA1[2] + HCA1[3] + HCA1[4] == 17:
                gameover = 1
                print('\nCongratulations player 2! YOU WON! You now have bragging rights over player 1 for the rest of your life!\n\n')

            # if game is over, stop while loop
            if gameover == 1:
                break

            # prompt to keep choosing until miss
            P2PR = int(input('Pick a row you think one of the opponents ship is on: '))
            while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:
                P2PR = int(input('Please select an integer between 1-10: '))
            P2PC = int(input('Pick a column you think one of the opponents ship is on: '))
            while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:
                P2PC = int(input('Please select an integer between 1-10: '))

            # check if point already picked
            while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point not equal to 0 then already picked point
                print('\nYou have already picked that point\n\n')
                P2PR = int(input('Pick a row you think one of the opponents ship is on: '))  # prompt to pick again
                while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:
                    P2PR = int(input('Please select an integer between 1-10: '))
                P2PC = int(input('Pick a column you think one of the opponents ship is on: '))
                while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:
                    P2PC = int(input('Please select an integer between 1-10: '))

            SB2[P2PR - 1][P2PC - 1] = -1  # set secondary board equal to -1 to show miss
            print('\nMISS!\n\n')
            pretty_print_list(SB2)

        # if player misses ship
        if PB1[P2PR - 1][P2PC - 1] == 0:  # if he picks point and no ship

            # check if point already picked
            while SB2[P2PR - 1][P2PC - 1] != 0:  # if secondary point not equal to 0 then point already picked
                print('\nYou have already picked that point\n\n')
                P2PR = int(input('Pick a row you think one of the opponents ship is on: '))  # prompt to pick again
            while P2PR != 1 and P2PR != 2 and P2PR != 3 and P2PR != 4 and P2PR != 5 and P2PR != 6 and P2PR != 7 and P2PR != 8 and P2PR != 9 and P2PR != 10:
                P2PR = int(input('Please select an integer between 1-10: '))
            P2PC = int(input('Pick a column you think one of the opponents ship is on: '))
            while P2PC != 1 and P2PC != 2 and P2PC != 3 and P2PC != 4 and P2PC != 5 and P2PC != 6 and P2PC != 7 and P2PC != 8 and P2PC != 9 and P2PC != 10:
                P2PC = int(input('Please select an integer between 1-10: '))

            SB2[P2PR - 1][P2PC - 1] = -1  # secondary board 10 -1 to show miss
            print('\nMISS!\n\n')
            pretty_print_list(SB2)


