# NT_SABADO2_migaja

Este componente es un microservicio desarrollado en Python encargado del procesamiento, limpieza y transformación de los datos analíticos del módulo de Gastos de la aplicación principal MigajaApp (desarrollada en Spring Boot).

El microservicio actúa como un puente de analítica en tiempo real: consume la API de Spring Boot, procesa los datos estructurados mediante Pandas y expone endpoints optimizados para que el Front-end renderice gráficos de manera eficiente.

**Arquitectura del Pipeline de Datos**

El flujo de información se ejecuta de forma síncrona en cada petición web:

    Consumo (consumo.py): Recupera los datos crudos en formato JSON desde el backend de Spring Boot (:8080/migaja/v1/gasto).

    Limpieza (limpiar_datos.py): Transforma el JSON en un DataFrame de Pandas, gestionando tipos de datos (como fechas y montos) y valores nulos.

    Análisis (descripcion_gastos.py): Genera resúmenes descriptivos de las métricas financieras de la entidad.

    Transformación (transformacion.py): Filtra los registros por tipoGasto y agrupa por fecha generando un conteo de frecuencias.

    Exposición (main.py): FastAPI despacha la información en un formato JSON plano, ideal para librerías de gráficos en el Front-end (Chart.js, Recharts, etc.).

**Estructura del Proyecto**
```text
NT_SABADO02_MIGAJA/
├── notebook/
│   ├── consumo.py              # Cliente HTTP (Requests) hacia Spring Boot
│   ├── descripcion_gastos.py   # Análisis descriptivo del DataFrame
│   ├── limpiar_datos.py        # Formateo y limpieza de tipos de datos
│   └── transformacion.py       # Agrupaciones y filtros específicos para gráficos
├── utils/
│   ├── __init__.py
│   └── simulacion_gastos.py
├── venv/                       # Entorno virtual de Python
├── .gitignore
├── main.py                     # Punto de entrada de la API (FastAPI + CORS)
├── README.md
└── requirements.txt            # Dependencias del proyecto

> # Requisitos e Instalación
Prerrequisitos

    Python 3.10 o superior instalado.

    El servicio de Spring Boot (MigajaApp) ejecutándose en el puerto 8080

##  Visualización en el Front-end

El JSON estructurado que devuelve este microservicio está optimizado para ser mapeado directamente en componentes de gráficos de líneas, barras o áreas. A continuación, se muestra un ejemplo de cómo el Front-end renderiza los datos transformados de la tabla `gastos`:

![Dashboard de Analítica de Gastos]
<img width="768" height="590" alt="image" src="https://github.com/user-attachments/assets/cddbbb02-ead2-4f92-b497-e61ffde36853" />
