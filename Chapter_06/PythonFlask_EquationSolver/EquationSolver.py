"""
      Content under Creative Commons Attribution license CC-BY 4.0, 
      code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

      http://en.wikipedia.org/wiki/MIT_License
      http://creativecommons.org/licenses/by/4.0/

      Created on april, 2018
      Last Modified on: may 15, 2018

"""
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    theEquation = 'a*x + b = c*x + d '
    numero = '0'
    theTerm = '0'
    theVar = 'x'
    oldEquation = theEquation
    if request.method == 'POST':
        theEquation = request.form['theEquation']
        numero = request.form['numero']
        theTerm = request.form['theTerm']
        theVar = request.form['theVar']
        try:
           from EquationSolver_funcs import newEq
           oldEquation = theEquation
           theEquation = newEq(theEquation, int(numero), theTerm, theVar)
           numero = ['                            ',
              ' add to both sides of that equation the term', 
              ' subtract from both sides of that equation the term', 
              ' multiply both sides of that equation by the term', 
              ' divide both sides of that equation by the term',
              ' to show the solution of that equation'][int(numero)]
        except Exception as errorCapturado:
           theTerm = " *** SOMETHING IS WRONG. PLEASE, TRY AGAIN ***  "
    return render_template('index.html', oldEquation=oldEquation, theEquation=theEquation, numero=numero, theTerm=theTerm, theVar=theVar)

if __name__ == '__main__':
    app.run(debug=True)

