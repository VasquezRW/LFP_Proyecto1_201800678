import subprocess
from desplegar import *
from AFD_MENU import *
from AFD_PEDIDO import *
from procesarMenu import *
from procesarPEDIDO import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from generarGraphviz import *

tk_menu = []
errores_menu = []
tk_pedidos = []
errores_pedidos = []
restaurante = None
fac = None


def esNumero(valor):
    try:
        return float(valor) if "." in valor else int(valor)
    except:
        return None


def escoger_archivo():
    ruta = Tk()
    a = askopenfilename()
    ruta.withdraw()
    return a


if __name__ == '__main__':
    try:
        op = None
        while op != 6:
            print("----------------------------------")
            print("Wilmer Estuardo Vasquez Raxon")
            print("201800678")
            print("Lenguajes Formales y de Programacion Seccion \"A+\" ")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to Semestre")
            print("----------------------------------")
            print("Bienvenido a Practica 1")
            print("1. Cargar menu")
            print("2. Cargar orden")
            print("3. Generar menu")
            print("4. Generar factura")
            print("4. Generar arbol")
            print("6. Salida")
            print("----------------------------------")
            op = int(input())

            if op == 1:
                print("----------------------------------")
                # ruta = input("Ingrese la ruta:\n")

                # ruta sin errores
                # ruta = "C:\\Users\\Storias\\Desktop\\LFP-Proyecto1-2021S1-main\\TacoBell\\MenuTacoBell.lfp"
                # ruta = "C:\\Users\\Storias\\Desktop\\LFP-Proyecto1-2021S1-main\\menu.lfp"
                # ruta con errores
                # ruta = "C:\\Users\\Storias\\Desktop\\LFP-Proyecto1-2021S1-main\\TacoBell\\MenuErrores.lfp"
                ruta = escoger_archivo()
                menu = afd_Entrada(ruta)
                tk_menu = menu[0]
                errores_menu = menu[1]

                # print("-----------------------Tokens-----------------------")
                # for i in range(len(tk_menu)):
                #     print(tk_menu[i].lexema)
                # print("-----------------------errores-----------------------")
                # for i in range(len(errores_menu)):
                #     print(errores_menu[i].caracter)
                restaurante = ordenarTKMenu(tk_menu)
                print("----------------------------------")

            elif op == 2:
                print("----------------------------------")
                # ruta
                # ruta = "C:\\Users\\Storias\\Desktop\\LFP-Proyecto1-2021S1-main\\TacoBell\\Orden2Errores.lfp"
                # ruta = "C:\\Users\\Storias\\Desktop\\LFP-Proyecto1-2021S1-main\\TacoBell\\OrdenTacoBell.lfp"
                # ruta = "C:\\Users\\Storias\\Desktop\\LFP-Proyecto1-2021S1-main\\orden.lfp"
                # ruta = "C:\\Users\\Storias\\Desktop\\LFP-Proyecto1-2021S1-main\\TacoBell\\MenuErrores.lfp"
                ruta = escoger_archivo()
                pedidos = afd_pedido(ruta)
                tk_pedidos = pedidos[0]
                errores_pedidos = pedidos[1]

                # print("-----------------------Tokens-----------------------")
                # for i in range(len(tk_pedidos)):
                #     print(tk_pedidos[i].lexema)
                # print("-----------------------errores-----------------------")
                # print(len(errores_pedidos))
                # for i in range(len(errores_pedidos)):
                #     print(errores_pedidos[i].caracter)
                # print("-----------------------errores-----------------------")
                # print(len(errores_pedidos))
                # for error in errores_pedidos:
                #     error.imprimir()

                print("----------------------------------")

            elif op == 3:
                print("----------------------------------")
                if len(tk_menu) == 0:
                    print("No se ha seleccionado un archivo de menu")
                else:
                    if len(errores_menu) == 0:
                        limOp = int(input("Desea poner un limite para las opciones ? \n"
                                          "1. Si\n"
                                          "2. No\n"))
                        if limOp == 1:
                            limite = float(input("Ingrese el limite: \n"))
                            desplegarMenuHTML(restaurante, limite)
                            desplegarTokensHTML(tk_menu)
                        elif limOp == 2:
                            desplegarMenuHTML(restaurante, None)
                        else:
                            print("Opcion invalida")
                    else:
                        print("Se detectaron errores en el menu")
                        print("Generando reporte...")
                        desplegarTokensErrorHTML(errores_menu)
                # print("Imprimir menu: ")
                # restaurante.imprimir()
                print("----------------------------------")
            elif op == 4:
                print("----------------------------------")
                if len(tk_menu) == 0:
                    print("No se ha seleccionado un archivo de menu")
                else:
                    fac = ordenarTKPedidos(tk_pedidos)
                    print("Imprimir Factura: ")
                    fac = procesar_Factura(restaurante, fac)

                    fac.imprimir()

                    if (len(errores_pedidos) == 0) or (fac.facturaCorrecta is True):
                        desplegarFacturaHTML(fac, restaurante)
                    else:
                        print("Se detectaron errores en el menu")
                        print("Generando reporte...")
                        desplegarTokensErrorHTML(errores_pedidos)
                print("----------------------------------")
            elif op == 5:
                print("----------------------------------")
                if len(tk_menu) == 0:
                    print("No se ha seleccionado un archivo de menu")
                else:
                    if len(errores_menu) == 0:
                        generarGrafica(restaurante)
                    else:
                        print("Se detectaron errores en el menu")
                        print("Generando reporte...")
                        desplegarTokensErrorHTML(errores_menu)
                print("----------------------------------")
            elif op == 6:
                print("----------------------------------")
                print("ADIOS...")
            else:
                print("nose :v")
    except ValueError:
        print("Ha ocurrido un error")