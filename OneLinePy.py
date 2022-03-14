#!/usr/bin/python
# -*- coding: utf-8 -*-
# Simple script that converts code into one line 

with open("code.py", "r") as code_file:
    code = bytes(code_file.read(), 'utf-8')
with open("out.py", "w+") as out_file:
    out_file.write("exec("+str(code)+")")
