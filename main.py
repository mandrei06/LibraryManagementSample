# I need to import random for generate a random unique id for each registred book
import random
# I need to import tkinter in order to create the GUI and to use widgets like Frame,Entry,Label,Button,etc
import tkinter as tk
# I need to import partial in order to call a function with parameters from the inside of a Tkinter Button,
# using command tag (command accept only function without parameters)
from functools import partial

# I generate a list of unique numbers using random.sample
randomID = random.sample(range(100, 999), 899)


# BOOKS
class Books():
    # class constructor in order to create a "Books" object
    def __init__(self, title, author, year, publisher, copies, pub_date):
        global randomID  # refer to the randomID defined on line 10
        self.ID = random.choice(randomID)  # chose a random ID from the list
        randomID.remove(self.ID)  # remove that ID from the list to not be able to use again
        self.title = title  # object title=the parameter title that I sent in constructor function
        self.author = author
        self.year = year
        self.publisher = publisher
        self.copies = copies
        self.pub_date = pub_date

    # different methods to set only a certain value
    def setTitle(self, value):
        self.title = value

    def setAuthor(self, value):
        self.author = value

    def setYear(self, value):
        self.year = value

    def setPublisher(self, value):
        self.publisher = value

    def setCopies(self, value):
        self.copies = value

    def setPubDate(self, value):
        self.pub_date = value

    def getTitle(self):
        return self.title

    # different methods in order to get a certain value
    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getPublisher(self):
        return self.publisher

    def getCopies(self):
        return self.copies

    def getPubDate(self):
        return self.pub_date

    def getId(self):
        return self.ID


# id_list is a list that will return the id of the books with a certain criteria
id_list = []
# bookList is a dictionary that will store each book in my library
bookList = {}
# totalBooks is a variable that will store the number of total books, including copies
totalBooks = 0


