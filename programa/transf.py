# transferencia.py
from db import conectar_bd
from usuario import Usuario

def realizar_transferencia():
    """Realiza una transferencia entre dos usuarios y muestra mensajes específicos."""
    nombre_usuario_remitente = input("Ingrese el nombre de usuario del remitente: ")
    nombre_usuario_receptor = input("Ingrese el nombre de usuario del receptor: ")
    monto = float(input("Ingrese el monto a transferir: "))

    remitente = Usuario.obtener_usuario_por_nombre(nombre_usuario_remitente)
    receptor = Usuario.obtener_usuario_por_nombre(nombre_usuario_receptor)

    if remitente is None:
        print("El remitente no existe o el nombre de usuario es incorrecto.")
        return
    
    if receptor is None:
        print("El receptor no existe o el nombre de usuario es incorrecto.")
        return
    
    if remitente[1] < monto:
        print("Fondos insuficientes.")
        return

    conn = conectar_bd()
    cur = conn.cursor()
    try:
        Usuario.actualizar_saldo(remitente[0], -monto)
        Usuario.actualizar_saldo(receptor[0], monto)
        
        cur.execute("INSERT INTO transferencias (id_remitente, id_receptor, monto) VALUES (%s, %s, %s)",
                    (remitente[0], receptor[0], monto))
        conn.commit()
        print("Transferencia completada exitosamente.")
    except Exception as e:
        print(f"Error al realizar la transferencia: {e}")
    finally:
        cur.close()
        conn.close()
