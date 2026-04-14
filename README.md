# Parcial2


#  Parcial 2 — Lenguajes de Programación 

## Descripción General

Este proyecto corresponde al **Parcial 2** de la asignatura **Lenguajes de Programación**. El objetivo es diseñar, implementar y analizar diferentes componentes relacionados con **gramáticas formales** y **análisis sintáctico**, aplicados al diseño de un lenguaje de programación que permita realizar operaciones **CRUD** sobre una base de datos.
---

## Contenido del Proyecto

### **1. Diseño de la Gramática**

Se diseña una **gramática libre de contexto (GLC)** que define un lenguaje de programación con capacidad de realizar operaciones CRUD:

* **Create**
* **Read**
* **Update**
* **Delete**

---

### **2. Implementación de la Gramática en BISON o ANTLR**

Se implementa la gramática en una herramienta generadora de analizadores sintácticos:

* **ANTLR** (Java, Python, u otro)

Se realizan pruebas para verificar que el analizador reconozca correctamente programas escritos en el lenguaje diseñado.
Ejemplo de entrada esperada:

```txt
CREATE user VALUES (id=1, name="Ana");
READ user WHERE id=1;
UPDATE user SET name="Carlos" WHERE id=1;
DELETE user WHERE id=1;
```

---

### **3. Implementación de un Analizador Sintáctico Ascendente en Python**

Se parte de la siguiente gramática:

```
E → E + T | T
T → T * F | F
F → (E) | id
```

#### Actividades desarrolladas:

* **Transformación a una gramática LL(1)** (eliminación de recursión por la izquierda y factorización).
* **Cálculo de los conjuntos**:

  * **FIRST**
  * **FOLLOW**
  * **PREDICT**
* **Diseño del algoritmo ascendente basado en pila.**
* **Implementación en Python** con pruebas sobre expresiones aritméticas válidas e inválidas.

---

### **3. Implementación de un Analizador Sintáctico Ascendente en Python Ambiguedad**
```
if E1 then if E2 then S1 else S2
```
```
Caso 1 (else interno)
if E1 then (if E2 then S1 else S2)
```

```
Caso 2 (else externo)
(if E1 then if E2 then S1) else S2
prop → if expr then prop
     | if expr then prop else prop
     | otras
```
---

### **4. Implementación del Parser con el Algoritmo CYK**

Se implementa el **algoritmo CYK (Cocke–Younger–Kasami)** para el análisis sintáctico de gramáticas en **Forma Normal de Chomsky (FNC)**.

#### Objetivos:

* Validar cadenas del lenguaje definido.
* Comparar su rendimiento con un **parser predictivo** (descendente LL(1)).

---

### **5. Algoritmo de Emparejamiento (Matching) para el Parser Descendente Recursivo**

Se diseña un **algoritmo de emparejamiento de tokens** que sirva como base para un **parser descendente recursivo**.

El algoritmo:

* Reconoce tokens definidos por la gramática.
* Valida la secuencia sintáctica mediante llamadas recursivas.
* Permite detectar errores de emparejamiento o estructura.

---

##  Requisitos Técnicos

* **Lenguajes:** Python 3.10+ / C / Java (según herramienta usada)
* **Herramientas:**

  * [ANTLR](https://www.antlr.org/)
    
* **Sistema operativo:** Windows, Linux o macOS

---

## Pruebas y Validación

Cada componente fue probado mediante casos de entrada válidos e inválidos, verificando:

* Reconocimiento de la estructura sintáctica.
* Detección de errores de parsing.
* Comparación de rendimiento (tiempos promedio y número de operaciones).

---

##  Resultados Esperados

* Comprensión de los distintos tipos de analizadores sintácticos (ascendentes y descendentes).
* Implementación práctica de gramáticas y algoritmos de parsing.
* Análisis comparativo del rendimiento entre **CYK** y **LL(1)**.
* Aplicación de conceptos teóricos a un lenguaje de propósito específico (CRUD).

---

