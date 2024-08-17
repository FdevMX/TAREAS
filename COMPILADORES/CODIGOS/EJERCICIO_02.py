# Alumno: Alfredo Lopez Mendez
# Matricula: A221639
# Fecha: 16 de Agosto del 2024

# Analizador lexico en python, 
# se incluye mas de 60 tokens, 30 palabras reservadas,
# interfaz grafica con botones y tablas

import re
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import simpledialog


# Lista de palabras reservadas
reserved_words = [
    'if', 'else', 'elif', 'for', 'in', 'while', 'break', 'continue', 'pass', 'return',
    'def', 'class', 'try', 'except', 'finally', 'with', 'as', 'raise', 'assert', 'import',
    'from', 'global', 'nonlocal', 'lambda', 'not', 'and', 'or', 'True', 'False', 'None'
]

# expresión regular que coincida con cualquier palabra reservada
reserved_pattern = r'\b(' + '|'.join(reserved_words) + r')\b'

# Definición de tokens
token_patterns = [
    ('PALABRA_RESERVADA', reserved_pattern), # Palabra reservada
    ('NUMERO', r'\d+'),                      # Número entero
    ('IDENTIFICADOR', r'[A-Za-z]\w*'),       # Identificador
    ('SUMA', r'\+'),                         # Operador de suma
    ('RESTA', r'-'),                         # Operador de resta
    ('MULTIPLICACION', r'\*'),               # Operador de multiplicación
    ('DIVISION', r'/'),                      # Operador de división
    ('PARENTESIS_IZQ', r'\('),               # Paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),               # Paréntesis derecho
    ('COMA', r','),                          # Coma
    ('PUNTO_Y_COMA', r';'),                  # Punto y coma
    ('DOS_PUNTOS', r':'),                    # Dos puntos
    ('IGUAL', r'='),                         # Operador de asignación
    ('MENOR_QUE', r'<'),                     # Operador menor que
    ('MAYOR_QUE', r'>'),                     # Operador mayor que
    ('MENOR_IGUAL', r'<='),                  # Operador menor o igual
    ('MAYOR_IGUAL', r'>='),                  # Operador mayor o igual
    ('IGUAL_IGUAL', r'=='),                  # Operador de igualdad
    ('DIFERENTE', r'!='),                    # Operador de desigualdad
    ('POTENCIA', r'\*\*'),                   # Operador de potencia
    ('MODULO', r'%'),                        # Operador de módulo
    ('MAS_IGUAL', r'\+='),                   # Operador de suma y asignación
    ('MENOS_IGUAL', r'-='),                  # Operador de resta y asignación
    ('POR_IGUAL', r'\*='),                   # Operador de multiplicación y asignación
    ('DIV_IGUAL', r'/='),                    # Operador de división y asignación
    ('MOD_IGUAL', r'%='),                    # Operador de módulo y asignación
    ('POT_IGUAL', r'\*\*='),                 # Operador de potencia y asignación
    ('ESPACIO', r'\s+'),                     # Espacios
    ('SIMBOLO', r'.'),                       # Otros caracteres
    ('COMILLAS_SIMPLES', r'\''),             # Comillas simples
    ('COMILLAS_DOBLES', r'\"'),              # Comillas dobles
    ('LLAVE_IZQ', r'{'),                     # Llave izquierda
    ('LLAVE_DER', r'}'),                     # Llave derecha
    ('CORCH_IZQ', r'\['),                    # Corchete izquierdo
    ('CORCH_DER', r'\]'),                    # Corchete derecho
    ('PUNTO', r'\.'),                        # Punto
    ('ARROBA', r'@'),                        # Arroba
    ('DOLAR', r'\$'),                        # Dólar
    ('GATO', r'\^'),                         # Gato
    ('BARRA_INVERSA', r'\\'),                # Barra invertida
    ('BARRA', r'/'),                         # Barra
    ('ASTERISCO', r'\*'),                    # Asterisco
    ('MAS', r'\+'),                          # Más
    ('MENOS', r'-'),                         # Menos
    ('TILDE', r'~'),                         # Tilde
    ('PIPE', r'\|'),                         # Pipe
    ('CIRCUNFLEXO', r'\^'),                  # Circunflejo
    ('DOS_PUNTOS_IGUAL', r'::'),             # Dos puntos igual
    ('MAYUSCULA', r'[A-Z]'),                 # Letra mayúscula
    ('MINUSCULA', r'[a-z]'),                 # Letra minúscula
    ('DIGITO', r'\d'),                       # Dígito
    ('NO_DIGITO', r'\D'),                    # No dígito
    ('LETRA', r'\w'),                        # Letra
    ('NO_LETRA', r'\W'),                     # No letra
    ('ESPACIO_BLANCO', r'\s'),               # Espacio en blanco
    ('NO_ESPACIO_BLANCO', r'\S'),            # No espacio en blanco
    ('COMENTARIO', r'\#.*'),                 # Comentario
    ('DECIMAL', r'\d+\.\d+'),                # Número decimal
    ('EXPONENTE', r'\d+[eE][-+]?\d+'),       # Número en notación exponencial
    ('CADENA_MULTILINEA', r'\"\"\".*?\"\"\"'), # Cadena multilinea entre comillas triples
    ('CADENA_MULTILINEA_SIMPLE', r"\'\'\'.*?\'\'\'"), # Cadena multilinea entre comillas triples simples
    ('COMENTARIO_MULTILINEA', r'\"\"\"[^\"]*\"\"\"'), # Comentario multilinea entre comillas triples
    ('PREGUNTA', r'\?'),                     # Signo de interrogación (no común en Python pero puede ser útil en otros contextos)
    ('GUION_BAJO', r'_'),                    # Guion bajo (a menudo usado en nombres de variables en Python)
]


