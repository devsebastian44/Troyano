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
├── configs/          # Plantillas de configuración (.gitignore protege variables reales)
├── data/             # Recolección de datos, capturas y volcados (Solo en entorno privado)
├── diagrams/         # Diagramas de arquitectura y flujo (C4, Draw.io)
├── docs/             # Documentación técnica, RFCs y manuales operativos
├── scripts/          # Funcionalidad DevSecOps y automatizaciones (ej. publish_public.ps1)
├── src/
│   ├── payload/      # Payload del lado del cliente / bot (Exclusivo entorno privado)
│   └── server/       # Listener del lado del servidor (C2)
├── tests/            # Cobertura de pruebas unitarias y mocks (Exclusivo entorno privado)
├── .gitlab-ci.yml    # Pipeline CI/CD (Tests + SAST)
└── README.md         # Documentación principal del proyecto
```

### Componentes Activos
1. **Servidor (C2)**: Escucha conexiones entrantes y emite comandos.
2. **Payload (Bot)**: Se conecta al servidor y ejecuta las instrucciones recibidas.

## 🚀 Comenzando (Entorno de Laboratorio)

### Requisitos Previos
- Python 3.8+
- Entorno Virtual (recomendado)

## 🔒 Estrategia DevSecOps: Publicación Segura (GitHub vs GitLab)

Este repositorio implementa una estrategia avanzada de **Diferenciación de Entornos** (Separación Público/Privado) para administrar el desarrollo profesional frente a la exposición pública:

- **GitLab (Entorno Privado / Source of Truth):** Laboratorio de desarrollo completo. Contiene la implementación funcional, todos los tests, automatización CI/CD, configuraciones, payloads completos y scripts críticos.
- **GitHub (Entorno Público / Portafolio educativo):** Versión sanitizada que actúa como un escaparate de arquitectura técnica y documentación, sin exponer el funcionamiento malicioso o la infraestructura interna.

### Flujo de Sancanitización Automática (`publish_public.ps1`)

Para garantizar de forma consistente y auditable que no se filtren artefactos sensibles en la rama de portafolio, el repositorio utiliza el script de seguridad integrado en `scripts/publish_public.ps1`. 

Este script oficial de publicación realiza los siguientes pasos DevSecOps:
1. **Validación Pre-vuelo**: Comprueba la limpieza del árbol y que la rama sea `main`.
2. **Sincronización Laboratorio**: Asegura el almacenamiento de todos los cambios de desarrollo en GitLab.
3. **Escudo de Rama**: Crea una rama paralela e independiente (`public`).
4. **Sanitización DevSecOps**:
   - Elimina `tests/` (Oculta métodos internos de aserción).
   - Elimina `configs/` (Prevención estructurada de fugas).
   - Elimina `scripts/` (Protege rutinas y despliegues del lab).
   - Elimina `src/payload/` (Desarma el componente ofensivo).
   - Elimina `.gitlab-ci.yml` (Oculta la topología de CI).
5. **Implementación Push Controlada**: Inyecta una nueva snapshot purgada a GitHub con Conventional Commits.
6. **Rollback Local**: Regresa el directorio de trabajo local y limpio a `main` para evitar la interrupción del desarrollo.

---

## 🚀 Instalación y Acceso (Bajo Petición)

> [!IMPORTANT]
> El repositorio completo con todo el código funcional está disponible en **GitLab** para acceso completo.

https://gitlab.com/group-cybersecurity-lab/Troyano-lab.git


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
