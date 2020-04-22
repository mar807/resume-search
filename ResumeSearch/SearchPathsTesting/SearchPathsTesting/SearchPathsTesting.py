# Marco Romero

import os

# folder path to our text test files
TEST_PATH = r'C:\\Users\\mar807\\Desktop\\resume-search\\ResumeSearch\\ResumeSearch\\testFiles'

#function that will display the file names and folder paths 
def pathingDir(dir):

    #listdir function returns a list containing the names of the entries in the directory given by path
    fileNames = os.listdir(dir)
    
    # loop through the all the files and prints the file names and paths
    for fileName in fileNames:
        print('File Name: ' + fileName)

        #prints the paths of the files
        print('Folder Path: ' + os.path.abspath(os.path.join(dir, fileName)), sep = '\n')

# calls the function with the file path as the argument
if __name__ == '__main__':
    pathingDir(TEST_PATH)