# token expresiones regulares patrones
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

def analyze_code():
    code = code_textbox.get('1.0', tk.END)
    tokens = tokenize(code)
    result_tree.delete(*result_tree.get_children())
    for i, token in enumerate(tokens):
        result_tree.insert('', 'end', values=(i+1, token[1], token[0]))

def clear_screen():
    code_textbox.delete('1.0', tk.END)
    result_tree.delete(*result_tree.get_children())

def paste_code():
    code_textbox.event_generate("<<Paste>>")


# Crear la ventana principal
root = tk.Tk()
root.title('Analizador Lexico')
root.geometry('1200x700')  # tamaño de la ventana
root.minsize(900, 600)  # tamaño mínimo de la ventana

# título a la aplicación
title_label = tk.Label(root, text="Analizador Lexico", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=3, sticky='ew')

# cuadro de texto para el código
code_label = tk.Label(root, text="Ingrese el código", font=("Helvetica", 12))
code_label.grid(row=1, column=0, sticky='ew')

# cuadro de texto para el código
code_textbox = scrolledtext.ScrolledText(root, width=40, height=10)
code_textbox.grid(row=2, column=0, rowspan=5, sticky='nsew', padx=10, pady=10)

# botones
paste_button = ttk.Button(root, text='Pegar', command=paste_code)
paste_button.grid(row=2, column=1, pady=10, padx=20)

analyze_button = ttk.Button(root, text='Analizar', command=analyze_code)
analyze_button.grid(row=3, column=1, pady=10, padx=20)

clear_button = ttk.Button(root, text='Limpiar', command=clear_screen)
clear_button.grid(row=4, column=1, pady=10, padx=20)

# título a la tabla de resultados
result_label = tk.Label(root, text="Resultados del análisis", font=("Helvetica", 12))
result_label.grid(row=1, column=2, sticky='ew')

# Treeview o tabla para los resultados
result_tree = ttk.Treeview(root, columns=('N', 'Token', 'Tipo'), show='headings')
result_tree.heading('N', text='N.')
result_tree.heading('Token', text='Token')
result_tree.heading('Tipo', text='Tipo')
result_tree.column('N', width=50)  # Define el ancho de la columna 'N'
result_tree.column('Token', width=200)  # Define el ancho de la columna 'Token'
result_tree.column('Tipo', width=200)  # Define el ancho de la columna 'Tipo'
result_tree.grid(row=2, column=2, rowspan=5, sticky='nsew', padx=10, pady=10)

# barras de desplazamiento para tabla
scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=result_tree.yview)
scrollbar_y.grid(row=2, column=3, rowspan=5, sticky='ns')
result_tree.configure(yscrollcommand=scrollbar_y.set)

scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=result_tree.xview)
scrollbar_x.grid(row=7, column=2, sticky='ew')
result_tree.configure(xscrollcommand=scrollbar_x.set)

# columnas y filas para que se expandan
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

root.mainloop()
