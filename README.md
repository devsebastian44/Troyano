# 🛡️ Troyano — RAT & Framework C2 en Python

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=flat&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%2010-informational?style=flat&logo=windows&logoColor=white)
![Security](https://img.shields.io/badge/Tipo-Malware%20Research-critical?style=flat&logo=hackthebox&logoColor=white)
![DevSecOps](https://img.shields.io/badge/Arquitectura-DevSecOps-purple?style=flat&logo=gitlab&logoColor=white)
![CI](https://img.shields.io/badge/CI%2FCD-GitLab%20Pipelines-orange?style=flat&logo=gitlab&logoColor=white)
![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-blue?style=flat&logo=creativecommons&logoColor=white)

> ⚠️ **AVISO ÉTICO:** Este proyecto es de uso estrictamente educativo y para investigación en ciberseguridad defensiva. El repositorio público en GitHub contiene únicamente componentes sanitizados, sin payloads operacionales. El autor no se responsabiliza por el uso indebido de este material fuera de entornos autorizados y controlados.

---

## 🧠 Overview

Este proyecto es un **Remote Access Trojan (RAT)** de investigación desarrollado íntegramente en Python, diseñado para funcionar sobre sistemas **Windows 10**. Implementa una arquitectura clásica de **Comando y Control (C2)** basada en comunicación TCP/IP, con el objetivo de estudiar, desde una perspectiva técnica ofensiva-defensiva, los vectores de ataque utilizados por malware real en entornos controlados de laboratorio.

El proyecto sigue una **estrategia DevSecOps de doble repositorio**: el entorno de desarrollo activo y el código fuente completo residen en GitLab (privado), mientras que GitHub actúa como vitrina pública y sanitizada del portafolio técnico. Esta separación garantiza que los componentes operacionales sensibles nunca se expongan públicamente, cumpliendo con principios de divulgación responsable.

Este proyecto parece estar orientado tanto a la **investigación personal en malware** como a la **demostración de buenas prácticas de seguridad en el ciclo de desarrollo**.

---

## ⚙️ Features

- **Arquitectura C2 Cliente-Servidor** implementada sobre sockets TCP/IP nativos de Python, permitiendo control remoto de sistemas objetivo en red.
- **Payload del lado cliente** (`src/payload/`) diseñado para ejecución en máquinas Windows 10, encargado de establecer la conexión reversa hacia el listener.
- **Servidor Listener C2** (`src/server/`) responsable de recibir conexiones entrantes, emitir comandos y gestionar las sesiones activas.
- **Ofuscación del payload** mediante integración con **PyArmor**, dificultando el análisis estático y la detección por soluciones antivirus convencionales.
- **Sanitización automatizada** del repositorio público a través del script `publish_public.ps1` (PowerShell), el cual elimina componentes sensibles antes de cada publicación en GitHub.
- **Pipeline CI/CD en GitLab** con etapas de linting (`flake8`), pruebas unitarias con mocks de red (`pytest`) y análisis estático de seguridad (`bandit`).
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
| CI/CD | GitLab Pipelines (`.gitlab-ci.yml`) |
| Automatización de publicación | PowerShell (`publish_public.ps1`) |
| Plataforma objetivo | Windows 10 |
| Diagramas de arquitectura | Draw.io / C4 Model |
| Licencia | Creative Commons BY-NC-SA 4.0 |

---

## 📦 Installation

> **Requisito previo:** Acceso al repositorio fuente completo en GitLab (el repositorio público en GitHub no contiene el payload operacional).

### 1. Clonar el repositorio (entorno de laboratorio)
```bash
git clone https://gitlab.com/group-cybersecurity-lab/Troyano.git
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

El servidor quedará en escucha en el host y puerto definidos en la configuración, esperando conexiones entrantes del payload.

### Ejecutar el Payload (Cliente / Agente)

En la máquina objetivo de prueba (VM):
```bash
python src/payload/troyano.py
```

### Ofuscar el Payload (opcional, entorno de lab)
```bash
# Usando scripts internos del laboratorio con PyArmor
pyarmor pack -e " --onefile" src/payload/troyano.py
```

### Publicar versión sanitizada a GitHub
```powershell
# Desde PowerShell en el entorno de desarrollo
.\scripts\publish_public.ps1
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
│   │   └── troyano.py           # Punto de entrada del payload — ELIMINADO en repo público
│   │
│   └── server/                  # Componente servidor (Listener C2)
│       └── server.py            # Listener TCP que gestiona sesiones remotas
│
├── tests/                       # Suite de pruebas unitarias con mocks de red
│                                # ELIMINADO en repo público (protect assertion methods)
│
├── configs/                     # Plantillas de configuración de red y parámetros
│                                # ELIMINADO en repo público (protect secrets)
│
├── scripts/
│   └── publish_public.ps1       # Script PowerShell de sanitización y publicación a GitHub
│                                # ELIMINADO en repo público (protect DevOps logic)
│
├── .gitlab-ci.yml               # Pipeline CI/CD: lint → test → SAST
│                                # ELIMINADO en repo público
│
├── .gitignore                   # Exclusiones estrictas: venv, .env, *.pem, *.key, data/*
├── LICENSE                      # CC BY-NC-SA 4.0 — Copyright 2025 Sebastián Zhunaula
└── README.md                    # Documentación principal del proyecto
```

> **Nota:** Las carpetas `tests/`, `configs/`, `scripts/` y `src/payload/` son **deliberadamente eliminadas** del repositorio público en GitHub mediante el script de sanitización `publish_public.ps1`, como parte de la estrategia DevSecOps de divulgación responsable.

---

## 🔐 Security

### Modelo de Amenaza y Uso Responsable

Este proyecto modela técnicas utilizadas por **malware real de tipo RAT**, y su estudio tiene un valor defensivo directo: comprender cómo operan estos vectores es fundamental para diseñar detecciones, reglas SIEM, y políticas de seguridad más efectivas.

### Superficies de riesgo identificadas en el código

- **Comunicación sin cifrado explícito en capa de aplicación:** La conexión TCP/IP entre payload y servidor podría ser detectada por inspección de tráfico (DPI). En entornos de investigación avanzados, se recomienda implementar cifrado TLS o túneles cifrados.
- **Ejecución remota de comandos:** La arquitectura C2 implica capacidad de ejecutar instrucciones arbitrarias en el sistema objetivo. `bandit` detecta y alerta sobre el uso de primitivas como `subprocess`, `os.system` o `eval` en el análisis SAST.
- **Ofuscación con PyArmor:** Reduce la superficie de detección estática, pero no garantiza indetectabilidad frente a soluciones EDR modernas con análisis de comportamiento dinámico.
- **Gestión de secretos:** El `.gitignore` excluye explícitamente `*.pem`, `*.key`, `.env`, y `credentials.json`, previniendo fugas de configuraciones de red sensibles.

### Principios de Divulgación Responsable aplicados

- El código del payload (`src/payload/`) **nunca se publica** en repositorios públicos.
- Cada publicación hacia GitHub pasa por el proceso de sanitización automatizado y auditable (`publish_public.ps1`).
- Los datos de laboratorio reales (`data/*`) están excluidos del repositorio, con excepción de una muestra de referencia inofensiva.
- El análisis SAST con `bandit` es una etapa **obligatoria y bloqueante** en el pipeline de CI/CD.

---

## 🌐 Repository Architecture

Este proyecto sigue una arquitectura distribuida de doble repositorio, diseñada para separar de forma auditable el entorno de investigación activo del portafolio público:

**GitHub** actúa como punto de presentación técnica: contiene la documentación, diagramas de arquitectura y componentes de red inofensivos. Es la cara pública del proyecto.

**GitLab** es el entorno de laboratorio completo y la fuente de verdad: contiene el código fuente íntegro, la suite de tests, el pipeline CI/CD (`flake8` → `pytest` → `bandit`) y los componentes operacionales que nunca se exponen públicamente.

### 🔗 Full Source Code

👉 Código completo disponible en GitLab: [https://gitlab.com/group-cybersecurity-lab/Troyano](https://gitlab.com/group-cybersecurity-lab/Troyano)

---

## 🚀 Roadmap

Basado en la arquitectura del proyecto y las herramientas detectadas, estas son las mejoras técnicas que probablemente enriquecerían el laboratorio:

- **Implementar cifrado TLS en el canal C2** para simular con mayor fidelidad el comportamiento de RATs modernos y hacer el tráfico de red indistinguible de conexiones legítimas HTTPS.
- **Persistencia en el sistema objetivo:** Incorporar módulos de persistencia (registro de Windows, tareas programadas) como vector de estudio defensivo.
- **Módulo de captura de pantalla / keylogger:** Ampliar las capacidades de demostración del payload para análisis de técnicas de exfiltración.
- **Dashboard web para el servidor C2:** Reemplazar la interfaz CLI del listener por un panel web (Flask/FastAPI) para una gestión visual de sesiones activas.
- **Integración con VirusTotal API:** Automatizar el análisis de detección del payload compilado contra motores antivirus como parte del pipeline CI/CD.
- **Contenedorización del entorno de laboratorio:** Usar Docker para empaquetar el servidor C2 y garantizar reproducibilidad del entorno de investigación.
- **Reglas YARA y Sigma:** Incluir reglas de detección derivadas del propio proyecto, documentando cómo detectar el RAT que se está construyendo.

---

## 📄 License

Este proyecto está distribuido bajo la licencia **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

Esto implica que:
- ✅ Puedes estudiar, compartir y adaptar el material.
- ❌ **No** puedes utilizarlo con fines comerciales.
- ❌ **No** puedes distribuir versiones modificadas bajo términos más restrictivos.
- ✅ Debes dar crédito al autor original.

📄 [Ver licencia completa](https://creativecommons.org/licenses/by-nc-sa/4.0/)

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
      <br/>
      <a href="https://gitlab.com/group-cybersecurity-lab">
        <img src="https://img.shields.io/badge/GitLab-group--cybersecurity--lab-orange?style=flat&logo=gitlab" />
      </a>
    </td>
  </tr>
</table>

> Este proyecto forma parte de un portafolio profesional en ciberseguridad ofensiva-defensiva, con enfoque en investigación de malware, arquitecturas C2 y prácticas modernas de DevSecOps aplicadas a entornos de alto riesgo.