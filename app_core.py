import numpy
import multiprocessing

def factorial(n):
    if n==1:
        return 1
    else:
        return factorial(n-1) * n
        

def multiplicacion(lista_n):
    mult = 1
    for num in lista_n:
        mult = mult * num
    return mult

def main():
    n = 10
    lista_numeros = [2, 4, 6, 10, 5]
    print(f"Calculando el factorial de {n}")
    factorial_value = factorial(n)
    print(f"Calculando la multiplicacion de {lista_numeros}")
    mult_value = multiplicacion(lista_numeros)
    
    task_1 = multiprocessing.Process(target=factorial, args = ([n]))
    task_2 = multiprocessing.Process(target = multiplicacion, args=[lista_numeros])

    task_1.start()
    task_2.start()

    task_1.join()
    task_2.join()

    print(f"Resultado del factorial: {factorial_value}")
    print(f"Resultado de la multiplicacion: {mult_value}")
    print(f"Tareas completadas")

if __name__ == '__main__':
    main()