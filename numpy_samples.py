import numpy as np

array_faltante = np.array([1.0, 2.0, 3, np.nan, 5, np.nan, 7, 8, 9])    
print(f"array con datos faltantes: {array_faltante}")

# Eliminar datos faltantes
array_sin_faltantes = array_faltante[~np.isnan(array_faltante)]
print(f"array sin datos faltantes: {array_sin_faltantes}")