import pandas as pd


def transformar_datos(df_limpio, tipo_gasto_filtro):

    filtro1 = df_limpio.query("tipoGasto == @tipo_gasto_filtro")

    agrupacion1 = filtro1.groupby("fecha")["id"].count().reset_index(name="cuenta")

    return agrupacion1
