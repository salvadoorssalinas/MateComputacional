from grafo import *

if __name__ == "__main__":
    while True:
        n = input("Ingrese el numero de nodos (5, 15): ")
        try:
            n = int(n)
            if 5 <= n <= 15: break
            else: print("ERROR: Fuera de rango. Ingrese nuevamente")
        except:
            print("ERROR: Entrada no válida. Ingrese nuevamente.")

    while True:
        manual = input("¿Desea ingresar los valores de la matriz? (s/n): ")
        manual = manual.lower()

        if manual == "s":
            manual = True
            break
        elif manual == "n":
            manual = False
            break

    matriz = generar_matriz(n, manual)
    print(matriz)

    custom_values = input("¿Desea utilizar valores personalizados para los nodos? (s/n): ")

    valores_nodos = []

    if custom_values.lower() == 's':
        for i in range(0, n):
            while True:
                v = input(f"Ingrese el valor personalizado para el nodo {i}: ")
                try:
                    valor = int(v)
                except:
                    valor = v.upper()

                if valor not in valores_nodos:
                    valores_nodos.append(valor)
                    break
                else:
                    print("ERROR: Valor ya ingresado. Ingrese uno diferente.")
    else:
        valores_nodos = [i for i in range(0, n)]
    
    grafo = Grafo(matriz, valores_nodos)

    grafo.mostrar_grafo()

    while True:
        i = input("Ingrese el nodo de inicio: ")
        f = input("Ingrese el nodo de fin: ")
        try:
            inicio = int(i)
            fin = int(f)
        except:
            inicio = i.upper()
            fin = f.upper()

        if inicio in valores_nodos and fin in valores_nodos and inicio != fin:  # Validación actualizada
            break
        else: print("ERROR: Valores no encontrados o fuera de Rango. Ingrese nuevamente.")
        
    if grafo.dijkstra(inicio, fin) == None:
        print("No existe un camino")
    else:
        camino, distancia = grafo.dijkstra(inicio, fin)
        print(f"Camino mínimo: {camino}, Distancia: {distancia}")
        min_path = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]
        grafo.mostrar_grafo(min_path)
    