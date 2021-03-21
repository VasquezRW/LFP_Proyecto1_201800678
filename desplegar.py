import subprocess
import time


def desplegarMenuHTML(rest, limite):
    try:
        f = open('menu.html', 'w')
        f.write("""<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand">
                    <img src="usacIcono.png" width="100" height="100">
                  </a>
                  <a class="navbar-brand">
                  <h2><b> Wilmer Estuardo Vasquez Raxon - 2018000678 </b></h2>
                  </a>
                </nav>
            </head>
            <body>""")
        f.write("<br><br>\n")
        f.write("""
            <div class="container" style="text-align: center;"><h4 > <b> """ + rest.nombre +
                """</b> </h4></div>
            <br>
            <div class="container" style="text-align: center;" > <ul class="list-group">""")

        for sec in rest.secciones:
            f.write("<h1>" + sec.nombre + "</h1>")

            if limite is None:
                for op in sec.opciones:
                    f.write("""<li class="list-group-item">""")
                    f.write("<h4>Nombre: </h4>" + op.nombre + " <h4> Precio:</h4> Q.{:,.2f}".format(float(op.precio)))
                    f.write("<br>")
                    f.write("Descripcion: " + op.descripcion + "\n")
                    f.write("</li>")
            elif limite is not None:
                for op in sec.opciones:
                    if float(op.precio) <= limite:
                        f.write("""<li class="list-group-item">""")
                        f.write(
                            "<h4>Nombre: </h4>" + op.nombre + " <h4> Precio:</h4> Q.{:,.2f}".format(float(op.precio)))
                        f.write("<br>")
                        f.write("Descripcion: " + op.descripcion + "\n")
                        f.write("</li>")

        f.write('\n</ul> </div> \n')
        fin = """</body>
                </html>"""
        f.write(fin)
        f.close()
        subprocess.Popen(['menu.html'], shell=True)
    except:
        print("algo ocurrio")


def desplegarFacturaHTML(fact, rest):
    try:
        f = open('factura.html', 'w')
        f.write("""<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand">
                    <img src="usacIcono.png" width="100" height="100">
                  </a>
                  <a class="navbar-brand">
                  <h2><b> Wilmer Estuardo Vasquez Raxon - 2018000678 </b></h2>
                  </a>
                </nav>
            <style>
            table, th {
              border: 1px solid black;
              border-collapse: collapse;
            }
            </style>
            </head>
            <body>""")
        f.write("<br><br>\n")
        f.write("""
            <div class="container" style="text-align: center;"><h4 > <b> """ + rest.nombre +
                """</b> </h4></div><br>""")
        f.write("""<div class="container" style="text-align: center;"><h4 > <b>  Factura No. 1""" +
                """</b> </h4></div><br>""")
        f.write("""<div class="container" style="text-align: center;"><h4 > <b> Fecha:  """ + time.strftime("%d/%m/%y") +
                """</b> </h4></div><br>""")
        f.write(""" <div class="container" style="text-align: left;"> <h4><b> Datos del Cliente</b> </h4></div>
            <br>""")
        f.write(""" <div class="container" style="text-align: left;"> <b>Nombre:  """ + fact.nombre +
                """</b> </div><br>""")
        f.write(""" <div class="container" style="text-align: left;"> <b>NIT: """ + fact.nit +
                """</b> </div><br>""")
        f.write(""" <div class="container" style="text-align: left;"> <b>Direccion: """ + fact.direccion +
                """</b> </div><br>""")
        f.write(""" <div class="container" style="text-align: left;"> <b>Descripcion</b> </div><br>""")
        f.write("""<div class="container" style="text-align: center;" > \n""")
        f.write("""<li class="list-group-item">""")
        f.write("<table style=\"width:100%\">\n")
        f.write("<tr>\n")
        f.write("<th><b> Cantidad </b></th>\n")
        f.write("<th><b> Nombre </b></th>\n")
        f.write("<th><b> Precio </b></th>\n")
        f.write("<th><b> Total </b></th>\n")
        f.write("</tr>\n")
        for ped in fact.pedidos:
            f.write("<tr>")
            f.write("<td> " + ped.cantidad + "</td>\n")
            f.write("<td> " + ped.nombre + "</td>\n")
            f.write("<td> Q{:,.2f}".format(float(ped.precio)) + "</td>\n")
            f.write("<td> Q{:,.2f}".format(float(ped.total)) + "</td>\n")
            f.write("</tr>\n")
        f.write("<tr>\n")
        f.write("<td> Subtotal</td>\n")
        f.write("<td> </td>\n")
        f.write("<td> </td>\n")
        f.write("<td> Q{:,.2f}".format(float(fact.subTotal)) + "</td>\n")
        f.write("</tr>\n")

        f.write("<tr>\n")
        f.write("<td> Propina ({:,.2f}".format(float(fact.propina)) + "%)</td>\n")
        f.write("<td> </td>\n")
        f.write("<td> </td>\n")
        f.write("<td> Q{:,.2f}".format(float(fact.totalPropina)) + "</td>\n")
        # .{:,.2f}".format(float(op.precio))
        f.write("</tr>\n")

        f.write("<tr>\n")
        f.write("<th><b> Total </b></th>\n")
        f.write("<th> </th>\n")
        f.write("<th> </th>\n")
        f.write("<th> Q{:,.2f}".format(float(fact.total)) + "</th>\n")
        f.write("</tr>\n")

        f.write("</table>\n")
        f.write('\n</li> \n')
        f.write('\n</div> \n')
        fin = """</body>
                </html>"""
        f.write(fin)
        f.close()
        subprocess.Popen(['factura.html'], shell=True)
    except:
        print("algo ocurrio")


