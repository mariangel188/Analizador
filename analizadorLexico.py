import re

# Conjuntos definidos
declaracion_variables = {'=', ':='}
datos_numericos = {'int', 'float'}
estructuras = {'if', 'elif', 'else', 'while', 'for', 'break', 'continue', 'pass'}
operadores_matematicos = {'+', '-', '*', '/', '//', '%', '**'}
operadores_comparacion = {'==', '!=', '<', '>', '<=', '>='}
operadores_logicos = {'and', 'or', 'not'}
operadores_asignacion = {'+=', '-=', '*=', '/=', '%=', '//=', '**='}
delimitadores = {'(', ')', '[', ']', '{', '}'}
funciones_built_in = {'print', 'input', 'len', 'range', 'type', 'int', 'float', 'str'}
palabras_reservadas = {'def', 'return', 'import', 'from', 'as', 'global', 'nonlocal', 'lambda', 'class', 'with', 'try',
                       'except', 'finally', 'raise', 'assert', 'yield', 'del', 'in', 'is', 'True', 'False', 'None'}
comentarios = {'#'}
separadores = {',', ':', '.', ';'}

# Función para dividir líneas en tokens
def tokenize(line):
    token_pattern = r'#.*|:=|==|!=|<=|>=|//|\*\*|[-+*/%=<>(),:{}[\];.]|\d+\.\d+|\d+|[a-zA-Z_]\w*'
    return re.findall(token_pattern, line)

# Clasificador de tokens
def clasificar_token(token):
    if token in declaracion_variables:
        return "Asignación"
    elif token in datos_numericos:
        return "Tipo de dato"
    elif token in estructuras:
        return "Estructura de control"
    elif token in operadores_matematicos:
        return "Operador matemático"
    elif token in operadores_comparacion:
        return "Operador de comparación"
    elif token in operadores_logicos:
        return "Operador lógico"
    elif token in operadores_asignacion:
        return "Operador de asignación"
    elif token in delimitadores:
        return "Delimitador"
    elif token in funciones_built_in:
        return "Función built-in"
    elif token in palabras_reservadas:
        return "Palabra reservada"
    elif token in separadores:
        return "Separador"
    elif re.fullmatch(r'\d+\.\d+|\d+', token):
        return "Número"
    elif re.fullmatch(r'[a-zA-Z_]\w*', token):
        return "Identificador"
    elif token.startswith("#"):
        return "Comentario"
    else:
        return "Token no reconocido"

# Función principal
def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for num_linea, linea in enumerate(archivo, start=1):
                print(f"\n📄 Línea {num_linea}: {linea.strip()}")
                tokens = tokenize(linea)
                for token in tokens:
                    categoria = clasificar_token(token)
                    if categoria != "Token no reconocido":
                        print(f"  ✔️ Token reconocido: '{token}' → {categoria}")
                    else:
                        print(f"  ❌ Error léxico: '{token}' no es válido.")
    except FileNotFoundError:
        print(f"⚠️ Archivo '{nombre_archivo}' no encontrado.")

# Llamada desde consola
if __name__ == "__main__":
    archivo_fuente = "C:/Users/Maria Angel/OneDrive/Escritorio/Trabajo de autómatas/analizador.txt"

    analizar_archivo(archivo_fuente)
