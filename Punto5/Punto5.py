import re

class AnalizadorDescendenteRecursivo:
    def __init__(self, entrada):
        self.tokens = self.tokenizar(entrada)
        self.posicion = 0  # posicion de token 

    def tokenizar(self, entrada):
        tokens = []
        entrada = entrada.strip()
        i = 0
        while i < len(entrada):
            if entrada[i].isspace():
                i += 1
                continue

            # Palabras clave
            if entrada[i:i+2] == "if":
                tokens.append("if")
                i += 2
            elif entrada[i:i+4] == "then":
                tokens.append("then")
                i += 4

            # Identificadores
            elif entrada[i].isalpha():
                j = i
                while j < len(entrada) and entrada[j].isalnum():
                    j += 1
                tokens.append(entrada[i:j])  # guardar nombre real
                i = j

            # Números
            elif entrada[i].isdigit():
                j = i
                while j < len(entrada) and entrada[j].isdigit():
                    j += 1
                tokens.append(entrada[i:j])
                i = j

            # Operadores y símbolos
            elif entrada[i] in ['+', '*', '(', ')', '=']:
                tokens.append(entrada[i])
                i += 1

            else:
                raise ValueError(f"Carácter no válido: {entrada[i]}")

        return tokens

    def emparejar(self, esperado):
        if self.posicion < len(self.tokens) and self.tokens[self.posicion] == esperado:
            self.posicion += 1
            return True
        return False

    # 
    def analizar_stmt(self):
        posicion_inicial = self.posicion

        # Caso: if expr then stmt
        if self.emparejar("if"):
            if self.analizar_E() and self.emparejar("then") and self.analizar_stmt():
                return True
            self.posicion = posicion_inicial
            return False

        # Caso: id = expr
        if self.posicion < len(self.tokens) and self.tokens[self.posicion].isidentifier():
            self.posicion += 1  # consumir id
            if self.emparejar("=") and self.analizar_E():
                return True
            self.posicion = posicion_inicial
            return False

        return False

    
    def analizar_E(self):
        posicion_inicial = self.posicion
        if self.analizar_T() and self.analizar_E_prima():
            return True
        self.posicion = posicion_inicial
        return False

    def analizar_E_prima(self):
        posicion_inicial = self.posicion
        if self.emparejar('+'):
            if self.analizar_T() and self.analizar_E_prima():
                return True
            self.posicion = posicion_inicial
            return False
        return True

    def analizar_T(self):
        posicion_inicial = self.posicion
        if self.analizar_F() and self.analizar_T_prima():
            return True
        self.posicion = posicion_inicial
        return False

    def analizar_T_prima(self):
        posicion_inicial = self.posicion
        if self.emparejar('*'):
            if self.analizar_F() and self.analizar_T_prima():
                return True
            self.posicion = posicion_inicial
            return False
        return True

    def analizar_F(self):
        posicion_inicial = self.posicion

        # identificadores o números
        if self.posicion < len(self.tokens) and (
            self.tokens[self.posicion].isidentifier() or self.tokens[self.posicion].isdigit()
        ):
            self.posicion += 1
            return True

        # paréntesis
        if self.emparejar('('):
            if self.analizar_E() and self.emparejar(')'):
                return True
            self.posicion = posicion_inicial

        return False

    def analizar(self):
        resultado = self.analizar_stmt()
        return resultado and self.posicion == len(self.tokens)


#  PRUEBAS
def probar_analizador(entrada):
    try:
        analizador = AnalizadorDescendenteRecursivo(entrada)
        print(f"\nEntrada: '{entrada}'")
        print(f"Tokens: {analizador.tokens}")
        if analizador.analizar():
            print("Resultado: Sintaxis correcta")
        else:
            print("Resultado: Sintaxis incorrecta")
    except ValueError as e:
        print(f"Resultado: Error - {e}")


#  PRUEBAS VÁLIDAS
probar_analizador("x = a + b")
probar_analizador("if x then y = a * b")
probar_analizador("if x then if y then z = a")

#  PRUEBAS INVÁLIDAS
probar_analizador("= x a")
probar_analizador("if then x")
probar_analizador("x = ")
