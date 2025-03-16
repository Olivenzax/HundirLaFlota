# Clases:

## Solo está Barco


class Barco:
    def __init__(self, nombre:str, num_casillas:int):
        self.nombre = nombre
        self.num_casillas = num_casillas
fragata = Barco("Fragata", 1)
destructor = Barco("Destructor", 2)
acorazado = Barco("Acorazado", 3)
portaaviones = Barco("Portaaviones", 4)        
