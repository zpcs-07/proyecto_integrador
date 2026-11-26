# Etapa 4 — Pruebas y validación

Todas las pruebas se hicieron corriendo main.py desde la consola, con el entorno virtual
activado, y metiendo los datos por teclado igual que lo haría cualquiera

Lo primero que probé fue el ejercicio de mi libreta, porque si eso no cuadra lo demás no
sirve de nada Las capturas están en evidencias/ejecuciones/

El menú tiene tres opciones: la 1 define la función y el intervalo, la 2 calcula el área y
la 3 sale Por eso casi todos los casos empiezan igual, con la opción 1

---

## CP-01 — El ejercicio original, comprobable a mano

**Objetivo:** Ver si el programa saca los mismos rectángulos que yo saqué con lápiz en el
paso 3 y el paso 4 de mi procedimiento

**Entradas:**

- Opción 1, grado 1, coeficientes 1 y 3, o sea f(x) = x + 3
- Límites a = -2 y b = 3
- Opción 2, n = 5, tipo derecho

**Resultado esperado:** 20.0, porque con n = 5 la fórmula de mi suma da
S(5) = 5 + 25(5+1)/(2·5) = 20

**Resultado obtenido:**

```
f(x) = x + 3
Intervalo definido: -2.0 a 3.0
Paso 1 - Amplitud: 5.0
Paso 2 - Delta x: 1.0
Rectangulo 1 - x: -1.0 - altura: 2.0 - area: 2.0
Rectangulo 2 - x: 0.0 - altura: 3.0 - area: 3.0
Rectangulo 3 - x: 1.0 - altura: 4.0 - area: 4.0
Rectangulo 4 - x: 2.0 - altura: 5.0 - area: 5.0
Rectangulo 5 - x: 3.0 - altura: 6.0 - area: 6.0
Resultado: 20.0
```

**Estado:** PASA

**Observaciones:** Esta es la prueba que más me importaba La amplitud 5 es mi paso 1, el
delta x de 1 es mi paso 2, las coordenadas -1, 0, 1, 2 y 3 son mi paso 3, y las alturas 2,
3, 4, 5 y 6 son mi paso 4, o sea f(x_i) = 1 + (5/n)i evaluada para i de 1 a 5 La suma
2+3+4+5+6 = 20 cuadra con la fórmula Los cuatro pasos de mi libreta salen en una sola
pantalla

---

## CP-02 — El mismo ejercicio con n grande, para ver el límite

**Objetivo:** Comprobar que conforme n crece la suma se acerca al 35/2 = 17.5 que saqué
tomando el límite

**Entradas:**

- La misma función f(x) = x + 3 y el mismo intervalo [-2, 3]
- Opción 2 cuatro veces, con n = 10, luego 100, luego 1000 y luego 10000, siempre tipo derecho

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
- Límites a = 0 y b = 1
- Opción 2, n = 1000, tipo medio

**Resultado esperado:** Algo muy cerca de 0.333333, porque el área bajo x^2 de 0 a 1 es 1/3

**Resultado obtenido:** Resultado: 0.333333

**Estado:** PASA

**Observaciones:** Lo escogí porque es un resultado que me sé de memoria y me deja ver si la
clase sirve para cualquier polinomio y no nada más para el mío También comprueba que
a_texto escriba bien las potencias, porque imprimió f(x) = x^2 y no f(x) = 1x^2 + 0x + 0

---

## CP-04 — Caso límite, el n más chico que se permite

**Objetivo:** Ver qué pasa con n = 1, que es el mínimo que acepta el programa Es un solo
rectángulo que cubre todo el intervalo

**Entradas:**

- f(x) = x + 3, a = -2, b = 3
- Opción 2, n = 1, tipo derecho

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
- Opción 1 con a = 2 y b = 2
- Opción 2, n = 5, tipo derecho

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
- Al elegir el tipo de punto escribí 0, luego hola, luego 7 y luego 5
- Aparte, entré a la opción 2 sin haber definido nada

**Resultado esperado:** Un mensaje claro en cada caso y volver a preguntar, nunca un error
de Python

**Resultado obtenido:**

- abc -> Eso no es un numero entero, intenta otra vez
- 99 -> El numero debe estar entre 1 y 3
- 0 en el tipo -> El numero debe estar entre 1 y 3
- hola en el tipo -> Eso no es un numero entero, intenta otra vez
- 7 en el tipo -> El numero debe estar entre 1 y 3
- 5 en el tipo -> El numero debe estar entre 1 y 3
- opción 2 sin definir -> Primero define la funcion y el intervalo con la opcion 1

**Estado:** PASA

**Observaciones:** Es la regla R4 En ningún momento salió un traceback ni se cerró el
programa Después de cada mensaje vuelve a preguntar lo mismo y sigue funcionando normal Se
ve en evidencias/ejecuciones/validaciones.png, donde después de aguantar los cuatro
intentos malos acepta el 1 y calcula bien el CP-04

---

## CP-07 — La regla del intervalo al revés

**Objetivo:** Probar la regla R1, que dice que si a es mayor que b el programa avisa y no
calcula

**Entradas:**

- Opción 1 con f(x) = 7, a = 5 y b = 1
- Luego opción 2, para ver si de verdad quedó sin intervalo

**Resultado esperado:** Que rechace el intervalo y que la opción 2 siga diciendo que no hay
nada definido

**Resultado obtenido:**

- Al definir el intervalo -> a no puede ser mayor que b
- Al entrar a la opción 2 -> Primero define la funcion y el intervalo con la opcion 1

**Estado:** PASA

