def addbooks():
    title=input("Enter the Title: ")
    author=input("Enter Author name: ")
    with open("library.txt", "a") as f:
        f.write(author + "," + title + "\n")
        print("Book Added Successfully")
        
def searchbooks():
    key=input("Enter the Title or Author to search: ")
    with open("library.txt", "r") as f:
        found=False
        names=f.read()
        names=names.lower()
        if key in names:
            print("Book Found!!")
        else:
            print("NO Matching Books!")
            
def report():
     with open("library.txt", "r") as f:
        names=f.read().split()
    
        print("Number of books:", len(names))
        print(names)
print("\n1. Add Books")
print("2. Search Book")
print("3. Report")
print("4. Exit")
choice=int(input("Enter Choice: "))
if choice==1:
    addbooks()
elif choice==2:
    searchbooks()
elif choice==3:
    report()
elif choice==4:
    exit(0)
else:
    print("Invalid Choice !")

        
