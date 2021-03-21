
class token:
    def __init__(self, no=None, lexema=None, fila=0, columna=0, tk=None):
        self.no = no
        self.lexema = lexema
        self.fila = fila
        self.columna = columna
        self.tk = tk

    def imprimir(self):
        print(f"No: {self.no} | Lexema: {self.lexema} | Fila: {self.fila} | Columna: {self.columna} | Token: {self.tk}")

    def imprime(self):
        print(f"{self.lexema}")


class tokenError:
    def __init__(self, no=None, caracter=None, fila=0, columna=0, descripcion=None):
        self.no = no
        self.caracter = caracter
        self.fila = fila
        self.columna = columna
        self.descripcion = descripcion

    def imprimir(self):
        print(f"No: {self.no} | Caracter: {self.caracter} | Fila: {self.fila} | Columna: {self.columna} | Descripcion: {self.descripcion}")

    def imprime(self):
        print(f"Caracter: {self.caracter} | Descripcion: {self.descripcion}")


class restaurant:
    def __init__(self, nombre=None):
        self.nombre = nombre
        self.secciones = []

    def imprimir(self):
        print(f"Restaurate: {self.nombre}")
        for sec in self.secciones:
            sec.imprimir()

    def buscarOpcion(self, identificador):
        for sec in self.secciones:
            if sec.buscarOp(identificador) is not None:
                return sec.buscarOp(identificador)
        return None


class seccion:
    def __init__(self, nombre=None):
        self.nombre = nombre
        self.opciones = []

    def imprimir(self):
        print(f"SECCION: {self.nombre}")
        for op in self.opciones:
            op.imprimir()

    def buscarOp(self, identificador):
        for op in self.opciones:
            if op.id == identificador:
                return op
        return None


class opcion:
    # [IDENTIFICADOR,’NOMBRE’;PRECIO;’DESCRIPCIÓN’]
    def __init__(self, id=None, nombre=None, precio=None, descripcion=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def imprimir(self):
        print(f"ID: {self.id} | nombre: {self.nombre} | precio: {self.precio} | Descripcion: {self.descripcion}")


class factura:
    def __init__(self, nombre=None, nit=None, direccion=None, propina=None):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.propina = propina
        self.pedidos = []
        self.subTotal = None
        self.total = None
        self.totalPropina = None
        self.facturaCorrecta = None

    def imprimir(self):
        print(f"Nombre: {self.nombre} | NIT: {self.nit} | Direccion: {self.direccion} | Propina: {self.propina}")
        for ped in self.pedidos:
            ped.imprimir()

    def calcularTotal(self):
        sTotal = 0
        for ped in self.pedidos:
            sTotal += float(ped.total)
        self.subTotal = str(sTotal)
        tp = sTotal*(float(self.propina)/100)
        t = sTotal + tp
        self.total = str(t)
        self.totalPropina = str(tp)


class pedido:
    def __init__(self, cantidad=None, id=None):
        self.cantidad = cantidad
        self.id = id
        self.precio = 0
        self.total = 0
        self.nombre = None

    def imprimir(self):
        print(f"Cantidad: {self.cantidad} | ID: {self.id} | Precio: {self.precio} | Total: {self.total}")


def procesar_Factura(rest, fact):
    for ped in fact.pedidos:
        if rest.buscarOpcion(ped.id) is not None:
            op = rest.buscarOpcion(ped.id)
            ped.precio = op.precio
            ped.nombre = op.nombre
            if "." in ped.cantidad or (0 >= float(fact.propina) and float(fact.propina) <= 100):
                fact.facturaCorrecta = False
            ped.total = str(float(ped.precio)*float(ped.cantidad))
        else:
            fact.facturaCorrecta = False
    fact.calcularTotal()
    return fact
