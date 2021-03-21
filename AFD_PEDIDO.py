from objetos import *


def afd_pedido(ruta):
    signos = [37, 44]
    guionBajo = [95]
    letrasminusculas = crearVectorLetras(65, 90)
    letrasmayusculas = crearVectorLetras(97, 122)
    letras = letrasminusculas + letrasmayusculas
    numeros = crearVectorLetras(48, 57)
    caracteresIDENTIFICADOR = letras + numeros + guionBajo
    finID = [32, "\n", 10]
    tokensPedidos = []
    erroresPedidos = []
    arreglos = [tokensPedidos, erroresPedidos]
    cache = ""
    noToken = 1
    noError = 1
    tkCorrecto = True
    num_Dec = 0
    with open(ruta, mode="r", encoding="utf-8") as fichero:
        fila = 1
        for linea in fichero.readlines():
            texto = linea
            estado = 0
            posicion = 0
            posAux = 0
            longitud = len(texto)
            while posicion < longitud:
                # print("entro aqui xd mmmmmhhhh ")
                charCode = ord(texto[posicion])
                char = texto[posicion]
                if estado == 0:
                    if charCode == 32 or charCode == 10:
                        posicion += 1
                        
                    # % ,
                    elif charCode in signos:
                        # print(f"se acepta {char} como signo")
                        tk = token(noToken, char, fila, posicion, "Signo")
                        tokensPedidos.append(tk)
                        noToken += 1
                        posicion += 1
                        posAux += 1

                    # [a-z]
                    elif charCode in letras:
                        estado = 1
                        cache += char
                        posicion += 1
                        posAux += 1

                    # [0-9]
                    elif charCode in numeros:
                        estado = 3
                        cache += char
                        posicion += 1
                        posAux += 1

                    # ' comilla simple
                    elif charCode == 39:
                        estado = 2
                        posicion += 1
                        posAux += 1

                    # estado de error
                    else:
                        print("error")
                        tkE = tokenError(noError, char, fila, posicion - len(cache), "caracter no valido")
                        print(ord(char))
                        erroresPedidos.append(tkE)
                        noError += 1
                        posicion += 1
                        posAux += 1
                        cache = ""

                # estado de identificador
                elif estado == 1:
                    # [a-z 0-9 _ ]
                    if charCode in caracteresIDENTIFICADOR:
                        cache += char
                        posicion += 1
                        posAux += 1
                    elif charCode in finID:
                        # print(f"se acepta {cache} como identificador")
                        tk = token(noToken, cache, fila, posicion - len(cache), "Identificador")
                        tokensPedidos.append(tk)

                        if tkCorrecto is False:
                            tkE = tokenError(noError, cache, fila, posicion - len(cache), "Identicador no valido")
                            erroresPedidos.append(tkE)
                            noError += 1

                        tkCorrecto = True
                        estado = 0
                        noToken += 1
                        cache = ""
                    else:
                        print(charCode)
                        print(char)
                        print(f"Caracter de identificador desconocido '{char}' code : {charCode} error detectado")
                        cache += char
                        posicion += 1
                        posAux += 1
                        tkCorrecto = False

                # estado de cadena
                elif estado == 2:
                    if charCode != 39:
                        cache += char
                        posicion += 1
                        posAux += 1

                    else:
                        # print(f"se acpeta {cache} como cadena")
                        if cache == "":
                            cache = "Sin Descripcion"
                        tk = token(noToken, cache, fila, posicion, "cadena")
                        tokensPedidos.append(tk)
                        noToken += 1
                        cache = ""
                        posicion += 1
                        posAux += 1
                        estado = 0

                # estado numero
                elif estado == 3:
                    if charCode in numeros:
                        cache += char
                        posicion += 1
                        posAux += 1

                    elif charCode == 46:
                        cache += char
                        posicion += 1
                        posAux += 1
                        estado = 4

                    elif charCode == 32 or charCode == 44 or charCode == 37:
                        # print(f"se acepta {cache} como numero")
                        tk = token(noToken, cache, fila, posicion - len(cache), "Numero")
                        tokensPedidos.append(tk)

                        if tkCorrecto is False:
                            tkE = tokenError(noError, cache, fila, posicion - len(cache), "numero no valido")
                            erroresPedidos.append(tkE)
                            noError += 1

                        tkCorrecto = True
                        # posicion += 1
                        # posAux += 1
                        noToken += 1
                        estado = 0
                        cache = ""

                    else:
                        cache += char
                        posicion += 1
                        posAux += 1
                        tkCorrecto = False

                # estado numero con decimal
                elif estado == 4:
                    if charCode in numeros:
                        cache += char
                        posicion += 1
                        posAux += 1
                        num_Dec += 1
                    elif charCode == 32 or charCode == 37 or charCode == 44:
                        # print(f"se acepta {cache} como Numero")
                        if num_Dec == 0:
                            cache += "0"
                        if tkCorrecto is False:
                            tkE = tokenError(noError, cache, fila, posicion - len(cache), "numero no valido")
                            erroresPedidos.append(tkE)
                            noError += 1
                        tk = token(noToken, cache, fila, posicion - len(cache), "Numero")
                        tokensPedidos.append(tk)
                        noToken += 1
                        tkCorrecto = True
                        # posicion += 1
                        # posAux += 1
                        estado = 0
                        num_Dec = 0
                        cache = ""

                    else:
                        posAux += 1
                        posicion += 1
                        cache += char
                        tkCorrecto = False

                # estado de error
                else:
                    print("error")
                    tkE = tokenError(noError, char, fila, posicion - len(cache), "caracter no valido")
                    erroresPedidos.append(tkE)
                    noError += 1
                    posicion += 1
                    posAux += 1
                    cache = ""

            fila += 1
    return arreglos


def crearVectorLetras(inicio, final):
    vector = []
    for i in range(inicio, final+1):
        vector.append(i)
    return vector
