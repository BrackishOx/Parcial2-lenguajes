# **Punto 3 - Ambigüedad en la gramática if-then-else**

## **Enunciado**

Demostrar que la siguiente gramática es ambigua y corregirla:

```
prop → if expr then prop
     | prop_emparejada

prop_emparejada → if expr then prop_emparejada else prop
                | otras
```
 Adicionalmente, se implementó un ejemplo práctico en Python para ilustrar el comportamiento de la gramática y reforzar la comprensión del problema de ambigüedad.
---

## **Demostración de ambigüedad**

Se analiza la siguiente cadena:

```
if E1 then if E2 then S1 else S2
```

Esta cadena tiene dos interpretaciones posibles:

### **Interpretación 1 (else asociado al if interno)**

```
if E1 then (if E2 then S1 else S2)
```

### **Interpretación 2 (else asociado al if externo)**

```
(if E1 then if E2 then S1) else S2
```

Dado que una misma cadena puede interpretarse de dos maneras distintas, la gramática es **ambigua**.

---

## **Análisis de la gramática dada**

Aunque la gramática intenta separar las producciones en emparejadas y no emparejadas, sigue permitiendo múltiples derivaciones para una misma cadena.

Esto ocurre porque el `else` puede asociarse tanto al `if` más interno como al más externo, generando ambigüedad.

---

## **Solución: gramática no ambigua**

Se define una nueva gramática que elimina la ambigüedad:

```
stmt → matched | unmatched

matched → if expr then matched else matched
        | otras

unmatched → if expr then stmt
          | if expr then matched else unmatched
```

---

## **Explicación**

* `matched`: representa instrucciones donde cada `if` tiene su `else`.
* `unmatched`: representa instrucciones donde hay `if` sin `else`.

Esta separación garantiza que el `else` se asocie siempre con el `if` más cercano, eliminando la ambigüedad.

---

## **Conclusión**

La ambigüedad en la gramática del `if-then-else` es un problema clásico en el diseño de lenguajes de programación. Mediante la separación en producciones `matched` y `unmatched`, es posible eliminar esta ambigüedad y definir una gramática clara y determinista.
