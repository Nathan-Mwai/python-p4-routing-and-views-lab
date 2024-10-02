#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    number_display = f""
    for i in range(parameter):
        number_display += f"{i}\n"
    return number_display

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        soln =  num1 + num2
    elif operation == '-':
        soln = num1 - num2
    elif operation == '*':
        soln = num1 * num2
    elif operation == 'div':
        soln = num1 / num2
    elif operation == '%':
        soln = num1 % num2
    else:
        return 'invalid format'
    return str(soln)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
