#!/usr/bin/env python
#-*- coding: utf-8 -*-
from os import path
from flask import Flask, render_template, request, redirect, url_for
from static import minimap

app = Flask(__name__)
json_filename = 'recs_info.json'

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

def json_crud(json_filename):
    if not path.exists(json_filename):
        create_new_file()
    try:
        data = read_file(json_filename)
    except:
        print('\nError\n¡Archivo dañado!\n')

def read_file(json_filename):
    """Reads a json file"""
    with open(json_file_name) as json_data:
        data = json.load(json_data)
    return data

def write_to_file():
    """Creates a json file"""
    with open(json_file_name, 'w') as outfile:
        json.dump(data, outfile)

def create_new_file(json_filename):
    json_data = open(json_filename, 'w')
    write_to_file()
    json_data.close()

if __name__ == '__main__':
    json_crud(json_filename)
    app.run(debug = True)
