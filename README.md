# 🛡️ Troyano — RAT & Framework C2 en Python

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=flat&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Tipo-Malware%20Research-critical?style=flat&logo=hackthebox&logoColor=white)
![GitHub](https://img.shields.io/badge/Repository-GitHub-blue?style=flat&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-blue?style=flat&logo=creativecommons&logoColor=white)

> ⚠️ **AVISO ÉTICO:** Este proyecto es de uso estrictamente educativo y para investigación en ciberseguridad defensiva. El autor no se responsabiliza por el uso indebido de este material fuera de entornos autorizados y controlados.

---

## 🧠 Overview

Este proyecto es un **Remote Access Trojan (RAT)** de investigación desarrollado íntegramente en Python, diseñado para funcionar sobre sistemas **Windows 10**. Implementa una arquitectura clásica de **Comando y Control (C2)** basada en comunicación TCP/IP, con el objetivo de estudiar, desde una perspectiva técnica ofensiva-defensiva, los vectores de ataque utilizados por malware real en entornos controlados de laboratorio.

Este proyecto parece estar orientado tanto a la **investigación personal en malware** como a la **demostración de buenas prácticas de seguridad en el ciclo de desarrollo**.

---

## ⚙️ Features

- **Arquitectura C2 Cliente-Servidor** implementada sobre sockets TCP/IP nativos de Python, permitiendo control remoto de sistemas objetivo en red.
- **Payload del lado cliente** (`src/payload/`) diseñado para ejecución en máquinas Windows 10, encargado de establecer la conexión reversa hacia el listener.
- **Servidor Listener C2** (`src/server/`) responsable de recibir conexiones entrantes, emitir comandos y gestionar las sesiones activas.
- **Ofuscación del payload** mediante integración con **PyArmor**, dificultando el análisis estático y la detección por soluciones antivirus convencionales.
- **Estructura profesional de proyecto** con separación por responsabilidades: código fuente, datos de laboratorio, diagramas de arquitectura y documentación técnica.
- **Gestión segura de secretos** mediante `.gitignore` estricto que excluye credenciales, claves `.pem`, configuraciones de red y archivos `.env`.

---

## 🛠️ Tech Stack

| Componente | Tecnología |
|---|---|
| Lenguaje principal | Python 3.12+ |
| Comunicación de red | Sockets TCP/IP (stdlib) |
| Ofuscación de payload | PyArmor |
| Empaquetado / compilación | PyInstaller |
| Linting de código | flake8 |
| Testing | pytest |
| Análisis de seguridad estático | bandit |
| Plataforma objetivo | Windows 10 |
| Diagramas de arquitectura | Draw.io / C4 Model |
| Licencia | Creative Commons BY-NC-SA 4.0 |

---

## 📦 Installation

### 1. Clonar el repositorio
```bash
git clone https://github.com/devsebastian44/Troyano.git
cd Troyano
```

### 2. Crear y activar el entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS (para desarrollo)
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar el entorno
Copia el archivo de ejemplo y define tus variables de entorno:
```bash
cp .env.example .env
# Edita .env con los parámetros de red: HOST, PORT, etc.
```

---

## ▶️ Usage

> Todos los pasos de uso deben realizarse **exclusivamente en entornos de laboratorio aislados** (máquinas virtuales sin conexión a redes productivas), con autorización explícita sobre los sistemas involucrados.

### Iniciar el Listener (Servidor C2)
```bash
python src/server/server.py
```

### Ejecutar el Payload (Cliente / Agente)
En la máquina objetivo de prueba (VM):
```bash
python src/payload/troyano.py
```

### Ofuscar el Payload (opcional)
```bash
pyarmor pack -e " --onefile" src/payload/troyano.py
```

### Ejecutar el pipeline de calidad
```bash
# Linting
flake8 src/

# Tests con mocks
pytest tests/

# Análisis estático de seguridad
bandit -r src/ -o bandit-report.json
```

---

## 📁 Project Structure
```
Troyano/
│
├── .github/                     # Workflows de GitHub Actions (CI/CD)
│   └── workflows/ci.yml         # Pipeline automatizado de calidad y seguridad
│
├── data/                        # Muestras de sesiones, volcados y capturas de laboratorio
│   └── sample_session.json      # Única muestra pública incluida (resto en .gitignore)
│
├── diagrams/                    # Diagramas de arquitectura del sistema
│                                # (C4 Model, flujos de red, Draw.io)
│
├── docs/                        # Documentación técnica, RFCs y manuales operativos
│
├── src/
│   ├── payload/                 # Componente cliente (agente de infección)
│   │   └── troyano.py           # Punto de entrada del payload
│   │
│   └── server/                  # Componente servidor (Listener C2)
│       └── server.py            # Listener TCP que gestiona sesiones remotas
│
├── tests/                       # Suite de pruebas unitarias con mocks de red
│
├── configs/                     # Plantillas de configuración de red y parámetros
│
├── scripts/
│   └── build.ps1                # Script de compilación
│
├── .gitignore                   # Exclusiones estrictas: venv, .env, *.pem, *.key, data/*
├── LICENSE                      # CC BY-NC-SA 4.0 — Copyright 2025 Sebastián Zhunaula
└── README.md                    # Documentación principal del proyecto
```

---

## 🔐 Security

### Modelo de Amenaza y Uso Responsable
Este proyecto modela técnicas utilizadas por **malware real de tipo RAT**, y su estudio tiene un valor defensivo directo.

### Superficies de riesgo identificadas en el código
- **Comunicación sin cifrado explícito:** La conexión TCP/IP podría ser detectada por DPI.
- **Ejecución remota de comandos:** `bandit` alerta sobre el uso de `subprocess` u `os.system`.
- **Ofuscación con PyArmor:** Reduce la detección estática pero no garantiza invisibilidad ante EDRs modernos.
- **Gestión de secretos:** `.gitignore` previene fugas de configuraciones sensibles.

---

## 🚀 Roadmap
- **Implementar cifrado TLS en el canal C2**.
- **Persistencia en el sistema objetivo**.
- **Módulo de captura de pantalla / keylogger**.
- **Dashboard web para el servidor C2**.
- **Integración con VirusTotal API**.
- **Contenedorización del entorno de laboratorio**.
- **Reglas YARA y Sigma** para detección.

---

## 🤝 Contributing

¡Las contribuciones son bienvenidas! Para colaborar:

1. Haz un **Fork** del proyecto.
2. Crea una rama para tu mejora (`git checkout -b feature/AmazingFeature`).
3. Realiza tus cambios y asegúrate de que los tests pasen (`pytest`).
4. Haz un **Commit** de tus cambios siguiendo [Conventional Commits](https://www.conventionalcommits.org/).
5. Haz un **Push** a la rama (`git push origin feature/AmazingFeature`).
6. Abre un **Pull Request**.

---

## 📄 License
Este proyecto está distribuido bajo la licencia **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

Copyright © 2025 **Sebastián Zhunaula** (devsebastian44)

---

## 👨‍💻 Author

<table>
  <tr>
    <td align="center">
      <b>Sebastián Zhunaula</b><br/>
      <sub>Security Researcher · Python Developer · DevSecOps</sub><br/><br/>
      <a href="https://github.com/devsebastian44">
        <img src="https://img.shields.io/badge/GitHub-devsebastian44-black?style=flat&logo=github" />
      </a>
    </td>
  </tr>
</table>