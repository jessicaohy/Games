# Jessica Oh Hui Yu

import tour

class invalidInput(Exception):
    pass

chessboardList = tour.Tour()    # creating a list (object) representing a chessboard

print(" ############ M E N U ##############")
print("1. Start")
print("2. Position")
print("3. Undo")
print("4. Save")
print("5. Restore")
print("6. Quit")
option = int(input("Enter choice (number): "))

while (option != 6):

    ## start ##
    if (option == 1):
        chessboardList.clear_board()
        chessboardList.create_chessboardList()

        coordinates = input("Enter position for knight to move to (row(0-7)_col(0-7)]): ")
        coordinates = coordinates.split(" ")    # a list of coordinates to place knight [row,col]

        # change to int type
        coordinates[0] = int(coordinates[0])
        coordinates[1] = int(coordinates[1])

        chessboardList.move_knight(coordinates)
        chessboardList.show_tour()

        numOfPossible = chessboardList.check_next_moves()
        chessboardList.display_possibleList(numOfPossible)

    ## position ##
    elif (option == 2):

        try:
            coordinates = input("Enter position for knight to move to (row(1-8)_col(a-h)]): ")
            coordinates = coordinates.split(" ")    # a list of coordinates to place knight [row,col]

            # change to int type
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])

            checkValidity = chessboardList.valid_move(coordinates, numOfPossible)
            if (checkValidity == False):
                raise invalidInput

        except invalidInput:
            print("Invalid input.")

            while checkValidity == False:

                coordinates = input("Enter position for knight to move to (row(1-8)_col(a-h)]) again: ")
                coordinates = coordinates.split(" ")  # a list of coordinates to place knight [row,col]

                 # change to int type
                coordinates[0] = int(coordinates[0])
                coordinates[1] = int(coordinates[1])

                checkValidity = chessboardList.valid_move(coordinates, numOfPossible)

        #if (checkValidity == True):
        chessboardList.move_knight(coordinates)
        chessboardList.show_tour()      # display chessboard

        numOfPossible = chessboardList.check_next_moves()   # find next moves
        chessboardList.next_moves(numOfPossible)            # make sure prev moves not in possible list
        chessboardList.display_possibleList(numOfPossible)  # display possible next moves

    elif (option == 3):
        chessboardList.undo()
        chessboardList.show_tour()

    elif (option == 4):
        chessboardList.copy()

    elif (option == 5):
        chessboardList.set()
        chessboardList.show_tour()



    print(" ############ M E N U ##############")
    print("1. Start")
    print("2. Position")
    print("3. Undo")
    print("4. Save")
    print("5. Restore")
    print("6. Quit")
    option = int(input("Enter choice (number): "))

## quit ##
print("Thank you for playing. See you soon!")










