#!/usr/bin/python
# -*- coding: utf-8 -*-
# A one line script that converts python code into one line... How useful                                
                                                                                  
with open("code.py", "r") as code_file, open("out.py", "w+") as out_file: out_file.write("exec("+str(bytes(code_file.read(), 'utf-8'))+")")
