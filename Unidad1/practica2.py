"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
#para usar un metodo privado se pone 'self._'
#para que sea publico se pone 'self.color'
class Coches:
    def __init__(self,color,marca,velocidad):
        self._color=color
        self._modelo=marca
        self._velocidad=velocidad

    def acelerar(self):
        pass

    def frenar(self):
        pass

    def tocar_claxon(self):
        pass


#Instanciar o crear objetos de la clase Coches
coche1=Coches('Blanco','VW',220)
coche2=Coches('Azul','Nissan',180)
print(f"El color del coche 1 es: ")









