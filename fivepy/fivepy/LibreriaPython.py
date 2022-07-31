def Menu():
    import tkinter as tk
    from tkinter import ttk
    from PIL import Image, ImageTk
    Ventana = tk.Tk()
    Ventana.title("Menu")
    Ventana.geometry("1300x800")

    I = ["Imagenes\\555.png", "Imagenes\\741.png", "Imagenes\\Fondo4"]

    t = ["CIRCUITO\nINTEGRAD0\n555", "AMPLIFICADOR\nOPERACIONAL\n741","CREDITOS"]

    T = "MENU DE CIRCUITOS INTEGRADOS"

    img = Image.open("Imagenes\Fondo3.jpg")
    img = img.resize((1300, 800), Image.ANTIALIAS)
    img_0 = ImageTk.PhotoImage(img, master=Ventana)
    tk.Label(Ventana, image=img_0, bd=0).pack()

    ver = 80
    hor = 300
    min = 175

    l1xn = 35
    l2xn = l1xn + hor
    l3xn = l2xn + hor
    l4xn = l3xn + hor
    entre2y3 = (l2xn + l3xn) // 2

    lnx1 = 0
    lnx2 = lnx1 + ver
    lnx3 = lnx2 + ver
    lnx4 = lnx3 + ver
    lnx5 = lnx4 + ver
    lnx6 = lnx5 + ver
    lnx7 = lnx6 + ver
    lnx8 = lnx7 + ver

    columna = [l1xn, l2xn, l3xn, l4xn, entre2y3]
    fila = [lnx1, lnx2, lnx3, lnx4, lnx5, lnx6, lnx7, lnx8]
    image = []

    x = 18
    y = 3
    f = "Arial 12"
    BG = '#26de57'
    FG = 'black'


    B1=tk.Button(Ventana, text=t[0], font=f, width=x, height=y, fg=FG, bg=BG, anchor=tk.CENTER,
                command=lambda: s(0)).place(x=columna[0], y=fila[2]+100)
    B2=tk.Button(Ventana, text=t[1], font=f, width=x, height=y, fg=FG, bg=BG, anchor=tk.CENTER,
                command=lambda: s(1)).place(x=columna[2], y=fila[2]+100)
    B3=tk.Button(Ventana, text=t[2], font=f, width=x, height=y, fg=FG, bg=BG, anchor=tk.CENTER,
                command=lambda: s(2)).place(x=columna[1]+200, y=fila[7])
    photo = Image.open(I[0]).resize((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(photo, master = Ventana) 
    tk.Label(Ventana, image = photo, bg="#8ee6a6").place(x=columna[0]+min, y=fila[1]+100)
    #####
    photo1 = Image.open(I[1]).resize((300, 300), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(photo1, master = Ventana) 
    tk.Label(Ventana, image = photo1, bg="#8ee6a6").place(x=columna[1]+500, y=fila[1]+100)

    def s(circuito):
        if circuito == 0:
            Menu0()
        elif circuito == 1:
            Menu1()
        elif circuito == 2:
            creditos()
    title = tk.Label(Ventana, text=T, font="Arial 23 bold", fg='#664300', bg='#ffff94',  width=45, height=1)
    title.place(x=entre2y3-300, y=lnx1+15)
    exit = tk.Button(Ventana, text='SALIDA', font="Arial 13", fg='black', bg='yellow',
                      width=10, height=2, command=Ventana.quit)
    exit.place(x=l4xn+200, y=lnx1+20)

    Ventana.resizable(width=False, height=False)
    tk.mainloop()  

def Menu0():
    import tkinter as tk
    from tkinter import ttk
    from PIL import Image, ImageTk
    Ventana = tk.Tk()
    Ventana.title("Menu")
    Ventana.geometry("1300x800")

    I = ["Imagenes\\1_MONOESTABLE.png", "Imagenes\\2_ASTABLE.png", "Imagenes\\3_REBOTE.png",
         "Imagenes\\4_CONTACTO.png", "Imagenes\\5_TEMPORIZADOR.png",
         "Imagenes\\6_CASCADA.png", "Imagenes\\7_INTERVALOMETRO.png",
         "Imagenes\\8_DETECTOR.png", "Imagenes\\9_ALARMA.png",
         "Imagenes\\10_DIVISOR.png", "Imagenes\\11_OSCILADOR.png",
         "Imagenes\\12_PULSO.png", "Imagenes\\13_FRECUENCIOMETRO.png",
         "Imagenes\\14_METRONOMO.png", "Imagenes\\15_JUGUETE.png",
         "Imagenes\\16_CERRADO.png", "Imagenes\\17_CHIRP.png",
         "Imagenes\\18_TONOS.png", "Imagenes\\19_TRESESTADOS.png",
         "Imagenes\\20_RAFAGA.png",
         "Imagenes\\21_EFECTOS.png", "Imagenes\\22_INTERMITENTE.png",
         "Imagenes\\23_FET.png", "Imagenes\\24_OSCURIDAD.png",
         "Imagenes\\25_INFRARROJO.png", "Imagenes\\26_TRANSMISOR.png",
         "Imagenes\\27_RECEPTOR.png", "Imagenes\\28_CONVERTIDOR.png"]

    t = ["#1: MONOESTABLE\nBASICO", "#2: ASTABLE\nBASICO", "#3: INTERRUPTOR\nSIN REBOTE",
         "#4: INTERRUPTOR\nACTIVADO\nPOR TOQUE", "#5: TEMPORIZADOR\nCON RELE",
         "#6: TEMPORIZADOR\nEN CASCADA", "#7: INTERVA-\nLOMETRO", "#8: DETECTOR\nDE PULSO\nFALTANTE",
         "#9: ALARMA DE\nFALLO DE\nEVENTO", "#10: DIVISOR DE\nFRECUENCIA",
         "#11: OSCILADOR DE\nCONTROL DE\nOLTAJE", "#12: GENERADOR\nDE PULSO", "#13: MEDIDOR DE\nFRECUENCIA",
         "#14: METRONOMO U\nOSCILADOR\nDE AUDIO", "#15: ORGANO DE\nJUGUETE", "#16: OSCILADOR\nCERRADO",
         "#17: GENERADOR DE\nCHIRRIDOS", "#18: GENERADOR\nDE TONOS", "#19: GENERADOR DE\nTONOS EN\n3 ESTADOS",
         "#20: GENERADOR\nDE RAFAGAS\nDE TONOS", "#21: GENERADOR\nDE EFECTOS\nDE SONIDO",
         "#22: lUZ INTER-\nMITENTE LED", "#23: REGULADOR DE\nPOTENCIA DE\nLAMPARA FET",
         "#24: DETECTOR DE\nLUZ Y\nOSCURIDAD", "#25: ALARMA DE\nSEGURIDAD POR\nINFRARROJO",
         "#26: TRANSMISOR\nANALOGICO DE\nONDAS DE LUZ", "#27: RECEPTOR\nANALOGICO DE\nONDAS DE LUZ",
         "#28: CONVERTIDOR\nDE DC A DC"]

    T = "MENU DE CIRCUITOS CON EL INTEGRADO 555"

    img = Image.open("Imagenes\Fondo2.jpg")
    img = img.resize((1300, 800), Image.ANTIALIAS)
    img_0 = ImageTk.PhotoImage(img, master=Ventana)
    tk.Label(Ventana, image=img_0, bd=0).pack()

    ver = 80
    hor = 300
    min = 175

    l1xn = 35
    l2xn = l1xn + hor
    l3xn = l2xn + hor
    l4xn = l3xn + hor
    entre2y3 = (l2xn + l3xn) // 2

    lnx1 = 0
    lnx2 = lnx1 + ver
    lnx3 = lnx2 + ver
    lnx4 = lnx3 + ver
    lnx5 = lnx4 + ver
    lnx6 = lnx5 + ver
    lnx7 = lnx6 + ver
    lnx8 = lnx7 + ver

    columna = [l1xn, l2xn, l3xn, l4xn, entre2y3]
    fila = [lnx1, lnx2, lnx3, lnx4, lnx5, lnx6, lnx7, lnx8]
    image = []

    x = 18
    y = 3
    f = "Arial 12"
    BG = 'orange'
    FG = 'black'

    def boton(numero, a, b):
        tk.Button(Ventana, text=t[numero], font=f, width=x, height=y, fg=FG, bg=BG, anchor="w",
                  command=lambda: s(numero)).place(x=columna[a], y=fila[b])

    def miniatura(numero, image, a, b):
        img1 = Image.open(I[numero])
        img1 = img1.resize((70, 70), Image.ANTIALIAS)
        image.append(ImageTk.PhotoImage(img1, master=Ventana))
        tk.Label(Ventana, image=image[numero]).place(x=columna[a] + min, y=fila[b])

    def s(circuito):
        if circuito == 0:
            monoestable()
        elif circuito == 1:
            astable()
        elif circuito == 2:
            rebote()
        elif circuito == 3:
            toque()
        elif circuito == 4:
            rele()
        elif circuito == 5:
            cascada()
        elif circuito == 6:
            intervalometro()
        elif circuito == 7:
            perdido()
        elif circuito == 8:
            alarma()
        elif circuito == 9:
            divisor()
        elif circuito == 10:
            voltaje()
        elif circuito == 11:
            pulsos()
        elif circuito == 12:
            frecuenciometro()
        elif circuito == 13:
            metronomo()
        elif circuito == 14:
            organo()
        elif circuito == 15:
            cerrado()
        elif circuito == 16:
            chirrido()
        elif circuito == 17:
            escalonado()
        elif circuito == 18:
            tres_estados()
        elif circuito == 19:
            rafaga()
        elif circuito == 20:
            sonido()
        elif circuito == 21:
            led()
        elif circuito == 22:
            lampara()
        elif circuito == 23:
            luz()
        elif circuito == 24:
            infrarrojo()
        elif circuito == 25:
            transmisor()
        elif circuito == 26:
            receptor()
        elif circuito == 27:
            convertidor()

    title = tk.Label(Ventana, text=T, font="Arial 23 bold", fg='#664300', bg='#ffff94',  width=45, height=1)
    title.place(x=entre2y3-300, y=lnx1+15)


    k = 0
    for j in [1, 2, 3, 4, 5, 6,7]:
        for i in [0, 1, 2, 3]:
            boton(k, i, j)
            miniatura(k, image, i, j)
            k += 1

    Ventana.resizable(width=False, height=False)
    tk.mainloop()


def monoestable():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.lines import Line2D
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  # reset the arrays
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,
        
    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)
    
    def animate():
        i=1
        j=1
        while i<=80:
            yield (1)
            i += 1 
        while True:
            yield (0)
    
    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,blit=True)
        canvas.draw()
        
    def pausar():
        ani.event_source.stop()

    def seleccion1():
        global seleccion_1
        seleccion_1 = combo.get()

    def seleccion2():
        global seleccion_2
        seleccion_2 = combo1.get()

    def seleccion11():
        global seleccion_11, valor11
        seleccion_11 = comboa.get()
        if seleccion_11 == "Kohm":
            valor11 = 1000
        if seleccion_11 == "Ohm":
            valor11 = 1
        if seleccion_11 == "Mohm":
            valor11 = 1e6

    def seleccion22():
        global seleccion_22, valor22
        seleccion_22 = combob.get()
        if seleccion_22 == "nF":
            valor22 = 1e-9
        if seleccion_22 == "pF":
            valor22 = 1e-12
        if seleccion_22 == "uF":
            valor22 = 1e-6

    def txt5():
        sum = f'{float(seleccion_1) * float(seleccion_2) * float(valor22) * float(valor11)} seg'
        txt6 = tkinter.Label(marco_principal, text=sum, font='Helvetica 13', width=25, height=1, bg='green', fg='#a0d995')
        txt6.place(x=l2xn, y=lnx4)

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\1_MONOESTABLE.png"
    I = "Imagenes\\1_MONOESTABLE1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640
    
    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)
    
    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    combo = ttk.Combobox(marco_principal, state="readonly",
                         values=["1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8",
                                 "8.2", "10", "12", "15",
                                 "18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180",
                                 "220", "270", "330", "390", "470", "510", "560", "680", "820"], width=15)
    combo.place(x=l1xn, y=lnx2)
    comboa = ttk.Combobox(marco_principal, state="readonly", values=["Ohm", "Kohm", "Mohm"], width=5)
    comboa.place(x=l2xn, y=lnx2)
    button = ttk.Button(marco_principal, text="Ingresar Datos",
                        command=lambda: [seleccion1(), seleccion11(), seleccion2(), seleccion22()])
    button.place(x=l1xn, y=lnx3)
    combo1 = ttk.Combobox(marco_principal, state="readonly",
                          values=["0.1", "0.12", "0.15", "0.18", "0.2", "0.22", "0.25", "0.27", "0.3", "0.39", "0.4",
                                  "0.47", "0.5", "0.56", "0.6", "0.68", "0.7", "0.8", "0.82", "1", "1.2", "1.5", "1.8",
                                  "2", "2.2", "2.5", "2.7", "3", "3.3", "3.9", "4", "4.7", "5",
                                  "5.6", "10", "12", "15", "18", "20", "22", "25", "27", "27", "30", "33", "39", "40",
                                  "47", "50", "56", "60", "68", "70", "80", "82", "100"], width=15)
    combo1.place(x=l3xn, y=lnx2)
    combob = ttk.Combobox(marco_principal, state="readonly", values=["pF", "nF", "uF"], width=5)
    combob.place(x=l4xn, y=lnx2)

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995',
                        command=iniciar)
    B1.place(x=l1xn, y=lnx1)
    
    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)
    
    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)
    
    B9 = tkinter.Button(marco_principal, text='Tiempo: ', width=15, height=1, bg='Orange', fg='#a0d995', command=txt5)
    B9.place(x=l1xn, y=lnx4)

    ventana.mainloop()


