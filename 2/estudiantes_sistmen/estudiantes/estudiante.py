from conexionBD import conexion, cursor

class Estudiantes:
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota

    @property
    def nombre(self):
        return self._nombre
    @property
    def nota(self):
            return self._nota

    @nombre.setter
    def nombre(self,nombre):
            self._nombre=nombre

    @nota.setter
    def nota(self,nota):
            self._nota=nota

    def insertar(self):
        try:
            sql = "INSERT INTO estudiante VALUES (null, %s, %s)"
            valores = (self._nombre, self._nota)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM estudiante")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar: {e}")
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM estudiante WHERE id = %s", (id,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False

    def actualizar(self, id):
        try:
          
            sql = "UPDATE estudiante SET nombre = %s, nota = %s WHERE id = %s"
            valores = (self._nombre, self._nota, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
