from grafo import *

class Aplicacion:
    def __init__(self):
        self.matriz = None
        self.grafo = None
        self.ventana = Tk()
        self.nodos = []
        self.formMatriz = None
        self.ventana.geometry("650x550")
        self.ventana.title("Problema del camino mínimo")
        self.ventana.config(background="#FFFFFF")
        self.configurar_componentes()

    def configurar_componentes(self):
        # codigo para centrar la ventana principal
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        # creación de labels, botones y entrys
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
        self.btnMatrizManual.place(x=250, y=130)

        self.btnVerGrafo = Button(self.ventana, text="Ver Grafo", command=self.ver_grafo, width="20", height="2")
        self.btnVerGrafo.place(x=450, y=130)

        self.nodo1_label = Label(text="Nodo inicial", font=("Arial", 12))
        self.nodo1_label.place(x=50, y=200)
        self.nodo1 = StringVar()
        self.nodo1entry = Entry(textvariable=self.nodo1, width="8")
        self.nodo1entry.place(x=50, y=230)

        self.nodo2_label = Label(text="Nodo final", font=("Arial", 12))
        self.nodo2_label.place(x=150, y=200)
        self.nodo2 = StringVar()
        self.nodo2entry = Entry(textvariable=self.nodo2, width="8")
        self.nodo2entry.place(x=150, y=230)

        self.btnCamino = Button(self.ventana, text="Hallar camino mínimo", command=self.camino_minimo, width="20", height="2")
        self.btnCamino.place(x=250, y=200)


    def crear_matriz(self):
        #try:
            self.numero_nodo = int(self.numero_entry.get())
            if self.numero_nodo < 5 or self.numero_nodo > 15:
                mb.showerror("Error", "Ingrese un numero entre 5 y 15")
            else:
                self.matriz = generar_matriz(self.numero_nodo, False)
                print(self.matriz)
                self.ver_matriz()
        #except:
            mb.showerror("Error", "Texto no válido")

    def ingresar_matriz(self):
        try:
            self.numero_nodo = int(self.numero_entry.get())
            if self.numero_nodo < 5 or self.numero_nodo > 15:
                mb.showerror("Error", "Ingrese un numero entre 5 y 15")
            else:
                self.ventana.iconify()
                self.matriz = generar_matriz(self.numero_nodo, True)
                self.ventana.deiconify()
                print(self.matriz)
                self.ver_matriz()
        except:
            mb.showerror("Error", "Texto no válido")


    def ver_matriz(self):
        # crear grafo a partir de la matriz
        self.nodos = [i for i in range(0, self.numero_nodo)]
        self.grafo = Grafo(self.matriz, self.nodos)

        # crear ventana para mostrar la matriz
        self.formMatriz = Tk()
        self.formMatriz.title("Matriz")
        self.formMatriz.resizable(False, False)

        # crear etiquetas para los encabezados de columnas
        for j in range(len(self.matriz)):
            label = Label(self.formMatriz, text=f"{j}")
            label.grid(row=0, column=j+1)

        # crear etiquetas para los encabezados de filas y valores
        for i in range(len(self.matriz)):
            # encabezado de la fila
            label = Label(self.formMatriz, text=f"{i}")
            label.grid(row=i+1, column=0)

            # valores de la matriz
            for j in range(len(self.matriz[i])):
                entry = Entry(self.formMatriz, width=8)
                entry.insert(0, str(self.matriz[i][j]))
                entry.grid(row=i+1, column=j+1)
        
        self.formMatriz.mainloop()

    def ver_grafo(self):
        if self.grafo != None:
            self.grafo.mostrar_grafo()
        else:
            mb.showerror("Error", "Debe crear una matriz")
    
    def camino_minimo(self):
        try:
            self.nodo1 = int(self.nodo1entry.get())
            self.nodo2 = int(self.nodo2entry.get())
        except:
            self.nodo1 = self.nodo1entry.get()
            self.nodo2 = self.nodo2entry.get()
            
        if self.grafo != None:
            if self.nodo1 in self.nodos and self.nodo2 in self.nodos:
                if self.nodo1 != self.nodo2:
                    try:
                        min_path, distancia = self.grafo.dijkstra(self.nodo1, self.nodo2)
                        print(min_path, distancia)
                        camino = [(min_path[i], min_path[i+1]) for i in range(len(min_path)-1)]
                        mb.showinfo("Camino mínimo", f"El camino mínimo es: {min_path}\nLa distancia es: {distancia}")
                        self.grafo.mostrar_grafo(camino)
                    except:
                        mb.showinfo("Camino mínimo", f"No existe un camino entre {self.nodo1} y {self.nodo2}")
                else:
                    mb.showerror("Error", "El nodo inicial y final deben ser diferentes")
            else:
                mb.showerror("Error", "Debe ingresar los nodos de inicio y fin")
        else:
            mb.showerror("Error", "Debe crear una matriz")

    def ejecutar(self):
        self.ventana.mainloop()

home = Aplicacion()
home.ejecutar()