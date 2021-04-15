#!/usr/local/bin/python3
# coding: utf-8

import cgitb
cgitb.enable()
 
from wsgiref.handlers import CGIHandler
from app import server
CGIHandler().run(server)

