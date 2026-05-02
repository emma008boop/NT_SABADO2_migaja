from utils.descripcion_gastos import describir_datos_gastos
from utils.simulacion_gastos import simular_gastos
from notebook.limpiar_datos import limpiar_datos
import pandas as pd

df = pd.DataFrame(simular_gastos(1000))

df_limpio = limpiar_datos(df)

df_descripcion = describir_datos_gastos(df_limpio)

print(df_descripcion)
print(df_limpio)