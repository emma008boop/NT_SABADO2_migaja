import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from notebook.consumo import consumir_servicios
from notebook.descripcion_gastos import describir_datos_gastos
from notebook.limpiar_datos import limpiar_datos
from notebook.transformacion import transformar_datos

app = FastAPI(
    title="Migaja Analytics API",
    description="API en Python para procesar y transformar datos de gastos",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/analytics/gastos-por-fecha")
def obtener_gastos_procesados(
    tipo_gasto: str = Query(
        ...,
        description="El tipo de gasto por el cual filtrar (ej. 'Hogar', 'Alimentacion')",
    ),
):

    try:
        datos_reales = consumir_servicios()

        df = pd.DataFrame(datos_reales)
        df_limpio = limpiar_datos(df)

        df_transformado = transformar_datos(df_limpio, tipo_gasto)

        resultado_final = df_transformado.to_dict(orient="records")

        return {"status": "success", "tipo_gasto": tipo_gasto, "data": resultado_final}

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error al procesar los datos: {str(e)}",
        }
