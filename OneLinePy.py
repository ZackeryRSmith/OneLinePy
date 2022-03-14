#!/usr/bin/python
# -*- coding: utf-8 -*-
# One line script that converts code into one line                                
                                                                                  
with open("code.py", "r") as code_file, open("out.py", "w+") as out_file: out_file.write("exec("+str(bytes(code_file.read(), 'utf-8'))+")")
