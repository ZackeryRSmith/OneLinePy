#!/usr/bin/python
# -*- coding: utf-8 -*-
# A one line script that converts python code into one line... How useful                                
                                                                                  
with open("code.py", "r") as c, open("out.py", "w+") as o: o.write("exec("+str(bytes(c.read(), 'utf-8'))+")")
