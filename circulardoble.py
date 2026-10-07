class Nodo:
    def __init__(self , cancion ):
        self.cancion = cancion
        self.siguiente = None
        self.siguiente = None


cancion1 = Nodo("Un rey sin reina")
cancion2 = Nodo("No te contaron mal")
cancion3 = Nodo("dont worry be happy")


cancion1.siguiente = cancion2
cancion2.siguiente = cancion3
cancion3.siguiente = cancion1


cancion1.anterior = cancion3
cancion2.anterior = cancion1
cancion3.anterior = cancion2


print("Canción actual:", cancion1.cancion)

print("Siguiente:", cancion1.siguiente.cancion)

print("Siguiente:", cancion1.siguiente.siguiente.cancion)

print("Siguiente:", cancion1.siguiente.siguiente.siguiente.cancion)



print("Anterior:", cancion1.anterior.cancion)