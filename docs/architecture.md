# Arquitectura del Servidor C2 y Payload

Este documento detalla los componentes técnicos del troyano de acceso remoto y su funcionamiento en red.

## 1. Listener del Servidor (C2)
El componente servidor está diseñado para ejecutarse en la máquina del investigador o atacante emulado.
- **Protocolo:** TCP (IPv4)
- **Manejo de Conexiones:** Escucha en un puerto especificado y acepta conexiones entrantes de bots comprometidos.
- **Flujo de Ejecución:**
  1. Bind a interfaz y puerto (ej. `0.0.0.0:4444`).
  2. Queda en estado `LISTEN`.
  3. Al recibir conexión, acepta el socket y entra en un bucle interactivo de comandos `while True`.
  4. Envía strings codificados en UTF-8 al bot.
  5. Recibe el resultado y lo imprime en consola.

## 2. Payload del Cliente (Bot)
El componente cliente se ejecuta en la máquina objetivo.
- **Conexión Inversa (Reverse Shell):** Inicia activamente una conexión hacia la IP/Puerto del C2.
- **Ejecución Local:** 
  - Utiliza librerías como `subprocess` u `os` para ejecutar los comandos recibidos en el shell del sistema operativo host.
  - Captura `stdout` y `stderr` localmente.
- **Retorno de Datos:** Envía la salida de nuevo al C2 a través del socket TCP activo.

## 3. Comandos Soportados
- Peticiones del sistema estándar (dir, ls, ipconfig, ifconfig).
- Cambios de directorio (`cd`).
- Descripción de archivos.

*Nota: La arquitectura y código fuente completo se mantienen únicamente en el repositorio privado de GitLab por razones de seguridad.*
