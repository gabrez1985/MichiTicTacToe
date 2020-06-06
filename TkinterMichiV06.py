from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import messagebox
from FuncionesMichiV01 import *
from _ast import Lambda


def GetImage1():
    global imagenjugador1
    imagenjugador1 = GetImageFromFolder()
    if imagenjugador1 != "":
        messagebox.showinfo("Seleccion Foto", "Foto Seleccionada Correctamente")
        imagen = Image.open(imagenjugador1)
        imagen.show()
    else:
        messagebox.showinfo("Seleccion Foto", "Volver a Intentar")


def GetImage2():
    global imagenjugador2
    imagenjugador2 = GetImageFromFolder()
    if imagenjugador2 != "":
        messagebox.showinfo("Seleccion Foto", "Foto Seleccionada Correctamente")
        imagen = Image.open(imagenjugador2)
        imagen.show()
    else:
        messagebox.showinfo("Seleccion Foto", "Volver a Intentar")


def IrAPantallaDeInicioPrograma():
    global EntryNombreJugador1
    global EntryNombreJugador2

    LabelInicial = Label(root, text='Ingrese datos de Jugadores en las' +
                                    'casillas de abajo')
    LabelInicial.grid(row=0, column=0, columnspan=2)

    LabelNombreJugador1 = Label(root, text='Ingrese Nombre Jugador1: ')
    LabelNombreJugador1.grid(row=1, column=0)

    LabelNombreJugador2 = Label(root, text='Ingrese Nombre Jugador2: ')
    LabelNombreJugador2.grid(row=2, column=0)

    EntryNombreJugador1 = Entry(root)
    EntryNombreJugador1.grid(row=1, column=1)

    EntryNombreJugador2 = Entry(root)
    EntryNombreJugador2.grid(row=2, column=1)

    LabelImagenJugador1 = Label(root, text='    Pulse boton para ingresar' +
                                           'imagen Jugador1: ')
    LabelImagenJugador1.grid(row=1, column=2)

    LabelImagenJugador2 = Label(root, text='    Pulse boton para ingresar' +
                                           'imagen Jugador2: ')
    LabelImagenJugador2.grid(row=2, column=2)

    BotonImagenJugador1 = Button(root, text='Abrir',
                                 command=GetImage1)
    BotonImagenJugador1.grid(row=1, column=3)

    BotonImagenJugador2 = Button(root, text='Abrir',
                                 command=GetImage2)
    BotonImagenJugador2.grid(row=2, column=3)

    BotonIniciarJuego = Button(root, text='IniciarJuego',
                               command=IrAPantallaInicioJuego)
    BotonIniciarJuego.grid(row=3, column=0)


def IrAPantallaInicioJuego():
    global Imagen1
    global Imagen2
    global ImagenJ1
    global ImagenJ2
    global jugadorqueiniciapartida
    global puntajejugador1
    global puntajejugador2
    global nombrejugador1
    global nombrejugador2
    global imagenjugador1
    global imagenjugador2

    nombrejugador1 = EntryNombreJugador1.get()   
    if nombrejugador1 == "":
        nombrejugador1 = 'Jugador1'

    nombrejugador2 = EntryNombreJugador2.get()
    if nombrejugador2 == "":
        nombrejugador2 = 'Jugador2'

    for widget in root.winfo_children():
        widget.destroy()

    puntajejugador1 = 0
    puntajejugador2 = 0

    jugadorqueiniciapartida = 2

    LabelNombreJugador1 = Label(root, text="   " + nombrejugador1 + "  ")
    LabelNombreJugador1.grid(row=0, column=0)

    LabelNombreJugador2 = Label(root, text="   " + nombrejugador2 + "  ")
    LabelNombreJugador2.grid(row=1, column=0)

    try:
        Imagen1 = Image.open(imagenjugador1)
        Imagen1.thumbnail((50, 50))
        Imagen1 = ImageTk.PhotoImage(Imagen1)
        LabelImagen1 = Label(root, image=Imagen1)
        LabelImagen1.grid(row=0, column=1)
    except:
        Imagen1 = Image.open('Anto.jpg')
        Imagen1.thumbnail((50, 50))
        Imagen1 = ImageTk.PhotoImage(Imagen1)
        LabelImagen1 = Label(root, image=Imagen1)
        LabelImagen1.grid(row=0, column=1)    

    try:
        Imagen2 = Image.open(imagenjugador2)
        Imagen2.thumbnail((50, 50))
        Imagen2 = ImageTk.PhotoImage(Imagen2)
        LabelImagen2 = Label(root, image=Imagen2)
        LabelImagen2.grid(row=1, column=1)
    except:
        Imagen2 = Image.open('AntoN10.png')
        Imagen2.thumbnail((50, 50))
        Imagen2 = ImageTk.PhotoImage(Imagen2)
        LabelImagen2 = Label(root, image=Imagen2)
        LabelImagen2.grid(row=1, column=1)

    ImagenJ1 = Image.open(imagenjugador1)
    ImagenJ1.thumbnail((tamanoimagenjugador, tamanoimagenjugador))

    ImagenJ2 = Image.open(imagenjugador2)
    ImagenJ2.thumbnail((tamanoimagenjugador, tamanoimagenjugador))

    IrAPantallaDeInicioPartida()


