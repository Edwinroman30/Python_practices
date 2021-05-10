import os
from datetime import datetime

#--------------------WORKING WITH DIRECTORIES AND FILES------------------------------
''' 
#chance directory>
os.chdir()

#TO work with folders:
os.mkdir('General_things')

#TO create a structure of folders;
os.makedirs('Myproyect/modules')

#TO remove specific folder:
os.rmdir('General_things')

#TO remove a structure of folders;
os.removedirs('Myproyect/modules')

os.rename('FolderA','FolderB')
 '''

#To list my data or folders
#print(os.listdir())

# OS.stat - nos provee una serie de informacion de nuestro archivo
ruta = os.path.join('/home/edwin/Documents/Python/Python_practices/To_Learn/OS_Module','test.txt')
info = os.stat(ruta)
#Ejemplo el tiempo de la fecha de modificacion.
time_info = os.stat(ruta).st_atime

print(datetime.fromtimestamp(time_info))

# Se usa el os.walk() para recorreger un yield en forma de arbol.
''' for dir_path,dir_name, filename in os.walk(os.getcwd()):
    print('Current_PATH: {} \nDirectories: {}\nFiles: {}\n'.format(dir_path,dir_name,filename))
 '''
 
print(os.environ.get('HOME'))