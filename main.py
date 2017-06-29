from flask import Flask, redirect, url_for, request, render_template, send_file
import os

app = Flask(__name__)
app.config['uploadfolder'] = '/uploadfolder'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/network')
def network():
    return render_template('network.html')

@app.route('/newsletter', methods=['GET', 'POST'])
def download():
    filename = 'WIPA-Newsletter-FEB2017.pdf'
    return send_file(filename, attachment_filename='FEB2017WIPA.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)