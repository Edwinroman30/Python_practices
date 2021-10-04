import pywhatkit

text_Container = """Cordial Saludos,
Les escribo porque he intentado acceder a la base de datos O’Reilly, he seguido cada uno de los pasos establecidos en el vídeo que 
tienen en la plataforma (https://www.youtube.com/watch?v=F4IVmXtCBLo), pero aun así, no logró acceder. Cuando realizo el paso me 
dice que el usuario ya existe: 

Crear un entorno virtual windows>

Comandos:
Crear carpeta donde estara el proyecto: mkdir nombre_carpeta

Crear Entorno virtual: 
py o python3 -m venv .\[nombre del entorno virtual]\

Dar permisos varios: 
tess

Activar el entorno virtual: 
Ir a la carpeta SCRIPT y ejecutar el file .\activate

.\[nombre del entorno virtual]\scripts\activate.bat


.. Ya podemos intalar librerias y codificar!


Desactivar el entorno virtual: 

En consola > deactivate

Para eliminar el entorno virtual:
rmdir .\[nombre del entorno virtual]\s

"""

pywhatkit.text_to_handwriting(text_Container, save_to = "mytext",rgb = (0,0,255))