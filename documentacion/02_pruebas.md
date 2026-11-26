# Etapa 4 — Pruebas y validación

Todas las pruebas se hicieron corriendo main.py desde la consola, con el entorno virtual
activado, y metiendo los datos por teclado igual que lo haría cualquiera

Lo primero que probé fue el ejercicio de mi libreta, porque si eso no cuadra lo demás no
sirve de nada Las capturas están en evidencias/ejecuciones/

---

## CP-01 — El ejercicio original, comprobable a mano

**Objetivo:** Ver si el programa saca los mismos rectángulos que yo saqué con lápiz en el
paso 3 y el paso 4 de mi procedimiento

**Entradas:**

- Opción 1, grado 1, coeficientes 1 y 3, o sea f(x) = x + 3
- Opción 3, a = -2, b = 3
- Opción 5, n = 5, tipo derecho

**Resultado esperado:** 20.0, porque con n = 5 la fórmula de mi suma da
S(5) = 5 + 25(5+1)/(2·5) = 20

**Resultado obtenido:** Resultado: 20.0

**Estado:** PASA

**Observaciones:** Con la opción 6 revisé los cinco rectángulos uno por uno y dan las
alturas 2, 3, 4, 5 y 6, que son exactamente las que salen de evaluar f(x_i) = 1 + (5/n)i
para i de 1 a 5 La suma 2+3+4+5+6 = 20 cuadra Este es el caso que más me importaba

---

## CP-02 — El mismo ejercicio con n grande, para ver el límite

**Objetivo:** Comprobar que conforme n crece la suma se acerca al 35/2 = 17.5 que saqué
tomando el límite

**Entradas:**

- La misma función f(x) = x + 3 y el mismo intervalo [-2, 3]
- Opción 5 cuatro veces, con n = 10, luego 100, luego 1000 y luego 10000, siempre tipo derecho

**Resultado esperado:** Que los números bajen acercándose a 17.5 sin pasarse

**Resultado obtenido:**

- n = 10 -> 18.75
- n = 100 -> 17.625
- n = 1000 -> 17.5125
- n = 10000 -> 17.50125

**Estado:** PASA

**Observaciones:** Esta es la prueba que demuestra que el programa está haciendo lo mismo
que yo hice en la libreta Con n = 10000 va 0.00125 arriba del 17.5, y mientras más suba la
n más se pega Nunca va a dar 17.5 clavado con el extremo derecho porque el límite es
cuando n tiende a infinito, y el programa no puede llegar hasta allá

---

## CP-03 — Otra función distinta, para ver que no está amarrado a mi caso

**Objetivo:** Probar con una parábola, que no tiene nada que ver con mi ejercicio, y ver si
también da bien

**Entradas:**

- Opción 1, grado 2, coeficientes 1, 0 y 0, o sea f(x) = x^2
- Opción 3, a = 0, b = 1
- Opción 5, n = 1000, tipo medio

**Resultado esperado:** Algo muy cerca de 0.333333, porque el área bajo x^2 de 0 a 1 es 1/3

**Resultado obtenido:** Resultado: 0.333333

**Estado:** PASA

**Observaciones:** Lo escogí porque es un resultado que me sé de memoria y me deja ver si la
clase sirve para cualquier polinomio y no nada más para el mío También comprueba que
a_texto escriba bien las potencias, porque imprimió f(x) = x^2

---

## CP-04 — Caso límite, el n más chico que se permite

**Objetivo:** Ver qué pasa con n = 1, que es el mínimo que acepta el programa Es un solo
rectángulo que cubre todo el intervalo

**Entradas:**

- f(x) = x + 3, a = -2, b = 3
- Opción 5, n = 1, tipo derecho

**Resultado esperado:** 30.0, porque con un solo rectángulo delta x vale 5, la única
coordenada es x_1 = -2 + 5 = 3, su altura es f(3) = 6, y 6 por 5 da 30

**Resultado obtenido:** Resultado: 30.0

**Estado:** PASA

**Observaciones:** Da bien aunque el número esté lejísimos del 17.5 Y así tiene que ser: con
un solo rectángulo la aproximación es malísima, pero no está mal calculada Es la diferencia
entre un error del programa y un resultado feo pero correcto

---

## CP-05 — Caso límite, el intervalo que no tiene ancho

**Objetivo:** Ver que si a y b son iguales el programa devuelve 0 sin ponerse a sumar
rectángulos de ancho cero

**Entradas:**

- f(x) = x + 3
- Opción 3, a = 2, b = 2
- Opción 5, n = 5, tipo derecho

**Resultado esperado:** 0, que es la regla R2

**Resultado obtenido:** Resultado: 0

**Estado:** PASA

**Observaciones:** El intervalo pasa la validación porque es_intervalo_valido pregunta si a
es menor o igual que b, y aquí son iguales Luego suma_riemann corta antes del ciclo y
devuelve 0 directo Si no tuviera ese corte, delta x valdría 0 y daría 0 de todas formas,
pero dando vueltas de más

