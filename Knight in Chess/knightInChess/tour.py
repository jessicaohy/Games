import unsorted_list_ADT

class Tour:

    def __init__(self):
        # creating rows
        self.boardList = unsorted_list_ADT.List(8)  # creating an empty list of size [length, the_array]
        self.possibleList = unsorted_list_ADT.List(8)
        self.pastList = unsorted_list_ADT.List(64)

        self.saveBoardList = unsorted_list_ADT.List(8)
        self.savePastList = unsorted_list_ADT.List(64)


    def create_chessboardList(self):
        """
        This function creates a chessboard list with the numbers in each position, according to the column number.
        :param:
        :return:
        :complexity: O(N)

        :return:
        """
        # creating columns
        singleList = unsorted_list_ADT.List(8)
        unsorted_list_ADT.add_last(singleList, "0")
        unsorted_list_ADT.add_last(singleList, "1")
        unsorted_list_ADT.add_last(singleList, "2")
        unsorted_list_ADT.add_last(singleList, "3")
        unsorted_list_ADT.add_last(singleList, "4")
        unsorted_list_ADT.add_last(singleList, "5")
        unsorted_list_ADT.add_last(singleList, "6")
        unsorted_list_ADT.add_last(singleList, "7")

        # creating a multidimensional array
        for i in range(8):                          # creating 8 lists in the array
            unsorted_list_ADT.add_last(self.boardList, singleList)


    def clear_board(self):
        """
        This function clears the chessboard.
        :param:
        :return:
        :complexity: O(1)
        """

        # reset column
        unsorted_list_ADT.reset(self.boardList)

        self.boardList = unsorted_list_ADT.List(8)


    def move_knight(self, coordinatesList): #############################################################
        """
        This function moves the knight to the position input by the user.
        Current location of the knight is marked with K.
        Past locations of the knight is marked with *.
        :param: coordinatesList
        :return:
        :complexity: O(N^2)
        """

        #numOfRows = unsorted_list_ADT.length(self.boardList)
        numOfRows = 8

        # copying self.boardList into pastBoardList
        pastBoardList = unsorted_list_ADT.List(8)
        for rowCount in range(numOfRows):
            copyRow = unsorted_list_ADT.get_item(self.boardList, rowCount)
            unsorted_list_ADT.add_last(pastBoardList, copyRow)



        ########### UPDATING K TO * #################
        for rowK in range(numOfRows):           # check every row for K
            checkRowList = unsorted_list_ADT.get_item(self.boardList, rowK)

            colK = unsorted_list_ADT.index(checkRowList, 'K')

            # FOUND K
            if (colK != None):

                updateRowList = unsorted_list_ADT.List(8)

                # update column
                c = 0
                while c < unsorted_list_ADT.length(checkRowList):
                    if (c == colK):
                        unsorted_list_ADT.add_last(updateRowList, '*')
                    else:
                        addPastItem = unsorted_list_ADT.get_item(checkRowList, c)
                        unsorted_list_ADT.add_last(updateRowList, addPastItem)
                    c+=1

                # update row
                unsorted_list_ADT.reset(self.boardList)

                r = 0
                while r < numOfRows:

                    pastRowList = unsorted_list_ADT.get_item(pastBoardList, r)

                    if (r == rowK ):
                        unsorted_list_ADT.add_last(self.boardList, updateRowList)
                    else:
                        unsorted_list_ADT.add_last(self.boardList, pastRowList)
                    r += 1
                # saving row and column of previous K
                onePastList = unsorted_list_ADT.List(2)
                unsorted_list_ADT.add_last(onePastList, rowK)
                unsorted_list_ADT.add_last(onePastList, colK)
                unsorted_list_ADT.add_last(self.pastList, onePastList)

        # print(self.boardList)

        ######### CREATING CURRENT POSITION FOR K #################

        # copying self.boardList into pastBoardList
        pastBoardList = unsorted_list_ADT.List(8)
        for rowCount in range(numOfRows):
            copyRow = unsorted_list_ADT.get_item(self.boardList, rowCount)
            unsorted_list_ADT.add_last(pastBoardList, copyRow)

        # reading in user's position choice
        rowNum = coordinatesList[0]       # number
        colNum = coordinatesList[1]
        #colLetter = coordinatesList[1]    # letter

        rowList = unsorted_list_ADT.get_item(self.boardList, rowNum)

        #colNum = unsorted_list_ADT.index(rowList, colLetter)  # finding column position

        # updating column for rowList
        newList = unsorted_list_ADT.List(8)

        c = 0
        while c < unsorted_list_ADT.length(rowList):

            if (c == colNum):
                unsorted_list_ADT.add_last(newList, 'K')
            else:  
                addPastItem = unsorted_list_ADT.get_item(rowList, c)
                unsorted_list_ADT.add_last(newList, addPastItem)

            c+=1

        # updating row for boardList
        unsorted_list_ADT.reset(self.boardList)

        r = 0
        while r < numOfRows:

            pastRowList = unsorted_list_ADT.get_item(pastBoardList, r)

            if (r == rowNum):
                unsorted_list_ADT.add_last(self.boardList, newList)
            else:
                unsorted_list_ADT.add_last(self.boardList, pastRowList)
            r += 1
