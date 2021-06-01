#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json, os
from os import path
from werkzeug.utils import secure_filename
#.#.#
from flask import Flask, render_template, request, redirect, url_for, jsonify
#.#.#
from static import minimap

app = Flask(__name__)
data = list()
json_filename = 'recs_info.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return jsonify(data)

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        info_json = minimap.write_minimap(uploaded_file.filename)
        info_json['minimap'] = f'static/minimap_{info_json["nombre_archivo"][:-4]}.png'
        write_to_file(json_filename, data, info_json)
        pov = secure_filename(info_json["punto_de_vista"])
        os.rename(uploaded_file.filename,f'./recs/{pov}_{uploaded_file.filename}')
    return render_template('generated.html', 
                            filename=uploaded_file.filename,
                            source='minimap_'+uploaded_file.filename[:-4]+'.png', 
                            info_json=info_json)

def json_crud(json_filename):
    """init the json file.
    Si el archivo no existe, se creará.
    Si el archivo existe, se intentará abrir.
    Si el archivo está dañado, se hará un backup
    del archivo dañado, y se creará un nuevo archivo.
    """
    if not path.exists(json_filename):
        data = create_new_file(json_filename)
        return data
    try:
        data = read_file(json_filename)
        return data
    except:
        print('\nError\n¡Archivo dañado!\n')
        import os
        os.rename(json_filename, json_filename+'_')
        return list()

def read_file(json_filename):
    """Reads a json file"""
    with open(json_filename) as json_data:
        data = json.load(json_data)
    return data

def write_to_file(json_filename, data, new_info):
    """Creates a json file"""
    if new_info:
        data.append(new_info)
    with open(json_filename, 'w') as outfile:
        json.dump(data, outfile)

def create_new_file(json_filename):
    """Creates a 'recs_info.json' file"""
    data = list()
    json_data = open(json_filename, 'w')
    write_to_file(json_filename, data, '')
    json_data.close()
    return data

def init_folders():
    if not path.exists('recs'):
        os.mkdir('recs')

if __name__ == '__main__':
    data = json_crud(json_filename)
    init_folders()
    app.run(debug = True)
