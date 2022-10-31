books = ["Python Crash Course", "Game Programming", "Code Complete",
         "Clean Code", "Python Crash Course", "The Pragmatic Programmer", "Python Crash Course"]

while "Python Crash Course" in books:
    books.remove("Python Crash Course")


#the wrong way
#for position in range(len(books)):
    #if books[position] == "Python Crash Course":
       # books.pop(position)


print(books)