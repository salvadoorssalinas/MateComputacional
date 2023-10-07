from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from grafo import *

# variables goblales
class Aplicacion:
    def __init__(self):
        self.matriz = None
        self.grafo = None
        self.ventana = Tk()
        self.ventana.geometry("650x550")
        self.ventana.resizable(False, False)
        self.ventana.title("Problema del camino mínimo")
        self.ventana.config(background="#FFFFFF")
        self.agregar_componentes()
    
    def agregar_componentes(self):
        self.titulo = Label(text="Problema del Camino Minimo", font=("Arial", 32))
        self.titulo.place(x=0, y=0)

        self.numero_nodo_label = Label(text="Ingrese n (5 - 15):", font=("Arial", 12))
        self.numero_nodo_label.place(x=22, y=70)
        self.numero_nodo = StringVar()
        self.numero_entry = Entry(textvariable=self.numero_nodo, width="8")
        self.numero_entry.place(x=22, y=100)

        self.btnMatrizRandom = Button(self.ventana, text="Crear matriz aleatoria", command=self.crear_matriz, width="20", height="2")
        self.btnMatrizRandom.place(x=50, y=130)

        self.btnMatrizManual = Button(self.ventana, text="Ingresar matriz", command=self.ingresar_matriz, width="20", height="2")
        self.btnMatrizManual.place(x=200, y=130)

        self.btnVerGrafo = Button(self.ventana, text="Ver Grafo", command=self.ver_grafo, width="20", height="2")
        self.btnVerGrafo.place(x=350, y=130)

    def crear_matriz(self):
        try:
            self.numero_nodo = int(self.numero_entry.get())
            if self.numero_nodo < 5 or self.numero_nodo > 15:
                mb.showerror("Error", "Ingrese un numero entre 5 y 15")
            else:
                self.matriz = generar_matriz(self.numero_nodo, False)
                print(self.matriz)
                dibujar_matriz(self.matriz)
        except:
            mb.showerror("Error", "Texto no válido")
    
    def ingresar_matriz(self):
        try:
            self.numero_nodo = int(self.numero_entry.get())
            if self.numero_nodo < 5 or self.numero_nodo > 15:
                mb.showerror("Error", "Ingrese un numero entre 5 y 15")
            else:
                self.ventana.withdraw()
                self.matriz = generar_matriz(self.numero_nodo, True)
                self.ventana.deiconify()
                print(self.matriz)
                dibujar_matriz(self.matriz)
        except:
            mb.showerror("Error", "Texto no válido")


    def ver_grafo(self):
        if self.matriz.all != None:
            self.grafo = Grafo(self.matriz, [i for i in range(0, self.numero_nodo)])
            self.grafo.mostrar_grafo()
        else:
            mb.showerror("Error", "Debe crear una matriz")

    def ejecutar(self):
        self.ventana.mainloop()

home = Aplicacion()
home.ejecutar()