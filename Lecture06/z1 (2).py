
## Некоторые начальные данные
a = -3
b = 2
def Line(x): return 2*x
def Parabola(x): return x**2
#############################

# Высчитывает производную в точке x от функции func -- имя функции.
def Def(func, x):
        eps = 10**(-5) ## Точность производной
        return (func(x+eps)-func(x))/(eps)

def Extremum(func, a, b):
    step = 10**(-3)## Точность

    X_value = [ii*step for ii in range(int(a/step),int(b/step))]
    extr = [ii for ii in X_value if (Def(func, ii - step)*Def(func, ii) < 0)]

    if extr == []:
       print(None)
    else:
       type_extr = ["min" if Def(func, Def(func, ii)) > 0 else "max" for ii in extr]
       [print(f"Для функции есть точка {extr[ii]} с погрешностью {step} -- это экстремум ({type_extr[ii]})") for ii in range(len(extr))];
    

Extremum(Line, a, b)
Extremum(Parabola, a, b)