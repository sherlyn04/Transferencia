# principal.py
from usuario import Usuario
from transf import realizar_transferencia

def registrar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    nombre_completo = input("Ingrese su nombre completo: ")
    num_cedula = input("Ingrese su número de cédula: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    Usuario.registrar_usuario(nombre_usuario, contrasena, nombre_completo, num_cedula, saldo_inicial)

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrarse")
        print("2. Hacer transferencia")

        eleccion = input("Seleccione una opción (1/2): ")
        if eleccion == '1':
            registrar_usuario()
        elif eleccion == '2':
            realizar_transferencia()
        else:
            print("Opción inválida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