class BookList(Books):

    def store(self, title, author, year, publisher, copies, pub_date):
        # in order to store a book in my dictionary, I choose to consider the book id the key,
        # and the rest of attributes, the key value
        # also, to find the book id I use getId method from Books class that will return the book id
        ID = Books.getId(self)
        bookList[ID] = [title, author, year, publisher, copies, pub_date]
        # I also print the information regarding the number of books in my library:
        BookList.printNumberInfo(copies)

    # prinNumberInfo is a method I used to display the number of books in my library:
    def printNumberInfo(copies):
        # refer to totalBooks global variable
        # I made that variable global because I want to refer to it everytime I add a book
        # I don't want to have a new variable for each book, because I will lose the count
        global totalBooks
        # I use StringVar in order to be able to display my variables because
        # textvariable attribute accept just tk.var and not String var
        totalBooks1 = tk.StringVar(root, value="total unique books:" + str(BookList.count(copies)))
        totalBooks2 = tk.StringVar(root, value="total copies books:" + str(totalBooks))
        # warningLabell is a warning label that informs about the number of unique/different books in library
        warningLabell = tk.Label(my_frameS, textvariable=totalBooks1, bg="yellow",
                                 fg="black",
                                 font=(None, 13), width=30,
                                 relief="groove")
        # place function help me to choose where on my screen to place the label
        warningLabell.place(x=600, y=630)
        # after function help me to destroy my label after a certain period of time
        warningLabell.after(3000, lambda: warningLabell.destroy())

        # warningLabell2 will display the number of total books, including copies
        # this label text will be the tk.StringVar from totalBooks2, bg which stands for background
        # will be yellow, fg (foreground) will be black, I choose a font of 13, the width of label of 30 pixels
        # I also use relief for a 3d effect
        warningLabell2 = tk.Label(my_frameS, textvariable=totalBooks2, bg="yellow",
                                  fg="black",
                                  font=(None, 13), width=30,
                                  relief="groove")
        warningLabell2.place(x=600, y=660)
        warningLabell2.after(3000, lambda: warningLabell2.destroy())

    # I create method search in order to search for a book with certain information
    def search(selection, option):
        # first of all, I clear my id_list in case of any previous search, to not return the id's from previous searches
        id_list.clear()
        # I check if the criteria of search is Title/Author/Publisher and I retain an integer that also represent the
        # position of my option in the list of book atributes
        if (option == 'Title'):
            option = 0
        elif (option == 'Author'):
            option = 1
        elif (option == "Publisher"):
            option = 3
        else:
            option = 5
        for ID in bookList:
            # search for the books that mark my criteria and save their ID in a list that will be returned by my function
            if (bookList[ID][option] == selection):
                id_list.append(ID)
        return id_list

    # editBook method will edit the book details
    def editBook(ID):
        # with get function I get the content of my Entry widgets, which contains the new information of a books
        title = titleEntry.get()
        author = authorEntry.get()
        year = yearEntry.get()
        publisher = publisherEntry.get()
        copies = copiesEntry.get()
        pubdate = pubdateEntry.get()
        # first of all, I check if the user complete every field
        if (title == "" or author == "" or year == "" or copies == "" or pubdate == ""):
            # in case that any field is not completed, the screen will display an error message on the screen
            warningLabell = tk.Label(my_frameS, text="Please fill all of the fields!", bg="red", fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
            warningLabell.after(6000, lambda: warningLabell.destroy())

        else:
            # in case that every field contain information, then I check for copies field to be a number using isdigit function
            # in this way it will help me when I want to count the books to not catch any errors
            if copies.isdigit():
                # if copies is a number I display a message like "Congratulation, the book was updated"
                warningLabell = tk.Label(my_frameS, text="Congratulation, the book was updated!", bg="yellow",
                                         fg="black",
                                         font=(None, 13), borderwidth=3,
                                         relief="groove")
                warningLabell.place(x=600, y=600)
                warningLabell.after(3000, lambda: warningLabell.destroy())
                # I also update my book in my dictionary
                # I convert ID to int because when I add my ID from my list it is a string
                bookList[int(ID)] = [title, author, year, publisher, copies, pubdate]




            else:
                # In case the number of copies is not a number I will prompt a message on the screen, waiting for the
                # user to insert a number
                warningLabell = tk.Label(my_frameS, text="The number of copies should be an integer!", bg="red",
                                         fg="black",
                                         font=(None, 13), borderwidth=3,
                                         relief="groove")
                warningLabell.place(x=600, y=600)

    # deleteBookF will delete a book; the method take as parameter the ID of the book that will be deleted
    def deleteBookF(ID):
        # we will need to modify totalBooks variable, because of deleting, the number will be changed
        global totalBooks
        try:
            # I use a try and except statement in case the user hit multiple time delete button
            # in this way, he will be notify that the book was deleted, or that he already delete the book
            totalBooks -= int(bookList[int(ID)][4])
            # del statement will delete from the dictionary the book with corespondent id
            # ID is a string so it need to be converted to int
            del bookList[int(ID)]
            # I also add GUI elements that will be displayed when the process is finished
            # The way I create this labels are the same as the previous one
            warningLabell = tk.Label(my_frameS, text="The book was deleted!", bg="yellow",
                                     fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
            warningLabell.after(3000, lambda: warningLabell.destroy())
        except:
            warningLabell = tk.Label(my_frameS, text="You already delete that book!", bg="yellow",
                                     fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
            warningLabell.after(3000, lambda: warningLabell.destroy())

    # count method take 1 parameter which represent the number of copies to add at totalBooks variable
    # also this methot return the current length of the bookList, using the len statement
    def count(copies):
        global totalBooks
        totalBooks += int(copies)
        return len(bookList)


# mainScreen is the first screen that is display on GUI
# this screen contain a welcome message and a button which open the application functionalities
def mainScreen():
    # Root will be the main screen on which I will add my widgets
    global root
    root = tk.Tk()
    # size of root screen in pixels
    root.geometry("1000x700")
    # background of root screen
    root['bg'] = 'green'
    global my_frame
    # I create a frame in my screen which will contain my label and button
    # I specify the width and the height of my frame, also the background
    my_frame = tk.Frame(root, width=1000, height=700)
    my_frame['bg'] = 'green'
    # with pack function I display the frame to the users
    # fill − Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal dimensions
    my_frame.pack(fill="both", expand=True)
    # Welcome Label
    greeting = tk.Label(my_frame, text="Welcome to Andy's library", bg="black", fg="white", font=(None, 30))
    greeting.place(x=250, y=100)

    # Buttons to start the app
    # This button trigger the loadS command, which will load the screen containing the option
    staffBtn = tk.Button(my_frame, text="Enter", bg="black", fg="white", width=20, height=2, font=(None, 10),
                         command=loadS)
    staffBtn.place(x=385, y=250)
    # root. mainloop() is a method on the main window which we execute when we want to run our application.
    # This method will loop forever, waiting for events from the user, until the user exits the program
    root.mainloop()


# goBack function will always go back to the main screen, destroying the current root
def goBack():
    root.destroy()

    mainScreen()


# bookSubmit function will submit a new book, creating an object with the book attributes, and also store the book
def bookSubmit():
    # like I explain at modify book, the get function will get the value of tk entries and will be passed to dictionary
    title = titleEntry.get()
    author = authorEntry.get()
    year = yearEntry.get()
    publisher = publisherEntry.get()
    copies = copiesEntry.get()
    pubdate = pubdateEntry.get()
    # check if all the fields are filled in and also display messages depends on the input using warning labels
    if (title == "" or author == "" or year == "" or copies == "" or pubdate == ""):
        warningLabell = tk.Label(my_frameS, text="Please fill all of the fields!", bg="red", fg="black",
                                 font=(None, 13), borderwidth=3,
                                 relief="groove")
        warningLabell.place(x=600, y=600)
    else:
        # check if copies variable represent a number, in order to keep the track of the number of books
        if copies.isdigit():

            warningLabell = tk.Label(my_frameS, text="Congratulation, the book was added!       ", bg="yellow",
                                     fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
            warningLabell.after(3000, lambda: warningLabell.destroy())

            # I create an BookList that inherit Books, so I need to use Books constructor
            book = BookList(title, author, year, publisher, copies, pubdate)
            # I also add my book to the dictionary
            book.store(title, author, year, publisher, copies, pubdate)

        else:
            warningLabell = tk.Label(my_frameS, text="The number of copies should be an integer!", bg="red",
                                     fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)


# ButtonsCommands (GUI component)
def addABookF():
    # I create a new frame that will contain all the fields that are needed to be completed in order to add a book
    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)

    titleLabel = tk.Label(loadFrame, text="Title:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                          relief="groove")

    # I set my variable global to be able to access them from submitBook function
    global titleEntry
    titleEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    titleEntry.place(x=170, y=20)
    titleLabel.place(x=20, y=20)

    authorLabel = tk.Label(loadFrame, text="Author:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                           relief="groove")
    global authorEntry
    authorEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    authorEntry.place(x=170, y=70)
    authorLabel.place(x=20, y=70)

    yearLabel = tk.Label(loadFrame, text="Year:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                         relief="groove")
    global yearEntry
    yearEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    yearEntry.place(x=170, y=120)
    yearLabel.place(x=20, y=120)

    publisherLabel = tk.Label(loadFrame, text="Publisher:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                              relief="groove")
    global publisherEntry
    publisherEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    publisherEntry.place(x=170, y=170)
    publisherLabel.place(x=20, y=170)

    copiesLabel = tk.Label(loadFrame, text="Number of copies:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                           relief="groove")
    global copiesEntry
    copiesEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    copiesEntry.place(x=170, y=220)
    copiesLabel.place(x=20, y=220)

    pubdateLabel = tk.Label(loadFrame, text="Publication date:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                            relief="groove")
    global pubdateEntry
    pubdateEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    pubdateEntry.place(x=170, y=270)
    pubdateLabel.place(x=20, y=270)

    # submitBook button will trigger the bookSubmit command that will get the field information and register the new book
    submitBook = tk.Button(loadFrame, text="Add a book", bg="black", fg="white", width=10, height=2, font=(None, 10),
                           command=bookSubmit)
    submitBook.place(x=175, y=350)


# updateABookF function will be the function that will help us to modify a book details
# this action is separated in four screen
# the first screen is the screen that allow us to choose by which attributes will search our book
def updateABookF():
    # I create a frame that will contain my OptionMenu widget
    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)

    ###label
    chooseLabel = tk.Label(loadFrame, text="Select the criterion by which you want to search for the book:", bg="black",
                           fg="white", font=(None, 12), borderwidth=3,
                           relief="groove")
    chooseLabel.place(x=20, y=10)

    # OptionList will be the possible choices of my OptionMenu
    OptionList = [
        "Title",
        "Author",
        "Publisher",
        "Publication date"
    ]
    variable = tk.StringVar(loadFrame)
    variable.set("Click here to select")

    # I need a callback function because I want to execute the function after I make my choice, and also
    # I want to be able to change my mind
    def callback(selection):
        global action_with_arg
        # I use partial in order to be able to call a function with a parameter
        action_with_arg = partial(updateABookF2, selection)
        # selectBtn will trigger the command described in action_with_arg, that is updateABookF2 and pass selection argument
        # I will need to retain "selection" variable in order to find this certain book attribute
        selectBtn = tk.Button(loadFrame, text="Submit", bg="black", fg="white", width=10, height=2, font=(None, 10),
                              command=action_with_arg)
        selectBtn.place(x=175, y=170)

    # my OptionMenu that contain my variable for the text that I want to display as default value ("Click here to select")
    opt = tk.OptionMenu(loadFrame, variable, *OptionList, command=callback)
    opt.config(width=30, font=('Helvetica', 12))
    opt.place(x=80, y=80)


# The second frame that my update function contain is created in updateABookF2 function
# This frame will contain a textbox/entry where the user should input the value corresponding to the selected attribute
def updateABookF2(option):
    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)

    chooseLabel = tk.Label(loadFrame, text="Please insert the " + option + " of the book that you are looking for",
                           bg="black",
                           fg="white", font=(None, 11), borderwidth=3,
                           relief="groove")
    chooseLabel.place(x=5, y=10)

    global searchEntry
    searchEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    searchEntry.place(x=140, y=70)

    # searchF function will search for the book with the selected attribute and its corresponding value
    def searchF():
        selection = searchEntry.get()
        # I check if the entry is empty or not, and display a message in case the value is empty
        if (selection == ""):
            warningLabell = tk.Label(my_frameS, text="Please enter a word to search for!", bg="red", fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
        else:
            # if the value is not empty, I go to the next screen, passing my arguments
            updateABookF3(selection, option)

    # submitBook button will trigger the searchF function
    submitBook = tk.Button(loadFrame, text="Search", bg="black", fg="white", width=10, height=2, font=(None, 10),
                           command=searchF)
    submitBook.place(x=175, y=150)


# updateABookF3 will display a new frame with a menu list, with all the results of books that match the criteria
# par example: if a user choose author, and tape in previous screen, the name of the author
# there can be multiple books from the same author, so I choose to use a menu list, in order to select the wanted book
def updateABookF3(selection, option):
    # I search for the books that match the criteria using the BookList method "search" that will return a list of books id
    findList = BookList.search(selection, option)

    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)

    if (not findList):
        # If our list is empty, that means we didn't find any books matching the criteria
        warningLabell = tk.Label(loadFrame,
                                 text="Sorry, we couldn't find the book you are searching for \n, please try again carefully!",
                                 bg="red", fg="black",
                                 font=(None, 13), borderwidth=3,
                                 relief="groove")
        warningLabell.place(x=15, y=60)
    else:
        # if we find at least one book, we create a OptionList for our OptionMenu
        OptionList = []
        for item in findList:
            # add in our bookList the ID as well because we will need it in order to update the book
            bookList[item].append(str(item))

            # we put our bookList in the optionList
            OptionList.append(bookList[item])
            variable = tk.StringVar(loadFrame)
            variable.set("Click here to select")

            # I need a callback function because I want to execute the function after I make my choice, and also
            # I want to be able to change my mind in case I want to choose something else
            def callback(selection):
                global action_with_arg
                # selectBtn will trigger the command described in action_with_arg, that is updateABookF4 and pass selection argument
                # I will need to retain "selection" variable in order to find this certain book attribute
                action_with_arg = partial(updateABookF4, selection)
                selectBtn = tk.Button(loadFrame, text="Submit", bg="black", fg="white", width=10, height=2,
                                      font=(None, 10),
                                      command=action_with_arg)
                selectBtn.place(x=175, y=170)

            # my OptionMenu that contain my variable for the text that I want to display as default value ("Click here to select")

            opt = tk.OptionMenu(loadFrame, variable, *OptionList, command=callback)
            opt.config(width=30, font=('Helvetica', 12))
            opt.place(x=80, y=80)


# Finally, updateABookF4 will represent the last frame that will display the book attributes with the
# possibility to change them, is the same form as in addABookF function, but the only difference is that
# this form fields will be automatically completed with the actual value of the attributes
def updateABookF4(selection):
    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)

    titleLabel = tk.Label(loadFrame, text="Title:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                          relief="groove")
    global titleEntry
    titleVariable = tk.StringVar(root, value=selection[0])
    titleEntry = tk.Entry(loadFrame, textvariable=titleVariable, font=(None, 13), borderwidth=3, relief="groove")
    titleEntry.place(x=170, y=20)
    titleLabel.place(x=20, y=20)

    authorLabel = tk.Label(loadFrame, text="Author:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                           relief="groove")
    global authorEntry
    authorVariable = tk.StringVar(root, value=selection[1])
    authorEntry = tk.Entry(loadFrame, textvariable=authorVariable, font=(None, 13), borderwidth=3, relief="groove")
    authorEntry.place(x=170, y=70)
    authorLabel.place(x=20, y=70)

    yearLabel = tk.Label(loadFrame, text="Year:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                         relief="groove")
    global yearEntry
    yearVariable = tk.StringVar(root, value=selection[2])
    yearEntry = tk.Entry(loadFrame, textvariable=yearVariable, font=(None, 13), borderwidth=3, relief="groove")

    yearEntry.place(x=170, y=120)
    yearLabel.place(x=20, y=120)

    publisherLabel = tk.Label(loadFrame, text="Publisher:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                              relief="groove")
    global publisherEntry
    publisherVariable = tk.StringVar(root, value=selection[3])
    publisherEntry = tk.Entry(loadFrame, textvariable=publisherVariable, font=(None, 13), borderwidth=3,
                              relief="groove")
    publisherEntry.place(x=170, y=170)
    publisherLabel.place(x=20, y=170)

    copiesLabel = tk.Label(loadFrame, text="Number of copies:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                           relief="groove")
    global copiesEntry
    copiesVariable = tk.StringVar(root, value=selection[4])
    copiesEntry = tk.Entry(loadFrame, textvariable=copiesVariable, font=(None, 13), borderwidth=3, relief="groove")
    copiesEntry.place(x=170, y=220)
    copiesLabel.place(x=20, y=220)

    pubdateLabel = tk.Label(loadFrame, text="Publication date:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                            relief="groove")
    global pubdateEntry
    pubdateVariable = tk.StringVar(root, value=selection[5])
    pubdateEntry = tk.Entry(loadFrame, textvariable=pubdateVariable, font=(None, 13), borderwidth=3, relief="groove")
    pubdateEntry.place(x=170, y=270)
    pubdateLabel.place(x=20, y=270)
    editBookAction = partial(BookList.editBook, selection[6])

    # down on the frame, there are two option for update the book by saving the changes or to delete the book
    # in that way, submitBook button will trigger the editBookAction command which I wrote it above and which
    # trigger the method editBook from BookList class and also pass the ID as parameter (selection[6])
    # and the deleteBook button work in the same way but this time will be trigger deleteBookF method
    # from BookList class which I also wrote it above
    submitBook = tk.Button(loadFrame, text="Save the changes", bg="black", fg="white", width=20, height=2,
                           font=(None, 10),
                           command=editBookAction)
    submitBook.place(x=175, y=310)
    deleteBookAction = partial(BookList.deleteBookF, selection[6])
    deleteBook = tk.Button(loadFrame, text="Delete this book", bg="black", fg="white", width=20, height=2,
                           font=(None, 10),
                           command=deleteBookAction)
    deleteBook.place(x=175, y=370)


# addAUserF function is mostly used to create the GUI used for adding a new user
def addAUserF():
    # loadFrame will be the main frame where I will load my register form
    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)
    # I add label and entry text box for each user attribute
    usernameLabel = tk.Label(loadFrame, text="Username:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                             relief="groove")
    global usernameEntry
    usernameEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    usernameEntry.place(x=170, y=20)
    usernameLabel.place(x=20, y=20)

    firstnameLabel = tk.Label(loadFrame, text="First Name:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                              relief="groove")
    global firstnameEntry
    firstnameEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    firstnameEntry.place(x=170, y=70)
    firstnameLabel.place(x=20, y=70)

    surnameLabel = tk.Label(loadFrame, text="Second Name:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                            relief="groove")
    global surnameEntry
    surnameEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    surnameEntry.place(x=170, y=120)
    surnameLabel.place(x=20, y=120)

    houseNrLabel = tk.Label(loadFrame, text="House number:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                            relief="groove")
    global houseNrEntry
    houseNrEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    houseNrEntry.place(x=170, y=170)
    houseNrLabel.place(x=20, y=170)

    streetnameLabel = tk.Label(loadFrame, text="Street Name:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                               relief="groove")
    global streetEntry
    streetEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    streetEntry.place(x=170, y=220)
    streetnameLabel.place(x=20, y=220)

    postcodeLabel = tk.Label(loadFrame, text="Postcode:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                             relief="groove")
    global postcodeEntry
    postcodeEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    postcodeEntry.place(x=170, y=270)
    postcodeLabel.place(x=20, y=270)

    emailLabel = tk.Label(loadFrame, text="Email:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                          relief="groove")
    global emailEntry
    emailEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    emailEntry.place(x=170, y=320)
    emailLabel.place(x=20, y=320)

    birthdayLabel = tk.Label(loadFrame, text="Birthday:", bg="black", fg="white", font=(None, 13), borderwidth=3,
                             relief="groove")
    global birthdayEntry
    birthdayEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    birthdayEntry.place(x=170, y=370)
    birthdayLabel.place(x=20, y=370)

    # submitBook will trigger userSubmit function
    submitBook = tk.Button(loadFrame, text="Add a user", bg="black", fg="white", width=10, height=2, font=(None, 10),
                           command=userSubmit)
    submitBook.place(x=175, y=400)
    # I also call printUserNumberInfo function to display the current number of users
    printUserNumberInfo()


# printUserNumberInfo is a function that display a notification about the number of users
# this will be a label placed in the bottom of screen
def printUserNumberInfo():
    # In order to find the number of users I call the method userNumber from UserList class
    totalUsers = tk.StringVar(root, value="total users:" + str(UserList.userNumber(UserList)))
    warningLabell = tk.Label(my_frameS, textvariable=totalUsers, bg="yellow",
                             fg="black",
                             font=(None, 13), width=30,
                             relief="groove")
    warningLabell.place(x=600, y=630)
    # this notify will be destroyed after 3000 miliseconds
    warningLabell.after(3000, lambda: warningLabell.destroy())


# I create updateAUserF function in order to delete a user
def updateAUserF():
    # I call printUserNumberInfo function to display the current number of users
    printUserNumberInfo()
    # I create a frame where I will load my widgets
    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)
    # info label
    chooseLabel = tk.Label(loadFrame, text="Please insert the user first name ",
                           bg="black",
                           fg="white", font=(None, 11), borderwidth=3,
                           relief="groove")
    chooseLabel.place(x=5, y=10)

    # textbox for search for first name of the user we want to delete

    global searchNEntry
    searchNEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    searchNEntry.place(x=140, y=70)

    def searchF():
        selection = searchNEntry.get()
        # check for empty entry
        if (selection == ""):
            warningLabell = tk.Label(my_frameS, text="Please enter the first name!", bg="red", fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
        else:
            # if the entry is not empty, we call deleteUser method from UserList class and pass the selection parameter
            # which represent the firstname of the user that we want to delete
            UserList.deleteUser(UserList, selection)

    # submitUser button will trigger the searchF command
    submitUser = tk.Button(loadFrame, text="Search and delete", bg="black", fg="white", width=30, height=2,
                           font=(None, 10),
                           command=searchF)

    submitUser.place(x=105, y=150)


# userDetail function is used to display user details
def userDetail():
    # I create a new frame where I will display all the user information
    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)
    # I call printUserNumberInfo function to display the current number of users
    printUserNumberInfo()
    loadFrame = tk.Frame(my_frameS, width=450, height=450)
    loadFrame['bg'] = 'black'
    loadFrame.place(x=350, y=100)
    # chooseLabel is a info label
    chooseLabel = tk.Label(loadFrame, text="Please insert the username ",
                           bg="black",
                           fg="white", font=(None, 11), borderwidth=3,
                           relief="groove")
    chooseLabel.place(x=5, y=10)

    # textbox entry to insert the username of the user that we want to search for
    global searchNEntry
    searchNEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
    searchNEntry.place(x=140, y=70)

    def searchF():
        selection = searchNEntry.get()
        # check for empty entry
        if (selection == ""):
            warningLabell = tk.Label(my_frameS, text="Please enter the username!", bg="red", fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
        else:
            # if the entry is not empty, we call userDetail method from UserList class and pass the selection parameter
            # which represent the username of the user that we want to search
            UserList.userDetail(UserList, selection)

    # submitUser button will trigger the searchF command
    submitBook = tk.Button(loadFrame, text="Search and delete", bg="black", fg="white", width=10, height=2,
                           font=(None, 10),
                           command=searchF)
    submitBook.place(x=175, y=150)


# loadS function will load the screen with the menu of functionality, also in this screen
# I will display multiple frames depends of the user choice
def loadS():
    # before to load the new screen, I have to destroy the old one
    my_frame.destroy()
    global my_frameS
    my_frameS = tk.Frame(root, width=1000, height=700)
    my_frameS['bg'] = 'green'
    my_frameS.pack(fill="both", expand=True)
    greeting = tk.Label(my_frameS, text="Welcome to the Portal", bg="black", fg="white", font=(None, 30))
    greeting.place(x=250, y=20)
    # menuFrame
    global menuFrame
    menuFrame = tk.Frame(my_frameS, width=200, height=450)
    menuFrame['bg'] = 'black'
    menuFrame.place(x=50, y=100)
    # buttons with commands that I described above, each button will open a frame where the content will be load
    addABook = tk.Button(menuFrame, text="Add a book", bg="black", fg="white", width=20, height=2, font=(None, 10),
                         command=addABookF)
    updateABook = tk.Button(menuFrame, text="Update a book", bg="black", fg="white", width=20, height=2,
                            font=(None, 10), command=updateABookF)
    addAUser = tk.Button(menuFrame, text="Add a user", bg="black", fg="white", width=20, height=2, font=(None, 10),
                         command=addAUserF)
    updateAUser = tk.Button(menuFrame, text="Delete a user", bg="black", fg="white", width=20, height=2,
                            font=(None, 10), command=updateAUserF)
    displayUserDetails = tk.Button(menuFrame, text="Display user details", bg="black", fg="white", width=20, height=2,
                                   font=(None, 10), command=userDetail)
    # also I add a back button which let us go back to the mainScreen
    back = tk.Button(menuFrame, text="Go back", bg="black", fg="white", width=20, height=2, font=(None, 10),
                     command=goBack)

    addABook.place(x=18, y=10)
    updateABook.place(x=18, y=50)
    addAUser.place(x=18, y=90)
    updateAUser.place(x=18, y=130)
    displayUserDetails.place(x=18, y=170)
    back.place(x=18, y=400)


# Users class in order to create Users object with the required attributes
class Users():
    # constructor for Users class
    def __init__(self, username, firstname, surname, houseNr, streetName, postcode, email, birthday):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.houseNr = houseNr
        self.streetName = streetName
        self.postcode = postcode
        self.email = email
        self.birthday = birthday

    # setters  for required attributes
    def setFirstname(self, value):
        self.firstname = value

    def setSurname(self, value):
        self.surname = value

    def setEmail(self, value):
        self.email = value

    def setBirthday(self, value):
        self.birthday = value

    # functions to get different attributes :
    def getUsername(self):
        return self.username

    def getFirstname(self):
        return self.firstname

    def getSurname(self):
        return self.surname

    def getHousenr(self):
        return self.houseNr

    def getStreetname(self):
        return self.streetName

    def getPostcode(self):
        return self.postcode

    def getEmail(self):
        return self.email

    def getBirthday(self):
        return self.birthday


# userList is an empty dictionary that will store each user details
userList = {}


# class UserList that inherit class Users
# being a child of Users class, will have access to parent methods(Users methods) like getEmail,getBirthday,etc
class UserList(Users):
    # store() method is used to store the user information in the userList dictionary
    # this method use methods from the parent class to get the necessary information
    def store(self):
        username = Users.getUsername(self)
        firstname = Users.getFirstname(self)
        surname = Users.getSurname(self)
        houseNr = Users.getHousenr(self)
        streetName = Users.getStreetname(self)
        postcode = Users.getPostcode(self)
        email = Users.getEmail(self)
        birthday = Users.getBirthday(self)
        # the key of the user will be the username of the user, because it will be unique
        userList[username] = [firstname, surname, houseNr, streetName, postcode, email, birthday]

    # deleteUser method is used to delete users
    # this method take one parameter that represent the firstname of the user
    def deleteUser(self, firstname):
        count = 0
        # count all the users with this firstname
        for key in userList:
            if userList[key][0] == firstname:
                count += 1
        if (count == 0):
            # in case there is no user with this first name, I display a label that let the user know that

            warningLabell = tk.Label(my_frameS,
                                     text="There no users with this name!",
                                     bg="red", fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
            warningLabell.after(3000, lambda: warningLabell.destroy())
        elif (count != 1):
            # in case there are more users with same firstname, I will create a form
            # and ask for username, which is 100% unique
            warningLabell = tk.Label(my_frameS,
                                     text="There are more users with this first name, please enter your username!",
                                     bg="red", fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
            warningLabell.after(2000, lambda: warningLabell.destroy())
            # in that way, I put a frame over my previous one, where will be the label and the entry box for the username
            loadFrame = tk.Frame(my_frameS, width=450, height=450)
            loadFrame['bg'] = 'black'
            loadFrame.place(x=350, y=100)
            ###label
            chooseLabel = tk.Label(loadFrame, text="Please insert the username ",
                                   bg="black",
                                   fg="white", font=(None, 11), borderwidth=3,
                                   relief="groove")
            chooseLabel.place(x=5, y=10)

            # textbox

            global searchNEntry
            searchNEntry = tk.Entry(loadFrame, font=(None, 13), borderwidth=3, relief="groove")
            searchNEntry.place(x=140, y=70)

            def searchF():
                selection = searchNEntry.get()
                if (selection == ""):
                    # check if the selection is empty

                    warningLabell = tk.Label(my_frameS, text="Please enter the username !", bg="red", fg="black",
                                             font=(None, 13), borderwidth=3,
                                             relief="groove")
                    warningLabell.place(x=600, y=600)
                else:
                    # if the selection is not empty we try to delete the username
                    try:
                        del userList[selection]
                        loadFrame.destroy()
                        printUserNumberInfo()
                    except:
                        # if the username doesn't exist we prompt a message and let the user know that
                        warningLabell = tk.Label(my_frameS,
                                                 text="There are no users with this username!",
                                                 bg="red", fg="black",
                                                 font=(None, 13), borderwidth=3,
                                                 relief="groove")
                        warningLabell.place(x=600, y=600)
                        warningLabell.after(4000, lambda: warningLabell.destroy())

            # after the user fill the entry and click on submit, the searchF function will be trigger
            submitBook = tk.Button(loadFrame, text="Search and delete", bg="black", fg="white", width=30, height=2,
                                   font=(None, 10),
                                   command=searchF)
            submitBook.place(x=105, y=150)

        else:
            # In case we find exactly one user with the entered firstname then we look to find this user username
            # and after we delete the user
            for key in userList:
                if userList[key][0] == firstname:
                    del userList[key]
                    warningLabell = tk.Label(my_frameS,
                                             text="The user was deleted!",
                                             bg="yellow", fg="black",
                                             font=(None, 13), borderwidth=3,
                                             relief="groove")
                    warningLabell.place(x=600, y=600)
                    warningLabell.after(3000, lambda: warningLabell.destroy())
                    break

    # userNumber function will return the length of the userList dictionary, namely the number of users
    def userNumber(self):
        return len(userList)

    # userDetail function will prompt to the GUI multiple labels containing user details
    def userDetail(self, username):
        loadFrame = tk.Frame(my_frameS, width=450, height=450)
        loadFrame['bg'] = 'black'
        loadFrame.place(x=350, y=100)

        username1 = tk.StringVar(root, value="Username: " + str(username))
        usernameLabel = tk.Label(loadFrame, textvariable=username1, bg="black", fg="white", font=(None, 13),
                                 borderwidth=3,
                                 relief="groove")
        usernameLabel.place(x=20, y=20)

        try:
            firstname = tk.StringVar(root, value="First name: " + str(userList[username][0]))
            firstnameLabel = tk.Label(loadFrame, textvariable=firstname, bg="black", fg="white", font=(None, 13),
                                      borderwidth=3,
                                      relief="groove")
            firstnameLabel.place(x=20, y=70)

            surname = tk.StringVar(root, value="Second name: " + str(userList[username][1]))
            surnameLabel = tk.Label(loadFrame, textvariable=surname, bg="black", fg="white", font=(None, 13),
                                    borderwidth=3,
                                    relief="groove")
            surnameLabel.place(x=20, y=120)

            houseNr = tk.StringVar(root, value="House number: " + str(userList[username][2]))
            houseNrLabel = tk.Label(loadFrame, textvariable=houseNr, bg="black", fg="white", font=(None, 13),
                                    borderwidth=3,
                                    relief="groove")
            houseNrLabel.place(x=20, y=170)

            streetName = tk.StringVar(root, value="Street name: " + str(userList[username][3]))
            streetNameLabel = tk.Label(loadFrame, textvariable=streetName, bg="black", fg="white", font=(None, 13),
                                       borderwidth=3,
                                       relief="groove")
            streetNameLabel.place(x=20, y=220)

            postcode = tk.StringVar(root, value="Postcode: " + str(userList[username][4]))
            postcodeLabel = tk.Label(loadFrame, textvariable=postcode, bg="black", fg="white", font=(None, 13),
                                     borderwidth=3,
                                     relief="groove")
            postcodeLabel.place(x=20, y=270)

            email = tk.StringVar(root, value="Email: " + str(userList[username][5]))
            emailLabel = tk.Label(loadFrame, textvariable=email, bg="black", fg="white", font=(None, 13),
                                  borderwidth=3,
                                  relief="groove")
            emailLabel.place(x=20, y=320)

            birthday = tk.StringVar(root, value="Birthday: " + str(userList[username][6]))
            birthdayLabel = tk.Label(loadFrame, textvariable=birthday, bg="black", fg="white", font=(None, 13),
                                     borderwidth=3,
                                     relief="groove")
            birthdayLabel.place(x=20, y=370)
            return userList[username]
        except:
            # the except will occur in case the username of the user doesn't exist, in that case
            # the programm can't display any information
            warningLabell = tk.Label(my_frameS, text="No user found!", bg="red", fg="black",
                                     font=(None, 13), borderwidth=3,
                                     relief="groove")
            warningLabell.place(x=600, y=600)
            warningLabell.after(3000, lambda: warningLabell.destroy())


# userSubmit function get the information from the GUI entry and pass them to Class in order to create an
# Users object and to store the user information
def userSubmit():
    username = usernameEntry.get()
    firstname = firstnameEntry.get()
    surname = surnameEntry.get()
    houseNr = houseNrEntry.get()
    streetName = streetEntry.get()
    postcode = postcodeEntry.get()
    email = emailEntry.get()
    birthday = birthdayEntry.get()
    # check if the entries are not empty
    if (
            username == "" or firstname == "" or surname == "" or houseNr == "" or streetName == "" or postcode == "" or email == "" or birthday
            == ""):
        warningLabell = tk.Label(my_frameS, text="Please fill all of the fields!", bg="red", fg="black",
                                 font=(None, 13), borderwidth=3,
                                 relief="groove")
        warningLabell.place(x=600, y=600)
    else:

        warningLabell = tk.Label(my_frameS, text="Congratulation, the user was added!       ", bg="yellow",
                                 fg="black",
                                 font=(None, 13), borderwidth=3,
                                 relief="groove")
        warningLabell.place(x=600, y=600)
        warningLabell.after(3000, lambda: warningLabell.destroy())
        # create an UserList object (that inherit Users class) using Users constructor
        user = UserList(username, firstname, surname, houseNr, streetName, postcode, email, birthday)
        # also we store the user information using store method
        user.store()
    # print the information about the current number of users registered
    printUserNumberInfo()


# I import datetime in order to work with dates
# I need dates when I have to borrow a book, I set up an overdue date
from datetime import date
import datetime

# loansList is a dictionary that keep track of every borrow book
loansList = {}


# Loans class in order to create Loans object
class Loans():

    def borrowBook(self, username, ID):
        # in order to borrow a book, we will chain the user to the books that he borrow
        # so, our dictionary key will be represented by username, and its value will be
        # represented by the ID of the book that he borrow and also a date
        # the date is calculated by add 14 days to the current day
        # in that way, the user can borrow a book for two weeks
        limitDate = date.today() + datetime.timedelta(days=14)
        if username not in loansList:
            # in case is first time that this user borrow
            loansList[username] = ([ID, limitDate])
        else:
            # in case this user already borrow something in the past
            loansList[username].append(ID)
            loansList[username].append(limitDate)

    # returnBook method will unchain the username from the Book that he borrow
    def returnBook(self, username, ID):
        del loansList[username][ID]

    # countLoans method will return the number of items in our dictionary, namely the number of loans
    def countLoans(self):
        return len(loansList)

    # overdueLoans method will return the username and the ID of book, for those loans which are overdue
    def overdueLoans(self):
        # I create a variable where I store today's date
        CurrentDate = datetime.date.today()

        for key in loansList:
            for i in range(1, len(loansList[key]), 2):
                # I compare the limitDate with CurrentDate, and if it is overdue, I will return the username
                # of the person who borrow the book and the ID of the book
                if (CurrentDate > loansList[key][i]):
                    return key, userList[key][0]

    # return the firstname, surname and email address name of a borrower of a given book
    def getInfo(self, ID):
        ok = 0
        for key in loansList:
            for i in range(0, len(loansList[key]), 2):
                if (loansList[key][i] == ID):
                    ok = 1
                    return userList[key][0], userList[key][1], userList[key][6]
        if (ok == 0):
            print("the book does not exist or is not borrowed")


mainScreen()
