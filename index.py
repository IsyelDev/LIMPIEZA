# 🔍 1. Seleccionar columnas
import pandas as pd

df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Sofía'],
    'Edad': [23, 30, 27],
    'Ciudad': ['Lima', 'Bogotá', 'Quito']
})

# Seleccionar una columna
df['Nombre']

# Seleccionar varias columnas
df[['Nombre', 'Edad']]


# 🔎 2. Filtrar tablas (filas)

# Personas mayores de 25 años
df[df['Edad'] > 25]

# Personas que viven en Lima
df[df['Ciudad'] == 'Lima']


# 🔗 3. Consolidar datos (ej. agrupar y resumir)

# Supón que hay varias personas de la misma ciudad
df.groupby('Ciudad')['Edad'].mean()  # Edad promedio por ciudad


# 🏷️ 4. Renombrar columnas

df.rename(columns={'Nombre': 'Nombre_Completo', 'Edad': 'Años'}, inplace=True)


# ➕ 5. Agregar datos (nuevas filas o columnas)

# Agregar nueva columna
df['País'] = ['Perú', 'Colombia', 'Ecuador']

# Agregar nueva fila
nueva_fila = pd.DataFrame([{
    'Nombre_Completo': 'Mario',
    'Años': 28,
    'Ciudad': 'Lima',
    'País': 'Perú'
}])

df = pd.concat([df, nueva_fila], ignore_index=True)


# 🗑️ 6. Eliminar columnas

df.drop(columns=['País'], inplace=True)


# 🔄 7. Unir tablas (merge / join)

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Sofía']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Edad': [23, 30, 27]
})

# Unir por la columna 'ID'
df_merged = pd.merge(df1, df2, on='ID')


# 📚 8. Concatenar tablas (una debajo de otra)

df_a = pd.DataFrame({
    'Nombre': ['Juan', 'Elena'],
    'Edad': [24, 29]
})

df_b = pd.DataFrame({
    'Nombre': ['Pedro', 'Lucía'],
    'Edad': [31, 26]
})

# Concatenar verticalmente
df_concat = pd.concat([df_a, df_b], ignore_index=True)


# 🎨 9. Formatear datos

# Convertir a mayúsculas
df['Ciudad'] = df['Ciudad'].str.upper()

# Redondear edades
df['Años'] = df['Años'].round(0)

# Cambiar tipo de dato
df['Años'] = df['Años'].astype(int)