def IrAPantallaDeInicioPartida():
    global ImagenMichi
    global ImagenMichiTk
    global jugadorqueiniciapartida
    global LabelImagenMichi
    global Boton11
    global Boton12
    global Boton13
    global Boton21
    global Boton22
    global Boton23
    global Boton31
    global Boton32
    global Boton33
    global posicionesjugador1
    global posicionesjugador2
    global turnojugador
    global LabelTurno

    posicionesjugador1 = []
    posicionesjugador2 = []

    jugadorqueiniciapartida = cambioturnojugador(jugadorqueiniciapartida)

    turnojugador = jugadorqueiniciapartida

    if turnojugador == 1:
        texto = "Turno Jugador: " + nombrejugador1
    elif turnojugador ==2:
        texto = "Turno Jugador: " + nombrejugador2
    LabelTurno = Label(root, text=texto)
    LabelTurno.grid(row=0, column=4)

    LabelPuntajeJugador1 = Label(root, text='   Puntaje ' + nombrejugador1 +
                                 ":   " + str(puntajejugador1))
    LabelPuntajeJugador1.grid(row=0, column=2)

    LabelPuntajeJugador2 = Label(root, text='   Puntaje ' + nombrejugador2 +
                                 ":   " + str(puntajejugador2))
    LabelPuntajeJugador2.grid(row=1, column=2)

    try:
        LabelImagenMichi.destroy()
    except:
        pass

    ImagenMichi = create_image(600, 600, (255, 255, 255, 255))
    Imagenlineavertical = create_image(5, 600, (0, 0, 0, 255))
    Imagenlineahorizontal = create_image(600, 5, (0, 0, 0, 255))
    ImagenMichi.paste(Imagenlineavertical, (195, 0, 200, 600))
    ImagenMichi.paste(Imagenlineavertical, (395, 0, 400, 600))
    ImagenMichi.paste(Imagenlineahorizontal, (0, 195, 600, 200))
    ImagenMichi.paste(Imagenlineahorizontal, (0, 395, 600, 400))
    ImagenMichiTk = ImageTk.PhotoImage(ImagenMichi)
    LabelImagenMichi = Label(root, image=ImagenMichiTk)
    LabelImagenMichi.grid(row=2, column=3)

    Boton11 = Button(root, padx=10, pady=5, text='11',
                     command=lambda: JugadaJugador('11'))
    Boton11.grid(row=2, column=3, sticky=SW, padx=80, pady=0)

    Boton12 = Button(root, padx=10, pady=5, text='12',
                     command=lambda: JugadaJugador('12'))
    Boton12.grid(row=2, column=3, sticky=SW, padx=80, pady=220)

    Boton13 = Button(root, padx=10, pady=5, text='13',
                     command=lambda: JugadaJugador('13'))
    Boton13.grid(row=2, column=3, sticky=NW, padx=80, pady=0)

    Boton21 = Button(root, padx=10, pady=5, text='21',
                     command=lambda: JugadaJugador('21'))
    Boton21.grid(row=2, column=3, sticky=SW, padx=280, pady=0)

    Boton22 = Button(root, padx=10, pady=5, text='22',
                     command=lambda: JugadaJugador('22'))
    Boton22.grid(row=2, column=3, sticky=SW, padx=280, pady=220)

    Boton23 = Button(root, padx=10, pady=5, text='23',
                     command=lambda: JugadaJugador('23'))
    Boton23.grid(row=2, column=3, sticky=NW, padx=280, pady=0)

    Boton31 = Button(root, padx=10, pady=5, text='31',
                     command=lambda: JugadaJugador('31'))
    Boton31.grid(row=2, column=3, sticky=SE, padx=80, pady=0)

    Boton32 = Button(root, padx=10, pady=5, text='32',
                     command=lambda: JugadaJugador('32'))
    Boton32.grid(row=2, column=3, sticky=SE, padx=80, pady=220)

    Boton33 = Button(root, padx=10, pady=5, text='33',
                     command=lambda: JugadaJugador('33'))
    Boton33.grid(row=2, column=3, sticky=NE, padx=80, pady=0)


