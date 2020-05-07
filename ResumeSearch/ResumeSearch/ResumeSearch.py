# Marco Romero

import tkinter
import os
import sys

root = tkinter.Tk()

# file dir path for a txt file
TEST_PATH = r"C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch\\testfiles"

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
def getDirectory():
    proTxt = professionTxt.get()
    key1Txt = keyword1Txt.get()
    key2Txt = keyword2Txt.get()

    # if profession text is software engineering, it will go to that file directory
    if proTxt == 'Software Engineering':
        path = r"C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch\\Software Engineering"
        # list all of the file names that are in the directory
        fileNames = os.listdir(path)

        # for loop that goes through all files in the directory
        for fileName in fileNames:
            # open the file with every for loop
            with open(os.path.join(fileNames, fileName), 'r') as searchFile:
                # then search all the lines in a file
                for line in searchFile:
                    # if one of the two keywords are in the file, then it will print the file name
                    if key1Txt in line or key2Txt in line:
                        print('File Name: ' + fileNames)
                    # close each file once it is done with it
                    fileName.close()

    elif proTxt == 'Project Manager':
        path = r"C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch\\Project Manager"
        fileNames = os.listdir(path)

        for fileName in fileNames:
            with open(fileName) as searchFile:
                for line in searchFile:
                    if key1Txt in line or key2Txt in line:
                        print('File Name: ' + fileName)

    elif proTxt == 'Database Developer':
        path = r"C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch\\Database Developer"
        fileNames = os.listdir(path)

        for fileName in fileNames:
            with open(fileName) as searchFile:
                for line in searchFile:
                    if key1Txt in line or key2Txt in line:
                        print('File Name: ' + fileName)

    elif proTxt == 'Walmart':
        path = r"C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch\\Walmart"
        fileNames = os.listdir(path)

        for fileName in fileNames:
            with open(fileName) as searchFile:
                for line in searchFile:
                    if key1Txt in line or key2Txt in line:
                        print('File Name: ' + fileName)

    
    #output = tkinter.Label(root, text = proTxt)
    #resumeSearchBox.create_window(400, 170, window = output)

# making a button
button = tkinter.Button(resumeSearchBox, text = 'Here comes the money!', bg = 'green', fg = 'white', command = getDirectory)
resumeSearchBox.create_window(400, 140, window = button)

# starts the program
resumeSearchBox.mainloop()


