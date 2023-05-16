m2 = [[9,3],
     [8,4],
     [5,7]]


m1 = [[9,7,3],
     [8,2,6]]

#O(n^3)

def MatrizMult(m1, m2):

    if len (m1[0]) == len (m2):

        tercerM = []
        for recorridoA in range(len(m1)):
            tercerM.append([])
            for recorridoB in range(len(m2[0])):
                tercerM[recorridoA].append(0)

        for multA in range (len(m1)):
            for multB in range(len(m2[0])):
                for creacionTercer in range(len(m1[0])):
                    tercerM[multA][multB] += m1[multA][creacionTercer] * m2[creacionTercer][multB]
        return creacionTercer
    else: 
        return None

result = MatrizMult(m1, m2)

if result == None:
    print("Error, matriz no es correcta")
else:
    for fila in result:
        print(fila, end=" ")
        for element in fila:
            print(element)