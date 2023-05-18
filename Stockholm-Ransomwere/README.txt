El código importa varias librerías necesarias para su correcto funcionamiento:

- os: para acceder al sistema de archivos y trabajar con los archivos de la carpeta especificada.
- argparse: para definir y gestionar los argumentos del programa.
- hashlib: para generar una clave de cifrado basada en una contraseña.
- AES: para cifrar y descifrar archivos.
A continuación, se definen los argumentos del programa mediante la clase ArgumentParser de argparse.

- La opción "-v" o "--version" muestra la versión del programa.
- La opción "-r" o "--reverse" se utiliza para deshacer la operación de cifrado y renombrado de archivos.
- La opción "-s" o "--silent" se utiliza para evitar que el programa muestre mensajes en la consola.
Después de definir los argumentos, se define la clave de cifrado y se genera una clave de inicialización (IV) utilizando la función sha256 de la librería hashlib. Se crea un objeto de cifrado AES utilizando la clave y el IV.

La función infect_folder() renombra y cifra los archivos con las extensiones definidas en la lista de extensiones.

_ Se define la carpeta que se va a cifrar mediante la variable folder_path.
_ La lista de extensiones se define en la variable extensions.
_ Se recorren los archivos de la carpeta especificada y se renombran/cifran los que corresponden.
_ Se genera un nuevo nombre de archivo cambiando la extensión del archivo original a ".ft".
_ Se comprueba si ya existe un archivo con el mismo nombre en la carpeta. Si es así, se salta al siguiente archivo.
_ Se abre el archivo original y se lee su contenido en la variable plaintext.
_ Si el tamaño del archivo no es un múltiplo de 16 bytes, se añaden espacios en blanco al final del archivo hasta que se completa un bloque de 16 bytes.
_ Se cifra el contenido del archivo utilizando el objeto de cifrado AES.
_ Se crea un nuevo archivo con el nombre nuevo y se escribe el contenido cifrado en el archivo.
_ Se elimina el archivo original.
_ Si args.silent es False, se muestra un mensaje en la consola informando sobre el archivo que se ha cifrado.
La función revert_infection() deshace la operación de cifrado y renombrado de archivos.

Se define la carpeta que se va a desinfectar mediante la variable folder_path.
Se recorren los archivos de la carpeta especificada y se desencriptan/renombran los que corresponden.
Se comprueba si el archivo tiene la extensión ".ft".
Se abre el archivo cifrado y se lee su contenido en la variable ciphertext.
Se descifra el contenido del archivo utilizando el objeto de cifrado AES.
Se crea un nuevo archivo con el nombre original y se escribe el contenido descifrado en el archivo.
Se elimina el archivo cifrado.
Si el programa se ejecuta con la opción "-r" o "--reverse", se llama a la función revert_infection(). En caso contrario, se llama a la función infect_folder().


-------COMPILAR
Si tu intencion es compilar el programa deberas instalar pyinstaller:
    - pip insall pyinstaller
Ejecuta el siguiente comando para crear el archivo ejecutable:
    - pyinstaller archivo.py