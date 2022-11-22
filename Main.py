class Main:
    books = []
    titleLength = 0
    authorLength = 0
    publisherLength = 0
    yearLength = 21
    isbnLength = 0
    noLength = 0

    # It opens the file, reads the file, splits the file into a list of books, removes the last item
    # in the list, and then for each book in the list, it creates a dictionary, and then adds the
    # dictionary to the list of books
    def readFile(self):
        openFile = open("lib_books.txt", "r")
        bookList = openFile.read().split("\n\n")
        bookList.pop()
        no = 1

        for book in bookList:
            bookDictionary = {}

            bookDictionary["no"] = str(no)
            bookDictionary["title"] = book.split("\n")[0].split("Title: ")[1]
            bookDictionary["author"] = book.split("\n")[1].split("Author: ")[1]
            bookDictionary["publisher"] = book.split("\n")[2].split("Publisher: ")[1]
            bookDictionary["publication year"] = book.split("\n")[3].split("Publication Year: ")[1]
            bookDictionary["isbn"] = book.split("\n")[4].split("ISBN: ")[1]
            no += 1
            self.books.append(bookDictionary)

    # It finds the length of the longest string in each of the four categories (title, author,
    # publisher, isbn) and stores it in the corresponding variable.
    def findLength(self):
        for book in self.books:
            if(len(book["no"]) > self.noLength): self.noLength = len(book["no"]) + 5
            if(len(book["title"]) > self.titleLength): self.titleLength = len(book["title"]) + 5
            if(len(book["author"]) > self.authorLength): self.authorLength = len(book["author"]) + 5
            if(len(book["publisher"]) > self.publisherLength): self.publisherLength = len(book["publisher"]) + 5
            if(len(book["isbn"]) > self.isbnLength): self.isbnLength = len(book["isbn"]) + 5

    # It reads the file, then asks the user to input a number to choose an action.
    def startProgram(self):
        self.readFile()

        while(True):
            print("\n---------------------------------------------------------------\n")
            print("Actions:\n[1] Display Book Lists\n[2] Add Book\n[3] Terminate Program")
            userChoice = int(input("Choice: "))

            # Checking if the user input is not 1 or 2. If it is not, it will print an error message 
            # and ask the user to input again.
            while(userChoice != 1 and userChoice != 2 and userChoice != 3):
                print("Invalid input! Please try again.")
                print("\n---------------------------------------------------------------\n")
                print("Actions:\n[1] Display Book Lists\n[2] Add Book")
                userChoice = int(input("Choice: "))

            # This is a for loop that iterates through the list of books.
            if(userChoice == 1):
                self.findLength()

                print("\n---------------------------------------------------------------\n")
                print(
                    "No." + ((self.noLength - 3) * " ") + 
                    "Title" + ((self.titleLength - 5) * " ") + 
                    "Author" + ((self.authorLength - 6) * " ") +
                    "Publisher" + ((self.publisherLength - 9) * " ") + 
                    "Publication Year" + ((self.yearLength - 16) * " ") + 
                    "ISBN")
                print((self.titleLength+self.authorLength+self.publisherLength+self.yearLength+self.isbnLength)*"-")

                for book in self.books:
                    print(book["no"], end = (self.noLength - len(book["no"])) * ' ')
                    print(book["title"], end = (self.titleLength - len(book["title"])) * ' ')
                    print(book["author"], end = (self.authorLength - len(book["author"])) * ' ')
                    print(book["publisher"], end = (self.publisherLength - len(book["publisher"])) * ' ')
                    print(book["publication year"], end = (self.yearLength - len(book["publication year"])) * ' ')
                    print(book["isbn"])

            # This is the code that will be executed if the user inputs 2. This code will ask the user
            # to input the book's title, author, publisher, publication year, and ISBN. After that, it
            # will add the book to the list of books.
            if(userChoice == 2):
                book = {}
                outputFile = open("lib_books.txt", "a")

                print("\n---------------------------------------------------------------\n")

                # Book Title
                book["no"] = str(len(self.books) + 1)
                book["title"] = input("Title: ")
                book["author"] = input("Author: ")
                book["publisher"] = input("Publisher: ")
                book["publication year"] = input("Publication Year: ")
                book["isbn"] = input("ISBN: ")

                outputFile.write("Title: " + book["title"]+"\n")
                outputFile.write("Author: " + book["author"]+"\n")
                outputFile.write("Publisher: " + book["publisher"]+"\n")
                outputFile.write("Publication Year: " + book["publication year"]+"\n")
                outputFile.write("ISBN: " + book["isbn"]+"\n\n")

                self.books.append(book)

                print("\n---------------------------------------------------------------\n")

                # Adding the book to the list of books.
                print("Book was added successfully!")

                outputFile.close()

            if(userChoice == 3): break

        print("\n---------------------------------------------------------------\n")
        print("Program ended!")

# Creating an instance of the Main class and then calling the startProgram method.
main = Main()
main.startProgram()