"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares (marca,color,modelo,velocidad,potencia,asientos) y con los operaciones de acelerar y frenar. Que los atributos y metodos sean publicos.
#Muestre el color de los coches
#Que los operaciones disminuyan o aumenten la velocidad segun sea el caso y hay jugar con los metodos e imprimes la velocidad final
#Los metodos privados no se puedn usar afuera de la calse
class Coches:
    marca=""
    color="Blanco"
    modelo=''
    velocidad=100
    potencia=0
    asientos=0

    def acelerar(self):
        self.velocidad+=1
        print(f'Ahora la velocidad es de: {self.velocidad}')

    def frenar(self):
        self.velocidad-=1
        print(f'Ahora la velocidad es de: {self.velocidad}')

coche1=Coches()
coche2=Coches()

print(f'El color del coche 1 es: {coche1.color}')
print(f'El color del coche 2 es: {coche2.color}')



for i in range(1,11):
    coche1.acelerar()