import io

""" To create a new file in Python, use the open() method, with one of the following parameters:
    "x" - Create - will create a file, returns an error if the file exist

    "a" - Append - will create a file if the specified file does not exist

    "w" - Write - will create a file if the specified file does not exist
 """

archivo = open("/home/edwin/Documents/Python/Python_practices/To_Learn/IO Module/mitexto.txt",'r+')

archivo.write('Bueno luego de un rato con errores, \nme di cuenta que se trataba del Path.')

archivo.close()


archivo = open("/home/edwin/Documents/Python/Python_practices/To_Learn/IO Module/mitexto.txt",'r+')

archivo.seek(len(archivo.read()))
archivo.write('By Edwin Roman')
mi_text = archivo.read()

archivo.close()

""" if(archivo.closed):
    print('Esta abierto')
else:
    print('TOdo en orden') """

print(mi_text)