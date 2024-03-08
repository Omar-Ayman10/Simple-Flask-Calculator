from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def Calculator():
    return render_template('calculator.html')

@app.route('/calculator', methods=['POST'])
def Calculate():
    result = None
    try:
        first_number = float(request.form['first_number'])
        second_number = float(request.form['second_number'])
    except Exception as exception:
        result = "Enter two numbers!"
        return render_template('calculator.html', result=result)
    
    operation = request.form['operation']

    if operation == "Add":
        result = first_number + second_number
    elif operation == "Subtract":
        result = first_number - second_number
    elif operation == "Multiply":
        result = first_number * second_number
    elif  operation == "Divide":
        if second_number == 0:
            result = "Undefined."
        else:
            result = first_number / second_number
    else:
        return "Invalid operation."
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True) 