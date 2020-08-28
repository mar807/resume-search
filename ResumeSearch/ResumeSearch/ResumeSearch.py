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
    # only getting the profession we are looking for so we know which directory to go to
    proTxt = clicked.get()

    # if profession text is software engineering, it will go to that file directory
    if proTxt == 'Software Engineer':
        
        # changes the directory we are looking at
        os.chdir("/Users/mar807/Desktop/resume-search/ResumeSearch/ResumeSearch/Software Engineering")

        path = r"C:\Users\mar807\Desktop\resume-search\ResumeSearch\ResumeSearch\Software Engineering"
        
        # go to another function that search through every file in the directory
        searchFiles(path)

    elif proTxt == 'Project Manager':
        os.chdir("/Users/mar807/Desktop/resume-search/ResumeSearch/ResumeSearch/Project Manager")
        path = r"C:\Users\mar807\Desktop\resume-search\ResumeSearch\ResumeSearch\Project Manager"

        searchFiles(path)

    elif proTxt == 'Database Developer':
        os.chdir("/Users/mar807/Desktop/resume-search/ResumeSearch/ResumeSearch/Database Developer")
        path = r"C:\Users\mar807\Desktop\resume-search\ResumeSearch\ResumeSearch\Database Developer"

        searchFiles(path)

def searchFiles(path):
    # getting the keywords that was typed in the application
    key1Txt = keyword1Txt.get()
    key2Txt = keyword2Txt.get()

    #list all of the file names that are in the directory
    fileNames = os.listdir(path)
        
    # for loop that goes through all files in the directory
    for fileName in fileNames:
        
        # if the file is a word doc, then it would do all of this
        if fileName.endswith('.docx'):
            #open the file with every loop
            document = docx.Document(fileName)
        
            # empty array that will append words on a document
            texts = []
            count = 0

            # then search all the lines in the file
            for line in document.paragraphs:
                #append each word or paragpraph 
                texts.append(line.text)
            
                # if a word matches with one of the keywords, then print out the file name
                if key1Txt in '\n'.join(texts) or key2Txt in '\n'.join(texts):
                        print(fileName)
                        break

        elif fileName.endswith('.pdf'):
            # creating pdf object
            pdf = PyPDF2.PdfFileReader(fileName)

            # open the file
            with open(fileName, 'rb') as f:

                # for loop depending on how many pages there is on the pdf file
                for pageNum in range(pdf.numPages):
                    # page numbers of pdf
                    pageObj = pdf.getPage(pageNum)

                    # keeps track of the text in the pdf file
                    text = pageObj.extractText()

                    # if the keyword is in the file, then it will print the file
                    if key1Txt in text or key2Txt in text:
                        print(fileName)
                        break

# making a button
button = tkinter.Button(resumeSearchBox, text = 'Here comes the money!', bg = 'green', fg = 'white', command = getDirectory)
resumeSearchBox.create_window(400, 140, window = button)

# starts the program
resumeSearchBox.mainloop()


