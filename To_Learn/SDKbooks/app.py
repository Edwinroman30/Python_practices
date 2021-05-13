from books import Book
import SDKbooks
from tabulate import tabulate

#ADD

principito = Book('The Prince Of Egypt', 295)
firstbook = Book('Something rare hapend', 75)
anotheone = Book('Bruss Lee', 150)
#print(principito.is_short())

#! INSERT
""" SDKbooks.addSDKbooks(principito)
SDKbooks.addSDKbooks(firstbook)
SDKbooks.addSDKbooks(anotheone) """
#! UPDATE
#print(SDKbooks.updateSDKbooks(principito,'the prince of egypt'.title(), 295))

#! DELETE
#print(SDKbooks.deleteSDKbooks(principito))

#! SELECT STAMENTS
d = SDKbooks.retrieveSDKbooks()
print('\nWITH TABULATE:\n')
print(tabulate(d, headers=["Title","Num. Pages"]))

print('\nUSING OBJECT PRESENTATION OR __STRIN__ METHOD:\n')
for data in d:
    print(Book(data[0], data[1]))