from objetos import *


def ordenarTKMenu(tokens):
    p_rest = obtenerRestaurante(tokens)
    restaurante = restaurant(tokens[p_rest].lexema)
    sub_SECCIONES = tokens[p_rest+1:]
    indices = obtenerIndicesSecciones(sub_SECCIONES)

    for i in range(0, len(indices) - 1):
        n_seccion = sub_SECCIONES[indices[i]].lexema
        sec = seccion(n_seccion)
        sub_opciones = sub_SECCIONES[indices[i]+2:indices[i+1]]
        indiceOpciones = obtenerIndicesOpciones(sub_opciones)
        print(indiceOpciones)
        
        for j in range(0, len(indiceOpciones) - 1):
            conSig = sub_opciones[indiceOpciones[j]:indiceOpciones[j + 1]]
            sub_opcion = quitarSignos(conSig)
            # format(float(sub_opcion[2].lexema), "8.,2f")
            # prec = format(float(sub_opcion[2].lexema), ":,.2f")
            op = opcion(sub_opcion[0].lexema, sub_opcion[1].lexema, sub_opcion[2].lexema, sub_opcion[3].lexema)
            # op.imprimir()
            sec.opciones.append(op)

        restaurante.secciones.append(sec)
    return restaurante


def obtenerIndicesSecciones(tokens):
    posSecciones = []
    pos = 0
    for tok in tokens:
        tipoTK = tok.lexema
        if tipoTK != ":":
            pos += 1
        elif tipoTK == ":":
            posSecciones.append(pos-1)
            pos += 1
    posSecciones.append(len(tokens))
    return posSecciones


def obtenerIndicesOpciones(tks):
    posOpciones = []
    pos = 0
    for tok in tks:
        tipoTK = tok.lexema
        if tipoTK != "[":
            pos += 1
        else:
            posOpciones.append(pos)
            pos += 1
    posOpciones.append(len(tks))
    return posOpciones


def quitarSignos(vector):
    sinSignos = []
    for elemento in vector:
        tk = elemento.lexema
        tipoTK = elemento.tk
        if tipoTK != "Signo":
            sinSignos.append(elemento)
    return sinSignos


def obtenerRestaurante(toks):
    ind = 0
    pos = 0
    for elemento in toks:
        tipoTK = elemento.lexema
        if tipoTK != "=":
            pos += 1
        else:
            ind = pos + 1
    return ind
