from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculator', methods=['POST', 'GET'])
def calculator():
    number1 = int(request.form['number1'])

    if 'number2' in request.form:
        number2 = int(request.form['number2'])
    else:
        number2 = 0

    operation = request.form['operation']

    if operation == 'math':
        total = number1 + number2
    elif operation == 'sub':
        total = number1 - number2
    elif operation == 'mult':
        total = number1 * number2
    elif operation == 'power':
        total = math.pow(number1, number2)
    elif operation == 'square_root':
        total = math.sqrt(number1)
    elif operation == 'logarithm':
        total = math.log10(number1)
    else:
        if number1 == 0 or number2 == 0:
            return "Voce nao pode fazer divisao por 0"

        total = number1 / number2

    return str(total)


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
