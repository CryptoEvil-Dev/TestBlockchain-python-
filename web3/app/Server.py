import json
from flask import Flask, render_template, redirect, request, url_for
from block import *
import re

app = Flask(__name__)


@app.route('/check')
def checktransaction():
    return render_template('CheckTransaction.html', block=Check_Blocks())

@app.route('/send/<string:name>/<int:amount>')
def send_token(name, amount):
    Add_Block('DNDSCAN',amount, name)
    return redirect('/check')

@app.route('/send', methods=['POST', 'GET'])
def send():

    if request.method == 'POST':
        n = request.form['name']
        a = request.form['amount']
        Add_Block('DNDSCAN', a, n)
        return redirect('/')

    return render_template('send.html')

@app.route('/')
def main_block():
    files = Show_Blocks()
    from_b = []
    amount_b = []
    to_b = []
    hash_b = []
    date_b = []

    for file in files:
        f = open('Blockchain/' + str(file))
        hash_b.append(json.load(f)['HASH'])
    for file in files:
        f = open('Blockchain/' + str(file))
        amount_b.append(json.load(f)['AMOUNT'])
    for file in files:
        f = open('Blockchain/' + str(file))
        from_b.append(json.load(f)['FROM'])
    for file in files:
        f = open('Blockchain/' + str(file))
        to_b.append(json.load(f)['TO'])
    for file in files:
        f = open('Blockchain/' + str(file))
        date_b.append(json.load(f)['DATE'])

    return render_template('main.html', id_b=files, from_b=from_b, amount_b=amount_b,to_b=to_b, hash_b = hash_b, time_b=date_b)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.40', port=8545)
