# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante= ((b ** 2) - (4 * a * c))

    if discriminante >= 0:
        r1 = (-b + (discriminante ** 0.5)) / (2 * a)
        r2 = (-b - (discriminante ** 0.5)) / (2 * a)
        if r1==r2:
            return f"({r1})"
        elif r1 != r2:
            return f"({r1}, {r2})"
    else:
        return "( )"


def value_y(a, b, c, x):

    valor= a * x**2 + b * x + c
    return valor


def to_string(a, b, c):

    if a==0 and b==0 and c==0:
        funcion= f"f(x)= 0"
    elif a==0 and b == 0:
        funcion= f"f(x) = {c}"
    elif a==0 and c==0:
        funcion= f"f(x) = {b} * X"
    elif b==0 and c==0:
        funcion= f"f(x) = {a} * X^2"
    elif a==0:
        funcion= f"f(x) = {b} * X + {c}"
    elif b==0:
        funcion= f"f(x) = {a} * X^2 + {c}"
    elif c==0:
        funcion= f"f(x) = {a} * X^2 + {b} * X"
    elif a !=0 and b !=0 and c !=0:
        funcion= f"f(x) = {a} * X^2 + {b} * X + {c}"
    else:
        return "error"

    return funcion


def derivation(a, b, c):

    if a !=0:
        if b !=0:
            derivada= f"f'(x) = {a*2} * X + {b}"
        elif b==0:
            derivada= f"f'(x) = {a*2} * X"
    elif a ==0:
        if b !=0:
            derivada= f"f'(x) = {b}"
        elif b ==0:
            derivada= f"f'(x) = 0"
