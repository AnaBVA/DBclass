#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
# Headers
print("Content-Type: text/html")
print()

print("""<html>
    <head><title>Formulario</title></head>
    <form method="post" action="login.py">
        Nombre: <input name="name" type="text" /> <br />
        Contrasena: <input name="password" type="password" /> <br />
        <button>Ingresar</button>
    </form>
    </html>""")
