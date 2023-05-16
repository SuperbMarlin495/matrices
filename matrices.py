a = [[1,2,3],
     [4,5,6]]

b = [[1,2],
     [3,4],
     [5,6]]

def multiplicacion_Matriz(a, b):

    if len (a[0]) == len (b):

        c = []
        for i in range(len(a)):
            c.append([])
            for j in range(len(b[0])):
                c[i].append(0)

        for i in range (len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    else: 
        return None

matriz = multiplicacion_Matriz(a, b)

if matriz == None:
    print("No se puede multiplicar matriz")
else:
    print("La matriz a: ", a)
    print("La matriz b: ", b)
    for fila in matriz:
        print("[", end=" ") 
        for element in fila:
            print(element, end=" ")
        print("]")



# El algoritmo es de orden: O(n^3)