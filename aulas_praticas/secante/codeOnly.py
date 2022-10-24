import math

def g(x0, x1, f):
    return (x0 * f(x1) - x1 *f(x0))/ (f(x1) - f(x0)) 


def parada1(f,xk, erro):
    if abs(f(xk)) <= erro: return 1
    else: return 0


def parada2(xkPlus1,xk, erro):
    if abs((xkPlus1 - xk) / xkPlus1 )  <= erro: return 1
    else: return 0


# a função inteira é passada como parâmetro
def metSecante(func,x0,x1,erro):
    if func(x0) > 0:
        apply = True
    elif func(x1) > 0:
        apply = True
    else: 
         raise Exception("x0 invalido")
    xk= g(x0,x1,func)
    xkMinus1 = x1
    print(xk)
    iter = 1
    while apply:
        if parada1(func, xk, erro) == 1:
            apply = False
            print("raíz: {}, iterações: {}".format(xk,iter ))
            return xk
        if (parada2(xk, xkMinus1, erro)) == 1:
            apply = False
            print("raíz: {}".format(xk))
            return xk
        if iter > 500: 
            print("excedeu limite")
            return -1
        xkPlus1 = g(xkMinus1, xk,func)
        xkMinus1 = xk
        xk = xkPlus1
        iter+=1


# a função do parametro
def P2(x):
    return (x**3) -x -1


erroPX = 0.002
result = metSecante(P2, 1.5, 1.7, erroPX)


# outro exemplo:

def P3(x):
    return x*math.log(x,10) -1



a0 = 2
b0 = 3
err = 0.002

metSecante(P3, a0,b0, err)