def astable():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import NW, ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  # reset the arrays
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=20:
            yield (1)
            i += 1 
        while j<=10:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
        

    def pausar():
        ani.event_source.stop()

    def seleccion1():
        global seleccion_1
        # Obtener la opción seleccionada.
        seleccion_1 = combo.get()
        print(seleccion_1)

    def seleccion2():
        global seleccion_2
        # Obtener la opción seleccionada.
        seleccion_2 = combo1.get()
        print(seleccion_2)

    def seleccion3():
        global seleccion_3
        # Obtener la opción seleccionada.
        seleccion_3 = combo2.get()
        print(seleccion_3)

    # ["Kohm", "Ohm", "Mohm"],
    def seleccion11():
        global seleccion_11, valor11
        # Obtener la opción seleccionada.
        seleccion_11 = comboa.get()
        if seleccion_11 == "Kohm":
            valor11 = 1000
        if seleccion_11 == "Ohm":
            valor11 = 1
        if seleccion_11 == "Mohm":
            valor11 = 1e6

    def seleccion22():
        global seleccion_22, valor22
        # Obtener la opción seleccionada.
        seleccion_22 = comboa1.get()
        if seleccion_22 == "Kohm":
            valor22 = 1000
        if seleccion_22 == "Ohm":
            valor22 = 1
        if seleccion_22 == "Mohm":
            valor22 = 1e6

    def seleccion33():
        global seleccion_33, valor33
        # Obtener la opción seleccionada.
        seleccion_33 = combob.get()
        if seleccion_33 == "nF":
            valor33 = 1e-9
        if seleccion_33 == "pF":
            valor33 = 1e-12
        if seleccion_33 == "uF":
            valor33 = 1e-6

    def txt5():
        tiempo1 = f'{0.693 * (float(seleccion_1) + float(seleccion_2)) * float(seleccion_3) * float(valor33) * float(valor22) * float(valor11)} seg'
        txt6 = tkinter.Label(marco_principal, text=tiempo1, font='Helvetica 13', width=12, height=1, bg='green',
                             fg='#a0d995', anchor=NW)
        txt6.place(x=l2xn + 15, y=lnx4 - 30)

    def txt6():

        tiempo2 = f'{0.693 * float(seleccion_2) * float(seleccion_3) * float(valor33) * float(valor22) * float(valor11)} seg'
        txt6 = tkinter.Label(marco_principal, text=tiempo2, font='Helvetica 13', width=12, height=1, bg='green',
                             fg='#a0d995', anchor=NW)
        txt6.place(x=l2xn + 15, y=lnx4 + 20)

    def txt7():

        Frec = f'{(1.44 / ((float(seleccion_1) + (2 * float(seleccion_2))) * float(valor33))) * float(valor22) * float(valor11)} Hz'
        txt6 = tkinter.Label(marco_principal, text=Frec, font='Helvetica 13', width=12, height=1, bg='green',
                             fg='#a0d995', anchor=NW)
        txt6.place(x=l1xn + 470, y=lnx4 + 20)

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=35)
    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\2_ASTABLE1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640
    I = "Imagenes\\2_ASTABLE.png"
    
    img1 = Image.open(I2)
    img1 = img1.resize((600, 620), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 620), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)
   
    combo = ttk.Combobox(marco_principal, state="readonly",
                         values=["1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8",
                                 "8.2", "10", "12", "15",
                                 "18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180",
                                 "220", "270", "330", "390", "470", "510", "560", "680", "820"], width=15)
    combo.place(x=l1xn, y=lnx2)

    comboa = ttk.Combobox(marco_principal, state="readonly", values=["Ohm", "Kohm", "Mohm"], width=5)
    comboa.place(x=l2xn, y=lnx2)

    combo1 = ttk.Combobox(marco_principal, state="readonly",
                          values=["1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8",
                                  "8.2", "10", "12", "15",
                                  "18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150",
                                  "180", "220", "270", "330", "390", "470", "510", "560", "680", "820"], width=15)
    combo1.place(x=l1xn, y=lnx2 + 35)

    comboa1 = ttk.Combobox(marco_principal, state="readonly", values=["Ohm", "Kohm", "Mohm"], width=5)
    comboa1.place(x=l2xn, y=lnx2 + 35)

    button = ttk.Button(marco_principal, text="Ingresar Datos",
                        command=lambda: [seleccion1(), seleccion11(), seleccion2(), seleccion22(), seleccion3(),
                                         seleccion33()])
    button.place(x=l1xn + 300, y=lnx2 + 35)

    combo2 = ttk.Combobox(marco_principal, state="readonly",
                          values=["0.1", "0.12", "0.15", "0.18", "0.2", "0.22", "0.25", "0.27", "0.3", "0.39", "0.4",
                                  "0.47", "0.5", "0.56", "0.6", "0.68", "0.7", "0.8", "0.82", "1", "1.2", "1.5", "1.8",
                                  "2", "2.2", "2.5", "2.7", "3", "3.3", "3.9", "4", "4.7", "5",
                                  "5.6", "10", "12", "15", "18", "20", "22", "25", "27", "27", "30", "33", "39", "40",
                                  "47", "50", "56", "60", "68", "70", "80", "82", "100"], width=15)
    combo2.place(x=l3xn, y=lnx2)

    combob = ttk.Combobox(marco_principal, state="readonly", values=["nF", "pF", "uF"], width=5)
    combob.place(x=l4xn, y=lnx2)

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)
    
    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)
    
    B9 = tkinter.Button(marco_principal, text='Tiempo 1: ', width=15, height=1, bg='Orange', fg='#a0d995', command=txt5)
    B9.place(x=l1xn, y=lnx4 - 30)

    B10 = tkinter.Button(marco_principal, text='Tiempo 2: ', width=15, height=1, bg='Orange', fg='#a0d995', command=txt6)
    B10.place(x=l1xn, y=lnx4 + 20)

    B11 = tkinter.Button(marco_principal, text='Frecuencia: ', width=15, height=1, bg='Orange', fg='#a0d995',
                         command=txt7)
    B11.place(x=l1xn + 340, y=lnx4 + 20)

    ventana.mainloop()


