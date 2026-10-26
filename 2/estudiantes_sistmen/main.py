from estudiantes import estudiante

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
        nombre = input("Ingrese el nombre de estudiante: ").upper().strip()
        notas = input("Ingrese la nota: ").upper().strip()
        regresar = (nombre,notas)
        return regresar
    def menu_estudiantes(self):
        opc = True
        while opc:
            self.borrarPantalla()
            opc = self.menuAcciones('estudiantes')

            match opc:
                case '1':
                    datosEstudiante = self.pedirDatos("Estudiantes")
                    # Estudiante1 = estudiante.Estudiantes(*datosEstudiante)
                    respuesta = estudiante.Estudiantes(*datosEstudiante).insertar()
                    self.respuesta_sql(respuesta)
                    # del Estudiante1
                case '2':
                    self.borrarPantalla()
                    id = int(input("ingrese el id del estudiante que desea eliminar....."))
                    # Estudiante1 = estudiante.Estudiantes('',0)
                    
                    respuesta = estudiante.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                    self.esperaTecla()
                    # del Estudiante1
                    
                case '3':
                    self.borrarPantalla()
                    id =int(input("ingrese el id del estudiante que desea eliminar....."))
                    datosEstudiante = self.pedirDatos("Estudiantes")
                    # Estudiante1 = estudiante.Estudiantes(*datosEstudiante)
                    
                    respuesta = estudiante.Estudiantes(*datosEstudiante).actualizar(id)
                    self.respuesta_sql(respuesta)
                    self.esperaTecla()
                    # del Estudiante1
                case '4':
                    # Estudiante1 = estudiante.Estudiantes('',0)
                    
                    registros = estudiante.Estudiantes.consultar()
                    if len(registros) > 0:
                        numEstudiantes = 1
                        print(f"\n\testudiante # {numEstudiantes}\n\tID:\tnombre: \tnota: \n")
                        for fila in registros:
                            print(f"\t{fila[0]} \t {fila[1]}\t {fila[2]}") 
                    else:
                        print("no se encontro informacion en la base de datos")
                    self.esperaTecla()
                    # del Estudiante1
                case '5':
                    opc = False
                case _:
                    self.opcInvalida()
    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = input("\t\t ::::menu principal:::::\n\t1- Estudiante\n\t2- salir\n\t elige una opcion....").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiantes()
                    self.esperaTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opcion = False
                case _:
                    self.borrarPantalla()
                    self.opcInvalida()



if __name__=="__main__":
    app=App()