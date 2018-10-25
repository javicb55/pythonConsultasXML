# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:08:34 2018

@author: Andrew
"""

import requests
import sys

def descargarWeb(url):

    r = requests.get(url)
    if r.status_code != 200:
        sys.stderr.write("! Error {} retrieving url {}".format(r.status_code, url))
        return None
    
    return r