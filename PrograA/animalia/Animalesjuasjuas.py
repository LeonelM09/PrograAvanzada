class Animales:
    def __init__(self,nombre,color,patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas

    def sonido_generico(self):
        print(f"imprimir sondio generico")

class Conejo(Animales):
    def sonido_conejo(self):
        print("squick squick")
    def caract(self):
        print(f"Mi conejo se llama {self.nombre}, es de color {self.color} y tiene {self.patas} patas")

class Ornitorrinco(Animales):
    def __init__(self, nombre, color, patas, pico):
        super().__init__(nombre, color, patas)
        self.pico=pico

    def caract(self):
        print(f"Mi ornitorrinco se llama {self.nombre}, es color {self.color}, tiene {self.patas} y su pico mide {self.pico}")

class Dinosaurio(Animales)
    def __init__(self, nombre, color, patas):
        super().__init__(nombre, color, patas, tipo)
        self.tipo=Dinosaurio

    def caract