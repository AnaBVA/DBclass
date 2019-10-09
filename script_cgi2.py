#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import platform

# Headers
print("Content-Type: text/html")
print()

print("<TITLE>My CGI </TITLE>")

url_input = cgi.FieldStorage()

print("""
<html>
<head>
    <title>Título de la página</title>
</head>
<h3>Hola %s!</h3>
</html>""" % url_input["nombre"].value)

# http://localhost:8890/script_cgi2.py?nombre=Ana
