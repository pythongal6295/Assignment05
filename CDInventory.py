#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#Kkauffman, 2020-Aug-09, Added code to some TODOs
#KKauffman, 2020-Aug-10, Added reading file functionality
#KKauffman, 2020-Aug-11, Improved formatting, improved menu choice 'l' and 'd'
#KKauffman, 2020-Aug-12, Improved menu choice 'd', added header for .txt file
#------------------------------------------#


# -- DATA -- #

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = {}  # dict of data row 
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PRESENTATION --#

#Using this path library to write a header for the .txt file
from os import path

#Create heading for the file
cd_header = 'ID,CD Title,Artist Name'

#Open file and save heading
if not path.exists(strFileName):
    objFile = open(strFileName, 'w')
    objFile.write(cd_header + '\n')
    objFile.close()

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break

    if strChoice == 'l':
        #Display the data from the external .txt file
        objFile = open(strFileName, 'r')
        lines = objFile.readlines()
        k = ''
        for item in lines:
            k = str(item).strip('\n') #Take out '\n' from when it was saved
            print(k, sep= ',') #Separate items with a comma
        objFile.close()
        pass

# -- PROCESSING -- #

    elif strChoice == 'a':  
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = {'ID':intID, 'Title':strTitle, 'Artist':strArtist}
        lstTbl.append(lstRow)
        print('\nYour data has been added to the CD inventory.')
        
# -- PRESENTATION -- #
        
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep= ', ')
            
    elif strChoice == 'd':
    # Deleting an entry the user inputted during the current run of the program
        print('Row Number, ID, CD Title, Artist')
        row_num = 0 #Defining a variable to add a row number to each row in the list
        for row in lstTbl:
            row_num += 1 #Increasing the row number each time the for loop runs
            print(row_num, *row.values(), sep= ', ')
    #Asking the user to provide the row number and then deleting it
        i = int(input('Enter the row number of the entry you wish to delete. '))
        i = i - 1
        lstTbl.pop(i)
        print('\nYour entry has been deleted.')
        pass

# -- PROCESSING -- #

    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('\nYour data has been saved.')

# -- Presentation -- #
        
    else:
        print('Please choose either l, a, i, d, s or x!')

