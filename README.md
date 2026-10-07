# 🟢 Fundación Adsis | Backoffice Ejecutivo y Motor de Gobierno del Dato

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-success.svg)]()
[![Stack: Python & Streamlit](https://img.shields.io/badge/Stack-Python%20%7C%20Streamlit%20%7C%20PostgreSQL-blue.svg)]()
[![Compliance: RGPD & AES-256](https://img.shields.io/badge/Compliance-RGPD%20%7C%20AES--256-orange.svg)]()
[![Architecture: Dockerized](https://img.shields.io/badge/Architecture-Docker%20Compose-blueviolet.svg)]()

Plataforma unificada de backoffice ejecutivo diseñada para la monitorización en tiempo real del impacto social, la unificación de sedes y la automatización de la gobernanza del dato en la red de la **Fundación Adsis**.

---

## 🏛️ Contexto y Propósito del Proyecto

En el marco de la transformación digital de la Fundación Adsis, este backoffice resuelve los retos críticos de interoperabilidad y control operativo derivados de operar en **13 provincias** y gestionar múltiples programas sociales. 

La plataforma consolida información heterogénea proveniente de diversos sistemas (ERP, CRM, SaaS y M365 SharePoint) en una única fuente de la verdad (`Single Source of Truth`), garantizando la trazabilidad absoluta de las intervenciones y optimizando la justificación de los fondos públicos auditados.

---

## 🚀 Arquitectura Técnica y Stack

El sistema se compone de una arquitectura modular y ligera contenerizada mediante **Docker Compose**:

* **Capa de Persistencia:** PostgreSQL 15 optimizada para transacciones ACID concurrentes y aislamiento de datos por sede.
* **Capa de Lógica y ORM:** SQLAlchemy para la gestión limpia de modelos relacionales, operaciones CRUD y mecanismos de *Fallback* de alta disponibilidad.
* **Capa de Interfaz y Analítica:** Streamlit para la visualización ejecutiva en tiempo real, integración de gráficos interactivos (Plotly) y control reactivo de estados.
* **Seguridad y Cifrado:** Anonimización de PII (Personally Identifiable Information) mediante hashing criptográfico (SHA-256) y cumplimiento estricto de los estándares de privacidad RGPD.
  ```text
┌─────────────────────────────────────────────────────────┐
│                   Docker Environment                    │
│                                                         │
│  ┌───────────────────────┐   SQLAlchemy   ┌───────────┐ │
│  │ Streamlit Dashboard   │ ──────────────>│ PostgreSQL│ │
│  │  (Port 8501 / UI & IA)│                │ (Port 5432│ │
│  └───────────────────────┘                └───────────┘ │
└─────────────────────────────────────────────────────────┘
 ```

---

## ✨ Características Principales

1. **Cuadro de Mando Ejecutivo (KPIs en Tiempo Real):** Monitorización de personas acompañadas, presupuesto público gestionado (18.90 M€, 81% del presupuesto oficial) y distribución provincial[cite: 11, 14].
2. **Simulador de Admisión Multicanal y Antiduplicidad:** Validación síncrona de expedientes que detecta de forma autónoma si una persona ya ha sido atendida en otra provincia, unificando el historial de manera transparente.
3. **Live Stream - Agentes IA Inspectores:** Consola en tiempo real integrada en el panel que muestra la trazabilidad de auditoría, control de integridad y sincronización con repositorios documentales (M365 / SharePoint).
4. **Gobierno del Dato & Open Data:** Funcionalidades de exportación masiva en CSV para auditorías externas y un visor estructurado en formato JSON listo para integraciones corporativas.

---

## ⚙️ Despliegue y Puesta en Marcha

Para desplegar el entorno completo de forma automatizada mediante contenedores, asegúrate de tener instalado **Docker** y **Docker Compose**.

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/desprogramaci/adsis-backoffice-ejecutivo.git
   cd adsis-backoffice-ejecutivo
   ```

2. **Levantar los servicios:**
   ```bash
    docker-compose up --build -d
   ```

3. **Acceder al panel ejecutivo:**
Abre tu navegador e introduce la siguiente URL:
👉 http://localhost:8501


📊 Estructura del Repositorio
  ```text
├── dashboard.py           # Interfaz ejecutiva en Streamlit y lógica de componentes
├── database.py            # Modelos ORM, sesión y conexión a PostgreSQL[cite: 16]
├── main.py                # Middleware REST con FastAPI, endpoints y log de gobernanza[cite: 19]
├── Dockerfile             # Definición de la imagen multinúcleo Python[cite: 18]
├── docker-compose.yml     # Orquestación de contenedores (App unificada + Base de datos)[cite: 17]
├── requirements.txt       # Dependencias del proyecto (FastAPI, Streamlit, SQLAlchemy, etc.)[cite: 20]
└── README.md              # Documentación técnica y ejecutiva
 ```

🔒 Seguridad y Cumplimiento Normativo
Principio de Mínimo Privilegio: Control de acceso basado en roles (RBAC) integrado en la arquitectura del backoffice.

Trazabilidad Inmutable: Registro de auditoría continuo supervisado por agentes de IA orientados a la detección de anomalías.

Protección de Datos Sensibles: Tratamiento cifrado de identificadores personales conforme a la normativa vigente de protección de datos (RGPD).

Desarrollado para la excelencia en la gestión social y la innovación tecnológica.