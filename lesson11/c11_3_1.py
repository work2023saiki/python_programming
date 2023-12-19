"""Flaskの実行"""
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'わんわん'

def main():
    app.debug = False
    app.run(host='172.16.0.186', port=5000)

if __name__ == '__main__':
    main()