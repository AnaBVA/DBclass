#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
# Headers
print("Content-Type: text/html")
print()

print("""<html>
    <head><title>Formulario de genes</title></head>
    <form method="get" action="gene_draw.py">
        Gene name: <input name="gene" type="text" /> <br />
        Start site: <input name="start" type="number" /> <br />
        End site: <input name="end" type="number" /> <br />
        Strand: <input name="strand" type="number" /> <br />
        <button>Ingresar</button>
    </form>
    </html>""")
