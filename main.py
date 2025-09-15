# Computation of the Area of a Trapezoid
from pyscript import display, document

def area_of_a_trapezoid(e):
    document.getElementById('output').innerHTML = ""
    a = float(document.getElementById('a').value)
    b = float(document.getElementById('b').value)
    h = float(document.getElementById('h').value)
    area = ((a + b) / 2) * h
        
    display(f'The area of a trapezoid with bases {a} & {b} and height {h} is {area}', target='output')