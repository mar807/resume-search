# Marco Romero

import tkinter
import os

root = tkinter.Tk()

# file dir path for a txt file
TEST_PATH = r"C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch"

# creates the canvas
resumeSearchBox = tkinter.Canvas(root, width = 500, height = 180)
resumeSearchBox.pack()

# fun label
greetingLabel = tkinter.Label(root, text = 'Search your resume!', fg = 'blue')
greetingLabel.config(font = ('helvetica', 14))
resumeSearchBox.create_window(250, 25, window = greetingLabel)

# adding all the lables for input boxes
label1 = tkinter.Label(root, text = 'Employee Type: ')
resumeSearchBox.create_window(50, 80, window = label1)

label2 = tkinter.Label(root, text = 'Keyword: ')
resumeSearchBox.create_window(69, 110, window = label2)

label3 = tkinter.Label(root, text = 'Keyword: ')
resumeSearchBox.create_window(69, 140, window = label3)

# adds all the text input boxes
professionTxt = tkinter.Entry(root)
resumeSearchBox.create_window(160, 80, window = professionTxt)

keyword1Txt = tkinter.Entry(root)
resumeSearchBox.create_window(160, 110, window = keyword1Txt)

keyword2Txt = tkinter.Entry(root)
resumeSearchBox.create_window(160, 140, window = keyword2Txt)

# this function will get the value that was inserted in text box. 
# will change accordingly in the future
def getDirectory(dir):
    proTxt = professionTxt.get()
    
    # ***************

    # saving these for the next function 
    # thought process: if the employee type exists, it will go to another function and search for the keywords
    
    # ***************
    
    # key1Txt = keyword1Txt.get()
    # key2Txt = keyword2Txt.get()

    fileNames = os.listdir(dir)

    # goes through all the files and file paths that exist in the directory
    for fileName in fileNames:
        print ('File Name: ' + fileName)
        print('Folder Path: ' + os.path.abspath(os.path.join(dir, fileName)), sep = '\n')

getDirectory(TEST_PATH)
    #output = tkinter.Label(root, text = proTxt)
    #resumeSearchBox.create_window(400, 170, window = output)

# making a button
button = tkinter.Button(resumeSearchBox, text = 'Here comes the money!', bg = 'green', fg = 'white', command = getDirectory)
resumeSearchBox.create_window(400, 140, window = button)

# starts the program
resumeSearchBox.mainloop()