def rebote():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  # reset the arrays
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        while i<=80:
            yield (1)
            i += 1 
        while True:
            yield (0)
                    

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
       
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\3_REBOTE1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\3_REBOTE.png"
    txt = "Circuito #3: INTERRUPTOR LIBRE DE REBOTE"
    txt1 = "La patita 2 del circuito integrado, recibe la señal \n" \
           "del conmutador momentáneo normalmente abierto (NO), \n" \
           "que en su estado norma tiene un nivel de voltaje alto \n" \
           "a través del resistor de R2. Cuando se presiona el \n" \
           "conmutador, el voltaje de la patita 2 momentáneamente \n" \
           "cae a 0 voltios, disparando el 555."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def toque():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  # reset the arrays
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
     
        while i<=80:
            yield (1)
            i += 1 
        while True:
            yield (0)
                    

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()


    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\4_CONTACTO1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\4_CONTACTO.png"
    txt = "Circuito #4: INTERRUPTOR ACTIVADO POR TOQUE"
    txt1 = "Hay 2 paneles táctiles para encender y apagar para detectar el cambio \n" \
           "de voltaje. Cuando tocamos el primer touchpad entre el pin 2 y tierra. \n" \
           "Nuestro dedo tiene resistencia y pasa la corriente a tierra, luego, en \n" \
           "el pin 2 es lógica baja. Hace que se ejecute el IC-555. Luego, el alto \n" \
           "voltaje sale del pin 3 (la salida). Después de eso, tocamos el panel \n" \
           "táctil que se encuentra entre el pin 6 y el voltaje de la fuente de \n" \
           "alimentación. La corriente fluye a través de nuestro dedo al pin6. \n" \
           "La lógica cambia a bajo voltaje."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def rele():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  # reset the arrays
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,
    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
  
    def animate():
        i=1
   
        while i<=70:
            yield (1)
            i += 1 
        while True:
            yield (0)
                    

    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\5_TEMPORIZADOR1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\5_TEMPORIZADOR.png"
    txt = "Circuito #5: TEMPORIZADOR CON RELE"
    txt1 = "Cerrando S1 comienza momentáneamente un ciclo de tiempo, el relé reacciona \n" \
           "durante todo el ciclo. R1 y C1 controlan el retardo de tiempo. C2 evita la \n" \
           "activación falsa. D2 absorbe el voltaje generado por la bobina del relé \n" \
           "cuando el relé esta apagado. Tenga cuidado al conectar dispositivos alimen-\n" \
           "tados por línea para retransmitir conexiones."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def cascada():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=40:
            yield (1)
            i += 1 
        while True:
            yield (0)
                 
    def animate1():
        i=1
        j=1
        while i<=40:
            yield (0)
            i += 1 
        while j<=40:
            yield (1)
            j += 1   
        while True:
            yield (0)
                 
            
    fig = plt.figure(figsize=(5, 2.2),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida 1', color='#a0d995', size=10, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
    
    def pausar():
        ani.event_source.stop()
################
    fig1 = plt.figure(figsize=(5, 2.2),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida 2', color='#a0d995', size=10, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope1 = Scope(ax)

    def iniciar1():
        global ani1
        ani1 = animation.FuncAnimation(fig, scope1.update, animate1, interval=20,
                                blit=True)
        canvas1.draw()
    
    def pausar1():
        ani1.event_source.stop()
###############
    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=15)
    canvas1 = FigureCanvasTkAgg(fig1, master=marco_principal)
    canvas1.get_tk_widget().place(x=15, y=250)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\6_CASCADA1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\6_CASCADA.png"
    txt = "Circuito #6: TEMPORIZADOR EN CASCADA"
    txt1 = "Basicamente son dos temporizadores, los cuales se encienden uno luego del otro.\n" \
           "Al dar el disparo, comienza el primero y cuando este termina inicia el segundo,\n" \
           "como se aprecia mejor en el grafico de la imagen hacia la derecha."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=lambda:[iniciar(),iniciar1()])
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=lambda:[pausar(),pausar1()])
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def intervalometro():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=10:
            yield (1)
            i += 1 
        while j<=40:
            yield (0)
            j += 1     
    def animate1():
        i=1
        j=1
        while i<=40:
            yield (1)
            i += 1 
        while j<=10:
            yield (0)
            j += 1   
            
    fig = plt.figure(figsize=(5, 2.2),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida 1', color='#a0d995', size=10, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
    
    def pausar():
        ani.event_source.stop()
################
    fig1 = plt.figure(figsize=(5, 2.2),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida 2', color='#a0d995', size=10, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope1 = Scope(ax)

    def iniciar1():
        global ani1
        ani1 = animation.FuncAnimation(fig, scope1.update, animate1, interval=20,
                                blit=True)
        canvas1.draw()
    
    def pausar1():
        ani1.event_source.stop()
###############

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=15)
    canvas1 = FigureCanvasTkAgg(fig1, master=marco_principal)
    canvas1.get_tk_widget().place(x=15, y=250)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\7_INTERVALOMETRO1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\7_INTERVALOMETRO.png"
    txt = "Circuito #7: INTERVALOMETRO"
    txt1 = "El temporizador 1 está conectado como oscilador astable que oscila a una \n" \
           "frecuencia determinada por R1 y C1. Termporizador 2 es de único disparo \n" \
           "que impulsa un relé a através de D1. El temporizador 1 activa el tempori-\n" \
           "zador 2 una vez por ciclo durante 3 a 5 segundos."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set
    
    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=lambda:[iniciar(),iniciar1()])
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=lambda:[pausar(),pausar1()])
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def perdido():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=70:
            yield (1)
            i += 1 
        while j<=40:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\8_DETECTOR1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\8_DETECTOR.png"
    txt = "Circuito #8: DETECTOR DE PULSO PERDIDO"
    txt1 = "Los pulsos entrantes restablecen continuamente el ciclo de tiempo. Un pulso \n" \
           "faltante permite completar el ciclo de tiempo, cambiando el estado de salida."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def alarma():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=40:
            yield (1)
            i += 1 
        while j<=10:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\9_ALARMA1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\9_ALARMA.png"
    txt = "Circuito #9: ALARMA DE FALLO DE EVENTO"
    txt1 = "Cuando se aplica energía, C1 comienza a cargarse a través de R2. A menos que S1 \n" \
           "sea cerrado antes de que se complete el ciclo de tiempo del 555, sonará el timbre.\n" \
           "S1 puede ser cualquier interruptor externo."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def divisor():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=80:
            yield (1)
            i += 1 
        while j<=8:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()
        
    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\10_DIVISOR1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\10_DIVISOR.png"
    txt = "Circuito #10: DIVISOR DE FRECUENCIA"
    txt1 = "En este circuito el 555 está conectado como un multivibrador monoestable. Una vez \n" \
           "que un ciclo de tiempo se inicia por un pulso de entrada, la entrada posterior los \n" \
           "pulsos no tienen ningún efecto hasta que se completa el ciclo. En la tabla se mues-\n" \
           "tran los típicos formas de onda de entrada y salida. (C1 * 0.1 micro Faradios, \n" \
           "R1 variado en valor)"

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def voltaje():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=10:
            yield (1)
            i += 1 
        while j<=5:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\11_OSCILADOR1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\11_OSCILADOR.png"
    txt = "Circuito #11: OSCILADOR DE CONTROL DE VOLTAJE"
    txt1 = "El 555 oscila a una frecuencia determinada por R2 y C1. Un voltaje aplicado a la \n" \
           "entrada cambia la frecuencia de oscilación del 555. Como el voltaje de entrada \n" \
           "aumenta, la frecuencia de oscilación disminuye para más volumen, omita R1 y conecte\n" \
           " el altavoz a tierra a través del capacitor de 4.7 micro Faradios."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def pulsos():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=20:
            yield (1)
            i += 1 
        while j<=5:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
  
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\12_PULSO1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\12_PULSO.png"
    txt = "Circuito #12: GENERADOR DE PULSOS"
    txt1 = "Usar como relog lógico digital generador de pulsos, \n" \
           "generador de señales, etc. (Es multiuso por su simple\n" \
           "funcionamiento y versatilidad)"

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def frecuenciometro():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.08):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 5.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        k=1
        l=1
        m=1
        n=0
        while n<=1:
            yield (0)
            n += 1 
        while i<=2:
            yield (1)
            i += 1 
        while j<=2:
            yield (2)
            j += 1    
        while k<=2:
            yield (3)
            k += 1 
        while l<=2:
            yield (4)
            l += 1    
        while m<=10:
            yield (4)
            m += 1      

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=300,
                                blit=True)
        canvas.draw()
 
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\13_FRECUENCIOMETRO1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\13_FRECUENCIOMETRO.png"
    txt = "Circuito #13: FRECUENCIOMETRO"
    txt1 = "Este circuito ultrasimplemétrico mide las señales de frecuencia de\n" \
           "audio. La señal de entrada debe oscilar entre 2.5 y 5 V. Para las\n" \
           "pruebas, conecte el generador de pulsos (circuito 555 #14) directamente\n" \
           "al pin 2 (omitir C1). R3 y C3 determinan el rango de frecuencia."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def metronomo():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  # reset the arrays
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=10:
            yield (1)
            i += 1 
        while j<=5:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\14_METRONOMO1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\14_METRONOMO.png"
    txt = "Circuito #14: METRONOMO Y OSCILADOR DE AUDIO"
    txt1 = 'Este circuito funcionará con uno o ambos dispositivos de salida. \n' \
           'El altavoz da más volumen, pero usa más corriente. Use R3 para reducir \n' \
           'volúmen. Aquí hay frecuencias típicas para varias configuraciones de R1.'

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def organo():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=20:
            yield (1)
            i += 1 
        while j<=10:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
   
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\15_JUGUETE1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\15_JUGUETE.png"
    txt = "Circuito #15: ORGANO DE JUGUETE"
    txt1 = "Este circuito es mas como un interesante juguete, se puede añadir \n" \
           "mas interruptores para accionar mas frecuencias, haciendo el circuito \n" \
           "más dinámico. Para mayor detalles en que valores del capacitor generan \n" \
           "especificas frecuencias, esta en la imagen de la derecha."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def cerrado():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=10:
            yield (1)
            i += 1 
        while j<=5:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
  
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\16_CERRADO1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\16_CERRADO.png"
    txt = "Circuito #16: OSCILADOR CERRADO"
    txt1 = "Este circuito te permitirá cambiar el tono generado por el 555 \n" \
           "por medio de una señal lógica externa. El símbolo triangular es \n" \
           "cualquiera puerta lógica externa. Puede encender y apagar el \n" \
           "tono conectándose la puerta de Q3 a -V o tierra (Ground) a través \n" \
           "de la resistencia  de 1M ohmios. R1 y C1 controlan la frecuencia \n" \
           "del tono. Q1 se puede conectar como una puerta conmutable en otra\n" \
           "parte del circuito."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def chirrido():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=20:
            yield (1)
            yield (0)
            i += 1 
        while j<=10:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\17_CHIRP1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\17_CHIRP.png"
    txt = "Circuito #17: GENERADOR DE CHIRRIDO"
    txt1 = "Este circuito aplica breves pulsos de corriente a un zumbador \n" \
           "piezoeléctrico (Radio Shack 273-065 o similar). Esto hace que \n" \
           "el timbre emita chirridos que llaman la atención. El circuito \n" \
           "es un buen dispositivo de advertencia.\n\n" \
           "R1 controla la tasa de chirridos. Use una resistencia fija de \n" \
           "100K ohmios para aproximadamente 2-3 chirridos por segundo. \n" \
           "C3 controla la duración de los chirridos. para larga duración \n" \
           "los pulsos (que se convierten en ráfagas de tono) aumentan C3 \n" \
           "a 0.22 micro Faradios o más. Reduzca el volumen insertando una \n" \
           "resistencia de 100-10.000 ohmios entre el pin 9 y zumbador \n" \
           "piezoeléctrico. Intente usar la fotorresistencia CDS para R1."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)
    
    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def escalonado():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 5.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        k=1
        l=1
        m=1
        n=1
        while i<=10:
            yield (5)
            i += 1 
        while j<=10:
            yield (4)
            j += 1          
        while k<=20:
            yield (3)
            k += 1   
        while l<=30:
            yield (2)
            l += 1   
        while m<=40:
            yield (1)
            m += 1   
        while n<=40:
            yield (0)
            n += 1  
    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
    
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\18_TONOS1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\18_TONOS.png"
    txt = "Circuito #18: GENERADOR DE TONOS ESCALONADOS"
    txt1 = "Este circuito produce sonidos que se asemejan a las cuerdas de violín \n" \
           "pulsadas al tambor a medida que se ajustan R1 y R3. la frecuencia de \n" \
           "salida escalonada disminuye en incrementos progresivamente más pequeños \n" \
           "a medida que R3 se reduce en valor. El gráfico que se muestra aquí es \n" \
           "tipico para los valores mostrados. Se puede cambiar C1, C2 y R1."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)
    
    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def tres_estados():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        k=1
        
        while i<=5:
            yield (1)
            yield (1)
            yield (1)
            yield (1)
            yield (0)
            yield (0)
            yield (0)
            yield (0)
            i += 1
        while k<=25:
            yield (0)
            k += 1  
              
    def animate1():
        i=1
        j=1
        while i<=5:
            yield (1)
            i += 1
        while j<=5:
            yield (0)
            j += 1  
    def animate2():
        i=1
        k=1
        j=1
        m=1
        n=1
        p=1
        while i<=5:
            yield (1)
            yield (1)
            yield (1)
            yield (1)
            yield (0)
            yield (0)
            yield (0)
            yield (0)
            i += 1
        while k<=10:
            yield (0)
            k += 1 
        while j<=10:
            yield (1)
            j += 1        
        while m<=10:
            yield (0)
            m += 1 
        while n<=10:
            yield (1)
            n += 1 
        while p<=10:
            yield (0)
            p += 1 
    fig = plt.figure(figsize=(5, 1.6),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Rafaga de Tono', color='#a0d995', size=10, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)
    
    fig1 = plt.figure(figsize=(5, 1.6),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Tono Constante', color='#a0d995', size=10, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope1 = Scope(ax)
    
    fig2 = plt.figure(figsize=(5, 1.6),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Dos Tonos', color='#a0d995', size=10, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope2 = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
    def iniciar1():
        global ani1
        ani1 = animation.FuncAnimation(fig, scope1.update, animate1, interval=20,
                                blit=True)
        canvas.draw()
    def iniciar2():
        global ani2
        ani2 = animation.FuncAnimation(fig, scope2.update, animate2, interval=20,
                                blit=True)
        canvas.draw()  
    def pausar():
        ani.event_source.stop()
    def pausar1():
        ani1.event_source.stop()
    def pausar2():
        ani2.event_source.stop()
    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=15)
    canvas1 = FigureCanvasTkAgg(fig1, master=marco_principal)
    canvas1.get_tk_widget().place(x=15, y=160)
    canvas2 = FigureCanvasTkAgg(fig2, master=marco_principal)
    canvas2.get_tk_widget().place(x=15, y=310)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\19_TRESESTADOS1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\19_TRESESTADOS.png"
    txt = "Circuito #19: GENERATOR DE TONO EN TRES ESTADOS"
    txt1 = "Este circuito genera 3 distintos estados de tonos: Ráfaga de Tono, \n" \
           "Tono constante y Dos tonos. El grafico lo explica mejor en la imagen \n" \
           "a la derecha. Se puede experimentar con otros valores para R1, C1, \n" \
           "R4 y C2; para modificar los tonos."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set
    
    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=lambda:[iniciar(),iniciar1(),iniciar2()])
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=lambda:[pausar(),pausar1(),pausar2()])
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def rafaga():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation


    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=20:
            yield (0)
            i += 1 
        while j<=70:
            yield (1)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
        
    def pausar():
        ani.event_source.stop()


    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\20_RAFAGA1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\20_RAFAGA.png"
    txt = "Circuito #20: GENERADOR DE RAFAGA DE TONO"
    txt1 = "Cuando S1 está cerrado, el altavoz emite un tono cuya frecuencia está \n" \
           "determinada por R1 y C1. Cuando se abre S1, el tono continúa durante \n" \
           "varios segundos, el tiempo requerido para que C2 se descargue a través \n" \
           "de R4. Aumentar C2 para aumentar duración de la ráfaga."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set


    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def sonido():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():

        j=1
        yield (1)

        while j<=20:
            yield (j**-2)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
  
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\21_EFECTOS1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\21_EFECTOS.png"
    txt = "Circuito #21: GENERADOR DE EFECTOS DE SONIDO"
    txt1 = "El primer 555 oscila a una frecuencia determinada por R1 y C1. Su \n" \
           "salida carga C2 a través de R3. El segundo 555 oscila a una frecuencia \n" \
           "determinado por R7, C3 y el voltaje en el pin 5 (es decir, la carga en C2).\n" \
           "Experimente con la configuración de R1 y R7 y los valores de R3 y C2 \n" \
           "para obtener el efecto de trinear. "

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set
    
    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def led():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=10:
            yield (1)
            i += 1 
        while j<=10:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
   
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\22_INTERMITENTE1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\22_INTERMITENTE.png"
    txt = "Circuito #22: LED INTERMITENTE"
    txt1 = "Este circuito impulsará tanto la luz visible como los diodos emisores de \n" \
           "infrarrojos. Usar LED rojo, verde o amarillo para hacer un intermitente de " \
           "luz visible. Usar emisor de infrarrojo cercano para hacer un transmisor potente.\n" \
           "Conectar célula solar, fotodiodo o fototransistor a amplificador para recibir señal."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set


    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def lampara():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=3:
            yield (1)
            i += 1 
        while j<=3:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\23_FET1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\23_FET.png"
    txt = "Circuito #23: REGULADOR DE POTENCIA DE LAMPARA FET"
    txt1 = "Este circuito es un regulador lineal de lámpara. En funcionamiento, el 555 \n" \
           "enciende y apaga Q1 a una velocidad determinada por R1 + R2 y C1. \n" \
           "Cuando Q1 está encendido, L1 tambien lo esta. la velocidad de conmutacion \n" \
           "es tan rápida que L1 parece brillar continuamente. Aumentar la velocidad \n" \
           "de conmutación aumenta el brillo aparente de L1.\n\n" \
           "Q1 debe estar correctamente calificado. por ejemplo, una linterna PR13 \n" \
           "de 6 voltios consume 0,5 amperios o 3 vatios. Por lo tanto, utilice un \n" \
           "IRF511 o FET de potencia similar. Conecte un disipador térmico TO-220 \n" \
           "para disipar el exceso de calor."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def luz():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=30:
            yield (1)
            i += 1 
        while j<=30:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
 
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\24_OSCURIDAD1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\24_OSCURIDAD.png"
    txt = "Circuito #24: DETECTOR DE LUZ U OSCURIDAD"
    txt1 = "Cuando S1 está en la posición 'L', el altavoz emite un tono cuando \n" \
           "la luz golpea al fotorresistor. Cuando S1 está en la posición 'D' \n" \
           "El altavoz cambia un tono cuando el fotorresistor NO esta iluminado."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def infrarrojo():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=20:
            yield (1)
            yield (0)
            i += 1 
        while j<=10:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()

    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\25_INFRARROJO1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\25_INFRARROJO.png"
    txt = "Circuito #25: ALARMA INFRARROJA DE SEGURIDAD"
    txt1 = "Suena la alarma cuando el inserto se mueve de entre el LED\n" \
           "(emisor de infrarrojos) y Q1. Las puertas del monitor, etc."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def transmisor():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=20:
            yield (1)
            i += 1 
        while j<=20:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
   
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\26_TRANSMISOR1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\26_TRANSMISOR.png"
    txt = "Circuito #26: TRANSMISOR ANALOGO DE ONDAS DE LUZ"
    txt1 = "Este circuito pulsa un diodo emisor de infrarrojos a una frecuencia\n" \
           "determinada por R1 y C1. El receptor (circuito #27) recibe Y \n" \
           "amplifica la señal infrarroja. A continuación, convierte la señal\n" \
           "frecuencia en una corriente que se muestra en un medidor de 0-1 mA.\n" \
           "Use lentes para aumentar el alcance. Para detalles completos, ver:\n" \
           "'The forrest mims circuit scrapbook' (M'Graw-Hill, 1983)"

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def receptor():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        j=1
        while i<=20:
            yield (1)
            i += 1 
        while j<=10:
            yield (0)
            j += 1          

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
   
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\27_RECEPTOR1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\27_RECEPTOR.png"
    txt = "Circuito #27: RECEPTOR ANALOGO DE ONDAS DE LUZ"
    txt1 = "Este circuito recibe las señales PFM (Modulación Pulso-Frecuencia)\n" \
           "del transmisor (circuito #26). Como se dijo en la explicación del \n" \
           "transmisor, este circuito receptor, recibe y amplifica la señal \n" \
           "infrarroja. Luego la convierte en una corriente de 0-1 mA. Para \n" \
           "mas detalles ver el circuito #26."

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()


