# Marco Romero

#just installed PyPDF2 library so I can read through pdf files.
# TODO: make if statements to handle doc files and pdf files. im assuming that if i keep the code the way it is, 
# i'll run into problems because it's going to start dealing with pdf and doc files.


import tkinter
import os
import sys
import docx
import PyPDF2

root = tkinter.Tk()

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

# making a dropdown list
OCCUPATIONS = [
    'Software Engineer', 
    'Database Developer', 
    'Project Manager'
    ]

clicked = tkinter.StringVar()
clicked.set(OCCUPATIONS[0]) 

choices = tkinter.OptionMenu(root, clicked, *OCCUPATIONS)
# figure a way to make it not change when changing the window size
choices.place(x = 95, y = 65)

label2 = tkinter.Label(root, text = 'Keyword: ')
resumeSearchBox.create_window(69, 110, window = label2)

label3 = tkinter.Label(root, text = 'Keyword: ')
resumeSearchBox.create_window(69, 140, window = label3)

keyword1Txt = tkinter.Entry(root)
resumeSearchBox.create_window(160, 110, window = keyword1Txt)

keyword2Txt = tkinter.Entry(root)
resumeSearchBox.create_window(160, 140, window = keyword2Txt)

# this function will get the value that was inserted in text box. 
# will change accordingly in the future
def getDirectory():
    proTxt = clicked.get()
    key1Txt = keyword1Txt.get()
    key2Txt = keyword2Txt.get()

    # if profession text is software engineering, it will go to that file directory
    if proTxt == 'Software Engineer':
        
        # changes the directory we are looking at
        os.chdir("/Users/mar807/Desktop/resume-search/ResumeSearch/ResumeSearch/Software Engineering")

        path = r"C:\Users\mar807\Desktop\resume-search\ResumeSearch\ResumeSearch\Software Engineering"
        
        readFiles poo
        # list all of the file names that are in the directory
        fileNames = os.listdir(path)

        # for loop that goes through all files in the directory
        for fileName in fileNames:
            # open the file with every for loop
            #with open(os.path.join(path, fileName), encoding = "Latin-1") as searchFile:

            document = docx.Document(fileName)

            # empty array that will append words on a document
            texts = []
            
            count = 0

            # then search all the lines in a file
            for line in document.paragraphs:
                # append each word or paragraph (look this up)
                 texts.append(line.text)

                # if a word matches with one of the keywords, then print out the file name
                 if key1Txt in '\n'.join(texts) or key2Txt in '\n'.join(texts):
                    print(fileName)
                    count += 1
                    # stops the for loop
                    break

            if count == 0:
                print('nothing in file: ' + fileName)
               
                # if it doesnt then print cant find or something
                #document.close()

    ################################################################### 
    #
    # I will not be commenting out what each line does since it is 
    # identical to the block of code up above
    #
    ###################################################################

    elif proTxt == 'Project Manager':

        os.chdir("/Users/mar807/Desktop/resume-search/ResumeSearch/ResumeSearch/Project Manager")

        path = r"C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch\\Project Manager"

        fileNames = os.listdir(path)

        for fileName in fileNames:
            document = docx.Document(fileName)
            
            texts = []
            
            for line in document.paragraphs:
                texts.append(line.text)

                if key1Txt in '\n'.join(texts) or key2Txt in '\n'.join(texts):
                    print(fileName)

    elif proTxt == 'Database Developer':

        os.chdir("/Users/mar807/Desktop/resume-search/ResumeSearch/ResumeSearch/Project Manager")

        path = r"C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch\\Database Developer"
        
        fileNames = os.listdir(path)

        for fileName in fileNames:
            documet = docx.Document(fileName)
            texts = []
            for line in document.paragraphs:
                texts.append(line.text)

                if key1Txt in '\n'.join(texts) or key2Txt in '\n'.join*(texts):
                    print(fileName)

    
    #output = tkinter.Label(root, text = proTxt)
    #resumeSearchBox.create_window(400, 170, window = output)

# making a button
button = tkinter.Button(resumeSearchBox, text = 'Here comes the money!', bg = 'green', fg = 'white', command = getDirectory)
resumeSearchBox.create_window(400, 140, window = button)

# starts the program
resumeSearchBox.mainloop()


