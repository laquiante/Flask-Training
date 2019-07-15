#!/usr/bin/env python

import logging
import socket

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

from nlmanager.nlpacket import *
from nlmanager.nlmanager import NetlinkManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)7s: %(m$
log = logging.getLogger()

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/ifl')
def Schnittstellen():
    if_list = []
    for msg in nlmanager.request_dump(RTM_GETLINK, socket.AF_UNSPEC, debug=True$
        if_list.append(msg.get_attribute_value(Link.IFLA_IFNAME))
    return render_template('schnittstellen.html', list=if_list)

if __name__=='__main__':
    nlmanager = NetlinkManager()
    app.run(host='0.0.0.0', debug=True)