def JugadaJugador(posicionjugador):
    global ImagenMichi
    global ImagenMichiTk
    global ImagenJ1
    global ImagenJ2
    global imagenjugador1
    global imagenjugador2
    global LabelImagenMichi
    global turnojugador
    global Boton11
    global Boton12
    global Boton13
    global Boton21
    global Boton22
    global Boton23
    global Boton31
    global Boton32
    global Boton33
    global Boton33
    global posicionesjugador1
    global posicionesjugador2
    global puntajejugador1
    global puntajejugador2
    global LabelTurno

    if turnojugador == 1:
        posicionesjugador1.append(posicionjugador)

    elif turnojugador == 2:
        posicionesjugador2.append(posicionjugador)

    ImagenJ1 = Image.open(imagenjugador1)
    ImagenJ1.thumbnail((tamanoimagenjugador, tamanoimagenjugador))
    anchoImagen1, largoImagen1 = ImagenJ1.size

    ImagenJ2 = Image.open(imagenjugador2)
    ImagenJ2.thumbnail((tamanoimagenjugador, tamanoimagenjugador))
    anchoImagen2, largoImagen2 = ImagenJ2.size

    LabelImagenMichi.destroy()

    for a in posicionesjugador1:
        ubicacionx = diccionariox[a]
        ubicaciony = diccionarioy[a]
        ImagenMichi.paste(ImagenJ1, (ubicacionx, ubicaciony, ubicacionx + anchoImagen1, ubicaciony + largoImagen1))

    for b in posicionesjugador2:
        ubicacionx = diccionariox[b]
        ubicaciony = diccionarioy[b]
        ImagenMichi.paste(ImagenJ2, (ubicacionx, ubicaciony, ubicacionx + anchoImagen2, ubicaciony + largoImagen2))

    ImagenMichiTk = ImageTk.PhotoImage(ImagenMichi)
    LabelImagenMichi = Label(root, image=ImagenMichiTk)
    LabelImagenMichi.grid(row=2, column=3)
    LabelImagenMichi.lower()
    # lower , y lift sirven para poner abajo o arriba de los otros widgets en la misma ubicacion

    if posicionjugador == '11':
        Boton11['state'] = DISABLED
    elif posicionjugador == '12':
        Boton12['state'] = DISABLED
    elif posicionjugador == '13':
        Boton13['state'] = DISABLED
    elif posicionjugador == '21':
        Boton21['state'] = DISABLED
    elif posicionjugador == '22':
        Boton22['state'] = DISABLED
    elif posicionjugador == '23':
        Boton23['state'] = DISABLED
    elif posicionjugador == '31':
        Boton31['state'] = DISABLED
    elif posicionjugador == '32':
        Boton32['state'] = DISABLED
    elif posicionjugador == '33':
        Boton33['state'] = DISABLED

    turnojugador = cambioturnojugador(turnojugador)

    try:
        LabelTurno.destroy()
    except:
        pass
    
    if turnojugador == 1:
        texto = "Turno Jugador: " + nombrejugador1
    elif turnojugador ==2:
        texto = "Turno Jugador: " + nombrejugador2
    LabelTurno = Label(root, text=texto)
    LabelTurno.grid(row=0, column=4)

    if esmichi(posicionesjugador1) == "MICHI GANADOR":
        messagebox.showinfo("Ganador", "MICHI - GANADOR JUGADOR 1: " + nombrejugador1)
        puntajejugador1 = puntajejugador1 + 1
        IrAPantallaDeInicioPartida()

    if esmichi(posicionesjugador2) == "MICHI GANADOR":
        messagebox.showinfo("Ganador", "MICHI - GANADOR JUGADOR 2: " + nombrejugador2)
        puntajejugador2 = puntajejugador2 + 1
        IrAPantallaDeInicioPartida()

    if (len(posicionesjugador1)+len(posicionesjugador2)) == 9 and esmichi(posicionesjugador1) == "NO" and esmichi(posicionesjugador2) == "NO":
        IrAPantallaDeInicioPartida()
        messagebox.showinfo("Empate", "Se ha empatado la partida")

root = Tk()
root.title(" Michi")
root.geometry("800x600")

imagenjugador1 = StringVar
imagenjugador2 = StringVar
Imagen1 = StringVar
Imagen2 = StringVar
ImagenJ1 = StringVar
ImagenJ2 = StringVar
ImagenMichi = StringVar
ImagenMichiTk = StringVar

EntryNombreJugador1 = StringVar
EntryNombreJugador2 = StringVar

LabelImagenMichi = StringVar
LabelTurno = StringVar

puntajejugador1 = IntVar
puntajejugador2 = IntVar
jugadorqueiniciapartida = IntVar
turnojugador = IntVar

nombrejugador1 = StringVar
nombrejugador2 = StringVar

Boton11 = StringVar
Boton12 = StringVar
Boton13 = StringVar
Boton21 = StringVar
Boton22 = StringVar
Boton23 = StringVar
Boton31 = StringVar
Boton32 = StringVar
Boton33 = StringVar

posicionesjugador1 = StringVar
posicionesjugador2 = StringVar

tamanoimagenjugador = 80
imagenjugador1 = 'Anto.jpg'
imagenjugador2 = 'AntoN10.png'
diccionariox = {'11': 40, '12': 40, '13': 40, '21': 240, '22': 240, '23': 240, '31': 440, '32': 440, '33': 440 }
diccionarioy = {'11': 440, '12': 240, '13': 40, '21': 440, '22': 240, '23': 40, '31': 440, '32': 240, '33': 40 }

IrAPantallaDeInicioPrograma()

root.mainloop()
