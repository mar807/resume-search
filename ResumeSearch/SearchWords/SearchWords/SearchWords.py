#Marco Romero

word = input("Enter word you are looking for: ")
FILE = r"C:\Users\mar807\Desktop\resume-search\ResumeSearch\SearchWords\rock.txt"

with open(FILE) as searchFile:
    for line in searchFile:
        if word in line:
            print('true')
        else:
            print('false')