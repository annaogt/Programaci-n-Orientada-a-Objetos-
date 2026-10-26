from coches import  coches,cochesbd


class App:
    def __init__(self):
        self.main()
    def esperaTecla (self):
        input("....OPRIMA CUALQUIER TECLA PARA CONTINUAR....")
    def borrarPantalla (self):
        print("\033c")
    def terminar(self):
        input("....gracias por usar el sisitema ")
    def opcInvalida(self):
         input ("...opcion invalida....\npresiona enter para continuar")
    def menuAcciones(self,tipo):
        print(f"\t\t...::::menu de tipo {tipo} :::.... ")
        opcion = input("\n\t1.- agregar  \n\t2.- Borrar \n\t3.- modificar \n\t4.- mostrar \n\t5.-regresar \n\t...seleciona una opcion...." ).strip()
        return opcion
    def respuesta_sql(self,respuesta):
        if respuesta:
            input("\t\t:::accion exitosa:::")
        else:
            input("\t\t:::!camarada al chile no jalo!:::")

    def pedirDatos(self,tipo):
        self.borrarPantalla()
        print(f"\t\t ::: REGISTRAR NUEVO {tipo.upper()} :::")
        marca = input("Ingrese la marca: ").upper().strip()
        color = input("Ingrese el color: ").upper().strip()
        modelo = input("Ingrese el modelo (año): ").upper().strip()
        velocidad = int(input("Ingrese la velocidad: "))
        potencia = int(input("Ingrese la potencia: "))
        asientos = int(input("Ingrese el número de asientos: "))
        regresar = (marca,color, modelo, velocidad, potencia, asientos)
        return regresar
    def menu_coches(self):
        opc = True
        while opc:
            self.borrarPantalla()
            opc = self.menuAcciones('coches')

            match opc:
                case '1':
                    datosCoche = self.pedirDatos("coches")
                    coche1 = cochesbd.Cochesbd(*datosCoche)
                    respuesta = coche1.insertar()
                    self.respuesta_sql(respuesta)
                    del coche1
                case '2':
                    self.borrarPantalla()
                    id = int(input("ingrese el id del coche que desea eliminar....."))
                    coche1 = cochesbd.Cochesbd('','','',0,0,0)
                    respuesta = coche1.eliminar(id)
                    self.respuesta_sql(respuesta)
                    self.esperaTecla()
                    del coche1
                    
                case '3':
                    self.borrarPantalla()
                    id =int( input("ingrese el id del coche que desea actualizar......"))
                    datosCoche = self.pedirDatos("coches")
                    coche1 = cochesbd.Cochesbd(*datosCoche)
                    respuesta = coche1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    self.esperaTecla()
                    del coche1
                case '4':
                    coche1 = cochesbd.Cochesbd('','','',0,0,0)
                    registros = coche1.consultar()
                    if len(registros) > 0:
                        numCoches = 1
                        print(f"\n\tcoche # {numCoches}\n\tID:\ttmarca\ttmarca:\tcolor:\t modelo:\tvelocidad:\t potencia:\tasientos:\n")
                        for fila in registros:
                            print(f"\t{fila[0]} \t {fila[1]}\t {fila[2]}\t {fila[3]}\t\t {fila[4]}\t {fila[5]}\t {fila[6]}") 
                    else:
                        print("no se encontro informacion en la base de datos")
                    self.esperaTecla()
                    del coche1
                case '5':
                    opc = False
                case _:
                    self.opcInvalida()
    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = input("\t\t ::::menu principal:::::\n\t1- Coches\n\t2- salir\n\t elige una opcion....").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_coches()
                    self.esperaTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opcion = False
                case _:
                    self.borrarPantalla()
                    self.opcInvalida()
            
if __name__ == "__main__":
    app = App()