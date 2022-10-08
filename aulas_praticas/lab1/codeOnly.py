
import math


# esse aqui é o arquivo com o código completo
# é o mesmo código do jupyter notebook.

def pondera(a,b,x1,x2, f):
    if f(x1) * f(x2) >0 and f(a)* f(x1) <0:
        return (a*abs(f(b)) + b*abs(f(a)/2))/ (abs(f(b)) + abs(f(a)/2)) 
    elif f(x1) * f(x2) >0 and f(a)* f(x1) >=0:
        return (a*abs(f(b)/2) + b*abs(f(a)))/ (abs(f(b)/2) + abs(f(a)))
    else: 
        return (a*abs(f(b)) + b*abs(f(a)))/ (abs(f(b)) + abs(f(a))) 


def FPM(a,b,err, func):
    iterations = 1
    maxIterations = 1000
    
    apply = True
        
    # condições de aplicação:
    # f(a0) < 0
    # f(b0) > 0
    # f(a)*f(b) <0
    # se algum dos dois for falso, não continua
    
    if (func(a) >= 0):
        apply = False
    if (func(b) <= 0):
        apply = False
    if (func(a) * func(b) >= 0):
        apply: False
    

           
    x1 = pondera(a,b,1,1,func)
    if abs(func(x1)) <= err:
        print("intervalo {}-{}  raíz encontrada: {}".format(a, b,x1))
        return a,b,x1

    
    # definição do primeiro intervalo
    if func(a) * func(x1) < 0:
        b = x1
    else: a = x1
    
    x2 = pondera(a,b,x1,1, func)
    
    while apply:
        if iterations > maxIterations: 
            print("excedeu limite")
            return

        if abs(func(x2)) <= err:
            print("iteração final {}, intervalo [{:.3f}, {:.3f}] raíz: {:.3f}".format(iterations, a, b,x2))
            return a,b,x2

        if func(a) * func(x2) < 0:
            b = x2
        else: a = x2

        # definição de novo x
        x2 = pondera(a,b,x1,x2, func)

        print("iteração {}, intervalo [{:.3f}, {:.3f}] x2: {:.3f}".format(iterations, a, b,x2))
        iterations +=1
            
    return x1



# O usuário pode construir o polinômio, mandar o intervalo e a tolerância direto para 
# a função FPM para calcular a raíz usando o método regula falsi modificado

a0 = 2
b0 = 3
err = 0.002


def P(x):
    return 3*(x**5) +x -5

result = FPM(a0,b0,err,P)
print(result)