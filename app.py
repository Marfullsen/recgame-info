#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from static import minimap

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        info_json = minimap.write_minimap(uploaded_file.filename)
        write(info_json)
    return render_template('generated.html', 
                            filename=uploaded_file.filename,
                            source='minimap_'+uploaded_file.filename[:-4]+'.png', 
                            info_json=info_json)

def write(info_json):
    """Creates a Json file"""
    pass

def read():
    """Reads a Json file"""
    pass

if __name__ == '__main__':
    read()
   app.run(debug = True)
