########## with keyword ##########

#Es una forma pero a lo largo se vuelve un poco complicado.
#shorthand for opening file and automatically closed outside indent
try:
    with open("input.txt", "r") as file: #Make sure it exists
        try:
            int(file.read())
        except FileNotFoundError as e: #example of using thin except here
            print("No se encontro el archivo")
            print(file.closed) #closed
        except ValueError as e:
            print('Error al parcer el archivo')
            #do whatever
except OSError as e:
    print('Error al abrir el documento.')
    




#I think this could be written like so but may require another try inside else:   
try:
    file = open('nope')
except OSError as e:
    print(e)
else:
    with file:
        #try:
            file.read()
        #except Exception as e:
        #    print(e)




#Forma tradicional y segura.

try:
    file = open("input.txt", "r") #Make sure it exists
    data = int(file.read()) #This should fail
except FileNotFoundError as e: #subclass of OSError
    print("This file is not found")
except OSError as e:
    print("Couldn't open file")
except PermissionError as e:
    print("file is locked")
except ValueError as e:
    print("Cannot parse data. Check file") 
except Exception as e:
    print(type(e))
    print(e)
finally:
    file.close()
    print("Always runs")