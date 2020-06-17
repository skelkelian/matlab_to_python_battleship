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