# -*- coding: utf-8 -*-

from __future__ import with_statement
from flask import Flask, request, url_for, redirect, \
    render_template

a = None
b = None
c = None
cal = None

# create our little application :)
app = Flask(__name__)

@app.route('/memo1')
def memo1():
    return render_template('memo1.html')

@app.route('/memo2')
def memo2():
    return render_template('memo2.html')

@app.route('/memo3')
def memo3():
    return render_template('memo3.html')

@app.route('/calcul', methods=['POST'])
def calcul():
    global a
    global b
    global c
    global cal

    if a is not None and b is not None:
        if cal == '+':
            c = str(float(a) + float(b))
        elif cal == '-':
            c = str(float(a) - float(b))
        else:
            cal = None
    return render_template('calcul.html', num=a, num2=b, num3=c, cal=cal)

@app.route('/calcul2', methods=['POST'])
def calcul2():
    global a
    global b
    global cal

    if 'plus' in request.form:
        cal = '+'
    elif 'minus' in request.form:
        cal = '-'
    elif 'mul' in request.form:
        cal = '*'
    elif 'div' in request.form:
        cal = '/'
    else:
        cal = None

    if request.method == 'POST':
        if request.form['num']!='' and request.form['num2']!='':
            a = request.form['num']
            b = request.form['num2']
            return redirect(url_for('sessions'))
        else:
            a = request.form['num']
            b = request.form['num2']
            if a =='':
                if b =='':
                    a = None
                    b = None
                else:
                    a = None
            else:
                b = None
            return redirect(url_for('calcul'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')