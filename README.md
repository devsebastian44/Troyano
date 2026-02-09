# 🛡️ Troyano en Python (Educativo)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![GitLab](https://img.shields.io/badge/GitLab-Repository-orange?logo=gitlab)
![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-blue)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Educational](https://img.shields.io/badge/Purpose-Educational%20Only-blue)
![Warning](https://img.shields.io/badge/⚠-Authorized%20Use%20Only-red)

## 🔍 Descripción del Proyecto

Este repositorio contiene una implementación básica de un Troyano de Acceso Remoto (RAT) en Python, diseñado estrictamente con **fines educativos** y para **investigación en análisis de malware**. Demuestra los conceptos fundamentales de la arquitectura Cliente-Servidor utilizada en frameworks C2 (Comando y Control).

Este proyecto forma parte de un portafolio de ciberseguridad que demuestra comprensión de:
- 📡 Programación de Sockets (TCP/IP)
- 💻 Ejecución Remota de Comandos
- 📂 Manipulación del Sistema de Archivos
- 🛡️ Técnicas de Evasión y Ofuscación (aplicación teórica)

## ⚠️ Aviso Legal y Ético

> [!IMPORTANT]
> **Esta herramienta es SOLO PARA FINES EDUCATIVOS.**
>
> El autor no aprueba el uso de este software para fines maliciosos. El uso de estas herramientas para atacar objetivos sin el consentimiento mutuo previo es ilegal. Es responsabilidad del usuario final obedecer todas las leyes locales, estatales y federales aplicables. Los desarrolladores no asumen ninguna responsabilidad y no son responsables de ningún mal uso o daño causado por este programa.

## 🏗️ Arquitectura del Proyecto

El proyecto está estructurado siguiendo estándares profesionales de DevSecOps:

```text
/
├── configs/          # Plantillas de configuración
├── scripts/          # Scripts de automatización y construcción
├── src/
│   ├── payload/      # Payload del lado del cliente (Objetivo)
│   └── server/       # Listener del lado del servidor (Atacante)
├── tests/            # Pruebas unitarias y de seguridad
└── README.md         # Documentación
```

### Componentes
1. **Servidor (C2)**: Escucha conexiones entrantes y emite comandos.
2. **Payload (Bot)**: Se conecta al servidor y ejecuta las instrucciones recibidas.

## 🚀 Comenzando (Entorno de Laboratorio)

### Requisitos Previos
- Python 3.8+
- Entorno Virtual (recomendado)

## 🔒 Estrategia de Seguridad (GitHub vs GitLab)

Este repositorio utiliza una estrategia de **Diferenciación de Entornos**:

- **GitHub (Público):** Escaparate para portafolio. Contiene la estructura, documentación, diagramas y **pseudocódigo educativo** para evitar la distribución de malware funcional.
- **GitLab (Privado):** Laboratorio de desarrollo. Contiene la implementación completa, payloads funcionales, tests automatizados y el pipeline de CI/CD con análisis estático de seguridad (SAST).

---

## 🚀 Instalación y Acceso (Bajo Petición)

> [!IMPORTANT]
> El acceso al repositorio de laboratorio, los payloads funcionales y las instrucciones de despliegue está restringido a investigadores autorizados para prevenir el mal uso de la herramienta.

Para solicitar acceso al entorno de desarrollo en **GitLab** y la documentación técnica completa, por favor contactar al desarrollador.

2. Configurar entorno:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt # (si aplica)
   ```

3. Configurar Conexión:
   Edita `configs/config.yaml` o modifica la dirección IP en `src/payload/troyano.py` para que apunte a tu listener.

### Uso

1. **Iniciar el Listener:**
   ```bash
   python src/server/server.py
   ```

2. **Ejecutar Payload (en VM/Objetivo):**
   ```bash
   python src/payload/troyano.py
   ```

3. **Comandos Disponibles:**
   - `cd <ruta>`: Cambiar directorio
   - `download <archivo>`: Descargar archivo del objetivo
   - `<cmd>`: Ejecutar comando del sistema (ej. `dir`, `whoami`)
   - `exit`: Cerrar conexión

## 🧪 Pruebas y CI/CD

Este proyecto utiliza **GitLab CI/CD** para pruebas automatizadas y análisis de seguridad.
- **Pruebas Unitarias**: Verifica la lógica de conexión (mocked).
- **SAST**: Pruebas de Seguridad de Aplicaciones Estáticas usando `bandit` para identificar vulnerabilidades en el código.

Para ejecutar pruebas localmente:
```bash
python -m unittest discover tests/
```

## 🔐 Ofuscación (investigación red team)

Para la investigación sobre evasión de AV, el payload puede ser ofuscado usando `pyarmor`.
*Nota: Las técnicas detalladas de ofuscación están reservadas para el repositorio privado de GitLab.*

```bash
# Ejemplo de comando
pyarmor gen src/payload/troyano.py
```
