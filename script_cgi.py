#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import platform

# Headers
print("Content-Type: text/html")
print()


print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print("Hello, world!")
print('<br>')
print('<br>')
print('<br>')
print('<br>')
print("<H4>Version de python:</H4>", platform.sys.version)
print('<br>')
print("<H4>path de python:</H4>",platform.sys.prefix)
