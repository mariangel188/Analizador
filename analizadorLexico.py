import re

# Colores (puedes quitar si no usas consola que los soporte)
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"

# Tabla de tokens
tokens = {
    'PALABRA_RESERVADA': r'\b(if|else|while|return|int|float|print)\b',
    'IDENTIFICADOR': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'NUMERO': r'\b\d+(\.\d+)?\b',
    'OPERADOR': r'==|!=|<=|>=|[+\-*/=<>]',
    'PARENTESIS': r'[()]',
    'LLAVES': r'[{}]',
    'PUNTO_Y_COMA': r';',
    'CADENA': r'"[^"\n]*"',
    'COMENTARIO': r'//.*'
}

# Combina todos los patrones en uno solo
token_regex = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in tokens.items())

# Analizar una línea
def analizar_linea(linea, num_linea):
    print(f"\n{YELLOW}Línea {num_linea}:{RESET} {linea.strip()}")

    # Detectar si la línea completa es un comentario
    if re.fullmatch(tokens['COMENTARIO'], linea.strip()):
        print(f"{GREEN}✔️  {linea.strip()} → COMENTARIO{RESET}")
        return

    for match in re.finditer(token_regex, linea):
        tipo = match.lastgroup
        valor = match.group()
        print(f"{GREEN}✔️  {valor} → {tipo}{RESET}")

    # Detectar errores (palabras no reconocidas)
    pos = 0
    for match in re.finditer(token_regex, linea):
        if match.start() > pos:
            error = linea[pos:match.start()].strip()
            if error:
                print(f"{RED}❌  Error: '{error}' no es un token válido{RESET}")
        pos = match.end()

    if pos < len(linea):
        error = linea[pos:].strip()
        if error:
            print(f"{RED}❌  Error: '{error}' no es un token válido{RESET}")

# Analizar archivo completo
def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for num_linea, linea in enumerate(archivo, start=1):
                analizar_linea(linea, num_linea)
    except FileNotFoundError:
        print(f"{RED}Archivo '{nombre_archivo}' no encontrado.{RESET}")

# Ruta al archivo
if __name__ == "__main__":
    ruta = r"C:\Users\Maria Angel\OneDrive\Escritorio\Trabajo de autómatas\Analizador\analizador.txt"
    analizar_archivo(ruta)
