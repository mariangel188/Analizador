# Analizador léxico
Un analizador léxico es un intérprete que se encaraga de leer el código fuente línea por línea para dividirlo en tokens y los clasifica segun sean palabras clave, operadores, identificadores o números.
# Definición del lenguaje
### Estructura general

El lenguaje en Python lee lo siguiente:
- Declaraciones de variables (`=`, `:=`)
- Tipos de datos (`int`, `float`)
- Estructuras de control (`if`, `else`, `while`, `for`)
- Funciones (`def`, `print`, `input`)
- Operadores matemáticos, lógicos y de comparación

### Instrucciones reconocidas

| Categoría                | Instrucciones                     |
|--------------------------|----------------------------------------------|
| Asignación               | =, :=                                    |
| Tipos de dato            | int, float                               |
| Estructuras de control   | if, else, elif, while, for         |
| Operadores matemáticos   | +, -, *, /, %, **                |
| Operadores comparación   | ==, !=, <, <=, >, >=              |
| Operadores lógicos       | and, or, not                           |
| Funciones comunes        | print(), input()                        |
| Delimitadores            | (), [], {}                             |
| Separadores              | ,, :, .                                |

## Sintaxis de cada instrucción
```
# Este es un programa de prueba
x = 10
y := 5.5                # Asignación con :=

if x > y:               # Estructura de control condicional
    print("x es mayor que y")  # Función built-in(print)
else:
    print("x no es mayor")

contador = 0
while contador < 3:     # Bucle while
    print("Contando:", contador)
    contador += 1       # Operador de asignación combinado

def saludar(nombre):    # Definición de función
    print("Hola", nombre)

saludar("Mariangel")    # Llamada a función
```
