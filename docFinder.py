# Create a program that reads from a document and then finds instances of a specified word

# This will be the search function which will search the document
import os


def Search():
    while True:
        try:
            print("""
                    ===============================
                    |||          MENU OPTIONS\t |||
                    ===============================
                    
                    \t [ S ] earch for filename
                    \t [ R ] ead from file
                    \t [ C ] opy Document
                    \t [ F ] ind word in file
                    \t [ X ] Exit program

                    """)
            inp = input("Enter a menu option: ")
            if inp.upper() == 'S':
                doc= input("Check to see if file exists, enter filename OR file path: ")
##                print(os.path.isfile(str(ReadDoc(doc))))
##                print("\n================")
##                DocReader.ReadDoc(doc)
                if DocReader.FileExists(doc) == True:
                    DocReader.FileExists(doc)
##                FindWords(doc)
            elif inp.upper() == 'F':
##                doc = input("Enter a word to find: ")
                doc = input("Ener the file name of the file which you want to search: ")
                FindWords(doc)
            elif inp.upper() == 'R':
                doc= input("Ener the file name of the file which you want to read: ")
                DocReader.ReadDoc(doc)
            elif inp.upper() == 'C':
                doc= input("Ener the file name of the file which you want to read: ")
                DocCopy.CopyDoc(doc)
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
            for line in f:
                print(line, end=' ')
            return

    def FileExists(file):
        with open(file, mode='r') as f:
            if os.path.exists(file) == True:
                print('\nThis file exists: ' ,os.path.exists(file))
            elif os.path.exists(file) == False:
                 print('\nThis file exists: ' ,os.path.exists(file))
            else:
                print('\nThis file exists: ' ,os.path.exists(file))
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
    def CopyDoc(file):
        file1 = open(file, mode='r')
        inp = input("Enter a name for the new copied file: ")
        file2 = open(inp, mode='w')

        newFile = file1.readline()
        while newFile:
            file2.write(newFile)
            newFile = file1.readline()
        print("\nCopy completed: " + str(os.path.exists(inp)))
        a = os.getcwd()
        print("\nYour file has been stored in " + "\n" + a)
        print("\nWhat is in your current dir: " + str(os.listdir(a)))
        file1.close()
        file2.close()

        
##        files = input("Enter the name of the filename OR file path you wish to copy: ")
##        fName = input("Enter a name for copied file: ")
##        with open(file, mode='r') as file1:
##            files = file1.readline()
##            file2 = open(file, mode='w')
##fun            while files:
##                file2.write(files)
##                files = file1.readline()
##            file1.close()
##            file2.close()

            


# Main function where program will be executed 
def Main():
##    ReadDoc('fun.txt')
##    doc = input("Ener the file name of the file which you want to search: ")
##    ReadDoc(doc)
    Search()
    
    return

Main()
