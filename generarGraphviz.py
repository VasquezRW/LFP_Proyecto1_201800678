import subprocess

from graphviz import Digraph


def generarGrafica(rest):
    try:
        dot = Digraph(comment='restaurante')
        dot.node('restaurante', rest.nombre)
        for sec in rest.secciones:
            dot.node('seccion'+sec.nombre, sec.nombre)
            dot.edge('restaurante', 'seccion'+sec.nombre)
            for opc in sec.opciones:
                texto = f"{opc.nombre}" + " Q.{:,.2f}".format(float(opc.precio)) + f"\n{opc.descripcion}"
                dot.node('opcion'+opc.id, texto)
                dot.edge('seccion'+sec.nombre, 'opcion'+opc.id)

        dot.render('graficoMenu.pdf', view=True)
        subprocess.Popen(['graficoMenu.pdf'], shell=True)

    except Exception as e:
        print("Algo ocurrio: " + str(e))