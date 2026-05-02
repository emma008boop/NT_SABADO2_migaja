import pandas as pd

def limpiar_datos(df_sucio):
    df_limpio = df_sucio.copy()
    
    columnas_texto = ["descripcion", "lugar", "observaciones"]
    for columna in columnas_texto:
        df_limpio[columna] = df_limpio[columna].astype("string").str.strip().str.lower()
    
    valores_validos_gastos = [
        "alimentación y bebidas", "transporte y movilidad", 
        "suministros de oficina", "servicios de limpieza", 
        "mantenimiento y reparaciones", "equipos y software", 
        "marketing y publicidad", "gastos varios"
    ]
    
    df_limpio["tipo_gasto"] = df_limpio["tipo_gasto"].where(
        df_limpio["tipo_gasto"].isin(valores_validos_gastos),
        pd.NA
    )
    
    df_limpio["id"] = pd.to_numeric(df_limpio["id"], errors='coerce')
    df_limpio["impacto_financiero"] = pd.to_numeric(df_limpio["impacto_financiero"], errors='coerce')
    df_limpio["monto"] = pd.to_numeric(df_limpio["monto"], errors='coerce')


    df_limpio = df_limpio[df_limpio["monto"] > 0]
    df_limpio = df_limpio[df_limpio["id"] > 0]
    
    df_limpio["fecha"] = pd.to_datetime(df_limpio["fecha"], errors='coerce')
    fecha_default = pd.to_datetime("2026-01-01")
    df_limpio["fecha"] = df_limpio["fecha"].fillna(fecha_default)
    
    columnas_obligatorias = ["id", "monto", "tipo_gasto"]
    df_limpio = df_limpio.dropna(subset=columnas_obligatorias)
    df_limpio = df_limpio.drop_duplicates()
    
    return df_limpio