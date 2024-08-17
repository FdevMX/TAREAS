# Alumno: Alfredo Lopez Mendez
# Matricula: A221639
# Fecha: 16 de Agosto del 2024

# mi primer analizador lexico que solo me reconoce
# numeros enteros, identificadores, operadores

import re

# Crear tokens
token_patterns = [
    ('NUMERO', r'\d+'),                      # Número entero
    ('IDENTIFICADOR', r'[A-Za-z]\w*'),       # Identificador
    ('SUMA', r'\+'),                         # Operador de suma
    ('RESTA', r'-'),                         # Operador de resta
    ('MULTIPLICACION', r'\*'),               # Operador de multiplicación
    ('DIVISION', r'/'),                      # Operador de división
    ('PARENTESIS_IZQ', r'\('),               # Paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),               # Paréntesis derecho
    ('ESPACIO', r'\s+'),                     # Espacios
    ('SIMBOLO', r'.'),                       # Otros caracteres
]

# Token expresiones regulares patrones
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
get_token = re.compile(token_regex).match

def tokenize(code):
    line_number = 1
    line_start = 0
    position = 0
    tokens = []

    while position < len(code):
        match = get_token(code, position)
        if not match:
            raise RuntimeError(f'Error de Analisis en posicion {position}')
        
        for name, value in match.groupdict().items():
            if value:
                if name != 'ESPACIO':
                    tokens.append((name, value))
                break
        position = match.end()

    return tokens

code = "x = 2 + 4 * (2 - 8)"
tokens = tokenize(code)

# Contador para enumerar las impresiones
contador = 1
for token in tokens:
    print(f"{contador}: {token}")
    contador += 1