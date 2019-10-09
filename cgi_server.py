#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http.server import HTTPServer, CGIHTTPRequestHandler


class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/"]


httpd = HTTPServer(("", 8890), Handler)
httpd.serve_forever()
