#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, send_file
from minimap import write_minimap

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10024 * 1024


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        write_minimap(uploaded_file.filename)
        return send_file(f'minimap_{uploaded_file.filename[:-4]}.png', attachment_filename=f'minimap_{uploaded_file.filename[:-4]}.png')
    return redirect(url_for('index'))
