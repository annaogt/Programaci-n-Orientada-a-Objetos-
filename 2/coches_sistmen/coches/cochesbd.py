from conexionBD import conexion, cursor 

class Cochesbd:
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad 
        self._potencia = potencia
        self._asientos = asientos
        

    def insertar(self):
        try:
            sql = "INSERT INTO coches VALUES (null, %s, %s, %s, %s, %s, %s)"
            valores = (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}") # Esto te dirá exactamente por qué falla
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from coches where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False
    def actualizar(self, id):
        try:
            # Quitamos la coma extra antes de WHERE
            sql = "UPDATE coches SET marca = %s, color = %s, modelo = %s, velocidad = %s, potencia = %s, asientos = %s WHERE id = %s"
            valores = (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
            return True
        except:
            return False