####################################################################################################

    def show_tour(self):
        """
        This function prints the chessboard.
        :param:
        :return:
        :complexity: Best Case: O(1). Worse Case: O(N^2)
        """
        # printPretty
        for row in range(unsorted_list_ADT.length(self.boardList)):
            rList = unsorted_list_ADT.get_item(self.boardList, row)
            for col in range(unsorted_list_ADT.length(rList)):
                print(unsorted_list_ADT.get_item(rList, col), end=" ")
            #print(rowList)
            print()



    def check_next_moves(self):
        """
        This function checks the next possible positions without removing the previously visited positions.
        :param:
        :return: countPosition
        :complexity: O(N^2)
        """
        unsorted_list_ADT.reset(self.possibleList)
        numOfRows = 8

        # check through every row to find K
        for checkRow in range(numOfRows):           # check every row for K
            checkRowList = unsorted_list_ADT.get_item(self.boardList, checkRow)

            colK = unsorted_list_ADT.index(checkRowList, 'K')

            # FOUND K
            if (colK != None):
                rowK = checkRow
                break

        #print("rowK: ", rowK, "colK: ", colK)

        singlePossibleList = unsorted_list_ADT.List(2)

        unsorted_list_ADT.add_last(singlePossibleList, "row")
        unsorted_list_ADT.add_last(singlePossibleList, "col")

        for i in range(8):
            unsorted_list_ADT.add_last(self.possibleList, singlePossibleList)


        onePossibleList = unsorted_list_ADT.List(2)
        countPosition = -1

        # CHECK RIGHT RIGHT, UP/DOWN
        if (colK + 2 <= 7):     # move right

            possibleCol = colK + 2


            if (rowK - 1 >= 0):  # move up
                possibleRow = rowK - 1
                countPosition += 1

                # copying self.possibleList into copyPossiblelist
                copyPossibleList = unsorted_list_ADT.List(8)
                # print("copyPoss1: ", self.possibleList)
                for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
                    copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
                    unsorted_list_ADT.add_last(copyPossibleList, copyRow)

                onePossibleList = unsorted_list_ADT.List(2)

                unsorted_list_ADT.add_last(onePossibleList, possibleRow)
                unsorted_list_ADT.add_last(onePossibleList, possibleCol)

                unsorted_list_ADT.reset(self.possibleList)
                r = 0
                while r < unsorted_list_ADT.length(copyPossibleList):

                    pastPossibleList = unsorted_list_ADT.get_item(copyPossibleList, r)

                    if (r == countPosition):
                        unsorted_list_ADT.add_last(self.possibleList, onePossibleList)

                    else:

                        unsorted_list_ADT.add_last(self.possibleList, pastPossibleList)

                    r += 1


                #print("right right up", self.possibleList)

            if (rowK + 1 <= 7):     # move down
                possibleRow = rowK + 1
                countPosition += 1


                # copying self.possibleList into copyPossiblelist
                copyPossibleList = unsorted_list_ADT.List(8)

                for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
                    copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
                    unsorted_list_ADT.add_last(copyPossibleList, copyRow)

                onePossibleList = unsorted_list_ADT.List(2)

                unsorted_list_ADT.add_last(onePossibleList, possibleRow)
                unsorted_list_ADT.add_last(onePossibleList, possibleCol)

                unsorted_list_ADT.reset(self.possibleList)

                r = 0
                while r < unsorted_list_ADT.length(copyPossibleList):

                    pastPossibleList = unsorted_list_ADT.get_item(copyPossibleList, r)

                    if (r == countPosition):
                        unsorted_list_ADT.add_last(self.possibleList, onePossibleList)

                    else:

                        unsorted_list_ADT.add_last(self.possibleList, pastPossibleList)

                    r += 1


                #print("left left down", self.possibleList)

        # CHECK LEFT LEFT, UP/DOWN
        if (colK - 2 >= 0):  # move right
            possibleCol = colK - 2

            if (rowK - 1 >= 0):  # move up
                possibleRow = rowK - 1
                countPosition += 1

                # copying self.possibleList into copyPossiblelist
                copyPossibleList = unsorted_list_ADT.List(8)

                for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
                    copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
                    unsorted_list_ADT.add_last(copyPossibleList, copyRow)
                #print("copyPossibleList creationg: ", copyPossibleList)

                onePossibleList = unsorted_list_ADT.List(2)

                unsorted_list_ADT.add_last(onePossibleList, possibleRow)
                unsorted_list_ADT.add_last(onePossibleList, possibleCol)

                unsorted_list_ADT.reset(self.possibleList)

                #print("copyPossibleList aft: ", copyPossibleList)
                r = 0
                while r < unsorted_list_ADT.length(copyPossibleList):

                    pastPossibleList = unsorted_list_ADT.get_item(copyPossibleList, r)

                    if (r == countPosition):
                        unsorted_list_ADT.add_last(self.possibleList, onePossibleList)

                    else:

                        unsorted_list_ADT.add_last(self.possibleList, pastPossibleList)

                    r += 1

                #print("left left up", self.possibleList)

            if (rowK + 1 <= 7):  # move down
                possibleRow = rowK + 1
                countPosition += 1

                # copying self.possibleList into copyPossiblelist
                copyPossibleList = unsorted_list_ADT.List(8)

                for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
                    copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
                    unsorted_list_ADT.add_last(copyPossibleList, copyRow)

                onePossibleList = unsorted_list_ADT.List(2)

                unsorted_list_ADT.add_last(onePossibleList, possibleRow)
                unsorted_list_ADT.add_last(onePossibleList, possibleCol)

                unsorted_list_ADT.reset(self.possibleList)

                r = 0
                while r < unsorted_list_ADT.length(copyPossibleList):

                    pastPossibleList = unsorted_list_ADT.get_item(copyPossibleList, r)

                    if (r == countPosition):
                        unsorted_list_ADT.add_last(self.possibleList, onePossibleList)

                    else:

                        unsorted_list_ADT.add_last(self.possibleList, pastPossibleList)

                    r += 1

                #print("right right down", self.possibleList)

        # CHECK UP UP, RIGHT/LEFT
        if (rowK - 2 >= 0):
            possibleRow = rowK - 2

            if (colK + 1 <= 7):
                possibleCol = colK + 1
                countPosition += 1

                # copying self.possibleList into copyPossiblelist
                copyPossibleList = unsorted_list_ADT.List(8)

                for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
                    copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
                    unsorted_list_ADT.add_last(copyPossibleList, copyRow)

                onePossibleList = unsorted_list_ADT.List(2)

                unsorted_list_ADT.add_last(onePossibleList, possibleRow)
                unsorted_list_ADT.add_last(onePossibleList, possibleCol)

                unsorted_list_ADT.reset(self.possibleList)

                r = 0
                while r < unsorted_list_ADT.length(copyPossibleList):

                    pastPossibleList = unsorted_list_ADT.get_item(copyPossibleList, r)

                    if (r == countPosition):
                        unsorted_list_ADT.add_last(self.possibleList, onePossibleList)

                    else:

                        unsorted_list_ADT.add_last(self.possibleList, pastPossibleList)

                    r += 1

                #print("up up right", self.possibleList)

            if (colK - 1 >= 0):
                possibleCol = colK - 1
                countPosition += 1

                # copying self.possibleList into copyPossiblelist
                copyPossibleList = unsorted_list_ADT.List(8)

                for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
                    copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
                    unsorted_list_ADT.add_last(copyPossibleList, copyRow)

                onePossibleList = unsorted_list_ADT.List(2)

                unsorted_list_ADT.add_last(onePossibleList, possibleRow)
                unsorted_list_ADT.add_last(onePossibleList, possibleCol)

                unsorted_list_ADT.reset(self.possibleList)

                r = 0
                while r < unsorted_list_ADT.length(copyPossibleList):

                    pastPossibleList = unsorted_list_ADT.get_item(copyPossibleList, r)

                    if (r == countPosition):
                        unsorted_list_ADT.add_last(self.possibleList, onePossibleList)

                    else:

                        unsorted_list_ADT.add_last(self.possibleList, pastPossibleList)

                    r += 1

                #print("up up left", self.possibleList)

        # CHECK DOWN DOWN, RIGHT/LEFT
        if (rowK + 2 <= 7):
            possibleRow = rowK + 2

            if (colK + 1 <= 7):
                possibleCol = colK + 1
                countPosition += 1
                # copying self.possibleList into copyPossiblelist
                copyPossibleList = unsorted_list_ADT.List(8)

                for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
                    copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
                    unsorted_list_ADT.add_last(copyPossibleList, copyRow)

                onePossibleList = unsorted_list_ADT.List(2)

                unsorted_list_ADT.add_last(onePossibleList, possibleRow)
                unsorted_list_ADT.add_last(onePossibleList, possibleCol)

                unsorted_list_ADT.reset(self.possibleList)

                r = 0
                while r < unsorted_list_ADT.length(copyPossibleList):

                    pastPossibleList = unsorted_list_ADT.get_item(copyPossibleList, r)

                    if (r == countPosition):
                        unsorted_list_ADT.add_last(self.possibleList, onePossibleList)

                    else:

                        unsorted_list_ADT.add_last(self.possibleList, pastPossibleList)

                    r += 1

                #print("down down right", self.possibleList)
            if (colK - 1 >= 0):
                possibleCol = colK - 1
                countPosition += 1

                # copying self.possibleList into copyPossiblelist
                copyPossibleList = unsorted_list_ADT.List(8)

                for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
                    copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
                    unsorted_list_ADT.add_last(copyPossibleList, copyRow)

                onePossibleList = unsorted_list_ADT.List(2)

                unsorted_list_ADT.add_last(onePossibleList, possibleRow)
                unsorted_list_ADT.add_last(onePossibleList, possibleCol)
                unsorted_list_ADT.reset(self.possibleList)

                r = 0
                while r < unsorted_list_ADT.length(copyPossibleList):

                    pastPossibleList = unsorted_list_ADT.get_item(copyPossibleList, r)

                    if (r == countPosition):
                        unsorted_list_ADT.add_last(self.possibleList, onePossibleList)

                    else:

                        unsorted_list_ADT.add_last(self.possibleList, pastPossibleList)

                    r += 1
                #print("down down left", self.possibleList)
        return countPosition

    def display_possibleList(self, countPosition):
        """
        This function prints the next possible positions.
        :param countPosition
        :return:
        :complexity: Best Case: O(1). Worse Case: O(N^2)
        """
         # printPretty
        print("\nNext Possible Positions:")
        for row in range(unsorted_list_ADT.length(self.possibleList)):

            if (row <= countPosition):
                rList = unsorted_list_ADT.get_item(self.possibleList, row)
                for col in range(unsorted_list_ADT.length(rList)):
                    print(unsorted_list_ADT.get_item(rList, col), end=" ")
                print()

        #print("PossibleList", self.possibleList)

    def next_moves(self, countPosition):
        """
        This function checks the next possible positions with the previously visited positions removed.
        :param countPosition
        :return:
        :complexity: O(N^2)
        """

        Tour.check_next_moves(self)
        #print("PossibleList", self.possibleList)

        # create a copy
        copyPossibleList = unsorted_list_ADT.List(8)
        for rowCount in range(unsorted_list_ADT.length(self.possibleList)):
            copyRow = unsorted_list_ADT.get_item(self.possibleList, rowCount)
            unsorted_list_ADT.add_last(copyPossibleList, copyRow)

        # for every possible next position
        for count in range(countPosition):

            # get the row and col of next possible position
            checkOnePossibleList = unsorted_list_ADT.get_item(copyPossibleList, count)
            nextPossibleRow = unsorted_list_ADT.get_item(checkOnePossibleList, 0)
            nextPossibleCol = unsorted_list_ADT.get_item(checkOnePossibleList, 1)

            #print("checkOnePossibleList: ", checkOnePossibleList)

            # check board list every row for *
            for rowAst in range(unsorted_list_ADT.length(self.boardList)):

                checkRowList = unsorted_list_ADT.get_item(self.boardList, rowAst)

                colAst = unsorted_list_ADT.index(checkRowList, '*')

                # FOUND *
                if (colAst != None):


                    if (rowAst == nextPossibleRow and colAst == nextPossibleCol):
                        unsorted_list_ADT.delete_item(self.possibleList, checkOnePossibleList)

                        #print(checkOnePossibleList)
                        #print("Final aft deleted list: ", self.possibleList)
                        break
        #print("Final possible list: ", self.possibleList)


    def valid_move(self, coordinatesList, countPosition):
        """
        This function check if user input for next position is valid.
        :param coordinatesList, self.poassibleList
        :return: True, False
        :complexity: Best Case: O(1). Worse Case: O(N).
        """

        # reading in user's position choice
        rowNum = coordinatesList[0]       # number
        colNum = coordinatesList[1]
        #colLetter = coordinatesList[1]    # letter

        if (rowNum==0 or rowNum==1 or rowNum==2 or rowNum==3 or rowNum==4 or rowNum==5 or rowNum==6 or rowNum==7):

            if (colNum == 0 or colNum == 1 or colNum == 2 or colNum == 3 or colNum == 4 or colNum == 5 or colNum == 6 or colNum == 7):

                Tour.next_moves(self, countPosition)
                # get a final list of next possible positions

                for countPossible in range(unsorted_list_ADT.length(self.possibleList)):

                    oneValidList = unsorted_list_ADT.get_item(self.possibleList, countPossible)

                    validRow = unsorted_list_ADT.get_item(oneValidList, 0)
                    validCol = unsorted_list_ADT.get_item(oneValidList, 1)

                    if (rowNum == validRow and colNum == validCol):
                        return True

                return False

            return False
        return False

    def undo(self):
        """
        This function undo the most recent position on the chessboard.
        :param:
        :return:
        :complexity: O(N^2)
        """
        if (unsorted_list_ADT.is_empty(self.pastList) == True):
            return False

        else:
            print("self.pastList: ", self.pastList)

            lastPosition = unsorted_list_ADT.length(self.pastList) - 1
            pastCoordinatesList = unsorted_list_ADT.get_item(self.pastList, lastPosition)


            # numOfRows = unsorted_list_ADT.length(self.boardList)
            numOfRows = 8

            # copying self.boardList into pastBoardList
            pastBoardList = unsorted_list_ADT.List(8)
            for rowCount in range(numOfRows):
                copyRow = unsorted_list_ADT.get_item(self.boardList, rowCount)
                unsorted_list_ADT.add_last(pastBoardList, copyRow)

            ########### UPDATING K TO * #################
            for rowK in range(numOfRows):  # check every row for K
                checkRowList = unsorted_list_ADT.get_item(self.boardList, rowK)

                colK = unsorted_list_ADT.index(checkRowList, 'K')

                # FOUND K
                if (colK != None):

                    updateRowList = unsorted_list_ADT.List(8)

                    # update column
                    c = 0
                    while c < unsorted_list_ADT.length(checkRowList):
                        if (c == colK):
                            unsorted_list_ADT.add_last(updateRowList, c)
                        else:
                            addPastItem = unsorted_list_ADT.get_item(checkRowList, c)
                            unsorted_list_ADT.add_last(updateRowList, addPastItem)
                        c += 1

                    # update row
                    unsorted_list_ADT.reset(self.boardList)

                    r = 0
                    while r < numOfRows:

                        pastRowList = unsorted_list_ADT.get_item(pastBoardList, r)

                        if (r == rowK):
                            unsorted_list_ADT.add_last(self.boardList, updateRowList)
                        else:
                            unsorted_list_ADT.add_last(self.boardList, pastRowList)
                        r += 1
            ######### CREATING CURRENT POSITION FOR K #################

            # copying self.boardList into pastBoardList
            pastBoardList = unsorted_list_ADT.List(8)
            for rowCount in range(numOfRows):
                copyRow = unsorted_list_ADT.get_item(self.boardList, rowCount)
                unsorted_list_ADT.add_last(pastBoardList, copyRow)

            # reading in user's position choice
            rowNum = unsorted_list_ADT.get_item(pastCoordinatesList, 0)
            colNum = unsorted_list_ADT.get_item(pastCoordinatesList, 1)
            # colLetter = coordinatesList[1]    # letter

            rowList = unsorted_list_ADT.get_item(self.boardList, rowNum)

            # colNum = unsorted_list_ADT.index(rowList, colLetter)  # finding column position

            # updating column for rowList
            newList = unsorted_list_ADT.List(8)

            c = 0
            while c < unsorted_list_ADT.length(rowList):

                if (c == colNum):
                    unsorted_list_ADT.add_last(newList, 'K')
                else:
                    addPastItem = unsorted_list_ADT.get_item(rowList, c)
                    unsorted_list_ADT.add_last(newList, addPastItem)

                c += 1

            # updating row for boardList
            unsorted_list_ADT.reset(self.boardList)

            r = 0
            while r < numOfRows:

                pastRowList = unsorted_list_ADT.get_item(pastBoardList, r)

                if (r == rowNum):
                            unsorted_list_ADT.add_last(self.boardList, newList)
                else:
                    unsorted_list_ADT.add_last(self.boardList, pastRowList)
                r += 1



            unsorted_list_ADT.delete_item(self.pastList, pastCoordinatesList)

            #print("self.pastList: ", self.pastList)


    def copy(self):
        """
        This function saves the current board list.
        :param:
        :return:
        :complexity: O(N^2)
        """
        # copying self.boardList into pastBoardList
        self.saveBoardList = unsorted_list_ADT.List(8)
        for rowCount in range(8):
            copyRow = unsorted_list_ADT.get_item(self.boardList, rowCount)
            unsorted_list_ADT.add_last(self.saveBoardList, copyRow)

        # copying self.pastList into savePastList
        self.savePastList = unsorted_list_ADT.List(64)
        for rowCount in range(unsorted_list_ADT.length(self.pastList)):
            copyRow = unsorted_list_ADT.get_item(self.pastList, rowCount)
            unsorted_list_ADT.add_last(self.savePastList, copyRow)

        # display
        print("Saved List: ")
        for row in range(unsorted_list_ADT.length(self.saveBoardList)):
            rList = unsorted_list_ADT.get_item(self.saveBoardList, row)
            for col in range(unsorted_list_ADT.length(rList)):
                print(unsorted_list_ADT.get_item(rList, col), end=" ")
            #print(rowList)
            print()

    def set(self):
        """
        This function restores the most recent saved board list.
        :param:
        :return:
        :complexity: O(N)
        """
        # copying self.boardList into pastBoardList
        #self.saveList = unsorted_list_ADT.List(8)
        self.boardList = unsorted_list_ADT.List(8)
        for rowCount in range(8):
            copyRow = unsorted_list_ADT.get_item(self.saveBoardList, rowCount)
            unsorted_list_ADT.add_last(self.boardList, copyRow)

        # copying self.pastList into savePastList
        self.pastList = unsorted_list_ADT.List(64)
        for rowCount in range(unsorted_list_ADT.length(self.savePastList)):
            copyRow = unsorted_list_ADT.get_item(self.savePastList, rowCount)
            unsorted_list_ADT.add_last(self.pastList, copyRow)






