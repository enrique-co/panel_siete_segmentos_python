""" 
panel_7_segmentos.py
Panel numérico que simula los paneles led de los dispositivos electrónicos.

La lista "numeros" es una lista de listas que contiene cada línea del número
por separado.
El funcionamieto es el siguiente:

para cada linea del rango (5):
    linea = "" 
    para cada digito del -numero introducido-:
        se concatena a la línea el elemento numeros[numero][linea]
        se concatena a la línea un espacio en blanco
    imprimir linea

Nota importante:
Solo funciona con números enteros. Si se introduce un decimal salta
una excepción:
    ValueError: invalid literal for int() with base 10: '.'
"""




NUMEROS = [
    [
        "###",
        "# #",
        "# #",
        "# #",
        "###"
    ],
    [
        "#",
        "#",
        "#",
        "#",
        "#"
    ],
    [
        "###",
        "  #",
        "###",
        "#  ",
        "###"
    ],
    [
        "###",
        "  #",
        "###",
        "  #",
        "###",
    ],
    [
        "# #",
        "# #",
        "###",
        "  #",
        "  #"
    ],
    [
        "###",
        "#  ",
        "###",
        "  #",
        "###"
    ],
    [
        "###",
        "#  ",
        "###",
        "# #",
        "###"
    ],
    [
        "###",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    [
        "###",
        "# #",
        "###",
        "# #",
        "###"
    ],
    [
        "###",
        "# #",
        "###",
        "  #",
        "  #"
    ]

]

def imprimePanel(numeros, numero=None):

    
    for i in range(5):
        linea = ""                   # Línea vacía
        for num in numero:           # Se comienza a recorrer el número indicado
            num= int(num)            # El número se convierte a entero
            linea += numeros[num][i]   # Se añade el número a la línea
            linea += "  "               # Se añade un espacio en blanco.
        print(linea)                 # Se la línea creada.



if __name__ == "__main__":
    numero = input("Introduce un número: ")
    imprimePanel(NUMEROS, numero)
