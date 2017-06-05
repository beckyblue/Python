'''
Using Python version 2.7
Title: File Mover
Scenario: Your employer wants a program to move all his .txt files from one folder to another
with the click of a click of a button.
On your desktop make 2 new folders.
Call one Folder A & the second Folder B.
Create 4 random .txt files & put them in Folder A.

Plan:
- Move the files from Folder A to Folder B.
- Print out each file path that got moved onto the shell.
- Upon viewing Folder A after the execution, the moved files should not be there.

'''

import shutil
import os



def moveFiles(folder):
    if(folder == "A"):
        source=os.listdir(os.path.abspath("/Users/Student/Desktop/Folder A/"))
        destination = os.path.abspath("/Users/Student/Desktop/Folder B/")
        folder = "/Users/Student/Desktop/Folder A/"
    else:
        source=os.listdir(os.path.abspath("/Users/Student/Desktop/Folder B/"))
        destination = os.path.abspath("/Users/Student/Desktop/Folder A/")
        folder = "/Users/Student/Desktop/Folder B/"

    for files in source:
        print ("Moved file:")
        print (os.path.abspath(folder + files))
        shutil.move(os.path.abspath(folder + files), destination)


def main():
    #See where the files are.
    if(os.listdir("/Users/Student/Desktop/Folder A/")):
        #files are in Folder A
        moveFiles("A")
    else:
        #files are in Folder B
        moveFiles("B")





if __name__ == "__main__": main()
