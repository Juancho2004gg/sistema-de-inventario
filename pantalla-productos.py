
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rosit\Escritorio\TEORIA DE SISTEMAS\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x729")
window.configure(bg = "#4B0082")


canvas = Canvas(
    window,
    bg = "#4B0082",
    height = 729,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    248.0,
    0.0,
    1000.0,
    729.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    248.0,
    729.0,
    fill="#008282",
    outline="")

canvas.create_rectangle(
    26.0,
    239.0,
    224.0,
    290.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    26.0,
    314.0,
    224.0,
    358.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    26.0,
    388.0,
    224.0,
    433.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    26.0,
    464.0,
    224.0,
    509.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    26.0,
    548.0,
    224.0,
    593.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    26.0,
    624.0,
    224.0,
    669.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    54.0,
    248.0,
    anchor="nw",
    text="Dashboard",
    fill="#000000",
    font=("Inter ExtraLightItalic", 25 * -1)
)

canvas.create_text(
    62.0,
    319.0,
    anchor="nw",
    text="Inventario",
    fill="#000000",
    font=("Inter ExtraLightItalic", 25 * -1)
)

canvas.create_text(
    78.0,
    394.0,
    anchor="nw",
    text="Ventas",
    fill="#000000",
    font=("Inter ExtraLightItalic", 25 * -1)
)

canvas.create_text(
    45.0,
    470.0,
    anchor="nw",
    text="Devoluciones",
    fill="#000000",
    font=("Inter ExtraLightItalic", 25 * -1)
)

canvas.create_text(
    62.0,
    552.0,
    anchor="nw",
    text="Productos",
    fill="#000000",
    font=("Inter ExtraLightItalic", 25 * -1)
)

canvas.create_text(
    62.0,
    629.0,
    anchor="nw",
    text="Clientes",
    fill="#000000",
    font=("Inter ExtraLightItalic", 25 * -1)
)

canvas.create_text(
    48.0,
    724.0,
    anchor="nw",
    text="Cerrar sesión",
    fill="#FFFFFF",
    font=("Inter ExtraLightItalic", 25 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    125.0,
    116.0,
    image=image_image_1
)

canvas.create_rectangle(
    272.0,
    193.0,
    947.0,
    495.0,
    fill="#00827A",
    outline="")

canvas.create_rectangle(
    272.0,
    144.0,
    947.0,
    193.0,
    fill="#210082",
    outline="")

canvas.create_text(
    282.0,
    159.0,
    anchor="nw",
    text="ProductoID",
    fill="#FFFFFF",
    font=("Inter ExtraLightItalic", 15 * -1)
)

canvas.create_text(
    380.0,
    159.0,
    anchor="nw",
    text="Nombre",
    fill="#FFFFFF",
    font=("Inter ExtraLightItalic", 15 * -1)
)

canvas.create_text(
    489.0,
    159.0,
    anchor="nw",
    text="Descripcion",
    fill="#FFFFFF",
    font=("Inter ExtraLightItalic", 15 * -1)
)

canvas.create_text(
    666.0,
    159.0,
    anchor="nw",
    text="CategoriaID",
    fill="#FFFFFF",
    font=("Inter ExtraLightItalic", 15 * -1)
)

canvas.create_text(
    857.0,
    159.0,
    anchor="nw",
    text="Precio",
    fill="#FFFFFF",
    font=("Inter ExtraLightItalic", 15 * -1)
)

canvas.create_rectangle(
    380.0,
    542.0,
    493.0,
    592.0,
    fill="#008282",
    outline="")

canvas.create_text(
    402.0,
    558.0,
    anchor="nw",
    text="Modificar",
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_rectangle(
    536.0,
    543.0,
    654.0,
    593.0,
    fill="#008282",
    outline="")

canvas.create_rectangle(
    704.0,
    543.0,
    822.0,
    593.0,
    fill="#008282",
    outline="")

canvas.create_text(
    567.0,
    559.0,
    anchor="nw",
    text="Eliminar",
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    733.0,
    559.0,
    anchor="nw",
    text="Agregar",
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_rectangle(
    272.0,
    58.0,
    498.0,
    108.0,
    fill="#008282",
    outline="")

canvas.create_text(
    284.0,
    68.0,
    anchor="nw",
    text="Mostrar variantes de producto",
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)
window.resizable(False, False)
window.mainloop()