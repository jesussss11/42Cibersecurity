import sys
def text_analyzer(texto=None):
    """Funcion que recoge una cadena de texto como argumento y muestra los caracteres que contiene, 
    numero de mayusculas, numero de minusculas, numero de signos de puntuacion y numero de espacios 
    Argumentos:
    args = La cadena que se va a utilizar.
    Retorna:
    #None
    """
    if texto is None or texto == "":
      texto = input("Cadena de texto: ")
    if not isinstance(texto, str):
        print("Error: el argumento debe ser una cadena.")
        return
    num_mayusculas = 0
    num_minusculas = 0
    num_puntuacion = 0
    num_espacion = 0
    for caracter in texto:
        if caracter.isupper():
            num_mayusculas += 1
        elif caracter.islower():
            num_minusculas += 1
        elif caracter.isspace():
            num_espacion += 1
        else:
            num_puntuacion +=1

    resultado = len(texto)        
    print("The text contains " + str(resultado)+ " character(s)")
    print("Upper letter(s): ", num_mayusculas)
    print("Lower letter(s): ", num_minusculas)
    print("Punctuation mark(s): ", num_puntuacion)
    print("Space(s): ", num_espacion)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        texto = " ".join(sys.argv[1:])
        text_analyzer(str(texto))
        sys.exit()
    elif len(sys.argv) > 2:
        print("Use only a argument")
        sys.exit()
    