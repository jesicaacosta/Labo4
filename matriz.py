matrix = [
         [2,4,5,8],
         [6,3,1,9]
]
# print(type(matrix))
# print('Matrix original ',matrix)

# matrix[1][0] = 15
# print('Cambiado por otro int' , matrix)

# matrix[1][0] = 'String'
# print('Cambiado por string ' , matrix)

# matrix[1][0] = 23.65
# print('Cambiado por float ', matrix)


# #funcion que sirve para todas las matrices que quiero inicializar
# # ya que les puedo otorgar tamaños y valores iniciales
# def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:str) -> list:
#          matriz = []
#          for i in range (cantidad_filas):
#                   fila = [valor_inicial] *cantidad_columnas
#                   matriz += [fila]
#          return matriz

# #matriz con dos filas, 4 columnas, valores cargados 0
# mi_matriz = inicializar_matriz(2,4,0) 
# print(mi_matriz)

# mi_matriz1 = inicializar_matriz(2,2,'i') 
# print(mi_matriz1)


# print('--- CARGA SECUENCIAL ---')

# matrix2 = [
#          [22,43,45,18],
#          [61,43,51,79]
# ]

# def cargar_matriz_secuencialmente(matrix2: list): #matrix:list indica que matrix debe ser una lista.
#     for i in range(len(matrix2)):  # Recorre las filas de la matriz
#         for j in range(len(matrix2[i])):  # Recorre las columnas de la matriz
#             matrix2[i][j] = int(input(f'Fila {i} Columna {j}: '))  # Asigna el valor ingresado

# cargar_matriz_secuencialmente(matrix2) 

# matrix3 = [
#          ["apple", "banana", "cherry", "date"],
#          ["elephant", "fox", "giraffe", "horse"],
#          ["ice", "juice", "kiwi", "lemon"],  # Nueva lista 1 con strings
#          ["moon", "nest", "owl", "penguin"]  # Nueva lista 2 con strings
# ]


# matrix2 = []
# print(matrix2)
# def cargar_matriz_aleatoriamente (matrix2:list):
# # Agregar las validaciones/retorno que sean necesarias
#          seguir = "S"
#          while seguir == "S":
#                   fila = int(input("Indice de fila: "))
#                   columna = int(input("Indice de columna: ")) 
#                   dato = int(input("Ingrese el número a cargar: "))
#                   matrix2[fila][columna] = dato
#                   seguir = input("Desea seguir cargando? S/N: ")

# cargar_matriz_aleatoriamente(matrix2)


# def buscar_valor (matriz:list, valor: int) :
#          for i in range(len(matriz)):
#                   for j in range(len(matriz[i])):
#                                     if matriz[i][j] == valor:
#                                              print(f'Encontrado en fila {i} clumna {j}')
#                                     else:
#                                              print("no encontrado")
                                             
                  
#RESULTANTE:  
#PRODUCTO ESCALAR: 
                          
# buscar_valor(matrix, 9)

#suma de matrices 
#matriz resulatdnte: creo una nueva matriz para no perder ninguna de las matrices  originales 

#multiplicacion de matrices 
#porque la resultante es menor que las matrizA * matrizB 



