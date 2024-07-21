# usuario.py
import bcrypt
from db import conectar_bd

class Usuario:
    @staticmethod
    def registrar_usuario(nombre_usuario, contrasena, nombre_completo, num_cedula, saldo_inicial):
        """Registra un nuevo usuario en la base de datos y muestra un mensaje."""
        conn = conectar_bd()
        cur = conn.cursor()
        contrasena_hash = bcrypt.hashpw(contrasena.encode(), bcrypt.gensalt())
        try:
            cur.execute(
                "INSERT INTO usuarios (nombre_usuario, contrasena, nombre_completo, num_cedula, saldo) VALUES (%s, %s, %s, %s, %s)",
                (nombre_usuario, contrasena_hash, nombre_completo, num_cedula, saldo_inicial)
            )
            conn.commit()
            print("Usuario registrado correctamente.")
        except Exception as e:
            print(f"Error al registrar el usuario: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def obtener_usuario_por_nombre(nombre_usuario):
        """Obtiene un usuario por su nombre de usuario."""
        conn = conectar_bd()
        cur = conn.cursor()
        try:
            cur.execute("SELECT id, saldo FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
            return cur.fetchone()
        except Exception as e:
            print(f"Error al obtener el usuario: {e}")
        finally:
            cur.close()
            conn.close()
        return None

    @staticmethod
    def actualizar_saldo(id_usuario, monto):
        """Actualiza el saldo de un usuario y muestra un mensaje de éxito o error."""
        conn = conectar_bd()
        cur = conn.cursor()
        try:
            cur.execute("UPDATE usuarios SET saldo = saldo + %s WHERE id = %s", (monto, id_usuario))
            conn.commit()
        except Exception as e:
            print(f"Error al actualizar el saldo: {e}")
        finally:
            cur.close()
            conn.close()
