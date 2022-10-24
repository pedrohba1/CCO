import numpy as np

# mesma matriz que tem nas aulas
matriz = np.array([
     [5,2,3,2],
    [1,5,1,1],
    [2,3,2,4]
]).astype(float)



def pivota(La, Lb,  numerand, pivot):
    Lb = np.array(Lb) - ((numerand/pivot)* np.array(La)) 
    return Lb

def aplicaLinha(matrix, a,b):
    return pivota(matrix[a], matrix[b], matrix[b][a], matrix[a][a])

def jordan(m):
        m = np.copy(m)
        l2 = aplicaLinha(m,0,1)
        l3 = aplicaLinha(m,0,2)
        m[1] = l2
        m[2] = l3
        m[2] = aplicaLinha(m,1,2)
        m[1] = aplicaLinha(m,2,1)
        m[0] = aplicaLinha(m,1,0)
        m[1] = aplicaLinha(m,0,1)
        m[0] = aplicaLinha(m,2,0)
        m[1] = aplicaLinha(m,2,1)
        
        return m


r = jordan(matriz)
print(r)
x1 = r[0][3]/ r[0][0]
x2 = r[1][3]/ r[1][1]
x3 = r[2][3]/ r[2][2]

print("x1 é {}".format(x1))
print("x2 é {}".format(x2))
print("x3 é {}".format(x3))


