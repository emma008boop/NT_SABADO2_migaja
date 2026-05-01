import pandas as pd


def limpiar_datos(df_sucio):
    df_limpio = df_sucio.copy()
    df_limpio = df_limpio.applymap(
        lambda x: x.strip().lower() if isinstance(x, str) else x
    )
