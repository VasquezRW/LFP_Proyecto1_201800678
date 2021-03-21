from objetos import *


def ordenarTKPedidos(tokens):
    p_datos = obtenerIndiceDatos(tokens)
    datos = tokens[:p_datos]
    datos_sSig = quitarSignos(datos)
    print("posicion %")
    print(p_datos)
    print(
        f"datos: {datos_sSig[0].lexema} | {datos_sSig[1].lexema} | {datos_sSig[2].lexema} | {datos_sSig[3].lexema} ")

    sub_pedidos = tokens[p_datos+1:]
    print("imprimir tokens sub pedidos")
    for sp in sub_pedidos:
        print(sp.lexema)

    fact = factura(datos_sSig[0].lexema, datos_sSig[1].lexema, datos_sSig[2].lexema, datos_sSig[3].lexema)
    indices = obtenerIndicesOpciones(sub_pedidos)
    print("Indices opciones")
    print(indices)
    for i in range(0, len(indices) - 1):
        sub_pedido = sub_pedidos[indices[i]:indices[i + 1]]
        ped_sSig = quitarSignos(sub_pedido)
        print(f"sub_pedido: {ped_sSig[0].lexema} | {ped_sSig[1].lexema}")
        ped = pedido(ped_sSig[0].lexema, ped_sSig[1].lexema)
        fact.pedidos.append(ped)
        ped.imprimir()
    return fact


def obtenerIndiceDatos(tokens):
    pos = 0
    for tok in tokens:
        tipoTK = tok.lexema
        if tipoTK != "%":
            pos += 1
        elif tipoTK == "%":
            return pos
        else:
            return None


def obtenerIndicesOpciones(tks):
    posOpciones = []
    pos = 0
    for tok in tks:
        lexemaTK = tok.lexema
        tipoTK = tok.tk
        if tipoTK == "Numero":
            posOpciones.append(pos)
            pos += 1
        else:
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
    print("opcion sin signos")
    for sig in sinSignos:
        print(sig.lexema)
    return sinSignos

