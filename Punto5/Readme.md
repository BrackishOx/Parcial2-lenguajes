# **Punto 5 - Analizador Descendente Recursivo**

## **Enunciado**

**5. Diseñe e implemente un algoritmo de emparejamiento para el algoritmo descendente recursivo.**

---

## **Ejecución**

```bash
python Punto5.py
```

---

## **Descripción**

Este analizador descendente recursivo valida un lenguaje simple que incluye:

* Asignaciones de variables
* Estructuras condicionales (`if-then`)
* Expresiones aritméticas con operadores `+` y `*`

---

## **Resultados esperados**

```
Entrada: 'x = a + b'
Tokens: ['x', '=', 'a', '+', 'b']
Resultado: Sintaxis correcta

Entrada: 'if x then y = a * b'
Tokens: ['if', 'x', 'then', 'y', '=', 'a', '*', 'b']
Resultado: Sintaxis correcta

Entrada: '= x a'
Tokens: ['=', 'x', 'a']
Resultado: Sintaxis incorrecta

Entrada: 'if then x'
Tokens: ['if', 'then', 'x']
Resultado: Sintaxis incorrecta
```

---

## **Características**

* **Lenguaje:** Python
* **Tipo de analizador:** Descendente Recursivo
* **Método:** Emparejamiento de tokens mediante funciones recursivas
* **Tipo de gramática:** LL(1), sin recursión por la izquierda

---

## **Gramática utilizada**

```
stmt → id = expr
     | if expr then stmt

expr → term expr'

expr' → + term expr'
      | ε

term → factor term'

term' → * factor term'
      | ε

factor → id | num | ( expr )
```

---

## **Entradas válidas**

* `x = a + b`
* `if x then y = a * b`
* `if x then if y then z = a`

---

## **Entradas inválidas**

* `= x a`
* `if then x`
* `x =`

---

## **Conclusiones**

* El analizador descendente recursivo permite implementar parsers de forma clara y estructurada.
* El algoritmo de emparejamiento asegura la correcta validación de los tokens.
* La inclusión de asignaciones y condicionales demuestra cómo extender el analizador a lenguajes más complejos.
* Este enfoque es fundamental en el diseño de compiladores e intérpretes.
