# Calculadora de Muestras Estratificadas

Este proyecto es un ejercicio universitario que implementa una calculadora de muestras estratificadas en Python. La herramienta permite calcular el tamaño de muestra para cada departamento en una organización, basándose en el número total de empleados y el tamaño de muestra deseado.

## Descripción

El programa realiza las siguientes tareas:

1. Solicita al usuario el número de departamentos.
2. Recopila información sobre cada departamento (nombre y número de empleados).
3. Pide al usuario el tamaño total de la muestra deseada.
4. Calcula el tamaño de muestra para cada departamento utilizando muestreo estratificado.
5. Muestra los resultados, incluyendo el porcentaje que representa la muestra del universo total.

## Requisitos

- Python 3.x
- pandas

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala la biblioteca pandas ejecutando:
   ```
   pip install pandas
   ```
3. Descarga el archivo `main.py` de este repositorio.

## Uso

1. Ejecuta el script desde la línea de comandos:
   ```
   python main.py
   ```
2. Sigue las instrucciones en pantalla para ingresar:
   - Número de departamentos
   - Nombre y número de empleados de cada departamento
   - Tamaño total de la muestra deseada
3. El programa mostrará:
   - El tamaño total del universo (número total de empleados)
   - El porcentaje que representa la muestra del universo
   - Una tabla con el tamaño de muestra y porcentaje para cada departamento

## Estructura del código

- El código utiliza pandas para manejar y calcular los datos eficientemente.
- Se emplea un bucle para recopilar la información de cada departamento.
- Los cálculos de muestreo estratificado se realizan utilizando operaciones vectorizadas de pandas.

## Resultados

El programa genera:
1. Un resumen del tamaño total del universo y el porcentaje que representa la muestra.
2. Una tabla que muestra, para cada departamento:
   - Nombre del departamento
   - Tamaño de muestra calculado
   - Porcentaje que representa respecto al total de la muestra

## Notas

- Este proyecto es una herramienta educativa para entender y aplicar el concepto de muestreo estratificado.
- La calculadora asume que el muestreo es proporcional al tamaño de cada estrato (departamento).
