import pandas as pd

print("Hola bienvenido a la calculadora de muestras estratificadas")
num_depas = int(input("Por favor ingrese el número de departamentos: "))

data = []

for i in range(num_depas):
    nombre = input(f"Ingrese el nombre del departamento {i+1}: ")
    empleados = int(input(f"Ingrese la cantidad de empleados en {nombre}: "))
    data.append({"Departamento": nombre, "Empleados": empleados})

muestreo = int(input("Ingrese el tamaño del muestreo: "))

df = pd.DataFrame(data)

# Suma de los valores de la columna "Empleados"
total_empleados = df['Empleados'].sum()

# Cálculo del porcentaje
porcentaje_muestra = (muestreo / total_empleados) * 100

# Calcular el tamaño de muestra para cada departamento
df['Tamaño Muestra'] = (df['Empleados'] / total_empleados) * muestreo

# Calcular el porcentaje de muestra para cada departamento
df['Porcentaje Muestra'] = (df['Tamaño Muestra'] / muestreo) * 100

print(f"\nEl tamaño total del universo es: {total_empleados}")
print(f"El porcentaje que representa la muestra del universo es: {porcentaje_muestra:.2f}%")
print("\nTamaño de muestra por departamento y porcentaje que representa respecto al total:")
print(df[['Departamento', 'Tamaño Muestra', 'Porcentaje Muestra']])