**Observaciones:** Lo importante aquí es la segunda parte No basta con que avise, tiene que
dejar el objeto integral sin crear Si nada más avisara y guardara el intervalo al revés, la
opción 2 calcularía un área negativa sin que yo me enterara

---

## CP-08 — Los tres tipos de punto con la misma integral

**Objetivo:** Correr el mismo ejercicio con los tres tipos de punto y ver que cada uno da
distinto, para entender cuál se acerca más

**Entradas:**

- f(x) = x + 3, a = -2, b = 3, siempre con n = 5
- Opción 2 tres veces, cambiando el tipo: derecho, izquierdo y medio

**Resultado esperado:** El izquierdo por debajo del 17.5, el derecho por encima, y el medio
en medio de los dos

**Resultado obtenido:**

- izquierdo -> 15.0, con alturas 1.0, 2.0, 3.0, 4.0 y 5.0
- derecho -> 20.0, con alturas 2.0, 3.0, 4.0, 5.0 y 6.0
- medio -> 17.5, con alturas 1.5, 2.5, 3.5, 4.5 y 5.5

**Estado:** PASA

**Observaciones:** Lo bonito es que el medio da 17.5 clavado con apenas n = 5, que es el
mismo número que me costó todo el límite en la libreta Pasa porque mi función es una recta:
con el punto medio, lo que le sobra a un rectángulo por un lado es justo lo que le falta por
el otro, y se cancela Con la parábola del CP-03 ya no da exacto, nada más se acerca mucho

También se nota que 15.0 y 20.0 quedan a la misma distancia del 17.5, uno 2.5 abajo y el
otro 2.5 arriba, y que el promedio de los dos da 17.5 Eso es porque la recta sube parejo

Están en evidencias/ejecuciones/punto_izquierdo.png y punto_medio.png, y el derecho en
caso_original.png

---

## CP-09 — Cambiar de función sin que se quede pegado el intervalo viejo

**Objetivo:** Ver que cuando defino otra función, el intervalo también se reemplaza y no se
queda el de antes

**Entradas:**

- Opción 1 con f(x) = x^2 en [0, 1], y calculo con n = 1000 tipo medio
- Opción 1 otra vez con f(x) = x + 3 en [-2, 3], y calculo con n = 5 tipo derecho

**Resultado esperado:** 0.333333 el primero y 20.0 el segundo, cada uno con su propio
intervalo

**Resultado obtenido:**

- f(x) = x^2 con intervalo 0.0 a 1.0 -> Resultado: 0.333333
- f(x) = x + 3 con intervalo -2.0 a 3.0 -> Resultado: 20.0

**Estado:** PASA

**Observaciones:** Este riesgo lo quité juntando la función y el intervalo en una sola
opción Antes estaban separados y se podía cambiar la función dejando el intervalo viejo, y
el programa integraba la función nueva sobre un intervalo que ya no le tocaba, sin avisar
Ahora no se puede: o defines las dos cosas, o no defines nada

---

## CP-10 — Una función que va por debajo del eje x

**Objetivo:** Probar la regla R3, que dice que el resultado puede salir negativo cuando la
curva está abajo del eje, y que eso no es un error

**Entradas:**

- Opción 1, grado 2, coeficientes 1, 0 y -4, o sea f(x) = x^2 - 4
- Límites a = -2 y b = 2
- Opción 2, n = 4, tipo medio

**Resultado esperado:** Un número negativo, porque entre -2 y 2 la parábola x^2 - 4 va toda
por debajo del eje

**Resultado obtenido:**

```
f(x) = x^2 - 4
Paso 1 - Amplitud: 4.0
Paso 2 - Delta x: 1.0
Rectangulo 1 - x: -1.5 - altura: -1.75 - area: -1.75
Rectangulo 2 - x: -0.5 - altura: -3.75 - area: -3.75
Rectangulo 3 - x: 0.5 - altura: -3.75 - area: -3.75
Rectangulo 4 - x: 1.5 - altura: -1.75 - area: -1.75
Resultado: -11.0
```

**Estado:** PASA

**Observaciones:** Las cuatro alturas salen negativas porque f(-1.5), f(-0.5), f(0.5) y
f(1.5) son todos negativos, y la suma -1.75 - 3.75 - 3.75 - 1.75 da -11 Se comprueba en la
cabeza Escogí este caso porque es el que demuestra que el programa está calculando la
integral y no el área geométrica: si fuera el área daría +11

También se ve la simetría, el primer rectángulo vale lo mismo que el último y el segundo lo
mismo que el tercero, que es lo que uno espera de una parábola centrada en el cero

---

## Resumen

- Casos ejecutados: 10
- Pasaron: 10
- Fallaron: 0

No tuve que corregir nada en esta etapa El único error que encontré en todo el proyecto fue
el del .0 en a_texto, y ese salió en la etapa 3 cuando revisé la primera clase, antes de
llegar a las pruebas Está contado en documentacion/03_uso_copilot.md

## Capturas

- evidencias/ejecuciones/menu_principal.png -> el menú con las 3 opciones
- evidencias/ejecuciones/caso_original.png -> el CP-01 completo, con los cuatro pasos de mi procedimiento y el 20.0
- evidencias/ejecuciones/validaciones.png -> el CP-06 aguantando entradas malas, y el CP-04 con n = 1 dando 30.0
- evidencias/ejecuciones/punto_izquierdo.png -> el CP-08 con extremo izquierdo dando 15.0
- evidencias/ejecuciones/punto_medio.png -> el CP-08 con punto medio dando 17.5 exacto
- evidencias/ejecuciones/area_negativa.png -> el CP-10 con f(x) = x^2 - 4 dando -11.0
