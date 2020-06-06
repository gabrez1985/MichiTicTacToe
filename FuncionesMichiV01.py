import os
from tkinter import filedialog
from PIL import Image, ImageOps, ImageColor


def GetImageFromFolder():
    currentdirectory = os.getcwd()
    imglocation = filedialog.askopenfilename(initialdir=currentdirectory,
                                             title='Select a File',
                                             filetypes=(('jpg files', '*.jpg'),
                                                        ('png files', '*.png'),
                                                        ('all files', '*.*')))
    return imglocation


def cambioturnojugador(turnojugadoractual):
    if turnojugadoractual == 1:
        turnojugador = 2
    elif turnojugadoractual == 2:
        turnojugador = 1
    else:
        turnojugador = 0
    return turnojugador


def create_image(i, j, color=(255, 255, 255, 255)):
    image = Image.new("RGBA", (i, j), color)
    return image


def esmichi(posicionesjugador):
    posicionesmichi = [('11', '21', '31'), ('12', '22', '32'), ('13', '23', '33'),
                       ('11', '12', '13'), ('21', '22', '23'), ('31', '32', '33'),
                       ('11', '22', '33'), ('13', '22', '31')]
    respuesta = "NO"
    for a in posicionesmichi:
        if a[0] in posicionesjugador and a[1] in posicionesjugador and a[2] in posicionesjugador:
            respuesta = "MICHI GANADOR"

    return respuesta