---

## CP-06 — Entradas inválidas

**Objetivo:** Ver que el programa aguanta cuando meto cosas que no son números, sin tronar
ni cerrarse

**Entradas, una por una:**

- En el menú escribí abc
- En el menú escribí 99
- En el coeficiente escribí hola
- Entré a la opción 2 sin haber definido función
- Entré a la opción 5 sin haber definido intervalo
- Entré a la opción 7 sin haber calculado nada

**Resultado esperado:** Un mensaje claro en cada caso y volver a preguntar, nunca un error
de Python

**Resultado obtenido:**

- abc -> Eso no es un numero entero, intenta otra vez
- 99 -> El numero debe estar entre 1 y 8
- hola -> Eso no es un numero, intenta otra vez, y lo vuelve a pedir
- opción 2 sin función -> Primero define una funcion con la opcion 1
- opción 5 sin intervalo -> Primero define un intervalo valido con la opcion 3
- opción 7 sin cálculos -> Todavia no has calculado nada

**Estado:** PASA

**Observaciones:** Es la regla R4 En ningún momento salió un traceback ni se cerró el
programa Después de cada mensaje vuelve al menú y sigue funcionando normal

---

## CP-07 — La regla del intervalo al revés

**Objetivo:** Probar la regla R1, que dice que si a es mayor que b el programa avisa y no
calcula

**Entradas:**

- f(x) = x + 3
- Opción 3, a = 5, b = 1
- Luego opción 4, para ver si de verdad quedó sin intervalo

**Resultado esperado:** Que rechace el intervalo y que la opción 4 siga diciendo que no hay
intervalo definido

**Resultado obtenido:**

- Al definir el intervalo -> a no puede ser mayor que b
- Al entrar a la opción 4 -> Primero define un intervalo valido con la opcion 3

**Estado:** PASA

**Observaciones:** Lo importante aquí es la segunda parte No basta con que avise, tiene que
dejar el objeto integral sin crear Si nada más avisara y guardara el intervalo al revés, la
opción 5 calcularía un área negativa sin que yo me enterara

---

## CP-08 — El punto medio con una recta

**Objetivo:** Comprobar algo que me llamó la atención: que con tipo medio el resultado da
clavado desde n chiquita

**Entradas:**

- f(x) = x + 3, a = -2, b = 3
- Opción 5, n = 5, tipo medio

**Resultado esperado:** 17.5 exacto, aunque n sea apenas 5

**Resultado obtenido:** Resultado: 17.5

**Estado:** PASA

**Observaciones:** Pasa porque mi función es una recta Con el punto medio, lo que le sobra a
un rectángulo por un lado es justo lo que le falta por el otro, y se cancela Por eso da
exacto y no hay que subirle la n Con la parábola del CP-03 ya no da exacto, nada más se
acerca mucho

---

## CP-09 — Que el intervalo viejo no se quede pegado

**Objetivo:** Probar que si cambio la función, el intervalo que ya tenía se borra

**Entradas:**

- Defino f(x) = x + 3, intervalo [-2, 3], calculo con n = 5
- Vuelvo a la opción 1 y defino f(x) = 2
- Entro directo a la opción 5 sin pasar por la opción 3
- Después defino el intervalo [0, 1] y calculo con n = 10
- Reviso el historial con la opción 7

**Resultado esperado:** Que la opción 5 me mande a definir intervalo, y que el historial
guarde cada cálculo con los límites que de verdad le tocaban

**Resultado obtenido:**

- Opción 5 después de cambiar la función -> Primero define un intervalo valido con la opcion 3
- Historial -> f(x) = x + 3 con [-2.0, 3.0] y n = 5 dio 20.0, y f(x) = 2 con [0.0, 1.0] y
  n = 10 dio 2.0

**Estado:** PASA

**Observaciones:** Esto no venía en mi especificación, lo encontré probando Si el intervalo
se quedara pegado, el programa integraría la función nueva sobre el intervalo viejo y el
número saldría mal sin ningún aviso El historial sí guardó bien los límites de cada uno por
separado

---

## Resumen

- Casos ejecutados: 9
- Pasaron: 9
- Fallaron: 0

No tuve que corregir nada en esta etapa El único error que encontré en todo el proyecto fue
el del .0 en a_texto, y ese salió en la etapa 3 cuando revisé la primera clase, antes de
llegar a las pruebas Está contado en documentacion/03_uso_copilot.md

## Capturas

- evidencias/ejecuciones/menu_principal.png -> el menú con las 8 opciones
- evidencias/ejecuciones/caso_original.png -> el CP-01 dando 20.0
- evidencias/ejecuciones/pruebas_adicionales.png -> las entradas inválidas del CP-06
