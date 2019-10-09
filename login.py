#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

# Headers
print("Content-Type: text/html")
print()

print("<html>")

form_input = cgi.FieldStorage()

if "name" not in form_input or "password" not in form_input:
    print("Debe rellenar todos los campos.")
else:
    print("Has iniciado sesion como %s." % form_input["name"].value)

print("</html>")
