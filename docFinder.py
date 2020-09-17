# Create a program that reads from a document and then finds instances of a specified word

# This will be the search function which will search the document
import os

class DocSearch():
    def Menu():
        while True:
            try:
                print("""
                        ===============================
                        |||          MENU OPTIONS\t |||
                        ===============================
                        
                        \t [ S ] earch for filename or path existence
                        \t [ R ] ead from file
                        \t [ C ] opy Document
                        \t [ F ] ind word in file
                        \t [ X ] Exit program

                        """)
                inp = input("Enter a menu option: ")
                if inp.upper() == 'S':
                    print("Enter a filename or file path to verify it's existence\n")
                    print("(( REMINDER )) When using file paths such as 'C:\Program Files'")
                    print(" Remember to use two '\\' backslash characters as one represents an escape character")
                    doc= input("Check to see if file exists, enter filename OR file path: ")
                    if DocReader.PathExists(doc) == True:
                        DocReader.PathExists(doc)
                        
                elif inp.upper() == 'F':
    ##                doc = input("Enter a word to find: ")
                    doc = input("Ener the file name of the file which you want to search: ")
                    FindWords(doc)
                elif inp.upper() == 'R':
                    DocReader.Menu()
                elif inp.upper() == 'C':
                    DocCopy.DocMenu()
                elif inp.upper() == 'X':
                    break
            except FileNotFoundError:
                print("\n================")
                print("ERROR: File Not Found")
                print("================\n")



                
    

        
# This will read the data from a specified file
class DocReader():
    def ReadDoc(file):
        with open(file, mode='r') as f:
            print("=======================================")
            print("Printing file contents: \n")
            for line in f:
                print('\t',line, end=' ')
            input("\n\nPress Enter to return to menu...")
            return

    def PathExists(path):
        print("This path exists: " + str(os.path.exists(path)) + ".")

    def Menu():
        print("Welcome to the DocReader section.\n")
        print("""Select from the following menu options: \n
            ====================================
            ||    [ ls ] List the current contents of the directory          |||
            ||    [ chdir ] Change the current directory                       |||
            ||    [ pwd ] Prints the current working directory             |||
            ||    [ read ] Reads the contents of the file                       |||
            ====================================
                """)
        inp = input("Enter a menu option: ")
        while inp != "":                
            if inp.lower() == 'ls':
                a = os.getcwd()
                b = os.listdir(a)
                for i, line in enumerate(b, start=1):
                    print("\tFILE # " + str(i) + "\t" + "(" + line + ")", end='\n')
                inp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
            elif inp.lower() == 'chdir':
                try:
                    ui = input("Enter the directory path you wish to change to: ")
                    os.chdir(ui)
                    print("The current directory is now: " + os.getcwd())
                    if os.path.exists(ui) == True:
                        inp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
                    elif os.path.exists(ui) == False:
                        inp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
                except OSError:
                    print("Directory not valid")
                    return
            elif inp.lower() == 'pwd':               
                print('\n==================================\n'+'\t'+os.getcwd()+'\n==================================\n')
                inp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
            elif inp.lower() == 'read':
                doc = input("Enter the name of the document you wish to read: ")
                DocReader.ReadDoc(doc)
                return

            


def FindWords(file):
    with open(file, mode='r') as f:
        line = f.readline()
        wList = []
        count = 0
        while line != "":
            wStr = str(line)
##            print(wStr)
            wList += wStr.split()
            wStr = wStr.strip()
##            print(wList)
            line = f.readline()
##            print(wStr)
        uInp = input("Enter options: [S]earch  |||     [E]xit:     ")
        while uInp != "":                
            if uInp.upper() == 'S':                    
                word = input("Enter a word to search for: ")
                ocr = wList.count(word)
                print("There are " + str(ocr) + " instances of the word " + word + ".")
                inp = input("[C]ontinue or [E]xit: ")
                if inp.upper() == 'C':
                    word = input("Enter a word to search for: ")
                    ocr = wList.count(word)
                    print("There are " + str(ocr) + " instances of the word " + word + ".")
                    inp = input("[C]ontinue or [E]xit: ")
                elif inp.upper() == 'E':
                    return
                else:
                    print("INVALID")
                    word = input("Enter a word to search for: ")
                    ocr = wList.count(word)
                    print("There are " + str(ocr) + " instances of the word " + word + ".")
                    inp = input("[C]ontinue or [E]xit: ")
            elif uInp.upper() == 'E':
                return
            uInp = input("\nEnter options: [S]earch  |||     [E]xit:     ")

class DocCopy():
    def DocMenu():
        print("Welcome to the DocCopy section.\n")
        print("""Select from the following menu options: \n
            ====================================
            ||    [ ls ] List the current contents of the directory          |||
            ||    [ chdir ] Change the current directory                       |||
            ||    [ pwd ] Prints the current working directory             |||
            ||    [ copy ] Copy a text file to a new file                         |||
            ====================================
                """)
        uInp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
        while uInp != '':
            a = os.getcwd()
            b = os.listdir(a)
            if uInp.lower() == 'ls':
                a = os.getcwd()
                for i, line in enumerate(b, start=1):
                    print("\tDir # " + str(i) + "\t" + "(" + line + ")", end='\n')
                uInp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
            elif uInp.lower() == 'chdir':
                try:                    
                    ui = input("Enter the directory path you wish to change to: ")
                    os.chdir(ui)
                    print("The current directory is now: " + os.getcwd())
                    if os.path.exists(ui) == True:
                        uInp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
                    elif os.path.exists(ui) == False:
                        uInp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
                except OSError:
                    print("Directory not valid")
                    break
            elif uInp.lower() == 'pwd':               
                print('\n==================================\n'+'\t'+os.getcwd()+'\n==================================\n')
                uInp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")
            elif uInp.lower() == 'copy':
                doc= input("Ener the file name of the file which you want to read: ")
                DocCopy.CopyDoc(doc)
                print("Welcome to the DocCopy section.\n")
                print("""Select from the following menu options: \n
                    ====================================
                    ||    [ ls ] List the current contents of the directory          |||
                    ||    [ chdir ] Change the current directory                       |||
                    ||    [ pwd ] Prints the current working directory             |||
                    ||    [ copy ] Copy a text file to a new file                         |||
                    ====================================
                        """)
                uInp = input("Select from one the following menu options: (''ENTER'' to return to menu)  ")                
                

    def CopyDoc(file):
                        
        file1 = open(file, mode='r')
        inp = input("Enter a name for the new copied file: ")
        file2 = open(inp, mode='w')

        newFile = file1.readline()
        # Writes what is in file1 to file2
        while newFile:
            file2.write(newFile)
            newFile = file1.readline()
        # Prints a True of False whether the file copy was completed    
        print("\nFile copy completed: " + str(os.path.exists(inp)))
        # Will list current directory
        a = os.getcwd()
        print("\nYour file has been stored at " + "\n" + a)
        print("\nFiles in your current dir: " + "[" + a + "]" +"\n")
        
        # Creates list of current directory and enumerates through the list
        b = os.listdir(a)
        for i, line in enumerate(b, start=1):
            print("\tFile # " + str(i) + "\t" + "(" + line + ")", end='\n')
        
        # Closes the files
        file1.close()
        file2.close()
        input("\nPress enter to return to menu...")         


# Main function where program will be executed 
def Main():
    DocSearch.Menu()    
    return

Main()
