# coding: utf-8
from flask import Flask, request, render_template, redirect, escape, Markup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('127.0.0.1', 8000, debug=True)