def desplegarTokensHTML(toks):
    try:
        f = open('tokens.html', 'w')
        f.write("""<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand">
                    <img src="usacIcono.png" width="100" height="100">
                  </a>
                  <a class="navbar-brand">
                  <h2><b> Wilmer Estuardo Vasquez Raxon - 2018000678 </b></h2>
                  </a>
                </nav>
                <style>
                table, th {
                  border: 1px solid black;
                  border-collapse: collapse;
                }
                </style>
            </head>
            <body>""")
        f.write("<br><br>\n")
        f.write("""
            <div class="container" style="text-align: center;"><h4 > <b> Tokens de Menu</b> </h4></div>
            <br>
            <div class="container" style="text-align: center;" > """)

        f.write("""<li class="list-group-item">""")
        f.write("<table style=\"width:100%\">\n")
        f.write("<tr>\n")
        f.write("<th><b> No </b></th>\n")
        f.write("<th><b> Lexema </b></th>\n")
        f.write("<th><b> Fila </b></th>\n")
        f.write("<th><b> Columna </b></th>\n")
        f.write("<th><b> Token </b></th>\n")
        f.write("</tr>\n")
        for tok in toks:
            f.write("<tr>")
            f.write("<td> " + str(tok.no) + "</td>\n")
            f.write("<td> " + tok.lexema + "</td>\n")
            f.write("<td>" + str(tok.fila) + "</td>\n")
            f.write("<td>" + str(tok.columna) + "</td>\n")
            f.write("<td>" + tok.tk + "</td>\n")
            f.write("</tr>\n")
        f.write("</table>\n")
        f.write('\n</li> \n')
        f.write('\n </div> \n')
        fin = """</body>
                </html>"""
        f.write(fin)
        f.close()
        subprocess.Popen(['tokens.html'], shell=True)
    except:
        print("algo ocurrio generando reporte de tokens")


def desplegarTokensErrorHTML(toks):
    try:
        f = open('tokensError.html', 'w')
        f.write("""<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

                <nav class="navbar navbar-dark bg-dark">
                  <a class="navbar-brand">
                    <img src="usacIcono.png" width="100" height="100">
                  </a>
                  <a class="navbar-brand">
                  <h2><b> Wilmer Estuardo Vasquez Raxon - 2018000678 </b></h2>
                  </a>
                </nav>
                <style>
                table, th {
                  border: 1px solid black;
                  border-collapse: collapse;
                }
                </style>
            </head>
            <body>""")
        f.write("<br><br>\n")
        f.write("""<div class="container" style="text-align: center;"><h4 > <b> Tokens de Error</b> </h4></div>
            <br><div class="container" style="text-align: center;" > """)

        f.write("""<li class="list-group-item">""")
        f.write("<table style=\"width:100%\">\n")
        f.write("<tr>\n")
        f.write("<th><b> No </b></th>\n")
        f.write("<th><b> Caracter </b></th>\n")
        f.write("<th><b> Fila </b></th>\n")
        f.write("<th><b> Columna </b></th>\n")
        f.write("<th><b> descripcion </b></th>\n")
        f.write("</tr>\n")
        for tok in toks:
            f.write("<tr>")
            f.write("<td> " + str(tok.no) + "</td>\n")
            f.write("<td> " + tok.caracter + "</td>\n")
            f.write("<td>" + str(tok.fila) + "</td>\n")
            f.write("<td>" + str(tok.columna) + "</td>\n")
            f.write("<td>" + tok.descripcion + "</td>\n")
            f.write("</tr>\n")
        f.write("</table>\n")
        f.write('\n</li> \n')
        f.write('\n </div> \n')
        fin = """</body>
                </html>"""
        f.write(fin)
        f.close()
        subprocess.Popen(['tokensError.html'], shell=True)
    except:
        print("algo ocurrio generando reporte de errores")