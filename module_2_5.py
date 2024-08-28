# Домашняя работа по уроку "Функции в Python.Функция с параметром"
# Задача "Матрица воплоти":

def get_matrix (n, m, value):
    matrix = []
    for i in range (n):
        a = []
        for j in range (m):
            a.append(value)
        matrix.append(a)
    return matrix

result1 = get_matrix(2,2, 10)
result2 = get_matrix(3,5, 42)
result3 = get_matrix(4,2, 13)
print (result1)
print (result2)
print (result3)

