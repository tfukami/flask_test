# coding: utf-8
from flask import Flask, request, render_template, redirect, escape, Markup, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', sentence='Flask-test')

@app.route('/getSentence/<string:sentence>', methods=['GET'])
def get_sentence(sentence):
    return render_template('index.html', sentence=sentence)

@ app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
