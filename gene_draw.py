#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi

from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio.SeqFeature import SeqFeature, FeatureLocation

form_input = cgi.FieldStorage()

gene = form_input["gene"].value
start = int(form_input["start"].value)
end = int(form_input["end"].value)
strand = int(form_input["strand"].value)

# posiciones absolutas
abs_start = 0
abs_end = end - start

gdd = GenomeDiagram.Diagram(gene)
gdt_features = gdd.new_track(1, greytrack=False)
gds_features = gdt_features.new_set()


feature = SeqFeature(FeatureLocation(abs_start,abs_end), strand= strand)
gds_features.add_feature(feature,
                         name=gene,
                         sigil="ARROW",
                         label=True,
                         label_size=25,
                         label_angle=0,
                         color = colors.blue)

gdd.draw(format='linear', pagesize=(25*cm,4*cm), fragments=1,
         start=abs_start, end=abs_end + abs_end/10)

gdd.write("images/GD_labels_default.png", "png")

# Headers
print("Content-Type: text/html")
print()

print("<html>")
print("<body>")

print("El nombre del gen es %s. " % gene)
print('<br>')
print ("La longitud es de %s bp" % abs_end)
print('<br>')
print('<br>')
print('<img src="images/GD_labels_default.png" >')
print("</body>")
print("</html>")