def convertidor():
    import tkinter
    from PIL import Image, ImageTk
    import tkinter as tk
    from tkinter import ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.lines import Line2D
    class Scope:
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata, color='#1ca9e6', linewidth=3)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt: 
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,

    def animate():
        i=1
        
        while i<=80:
            yield (1)
            i += 1 
        while True:
            yield (0)
                    

    fig = plt.figure(figsize=(5, 3.5),facecolor='#252626')
    ax = plt.axes(xlim=(0, 2), ylim=(-0.5, 1.5),facecolor='#252626')
    ax.set_facecolor("#094542")
    plt.title('Grafica Señal de Salida', color='#a0d995', size=16, family='Arial')
    plt.grid(True)
    plt.xticks(color='#252626')
    plt.yticks(color='#252626')
    scope = Scope(ax)

    def iniciar():
        global ani
        ani = animation.FuncAnimation(fig, scope.update, animate, interval=20,
                                blit=True)
        canvas.draw()
  
    def pausar():
        ani.event_source.stop()

    ventana = tkinter.Tk()
    ventana.config(bg="#a0d995")
    marco_principal = tkinter.Frame(ventana)
    marco_principal.pack(side="left", expand=True)
    marco_principal.config(bg="#a0d995", width="660", height="730")

    marco_principal2 = tkinter.Frame(ventana)
    marco_principal2.pack()
    marco_principal2.pack(side="right", expand=True)
    marco_principal2.config(bg="#a0d995", width="650", height="730")

    canvas = FigureCanvasTkAgg(fig, master=marco_principal)
    canvas.get_tk_widget().place(x=15, y=85)

    l1xn = 35
    l2xn = 155
    l3xn = 275
    l4xn = 395
    BG = "white"
    I2 = "Imagenes\\28_CONVERTIDOR1.png"
    lnx1 = 495
    lnx2 = 540
    lnx3 = 585
    lnx4 = 640

    I = "Imagenes\\28_CONVERTIDOR.png"
    txt = "Circuito #28: CONVERTIDOR DE DC A DC"
    txt1 = "Este circuito aplica una corriente pulsante a la bobina de un \n" \
           "transformador. El voltaje de entrada es potenciado por la segunda bobina \n" \
           "del transformador. Utilícelo para alimentar lámparas de neón, pantallas de\n" \
           "plasma, etc. Precaución: NO TOCAR CABLES DE SALIDA! (R3 suelta la carga de \n" \
           "C2 cuando se retira V_IN)"

    img1 = Image.open(I2)
    img1 = img1.resize((600, 650), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img1, master=marco_principal2)

    img2 = Image.open(I)
    img2 = img2.resize((600, 650), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img2, master=marco_principal2)

    panel = tk.Label(marco_principal2, image=img_2)
    panel.grid(row=0, column=1)
    panel.config(bg=BG)

    def atras():
        global panel
        panel = tk.Label(marco_principal2, image=img_2)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    def adelante():
        global panel
        panel = tk.Label(marco_principal2, image=img_1)
        panel.grid(row=0, column=1)
        panel.config(bg=BG)

    elemento1 = tk.Text(marco_principal, height=1, bg='light green', font='Helvetica 13', fg='black')
    elemento1.place(x=l1xn, y=lnx2)
    elemento1.insert(0.0, txt)
    elemento1["state"] = tk.DISABLED

    elemento2 = tk.Text(marco_principal, height=5, bg='yellow', font='Helvetica 13', fg='black')
    elemento2.place(x=l1xn, y=lnx3)
    elemento2.insert(0.0, txt1)
    elemento2["state"] = tk.DISABLED

    scrollbar1 = ttk.Scrollbar(marco_principal, orient='vertical', command=elemento2.yview)
    scrollbar1.place(x=l1xn - 20, y=lnx3)
    elemento2['yscrollcommand'] = scrollbar1.set

    B1 = tkinter.Button(marco_principal, text='Iniciar el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=iniciar)
    B1.place(x=l1xn, y=lnx1)

    B2 = tkinter.Button(marco_principal, text='Detener el gráfico', width=15, height=1, bg='#187498', fg='#a0d995', command=pausar)
    B2.place(x=l2xn, y=lnx1)

    B5 = tkinter.Button(marco_principal2, text='>>', font='Helvetica 15', bg='dark green', fg='#a0d995', command=adelante)
    B5.grid(row=0, column=2)

    B6 = tkinter.Button(marco_principal2, text='<<', font='Helvetica 15', bg='dark green', fg='#a0d995', command=atras)
    B6.grid(row=0, column=0)

    ventana.mainloop()

def Menu1():
    import tkinter as tk
    from tkinter import ttk
    from PIL import Image, ImageTk
    Ventana = tk.Tk()
    Ventana.title("Menu")
    Ventana.geometry("1300x800")
    I = ["Imagenes\\resist.ico","Imagenes\\INVER.png", "Imagenes\\NOINVER.png", "Imagenes\\SUMADOR.png","Imagenes\\CIRCDERIVADOR.png","Imagenes\\CIRINTEGRADOR.png"]
    t = ["1.  INTRODUCCION ","2.  SUMADOR  ","3.  NO INVERSOR  ","4.  INVERSOR","5.   DERIVADOR  ","6.   INTEGRADOR"," "," "]
    
    T = "MENU DE CIRCUITOS AMPLIFICADOR"
    img = Image.open("Imagenes\\FONDO.png")
    img = img.resize((1300, 800),Image.ANTIALIAS)
    img_0 = ImageTk.PhotoImage(img,master=Ventana)
    tk.Label(Ventana, image=img_0, bd=0).pack()

    ver = 80
    hor = 300
    min = 175

    l1xn = 35
    l2xn = l1xn + hor
    l3xn = l2xn + hor
    l4xn = l3xn + hor
    entre2y3 = (l2xn + l3xn) // 2

    lnx1 = 0
    lnx2 = lnx1 + ver
    lnx3 = lnx2 + ver
    lnx4 = lnx3 + ver
    lnx5 = lnx4 + ver
    lnx6 = lnx5 + ver
    lnx7 = lnx6 + ver
    lnx8 = lnx7 + ver

    columna = [l1xn, l2xn, l3xn, l4xn, entre2y3]
    fila = [lnx1, lnx2, lnx3, lnx4, lnx5, lnx6, lnx7, lnx8]

    x = 18
    y = 3
    f = "Arial 12"
    BG = 'green2'
    FG = 'black'
    def boton(numero, a, b):

        tk.Button(Ventana, text=t[numero], font=f, width=x, height=y, fg=FG, bg=BG, anchor="w",
				  command=lambda: s(numero)).place(x=columna[a], y=fila[b])
####1
    photo = Image.open(I[0]).resize((70, 70), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(photo, master = Ventana) 
    tk.Label(Ventana, image = photo).place(x=columna[0]+min, y=fila[1])
    
    photo0 = Image.open(I[1]).resize((70, 70), Image.ANTIALIAS)
    photo0 = ImageTk.PhotoImage(photo0, master = Ventana) 
    tk.Label(Ventana, image = photo0,).place(x=columna[1]+min, y=fila[1])
    #####
    photo1 = Image.open(I[2]).resize((70, 70), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(photo1, master = Ventana) 
    tk.Label(Ventana, image = photo1).place(x=columna[2]+min, y=fila[1])
    #####
    photo2 = Image.open(I[3]).resize((70, 70), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(photo2, master = Ventana) 
    tk.Label(Ventana, image = photo2).place(x=columna[3]+min, y=fila[1])
####2
    photo3 = Image.open(I[4]).resize((70, 70), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(photo3, master = Ventana) 
    tk.Label(Ventana, image = photo3).place(x=columna[0]+min, y=fila[2])
    ####
    photo4 = Image.open(I[5]).resize((70, 70), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(photo4, master = Ventana) 
    tk.Label(Ventana, image = photo4).place(x=columna[1]+min, y=fila[2])
    ####
    def s(circuito):
        if circuito == 0:
            Introduccion()
        elif circuito == 1:
            sumador()
        elif circuito == 2:
            no_inversor()
        elif circuito == 3:
            inversor()
        elif circuito == 4:
            derivador()
        elif circuito == 5:
            integrador()
   
    title = tk.Label(Ventana, text=T, font="Arial 23 bold", fg='#664300', bg='#ffff94',  width=45, height=1)
    title.place(x=entre2y3-300, y=lnx1+15)

    k = 0
    for j in [1, 2]:
        for i in [0, 1, 2, 3]:
            boton(k, i, j)
            k += 1
    Ventana.resizable(width=False, height=False)
    tk.mainloop()
def Introduccion():
	import sys
	import pygame
	pygame.init()

	size = (900,480)

	BLANCO = (255,255,255)
	negro = (0,0,0)
	##crear ventana
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	background = pygame.image.load("Imagenes\\FONDO.PNG").convert()

	fuente = pygame.font.SysFont("segoe print", 11, bold=1)
	fuente2 = pygame.font.SysFont("Arial", 13, bold=1)
	fuente3 = pygame.font.SysFont("Arial", 20, bold=1)
	fuente4 = pygame.font.SysFont("Arial", 16, bold=1)
	##texto cuadripolo
	textc1 = fuente2.render("U1",True, BLANCO)
	textc2 = fuente2.render("U2", True, BLANCO)
	textc3 = fuente3.render("A", True, BLANCO)

	textc4 = fuente4.render("U2 = A*U1", True, BLANCO)
	textc5 = fuente4.render("Vo = A*Ve",True, BLANCO)

	textc6 = fuente4.render("R1", True, BLANCO)
	textc7 = fuente4.render("R2",True, BLANCO)
	textc8 = fuente4.render("Ve", True, BLANCO)
	textc9 = fuente4.render("Vo", True, BLANCO)



	textc10 = fuente4.render("Vo = Ve*((R2/R1)+1)", True, BLANCO)

	textc11 = fuente4.render("Ve = 0", True, BLANCO)
	textc12 = fuente4.render("Ie = 0", True, BLANCO)

	textc13 = fuente4.render("Ve", True, BLANCO)
	textc14 = fuente4.render("Vo", True, BLANCO)
	textc15 = fuente4.render("A", True, BLANCO)
	##texto de la presentacion
	texto1 = fuente.render("Teoricamente un amplificador operacional se puede  ",True, BLANCO)
	texto2 = fuente.render("entender como un bloque que tiene dos entradas y ",True, BLANCO )
	texto3 = fuente.render("dos salidas:", True, BLANCO)

	texto4 = fuente.render("Donde se dice que la salida es igual a una constante", True, BLANCO)
	texto5 = fuente.render("por la entrada:", True, BLANCO)

	texto6 = fuente.render("En los amplificadores operacionales, dicha constante ",True, BLANCO)
	texto7 = fuente.render("'A' oscila entre los valores de 100.000, 200.000", True, BLANCO)
	texto8 = fuente.render("y 300.000 unidades,  que son valores dados por el ", True, BLANCO)
	texto9 = fuente.render("fabricante. ", True, BLANCO)

	texto10 = fuente.render("El esquema básico para modelar a un circuito  ", True, BLANCO)
	texto11 = fuente.render("operacional es el siguiente: ", True, BLANCO)


	texto12 = fuente.render("Donde: ", True, BLANCO)
	texto13 = fuente.render("Vo = voltaje de salida ", True, BLANCO)
	texto14 = fuente.render("A = constante de ganancia: ", True, BLANCO)
	texto15 = fuente.render("Ve = voltaje de entrada: ", True, BLANCO)

	texto16 = fuente.render("Como ya se mencionó la constante de ganancia es ", True, BLANCO)
	texto17 = fuente.render("un número muy grande, por lo que si el voltaje de  ", True, BLANCO)
	texto18 = fuente.render("entrada sería igual a 1 voltio el voltaje de salida ", True, BLANCO)
	texto19 = fuente.render("sería igual a 100.000 voltios. ¿Ese resultado tiene ", True, BLANCO)
	texto20 = fuente.render("sentido?. La respuesta es no. ", True, BLANCO)
	texto21 = fuente.render("Por lo tanto de este planteo nacen dos condiciones ", True, BLANCO)
	texto22 = fuente.render("para el uso de amplificadores operacionales", True, BLANCO)

	texto23 = fuente.render("1. La primera condición indica que el voltaje de ", True, BLANCO)
	texto24 = fuente.render("entrada debe ser un número que tienda a cero (en   ", True, BLANCO)
	texto25 = fuente.render("la practica se asume que el voltaje de entrada  ", True, BLANCO)
	texto26 = fuente.render("es cero), esto tiene sentido ya que si el voltaje ", True, BLANCO)
	texto27 = fuente.render("de entrada es por ejemplo 0.0001, tendríamos un ", True, BLANCO)
	texto28 = fuente.render("voltaje de salida igual a 10 voltios, lo cual es ", True, BLANCO)
	texto29 = fuente.render("un resultado razonable.", True, BLANCO)

	texto30 = fuente.render("2. La segunda condición se desprende de la primera ", True, BLANCO)
	texto31 = fuente.render("e indica que la corriente que entra al amplificador ", True, BLANCO)
	texto32 = fuente.render("operacional también debe ser cero", True, BLANCO)

	texto33 = fuente.render("Ahora si hacemos que nuestro circuito sea mas ", True, BLANCO)
	texto34 = fuente.render("complejo y conectamos resistencias entre las ", True, BLANCO)
	texto35 = fuente.render("terminales de entrada y de salida, obtendremos ",True, BLANCO)
	texto36 = fuente.render("que el voltaje de salida estará en función de ", True, BLANCO)
	texto37 = fuente.render("las resistencias que coloquemos y el voltaje de", True, BLANCO)
	texto38 = fuente.render("entrada.", True, BLANCO)

	texto39 = fuente.render("Aplicando las leyes de kirchoff y las dos ", True, BLANCO)
	texto40 = fuente.render("condiciones de ganancia a este nuevo circuito, ",True, BLANCO)
	texto41 = fuente.render("obtendremos la siguiente igualdad:", True, BLANCO)

	texto42 = fuente.render("Finalmente podemos observar que en la nueva ", True, BLANCO)
	texto43 = fuente.render("configuracion el voltaje de salida ya no depende", True, BLANCO)
	texto44 = fuente.render("de la ganancia del amplificador operacional",True, BLANCO)
	texto45 = fuente.render("sino solamente de las resistencias que conectemos y", True, BLANCO)
	texto46 = fuente.render("del voltaje de entrada, lo cual es de gran ayuda", True, BLANCO)
	texto47 = fuente.render("puesto que ahora se puede obtener el voltaje de ", True, BLANCO)
	texto48 = fuente.render("salida que se desee solo cambiando las resistencias ", True, BLANCO)
	texto49 = fuente.render("y el voltaje de entrada.", True, BLANCO)




	##coordenadas
	cord_x1= 50
	cord_y1 = 450
	cord_x2= 60
	cord_y2 = 450
	cord_x3= 55
	cord_y3 = 440

	ncordx1 = 650
	ncordy1 = 180
	ncordx2 = 650
	ncordy2 = 188
	ncordx3 = 658
	ncordy3 = 184

	mcordx1 = 694
	mcordy1 = 130
	mcordx2 = 694
	mcordy2 = 138
	mcordx3 = 702
	mcordy3 = 134

	pcordx1 = 810
	pcordy1 = 200
	pcordx2 = 810
	pcordy2 = 208
	pcordx3 = 818
	pcordy3 = 204

	##velocidad a la que se movera el cuadrado
	speed_y = -0.6
	##velocidad a la que se movera el cuadrado
	nspeedx = 0.6
	nspeedy = -0.6
	##velocidad a la que se movera el cuadrado
	mspeedx = 0.6
	mspeedy = 0.6
	##velocidad a la que se movera el cuadrado
	pspeedx = 0.6


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		##logica
		##logica para el triangulo que se mueve de la caja 1
		cord_y1 += speed_y
		cord_y2 += speed_y
		cord_y3 += speed_y

		if (cord_y1 < 395):
			if (cord_y2 < 395):
				if (cord_y3 < 385):
					cord_x1 = 60
					cord_y1 = 385
					cord_x2 = 60
					cord_y2 = 395
					cord_x3 = 70
					cord_y3 = 390

					speed_y = 0
		if (cord_x1 > 59):
			if (cord_x2 > 59):
				if (cord_x3 > 69):
					speed_x = 0.6
					cord_x1 += speed_x
					cord_x2 += speed_x
					cord_x3 += speed_x
		if (cord_x1 >200 ):
			if (cord_x2 > 200):
				if (cord_x3 > 210):
					cord_x1 = 50
					cord_y1 = 450
					cord_x2 = 60
					cord_y2 = 450
					cord_x3 = 55
					cord_y3 = 440
					speed_y = -0.6
					cord_y1 += speed_y
					cord_y2 += speed_y
					cord_y3 += speed_y

		##logica para el triangulo que se mueve de la caja 3
		if (ncordx3 > 657):
			ncordx1 += nspeedx
			ncordx2 += nspeedx
			ncordx3 += nspeedx
		if (ncordx3 > 690):
			nspeedx = 0
			ncordx1 = 686
			ncordy1 = 180
			ncordx2 = 694
			ncordy2 = 180
			ncordx3 = 690
			ncordy3 = 172
		if (ncordx3 > 689 and ncordy3 <173):
			nspeedy = -0.6
			ncordy1 += nspeedy
			ncordy2 += nspeedy
			ncordy3 += nspeedy
			if (ncordy3 < 140):
				ncordx1 = 650
				ncordy1 = 180
				ncordx2 = 650
				ncordy2 = 188
				ncordx3 = 658
				ncordy3 = 184
				nspeedx = 0.6
				ncordx1 += nspeedx
				ncordx2 += nspeedx
				ncordx3 += nspeedx

		##logica para el triangulo que se mueve de la caja 3 2
		if (mcordx3 > 701):
			mcordx1 += mspeedx
			mcordx2 += mspeedx
			mcordx3 += mspeedx
		if (mcordx3 > 810):
			mspeedx = 0
			mcordx1 = 806
			mcordy1 = 142
			mcordx2 = 814
			mcordy2 = 142
			mcordx3 = 810
			mcordy3 = 150

		if (mcordx3 > 809 and mcordy3 > 149):
			mspeedy = 0.5
			mcordy1 += mspeedy
			mcordy2 += mspeedy
			mcordy3 += mspeedy
		if (mcordy3 > 210):
			mcordx1 = 694
			mcordy1 = 130
			mcordx2 = 694
			mcordy2 = 138
			mcordx3 = 702
			mcordy3 = 134

			mspeedx = 0.6
			mcordx1 += mspeedx
			mcordx2 += mspeedx
			mcordx3 += mspeedx

		##logica para el triangulo que se mueve de la caja 3 2
		if (pcordx3 > 817):
			pspeedx = 0.3
			pcordx1 += pspeedx
			pcordx2 += pspeedx
			pcordx3 += pspeedx
		if (pcordx3 > 850):
			pcordx1 = 810
			pcordy1 = 200
			pcordx2 = 810
			pcordy2 = 208
			pcordx3 = 818
			pcordy3 = 204
			pspeedx = 0.3
			pcordx1 += pspeedx
			pcordx2 += pspeedx
			pcordx3 += pspeedx

		##color de fondo
		screen.fill("#F0FFFF")
		##zona de dibujo
		##cuadripolo
		screen.blit(background, [0, 0])
		pygame.draw.line(screen,BLANCO,(100,75), (180,75))
		pygame.draw.line(screen, BLANCO, (100, 75), (100, 120))
		pygame.draw.line(screen, BLANCO, (100, 120), (180, 120))
		pygame.draw.line(screen, BLANCO, (180, 120), (180, 75))

		pygame.draw.line(screen, BLANCO, (60,88), (100,88))
		pygame.draw.line(screen, BLANCO, (60, 108), (100, 108))
		pygame.draw.line(screen, BLANCO, (180, 88), (220, 88))
		pygame.draw.line(screen, BLANCO, (180, 108), (220,108))

		pygame.draw.lines(screen, BLANCO, True, [(400,345), (490,345), (490,375), (400,375)])
		pygame.draw.lines(screen, BLANCO, True, [(400, 435), (480, 435), (480, 470), (400, 470)])
		pygame.draw.lines(screen, BLANCO, True, [(400, 10), (490, 10), (490, 40), (400, 40)])
		pygame.draw.lines(screen, BLANCO, True, [(100, 180), (200, 180), (200, 215), (100, 215)])
		pygame.draw.lines(screen, BLANCO, True, [(660, 306), (830, 306), (830, 334), (660, 334)])
		##triangulo caja 3
		pygame.draw.lines(screen,BLANCO, True, [(720,180), (720,240), (780,210)])
		pygame.draw.line(screen, BLANCO, (690, 195), (720, 195))
		pygame.draw.line(screen, BLANCO,(690, 225), (720, 225))

		pygame.draw.line(screen, BLANCO,(780, 210), (830, 210))
		pygame.draw.line(screen, BLANCO, (830, 210), (830, 230))
		pygame.draw.line(screen, BLANCO, (810, 230), (850, 230))
		pygame.draw.line(screen, BLANCO, (820, 235), (840, 235))

		pygame.draw.lines(screen, BLANCO, False,
						[(675, 195), (677,190),(680,200),(682,190),(685,200),(687,190),(690,195)])
		pygame.draw.line(screen, BLANCO, (655, 195), (675, 195))
		pygame.draw.line(screen, BLANCO, (700, 195), (700, 145))
		pygame.draw.line(screen, BLANCO, (700, 145), (735, 145))

		pygame.draw.line(screen, BLANCO, (655, 195), (655, 220))
		pygame.draw.line(screen, BLANCO, (640, 220), (670, 220))
		pygame.draw.line(screen, BLANCO, (647, 225), (662, 225))


		pygame.draw.lines(screen, BLANCO, False,
						[(735,145),(737,140),(740,150),(742,140),(745,150),(747,140),(750,145)])
		pygame.draw.line(screen, BLANCO, (750, 145), (803, 145))
		pygame.draw.line(screen, BLANCO, (803, 145), (803, 210))

		pygame.draw.line(screen, BLANCO, (730, 200), (738, 200))
		pygame.draw.line(screen, BLANCO, (730, 220), (738, 220))
		pygame.draw.line(screen, BLANCO, (734, 217), (734, 223))
			##Triangulo que se mueve en la caja 3
		pygame.draw.polygon(screen, BLANCO, [(ncordx1,ncordy1), (ncordx2,ncordy2), (ncordx3,ncordy3)])

			##Triangulo que se mueve en la caja 3 2
		pygame.draw.polygon(screen, BLANCO, [(mcordx1,mcordy1), (mcordx2,mcordy2), (mcordx3,mcordy3)])

			##Triangulo que se mueve en la caja 3 3
		pygame.draw.polygon(screen, BLANCO, [(pcordx1,pcordy1), (pcordx2,pcordy2), (pcordx3,pcordy3)])

		##triangulo que usare mas tarde
		pygame.draw.polygon(screen,BLANCO, [(cord_x1,cord_y1), (cord_x2,cord_y2), (cord_x3,cord_y3)])
		pygame.draw.line(screen,BLANCO, (300,0), (300,480))
		pygame.draw.line(screen,BLANCO, (600,0), (600,480))

		pygame.draw.line(screen,BLANCO, (110,365), (110,415))
		pygame.draw.line(screen, BLANCO, (110, 365), (160, 390))
		pygame.draw.line(screen, BLANCO, (110, 415), (160, 390))

		pygame.draw.line(screen, BLANCO, (40, 377), (110, 377))
		pygame.draw.line(screen, BLANCO, (40, 360), (40, 395))
		pygame.draw.line(screen, BLANCO, (35, 370), (35, 385))


		pygame.draw.line(screen, BLANCO, (65, 403), (110, 403))
		pygame.draw.line(screen, BLANCO, (65, 403), (65, 420))
		pygame.draw.line(screen, BLANCO, (65, 420), (65, 440))

		pygame.draw.line(screen, BLANCO, (160, 390), (180, 390))
		pygame.draw.line(screen, BLANCO, (180, 390), (180, 415))
		pygame.draw.line(screen, BLANCO, (160, 415), (200, 415))
		pygame.draw.line(screen, BLANCO, (170, 420), (190, 420))

		pygame.draw.line(screen, BLANCO, (115, 377), (121, 377))
		pygame.draw.line(screen, BLANCO, (115, 403),(121, 403))
		pygame.draw.line(screen, BLANCO, (118, 400), (118, 406))



		##posicion de los textos de formulas etc
		screen.blit(textc1, (40,90))
		screen.blit(textc2, (226, 90))
		screen.blit(textc3, (135, 85))

		screen.blit(textc4, (115, 190))

		screen.blit(textc5, (405, 15))

		screen.blit(textc6, (670, 170))
		screen.blit(textc7, (735,120))
		screen.blit(textc8, (680, 220))
		screen.blit(textc9, (850, 210))

		screen.blit(textc10, (670,310))

		screen.blit(textc11, (420, 350))
		screen.blit(textc12, (420, 445))

		screen.blit(textc13, (70, 410))
		screen.blit(textc14, (170, 365))
		screen.blit(textc15, (122, 381))



		##posicion de los textos de la presentacion
		screen.blit(texto1, (10,10))
		screen.blit(texto2, (10,26))
		screen.blit(texto3, (10,42))

		screen.blit(texto4, (10, 144))
		screen.blit(texto5, (10, 160))

		screen.blit(texto6, (10, 224))
		screen.blit(texto7, (10, 240))
		screen.blit(texto8, (10, 256))
		screen.blit(texto9, (10, 272))

		screen.blit(texto10, (10, 292))
		screen.blit(texto11, (10, 308))


		screen.blit(texto12, (310, 40))
		screen.blit(texto13, (310, 56))
		screen.blit(texto14, (310, 72))
		screen.blit(texto15, (310, 88))

		screen.blit(texto16, (310, 108))
		screen.blit(texto17, (310, 124))
		screen.blit(texto18, (310, 140))
		screen.blit(texto19, (310, 156))
		screen.blit(texto20, (310, 172))
		screen.blit(texto21, (310, 188))
		screen.blit(texto22, (310, 204))

		screen.blit(texto23, (310, 226))
		screen.blit(texto24, (310, 242))
		screen.blit(texto25, (310, 258))
		screen.blit(texto26, (310, 274))
		screen.blit(texto27, (310, 290))
		screen.blit(texto28, (310, 306))
		screen.blit(texto29, (310, 322))

		screen.blit(texto30, (310, 376))
		screen.blit(texto31, (310, 392))
		screen.blit(texto32, (310, 408))

		screen.blit(texto33, (610, 10))
		screen.blit(texto34, (610, 26))
		screen.blit(texto35, (610, 42))
		screen.blit(texto36, (610, 58))
		screen.blit(texto37, (610, 75))
		screen.blit(texto38, (610, 90))

		screen.blit(texto39, (610, 255))
		screen.blit(texto40, (610, 271))
		screen.blit(texto41, (610, 287))

		screen.blit(texto42, (610, 334))
		screen.blit(texto43, (610, 350))
		screen.blit(texto44, (610, 366))
		screen.blit(texto45, (610, 382))
		screen.blit(texto46, (610, 398))
		screen.blit(texto47, (610, 414))
		screen.blit(texto48, (610, 430))
		screen.blit(texto49, (610, 446))






		##para ver que figuras mas podemos dibujar con pygame ponemos en google pygame draw rect##

		#actualizar pantalla

		pygame.display.flip()
		clock.tick(60)   
def sumador():
	import tkinter as tk
	from tkinter import ttk
	from tokenize import Imagnumber
	import webbrowser


	ventana= tk.Tk()
	#StringVar, IntVar, DoubleVar - VARIABLES
	res = tk.StringVar()
	#**********************VENTANA*******************
	ventana.title("SUMADOR")
	ventana.iconbitmap("IMAGENES\INVERSOR.ico")
	ventana.resizable(False,False)
	ventana.geometry("853x480")
	ventana.config(cursor="hand2")
 
	#**************************FUNCION****************************
	def calculo():
		global resvoltaje
		num1 = float(resistenciauno.get())
		num2 = float(resistenciados.get())
		num3 = float(resistenciatres.get())
		numf = float(resistenciaf.get())
		v1 = float(voltaje.get())
		v2 = float(voltajedos.get())
		v3 = float(voltajetres.get())
		uniuno = int(unidad.get())    
		unidos = int(unidaddos.get())
		unitres = int(unidadtres.get())
		unif = int(unidadf.get())
		univo1 = int(unidadv.get())
		univo2 = int(unidadv2.get())
		univo3 = int(unidadv3.get())
  
##########
		resvoltaje = f'El voltaje de salida es :{(-numf*unif)*((v1*univo1)/(num1*uniuno)+((v2*univo2)/(num2*unidos))+((v3*univo3)/(num3*unitres)))} vol'
		tk.Label(ventana,text=resvoltaje, fg= "white", bg= "RoyalBlue4", width=25, height=1).place(x=60, y = 325)
#########

	def web():
			url = ["https://www.tinkercad.com/things/7zasW3PeXSy-copy-of-sumador/editel?tenant=circuits"]
			webbrowser.register("chrome",None,webbrowser.BackgroundBrowser("C://Users//Capital PC//AppData//Local//Google//Chrome//Application//chrome.exe"))
			w = webbrowser.get("chrome")
			w.open(url[0])
	#**************** EXPORTACION DE LA IMAGEN********************
	imagen = tk.PhotoImage(file='IMAGENES\\IMAGENSUMADOR.PNG',master=ventana)
	imagencir = tk.PhotoImage(file='IMAGENES\\SUMADOR.PNG',master=ventana)
	formula = tk.PhotoImage(file='IMAGENES\\FORSUMADOR.PNG',master=ventana)
	fondo = tk.Label(ventana, image = imagen).place(x=0, y = 0 )
	circuitoboton = tk.Label(ventana, image=imagencir, relief="groove", bd="5", bg="blue2").place(x=550, y = 40)
	forminver = tk.Label(ventana, image= formula, relief="groove", bd="5", bg="blue2").place(x=60, y = 410)
	#*******************TITULO********************
	titulo=tk.Label(ventana,text="AMPLIFICADOR OPERACIONAL - SUMADOR", ancho=tk.CENTER, fg= "white", bg= "RoyalBlue4")
	titulo.config(font=("Bahnschrift SemiLight",15))
	titulo.place(x=250, y=10)

	#*****************BOTONES**********************
	textoresuno = tk.Label(ventana, relief="raised", bg= "orange", text="R1:   ")
	textoresuno.config(font=("Bahnschrift SemiLight",12))
	textoresuno.place(x= 65, y = 70)
	resistenciauno = ttk.Combobox(ventana,state="readonly")
	resistenciauno.place(x=110, y= 70)
	resistenciauno['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8", "8.2", "10", "12", "15",
	"18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180", "220", "270", "330", "390", "470", "510", "560", "680", "820")
	resistenciauno.current(0)
	unidad = ttk.Combobox(ventana,state="readonly")
	unidad.place(x=270,y=70)
	unidad['values']=("1", "1000", "1000000")
	unidad.current(1)

	textoresdos = tk.Label(ventana, relief="raised", bg= "orange", text="R2:  ")
	textoresdos.config(font=("Bahnschrift SemiLight",12))
	textoresdos.place(x= 65, y = 100)
	resistenciados = ttk.Combobox(ventana,state="readonly")
	resistenciados.place(x=110, y= 100)
	resistenciados['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8", "8.2", "10", "12", "15",
	"18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180", "220", "270", "330", "390", "470", "510", "560", "680", "820")
	resistenciados.current(0)
	unidaddos = ttk.Combobox(ventana,state="readonly")
	unidaddos.place(x=270,y=100)
	unidaddos['values']=("1", "1000", "1000000")
	unidaddos.current(1)

	textorestres = tk.Label(ventana, relief="raised", bg= "orange", text="R3:  ")
	textorestres.config(font=("Bahnschrift SemiLight",12))
	textorestres.place(x= 65, y = 130)
	resistenciatres = ttk.Combobox(ventana,state="readonly")
	resistenciatres.place(x=110, y= 130)
	resistenciatres['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8", "8.2", "10", "12", "15",
	"18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180", "220", "270", "330", "390", "470", "510", "560", "680", "820")
	resistenciatres.current(0)
	unidadtres = ttk.Combobox(ventana,state="readonly")
	unidadtres.place(x=270,y=130)
	unidadtres['values']=("1", "1000", "1000000")
	unidadtres.current(1)

	textoresf = tk.Label(ventana, relief="raised", bg= "orange", text="Rf:  ")
	textoresf.config(font=("Bahnschrift SemiLight",12))
	textoresf.place(x= 65, y = 160)
	resistenciaf = ttk.Combobox(ventana,state="readonly")
	resistenciaf.place(x=110, y= 160)
	resistenciaf['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8", "8.2", "10", "12", "15",
	"18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180", "220", "270", "330", "390", "470", "510", "560", "680", "820")
	resistenciaf.current(0)
	unidadf = ttk.Combobox(ventana,state="readonly")
	unidadf.place(x=270,y=160)
	unidadf['values']=("1", "1000", "1000000")
	unidadf.current(1)

	textovoltaje = tk.Label(ventana, relief="raised", bg= "orange", text="V1:   ")
	textovoltaje.config(font=("Bahnschrift SemiLight",12))
	textovoltaje.place(x= 65, y = 190)
	voltaje = ttk.Combobox(ventana,state="readonly")
	voltaje.place(x=110, y =190)
	voltaje['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8")
	voltaje.current(0)
	unidadv = ttk.Combobox(ventana,state="readonly")
	unidadv.place(x=270,y=190)
	unidadv['values']=("1", "1000", "1000000")
	unidadv.current(1)

	textovoltajedos = tk.Label(ventana, relief="raised", bg= "orange", text="V2:   ")
	textovoltajedos.config(font=("Bahnschrift SemiLight",12))
	textovoltajedos.place(x= 65, y = 220)
	voltajedos = ttk.Combobox(ventana,state="readonly")
	voltajedos.place(x=110, y =220)
	voltajedos['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8")
	voltajedos.current(0)
	unidadv2 = ttk.Combobox(ventana,state="readonly")
	unidadv2.place(x=270,y=220)
	unidadv2['values']=("1", "1000", "1000000")
	unidadv2.current(1)

	textovoltajetres = tk.Label(ventana, relief="raised", bg= "orange", text="V3:   ")
	textovoltajetres.config(font=("Bahnschrift SemiLight",12))
	textovoltajetres.place(x= 65, y = 250)
	voltajetres = ttk.Combobox(ventana,state="readonly")
	voltajetres.place(x=110, y =250)
	voltajetres['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8")
	voltajetres.current(0)
	unidadv3 = ttk.Combobox(ventana,state="readonly")
	unidadv3.place(x=270,y=250)
	unidadv3['values']=("1", "1000", "1000000")
	unidadv3.current(1)
	#********************BOTON DE CALCULAR*********************
	boton = tk.Button(ventana,relief="raised", text="Calcular", command=calculo, bg="green2")
	boton.config(font=("Bahnschrift SemiLight",12))
	boton.place(x = 125, y=280)

	#*******************BOTON DE PAGINA WEB****************************
	boton_pagweb = tk.Button(ventana,relief="raised", text="Pagina Web", command=web, bg="green2")
	boton_pagweb.config(font=("Bahnschrift SemiLight",12))
	boton_pagweb.place(x = 125, y=360)


	resultado = tk.Label(ventana, textvariable=res, fg= "white", bg="RoyalBlue4")
	resultado.config(font=("Bahnschrift SemiLight",15))
	resultado.place(x=60,y=320)
	ventana.mainloop()
def no_inversor():
	import tkinter as tk
	from tkinter import ttk
	from tokenize import Imagnumber
	import webbrowser

	ventana= tk.Tk()
	#StringVar, IntVar, DoubleVar - VARIABLES
	res = tk.StringVar()
	#**********************VENTANA*******************
	ventana.title("NO INVERSOR")
	ventana.iconbitmap("IMAGENES\\INVERSOR.ico")
	ventana.resizable(False,False)
	ventana.geometry("853x480")
	ventana.config(cursor="hand2")
	#**************************FUNCION****************************
	def calculo():
		runos = float(resistenciauno.get())
		rdos = float(resistenciados.get())
		vol = float(voltaje.get())
		uniuno = int(unidad.get())    
		unidos = int(unidaddos.get())
		unitres = int(unidadtres.get())
		
		resvoltaje = f'El voltaje de salida es:{(vol*unitres)*(1+((rdos*unidos)/(runos*uniuno)))} vol'
		tk.Label(ventana,text=resvoltaje, fg="white",bg = "RoyalBlue4",width=25, height=1).place(x=50, y=230)
#####
	def web():
		url = ["https://www.tinkercad.com/things/6VjEIukdd7d-copy-of-no-inversor/editel?tenant=circuits"]
		webbrowser.register("chrome",None,webbrowser.BackgroundBrowser("C://Users//Capital PC//AppData//Local//Google//Chrome//Application//chrome.exe"))
		w = webbrowser.get("chrome")
		w.open(url[0])

	#**************** EXPORTACION DE LA IMAGEN********************
	imagen = tk.PhotoImage(file='IMAGENES\\IMAGENNOINVERSOR.png',master= ventana)
	imagencir = tk.PhotoImage(file='IMAGENES\\NOINVER.png',master= ventana)
	formula = tk.PhotoImage(file='IMAGENES\\FORNOINVER.png',master= ventana)
	fondo = tk.Label(ventana, image = imagen).place(x=0, y = 0 )
	circuitoboton = tk.Label(ventana, image=imagencir, relief="groove", bd="5", bg="blue2").place(x=520, y = 50)
	forminver = tk.Label(ventana, image= formula, relief="groove", bd="5", bg="blue2").place(x=650, y = 235)
	#*******************TITULO********************
	titulo=tk.Label(ventana,text="AMPLIFICADOR OPERACIONAL - NO INVERSOR", ancho=tk.CENTER, fg= "white", bg= "RoyalBlue4")
	titulo.config(font=("Bahnschrift SemiLight",15))
	titulo.place(x=250, y=10)

	#*****************BOTONES**********************
	textoresuno = tk.Label(ventana, relief="raised", bg= "orange", text="R1:   ")
	textoresuno.config(font=("Bahnschrift SemiLight",12))
	textoresuno.place(x= 65, y = 70)
	resistenciauno = ttk.Combobox(ventana,state="readonly")
	resistenciauno.place(x=110, y= 70)
	resistenciauno['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8", "8.2", "10", "12", "15",
	"18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180", "220", "270", "330", "390", "470", "510", "560", "680", "820")
	resistenciauno.current(0)
	unidad = ttk.Combobox(ventana,state="readonly")
	unidad.place(x=270,y=70)
	unidad['values']=("1", "1000", "1000000")
	unidad.current(1)


	textoresdos = tk.Label(ventana, relief="raised", bg= "orange", text="R2:  ")
	textoresdos.config(font=("Bahnschrift SemiLight",12))
	textoresdos.place(x= 65, y = 100)
	resistenciados = ttk.Combobox(ventana,state="readonly")
	resistenciados.place(x=110, y= 100)
	resistenciados['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8", "8.2", "10", "12", "15",
	"18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180", "220", "270", "330", "390", "470", "510", "560", "680", "820")
	resistenciados.current(0)
	unidaddos = ttk.Combobox(ventana,state="readonly")
	unidaddos.place(x=270,y=100)
	unidaddos['values']=("1", "1000", "1000000")
	unidaddos.current(1)

	textovolatje = tk.Label(ventana, relief="raised", bg= "orange", text="Vint:")
	textovolatje.config(font=("Bahnschrift SemiLight",12))
	textovolatje.place(x= 65, y = 130)
	voltaje = ttk.Combobox(ventana,state="readonly")
	voltaje.place(x=110, y =130)
	voltaje['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8")
	voltaje.current(0)
	unidadtres = ttk.Combobox(ventana,state="readonly")
	unidadtres.place(x=270,y=130)
	unidadtres['values']=("1", "1000", "1000000")
	unidadtres.current(1)

	#********************BOTON DE CALCULAR*********************
	boton = tk.Button(ventana,relief="raised", text="Calcular", command=calculo, bg="green2")
	boton.config(font=("Bahnschrift SemiLight",12))
	boton.place(x = 125, y=180)

	#*******************BOTON DE PAGINA WEB****************************
	boton_pagweb = tk.Button(ventana,relief="raised", text="Pagina Web", command=web, bg="green2")
	boton_pagweb.config(font=("Bahnschrift SemiLight",12))
	boton_pagweb.place(x = 125, y=280)

	resultado = tk.Label(ventana, textvariable=res, fg= "white", bg="RoyalBlue4")
	resultado.config(font=("Bahnschrift SemiLight",15))
	resultado.place(x=60,y=230)
	ventana.mainloop()
def inversor():
	import tkinter as tk
	from tkinter import ttk
	from tokenize import Imagnumber
	import webbrowser

	ventana= tk.Tk()
	#StringVar, IntVar, DoubleVar - VARIABLES
	res = tk.StringVar()
	#**********************VENTANA*******************
	ventana.title("INVERSOR")
	ventana.iconbitmap("IMAGENES\\INVERSOR.ico")
	ventana.resizable(False,False)
	ventana.geometry("853x480")
	ventana.config(cursor="hand2")
	#**************************FUNCION****************************
	def calculo():
		runos = float(resistenciauno.get())
		rdos = float(resistenciados.get())
		vol = float(voltaje.get())
		uniuno = float(unidad.get())    
		unidos = float(unidaddos.get())
		unitres = float(unidadtres.get())
        
		resvoltaje = f'El voltaje de salida es:{((vol*unitres)*(rdos*unidos)/(runos*uniuno))} vol'
		tk.Label(ventana,text=resvoltaje,fg = "white", bg = "RoyalBlue4", width=25, height=1).place(x=50, y = 230)

	def web():
		url = ["https://www.tinkercad.com/things/1vcnsnwOkkP-copy-of-inversor/editel?tenant=circuits"]
		webbrowser.register("chrome",None,webbrowser.BackgroundBrowser("C://Users//Capital PC//AppData//Local//Google//Chrome//Application//chrome.exe"))
		w = webbrowser.get("chrome")
		w.open(url[0])
	#**************** EXPORTACION DE LA IMAGEN********************
	imagen = tk.PhotoImage(file='IMAGENES\\IMAGENINVERSOR.PNG',master= ventana)
	imagencir = tk.PhotoImage(file='IMAGENES\\INVER.PNG',master= ventana)
	formula = tk.PhotoImage(file='IMAGENES\\FORINVER.PNG',master= ventana)
	fondo = tk.Label(ventana, image = imagen).place(x=0, y = 0 )
	circuitoboton = tk.Label(ventana, image=imagencir, relief="groove", bd="5", bg="blue2").place(x=520, y = 50)
	forminver = tk.Label(ventana, image= formula, relief="groove", bd="5", bg="blue2").place(x=650, y = 235)
	#*******************TITULO********************
	titulo=tk.Label(ventana,text="AMPLIFICADOR OPERACIONAL - INVERSOR", ancho=tk.CENTER, fg= "white", bg= "RoyalBlue4")
	titulo.config(font=("Bahnschrift SemiLight",15))
	titulo.place(x=250, y=10)

	#*****************BOTONES**********************
	textoresuno = tk.Label(ventana, relief="raised", bg= "orange", text="R1:   ")
	textoresuno.config(font=("Bahnschrift SemiLight",12))
	textoresuno.place(x= 65, y = 70)
	resistenciauno = ttk.Combobox(ventana,state="readonly")
	resistenciauno.place(x=110, y= 70)
	resistenciauno['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8", "8.2", "10", "12", "15",
	"18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180", "220", "270", "330", "390", "470", "510", "560", "680", "820")
	resistenciauno.current(0)
	unidad = ttk.Combobox(ventana,state="readonly")
	unidad.place(x=270,y=70)
	unidad['values']=("1", "1000", "1000000")
	unidad.current(1)

	textoresdos = tk.Label(ventana, relief="raised", bg= "orange", text="R2:  ")
	textoresdos.config(font=("Bahnschrift SemiLight",12))
	textoresdos.place(x= 65, y = 100)
	resistenciados = ttk.Combobox(ventana,state="readonly")
	resistenciados.place(x=110, y= 100)
	resistenciados['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8", "8.2", "10", "12", "15",
	"18", "22", "27", "33", "39", "47", "51", "56", "68", "82", "100", "120", "150", "180", "220", "270", "330", "390", "470", "510", "560", "680", "820")
	resistenciados.current(0)
	unidaddos = ttk.Combobox(ventana,state="readonly")
	unidaddos.place(x=270,y=100)
	unidaddos['values']=("1", "1000", "1000000")
	unidaddos.current(1)


	textovolatje = tk.Label(ventana, relief="raised", bg= "orange", text="Vint:")
	textovolatje.config(font=("Bahnschrift SemiLight",12))
	textovolatje.place(x= 65, y = 130)
	voltaje = ttk.Combobox(ventana,state="readonly")
	voltaje.place(x=110, y =130)
	voltaje['values']=("1", "1.2", "1.5", "1.8", "2.2", "2.7", "3.3", "3.9", "4.7", "5.1", "5.6", "6.8")
	voltaje.current(0)
	unidadtres = ttk.Combobox(ventana,state="readonly")
	unidadtres.place(x=270,y=130)
	unidadtres['values']=("1", "1000", "1000000")
	unidadtres.current(1)

	#********************BOTON DE CALCULAR*********************
	boton = tk.Button(ventana,relief="raised", text="Calcular", command=calculo, bg="green2")
	boton.config(font=("Bahnschrift SemiLight",12))
	boton.place(x = 125, y=180)

	#*******************BOTON DE PAGINA WEB****************************
	boton_pagweb = tk.Button(ventana,relief="raised", text="Pagina Web", command=web, bg="green2")
	boton_pagweb.config(font=("Bahnschrift SemiLight",12))
	boton_pagweb.place(x = 125, y=280)


	resultado = tk.Label(ventana, textvariable=res, fg= "white", bg="RoyalBlue4")
	resultado.config(font=("Bahnschrift SemiLight",15))
	resultado.place(x=60,y=230)
	ventana.mainloop() 
def derivador():
    import tkinter as tk
    from tkinter import messagebox, IntVar
    from typing import Type
    from tkinter import ttk
    import sympy as sy
    import webbrowser

    window = tk.Tk()
    ## definiendo
    valorresistor = tk.DoubleVar()
    valorcapacitor = tk.DoubleVar()
    valorvoltaje = tk.StringVar()
    res = tk.StringVar()

    comboa = tk.DoubleVar()

    ##
    window.title('Amplificador operacional Derivador')
    window.geometry("853x480")
    window.resizable(0, 0)
    window.config(bg="white")
    window.iconbitmap("IMAGENES\\resist.ico")

    ## imagen ##
    imagen = tk.PhotoImage(file="IMAGENES\\fondoderivador.PNG",master= window)
    imagencir = tk.PhotoImage(file='IMAGENES\\CIRCDERIVADOR.PNG',master= window)
    formula = tk.PhotoImage(file='IMAGENES\\FORMULADERIVADOR.png', master = window)
    fondo = tk.Label(window, image = imagen).place(x=0, y = 0 )
    circuitoboton = tk.Label(window, image=imagencir, relief="groove", bd="5", bg="blue2").place(x=320, y = 60)
    forminver = tk.Label(window, image= formula, relief="groove", bd="5", bg="blue2").place(x=625, y = 90)



    #integral
    t=sy.Symbol("t")

    #TITULO
    titulo = tk.Label(window,text="AMPLIFICADOR OPERACIONAL - DERIVADOR", ancho=tk.CENTER, fg= "white", bg= "RoyalBlue4")
    titulo.config(font=("Bahnschrift SemiLight",15))
    titulo.place(x=250, y=10)


    def seleccion11():
        global seleccion_11, valor11
        seleccion_11 = comboa.get()
        if seleccion_11 == "Kohm":
            valor11 = 1000
        if seleccion_11 == "Ohm":
            valor11 = 1
        if seleccion_11 == "Mohm":
            valor11 = 1e6

    def seleccion22():
        global seleccion_22, valor22
        seleccion_22 = combob.get()
        if seleccion_22 == "nF":
            valor22 = 1e-9
        if seleccion_22 == "pF":
            valor22 = 1e-12
        if seleccion_22 == "uF":
            valor22 = 1e-6
    ## funciones ##
    def vres():
        global val1
        val1=valorresistor.get()
    def vcap():
        global val2
        val2=valorcapacitor.get()
    def vvol():
        global val3
        val3=valorvoltaje.get()
    def suma():
        sum = f'El volatje de salida es: {((-1)*val1*val2*valor11*float(valor22)) * sy.diff(val3, t)} vol'
        tk.Label(window,text=sum,fg="white",bg="RoyalBlue4",width=25, height=1).place(x=60, y = 230)

    def web():
        url = ["https://www.tinkercad.com/things/5IFKZBv2XRf-copy-of-derivador-amp-op/editel?tenant=circuits"]

        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(
            "C://Users//Capital PC//AppData//Local//Google//Chrome//Application//chrome.exe"))

        w = webbrowser.get("chrome")
        w.open(url[0])

    ## cajas de resistencias y labels de cajitas
    cuadroTextocapacitor = tk.Spinbox(window, from_=1, to=5000, increment=0.1, textvariable=valorcapacitor)
    cuadroTextocapacitor.config(font=("Bahnschrift SemiLight",12), width = 12)
    cuadroTextocapacitor.place(x=110, y= 100)

    capacitorLabel = tk.Label(window, relief="raised", bg= "orange", text="C:  ")
    capacitorLabel.config(font=("Bahnschrift SemiLight",12))
    capacitorLabel.place(x= 65, y = 100)

    combob = ttk.Combobox(window, state="readonly", values=["pF", "nF", "uF"], width=5)
    combob.config(font=("Bahnschrift SemiLight",12))
    combob.place(x=250, y= 99)

    cuadroTextoresistor = tk.Spinbox(window, from_=1, to=5000, increment=0.1, textvariable=valorresistor)
    cuadroTextoresistor.config(font=("Bahnschrift SemiLight",12), width =12)
    cuadroTextoresistor.place(x=110, y= 70)

    resistorLabel = tk.Label(window, relief="raised", bg= "orange", text="R:  ")
    resistorLabel.config(font=("Bahnschrift SemiLight",12))
    resistorLabel.place(x= 65, y = 70)

    comboa = ttk.Combobox(window, state="readonly", values=["Ohm", "Kohm", "Mohm"], width=5)
    comboa.config(font=("Bahnschrift SemiLight",12))
    comboa.place(x=250, y= 69)

    cuadroTextovoltajein = tk.Entry(window, textvariable=valorvoltaje)
    cuadroTextovoltajein.config(font=("Bahnschrift SemiLight",12))
    cuadroTextovoltajein.place(x=110, y =130)

    voltajeinLabel = tk.Label(window, relief="raised", bg= "orange", text="Vint:")
    voltajeinLabel.config(font=("Bahnschrift SemiLight",12))
    voltajeinLabel.place(x= 65, y = 130)


    ## boton##
    boton = tk.Button(window,relief="raised", text="Calcular", command=suma, bg="green2")
    boton.config(font=("Bahnschrift SemiLight",12))
    boton.place(x = 125, y=200)
    boton1 = tk.Button(window,relief="raised", text="Ingresar Datos", command=lambda:[seleccion11(),seleccion22(),vres(),vcap(),vvol()], bg="#9116C6")
    boton1.config(font=("Bahnschrift SemiLight",10))
    boton1.place(x = 112, y=160)
    boton_pagweb = tk.Button(window,relief="raised", text="Pagina Web", command=web, bg="#12B2BF")
    boton_pagweb.config(font=("Bahnschrift SemiLight",12))
    boton_pagweb.place(x = 115, y=300)

    ## label Resultado##

    resultado = tk.Label(window, textvariable=res, fg= "white", bg="RoyalBlue4")
    resultado.config(font=("Bahnschrift SemiLight",12))
    resultado.place(x=60,y=230)


    window.mainloop()
def integrador():
    import tkinter as tk
    from tkinter import messagebox, IntVar
    from typing import Type
    from tkinter import ttk
    import sympy as sy
    import webbrowser

    ## ventana principal ##


    window = tk.Tk()
    ## definiendo
    valorresistor = tk.DoubleVar()
    valorcapacitor = tk.DoubleVar()
    valorvoltaje = tk.StringVar()
    res = tk.StringVar()



    ##
    window.title('Amplificador operacional Integrador')
    window.geometry("853x480")
    window.resizable(0, 0)
    window.config(bg="white")
    window.iconbitmap("IMAGENES\\resist.ico")

    ## imagen ##
    imagen = tk.PhotoImage(file="IMAGENES\\fondointegrador.png",master= window)
    imagencir = tk.PhotoImage(file='IMAGENES\\CIRINTEGRADOR.png',master= window)
    formula = tk.PhotoImage(file='IMAGENES\\FORMULAINTEGRADOR.png',master= window)
    fondo = tk.Label(window, image = imagen).place(x=0, y = 0 )
    circuitoboton = tk.Label(window, image=imagencir, relief="groove", bd="5", bg="blue2").place(x=320, y = 60)
    forminver = tk.Label(window, image= formula, relief="groove", bd="5", bg="blue2").place(x=625, y = 90)

    #integral
    t=sy.Symbol("t")

    #TITULO
    titulo = tk.Label(window,text="AMPLIFICADOR OPERACIONAL - INTEGRADOR", ancho=tk.CENTER, fg= "white", bg= "RoyalBlue4")
    titulo.config(font=("Bahnschrift SemiLight",15))
    titulo.place(x=250, y=10)


    def seleccion11():
        global seleccion_11, valor11
        seleccion_11 = comboa.get()
        if seleccion_11 == "Kohm":
            valor11 = 1000
        if seleccion_11 == "Ohm":
            valor11 = 1
        if seleccion_11 == "Mohm":
            valor11 = 1e6

    def seleccion22():
        global seleccion_22, valor22
        seleccion_22 = combob.get()
        if seleccion_22 == "nF":
            valor22 = 1e-9
        if seleccion_22 == "pF":
            valor22 = 1e-12
        if seleccion_22 == "uF":
            valor22 = 1e-6
    ## funciones ##
    def vres():
        global val1
        val1=valorresistor.get()
    def vcap():
        global val2
        val2=valorcapacitor.get()
    def vvol():
        global val3
        val3=valorvoltaje.get()
    def suma():

        sum = f'El volatje de salida es:{((-1)*val1*val2*valor11*float(valor22)) * sy.diff(val3, t)} vol'
        tk.Label(window,text=sum,fg="white",bg="RoyalBlue4",width=35, height=1).place(x=60, y = 230)

    def web():
        url = ["https://www.tinkercad.com/things/4H3AHwzflgj-derivador-amp-op/editel"]

        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(
            "C://Users//Capital PC//AppData//Local//Google//Chrome//Application//chrome.exe"))

        w = webbrowser.get("chrome")
        w.open(url[0])

    ## cajas de resistencias y labels de cajitas
    cuadroTextocapacitor = tk.Spinbox(window, from_=1, to=5000, increment=0.1, textvariable=valorcapacitor)
    cuadroTextocapacitor.config(font=("Bahnschrift SemiLight",12), width = 12)
    cuadroTextocapacitor.place(x=110, y= 100)

    capacitorLabel = tk.Label(window, relief="raised", bg= "orange", text="C:  ")
    capacitorLabel.config(font=("Bahnschrift SemiLight",12))
    capacitorLabel.place(x= 65, y = 100)

    combob = ttk.Combobox(window, state="readonly", values=["pF", "nF", "uF"], width=5)
    combob.config(font=("Bahnschrift SemiLight",12))
    combob.place(x=250, y= 99)

    cuadroTextoresistor = tk.Spinbox(window, from_=1, to=5000, increment=0.1, textvariable=valorresistor)
    cuadroTextoresistor.config(font=("Bahnschrift SemiLight",12), width =12)
    cuadroTextoresistor.place(x=110, y= 70)

    resistorLabel = tk.Label(window, relief="raised", bg= "orange", text="R:  ")
    resistorLabel.config(font=("Bahnschrift SemiLight",12))
    resistorLabel.place(x= 65, y = 70)

    comboa = ttk.Combobox(window, state="readonly", values=["Ohm", "Kohm", "Mohm"], width=5)
    comboa.config(font=("Bahnschrift SemiLight",12))
    comboa.place(x=250, y= 69)

    cuadroTextovoltajein = tk.Entry(window, textvariable=valorvoltaje)
    cuadroTextovoltajein.config(font=("Bahnschrift SemiLight",12))
    cuadroTextovoltajein.place(x=110, y =130)

    voltajeinLabel = tk.Label(window, relief="raised", bg= "orange", text="Vint:")
    voltajeinLabel.config(font=("Bahnschrift SemiLight",12))
    voltajeinLabel.place(x= 65, y = 130)
    ## boton##
    boton = tk.Button(window,relief="raised", text="Calcular", command=suma, bg="green2")
    boton.config(font=("Bahnschrift SemiLight",12))
    boton.place(x = 125, y=200)
    boton1 = tk.Button(window,relief="raised", text="Ingresar Datos", command=lambda:[seleccion11(),seleccion22(),vres(),vcap(),vvol()], bg="#9116C6")
    boton1.config(font=("Bahnschrift SemiLight",10))
    boton1.place(x = 112, y=160)
    boton_pagweb = tk.Button(window,relief="raised", text="Pagina Web", command=web, bg="#12B2BF")
    boton_pagweb.config(font=("Bahnschrift SemiLight",12))
    boton_pagweb.place(x = 115, y=300)

    ## label Resultado##

    resultado = tk.Label(window, textvariable=res, fg= "white", bg="RoyalBlue4")
    resultado.config(font=("Bahnschrift SemiLight",12))
    resultado.place(x=60,y=230)


    window.mainloop()

def creditos():
    import tkinter as tk
    from PIL import Image,ImageTk

    class A:
        def __init__(self, ventana1):
            self.ventana = ventana1
            self.ventana.title("Creditos")
            self.ventana.geometry("1300x700")
            
            img = Image.open("Imagenes\Fondo4.jpg")
            img = img.resize((1300, 700),Image.ANTIALIAS)
            self.bg= ImageTk.PhotoImage(img, master=ventana)


            canvas = tk.Canvas(self.ventana)
            x1=200
            x2=600
            x3=700
            x4=745
            x5=670
            y1=120
            y2=200
            y3=280
            y4=325
            y5=370
            y6=415
            y7=460
            y8=505
            y9=585
            y10=665
            canvas.create_image(0, 0, image=self.bg, anchor=tk.NW)
            canvas.create_text(667, 58, text="CRÉDITOS:", font=("Georgia", 45, "bold"), fill='white')
            canvas.create_text(670, 60, text="CRÉDITOS:", font=("Georgia", 45, "bold"), fill='#800000')
            canvas.create_text(x1-2, y1-1, text="Carrera:", font=("Georgia", 30, "bold"), fill='white')
            canvas.create_text(x1, y1, text="Carrera:", font=("Georgia", 30, "bold"), fill='#ff4000')
            canvas.create_text(x1-2, y2-1, text="Materia:", font=("Georgia", 30, "bold"), fill='white')
            canvas.create_text(x1, y2, text="Materia:", font=("Georgia", 30, "bold"), fill='#ff4000')
            canvas.create_text(x1+33, y3-1, text="Integrantes:", font=("Georgia", 30, "bold"), fill='white')
            canvas.create_text(x1+35, y3, text="Integrantes:", font=("Georgia", 30, "bold"), fill='#ff4000')
            canvas.create_text(x2-2, y1-1, text="Ingeniería Electrónica", font=("Georgia", 31), fill='white')
            canvas.create_text(x2, y1, text="Ingeniería Electrónica", font=("Georgia", 31), fill='#9b59b6')
            canvas.create_text(x2-2, y2-1, text="ETN-307  Programación", font=("Georgia", 31), fill='white')
            canvas.create_text(x2, y2, text="ETN-307  Programación", font=("Georgia", 31), fill='#9b59b6')
            canvas.create_text(x3-2, y3-1, text="Univ. Luis Rafael Alberto Limachi", font=("Georgia", 31), fill='white')
            canvas.create_text(x3, y3, text="Univ. Luis Rafael Alberto Limachi", font=("Georgia", 31), fill='#af7ac5')
            canvas.create_text(x4-2, y4-1, text="Univ. Kehizzy Jacqueline Griffiths Alba", font=("Georgia", 31), fill='white')
            canvas.create_text(x4, y4, text="Univ. Kehizzy Jacqueline Griffiths Alba", font=("Georgia", 31), fill='#9b59b6')
            canvas.create_text(x5-2, y5-1, text="Univ. Augusto Bautista Colque", font=("Georgia", 31), fill='white')
            canvas.create_text(x5, y5, text="Univ. Augusto Bautista Colque", font=("Georgia", 31), fill='#af7ac5')
            canvas.create_text(x5+11, y6-1, text="Univ. Aron Rene Quisbert Parra", font=("Georgia", 31), fill='white')
            canvas.create_text(x5+13, y6, text="Univ. Aron Rene Quisbert Parra", font=("Georgia", 31), fill='#9b59b6')
            canvas.create_text(x3-2, y7-1, text="Univ. Carlos Javier Tarqui Ticona", font=("Georgia", 31), fill='white')
            canvas.create_text(x3, y7, text="Univ. Carlos Javier Tarqui Ticona", font=("Georgia", 31), fill='#af7ac5')
            canvas.create_text(x3+18, y8-1, text="Univ. Itamar Esteban Nina Mamani", font=("Georgia", 31), fill='white')
            canvas.create_text(x3+20, y8, text="Univ. Itamar Esteban Nina Mamani", font=("Georgia", 31), fill='#9b59b6')
            canvas.create_text(x1+33, y9-1, text="Agradecimientos:", font=("Georgia", 30, "bold"), fill='white')
            canvas.create_text(x1+35, y9, text="Agradecimientos:", font=("Georgia", 30, "bold"), fill='#ff4000')
            canvas.create_text(x4-2, y9-1, text="Ing. Juan Carlos Duchen Cuellar", font=("Georgia", 31), fill='white')
            canvas.create_text(x4, y9, text="Ing. Juan Carlos Duchen Cuellar", font=("Georgia", 31), fill='#9b59b6')
            canvas.create_text(667, y10, text="UMSA", font=("Georgia", 25, "bold"), fill='white')
            canvas.create_text(670, y10, text="UMSA", font=("Georgia", 25, "bold"), fill='#800000')
            canvas.pack(fill="both", expand=True)
    ventana = tk.Tk()
    obj = A(ventana)
    ventana.mainloop()
  
