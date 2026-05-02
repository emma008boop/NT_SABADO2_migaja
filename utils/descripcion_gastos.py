def describir_datos_gastos(df_limpio):
    print("*** Descripcion ***")
    print(f"Numero de filas de dataset: {df_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {df_limpio.shape[1]}")
    print(f"Listado de columnas disponibles: {list(df_limpio.columns)}")
    print(f"flujo de dato de cada atributo: {df_limpio.dtypes}")
    
    print("\n*** ESTADISTICAS ***")
    print(df_limpio[['id', 'monto', 'impacto_financiero']].describe())
    
    print("\n*** CONTEOS ***")
    print(f"Conteos de monto:\n{df_limpio['monto'].value_counts()}")
    print(f"Conteos de impacto financiero:\n{df_limpio['impacto_financiero'].value_counts()}")
    
    print("\n*** DESCRIPCION DE FECHAS ***")
    print(f"Fecha máxima: {df_limpio['fecha'].max()}")