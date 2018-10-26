# -*- coding: utf-8 -*-
"""
    Consultas del xml --> NEWSELUJA_queries_spanish.xml
    
    Este programa invoca a la función formatearXML() que transforma el archivo xml a json.

    Después hace una petición al crawler y devuelve 100 consultas

    Las recibimos en formato json y los guardamos en un árbol de directorios
"""

import formateo_xml

formateo_xml.formatearXML()