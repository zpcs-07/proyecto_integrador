# Etapa 1 — Análisis del problema

## 1. Nombre del problema y asignatura

**Problema:** Área bajo la curva con la integral definida, resuelta como límite de una suma
de Riemann

**Asignatura donde lo estudié:** Cálculo

Lo vimos cuando entramos a integrales definidas La idea era entender que la integral es una
suma de rectangulitos, y que entre más rectángulos metes, más se acerca al área de verdad

## 2. Descripción, justificación y planteamiento original

### De qué va el problema

Tengo una función y un intervalo Quiero saber cuánta área hay entre la curva y el eje x,
entre esos dos límites

La forma en que lo vimos es esta: parto el intervalo en n pedazos iguales, pongo un
rectángulo sobre cada pedazo, sumo todas las áreas, y luego hago que n se vaya al infinito

```
Área = lim (n→∞) Σ (i=1 hasta n) f(x_i) · Δx
```

### Por qué este problema sirve para el proyecto

Porque se parte en dos cosas que no se tocan, y de ahí salen las dos clases La función solo
necesita saber evaluarse en un punto La integral necesita los límites y en cuántos
rectángulos partir

Y de paso usa todo lo que pide el proyecto: un ciclo para recorrer los n rectángulos, una
lista para guardar los coeficientes, y condiciones para las validaciones No es nada más
pedir dos números y hacer una cuenta

### Planteamiento original (tal cual lo hice en la libreta)

Ejemplos integrales definidas

Calcular la integral desde -2 hasta 3 de (x + 3) dx usando la definición de integral
definida como límite de una suma de Riemann

Estos fueron los 4 pasos que seguí:

1. Definir la amplitud del intervalo: A = x_f − x_i
2. Escoger el tamaño de los subintervalos: Δx = A / n
3. Establecer la coordenada x del i-ésimo subintervalo: x_i = x_0 + i·Δx
4. Expresar f(x) en términos de x_i

## 3. Entradas

- grado -> int -> de 0 a 10 -> El grado del polinomio
- coeficientes -> list[float] -> grado + 1 números -> Los coeficientes, del término más grande al independiente
- limite_inferior (a) -> float -> cualquier real -> Dónde empieza el intervalo
- limite_superior (b) -> float -> cualquier real -> Dónde termina el intervalo
- n -> int -> 1 o más -> En cuántos rectángulos parto el intervalo
- tipo_punto -> str -> derecho, izquierdo o medio -> Qué punto del rectángulo uso para la altura
- opcion_menu -> int -> 1, 2 o 3 -> Lo que elijo en el menú

## 4. Procesos: fórmulas, reglas y decisiones

### Las fórmulas

1. **Amplitud:** A = b − a, es mi paso 1
2. **Tamaño del subintervalo:** Δx = A / n, es mi paso 2
3. **Coordenada del punto i**, mi paso 3:
   - derecho: x_i = a + i·Δx, con i de 1 a n (el que usé en la libreta)
   - izquierdo: x_i = a + (i−1)·Δx
   - medio: x_i = a + (i − 0.5)·Δx
4. **Evaluar la función:** f(x) = c_n·x^n + ... + c_1·x + c_0, es mi paso 4
5. **Suma de Riemann:** S(n) = Σ (i=1 hasta n) f(x_i) · Δx

### Reglas que el programa debe respetar

- **R1** Si a es mayor que b, aviso y no calculo El orden importa porque cambia el signo
- **R2** Si a es igual a b, el resultado es 0 directo, sin sumar nada
- **R3** El resultado puede salir negativo si la curva va por debajo del eje x Eso no es un
  error, es lo que significa la integral
- **R4** Si escriben algo que no es número, lo rechazo y vuelvo a preguntar El programa nunca
  debe tronar
- **R5** n tiene que ser entero y de 1 para arriba
- **R6** No se calcula nada si todavía no hay función ni intervalo El menú avisa
- **R7** Los coeficientes tienen que ser exactamente grado + 1

## 5. Salidas esperadas

- La función escrita bonita, tipo f(x) = x + 3
- La amplitud A
- El Δx para la n que elegí
- La suma de Riemann S(n), que es el área aproximada
- Los primeros rectángulos con su x y su altura, para comprobar a mano

## 6. Ejemplo original resuelto

Este es el ejercicio de la foto, el que tiene que reproducir el programa

**Integral:** desde -2 hasta 3 de (x + 3) dx

**Paso 1 — amplitud:**

```
A = x_f − x_i = 3 − (−2) = 5
```

**Paso 2 — tamaño de los subintervalos:**

```
Δx = A/n = 5/n
```

**Paso 3 — coordenada x del punto i:**

```
x_i = x_0 + i·Δx = −2 + (5/n)·i
```

**Paso 4 — la función en términos de x_i:**

```
f(x) = x + 3
f(x_i) = (−2 + (5/n)i) + 3 = 1 + (5/n)i
```

**Armando la suma:**

```
Área = lim (n→∞) Σ (i=1 hasta n) [ 1 + (5/n)i ] · (5/n)

     = lim (n→∞) [ Σ (5/n) + Σ (25/n²)·i ]

     = lim (n→∞) [ (5/n)·n + (25/n²) · n(n+1)/2 ]

     = lim (n→∞) [ 5 + (25/2) · (n² + n)/n² ]

     = lim (n→∞) [ 5 + (25/2)·(1 + 1/n) ]

     = lim (n→∞) [ 5 + 25/2 + 25/(2n) ]
```

El 25/(2n) se va a 0 cuando n tiende a infinito, y queda:

```
Área = 5 + 25/2 = 35/2 = 17.5 u²
```

**Resultado conocido: 35/2 = 17.5 u²**

Mi suma usa el extremo derecho, así que el programa tiene que irse acercando a 17.5 conforme
le suba la n Eso es justo lo que dice el límite

## 7. Alcance de la aplicación

Lo que sí hace:

1. Pide una función y un intervalo, y los valida
2. Escribe la función de forma legible
3. Saca la amplitud y el Δx
4. Calcula la suma de Riemann con punto derecho, izquierdo o medio
5. Muestra los primeros rectángulos para comprobar a mano
6. Sale de forma ordenada

El menú se queda en tres opciones: definir, calcular y salir Todo lo demás se imprime dentro
del cálculo, en el orden de mis cuatro pasos

Lo que **no** hace:

- Funciones que no sean polinomios, o sea nada de senos, cosenos ni exponenciales
- Integrales impropias o con límites infinitos
- Gráficas, porque es de consola

## 8. Comprobación de que cumple los requisitos técnicos

- Problema de otra materia -> Sí, de Cálculo, y tengo la foto de la libreta
- Entradas, procesos y salidas -> Sí, en las secciones 3, 4 y 5
- Reglas y validaciones -> Sí, las reglas R1 a R7
- Viable en consola -> Sí, todo es teclado y texto
- Dos clases con responsabilidades distintas -> Sí, FuncionPolinomial evalúa la función e IntegralDefinida parte el intervalo y suma
- Ejemplo verificable -> Sí, el 17.5 de la libreta
- Variables, operaciones, condiciones y ciclos -> Sí, ciclos para evaluar y para sumar, y condiciones en las validaciones
- Al menos una lista -> Sí, dos: la de coeficientes y la que devuelve detalle_rectangulos
- main.py y clases separados -> Sí, main.py con el menú y la carpeta clases con un archivo por clase

## 9. Nota sobre el diseño

Mis 4 pasos se convierten casi uno a uno en métodos:

- Paso 1, la amplitud -> calcular_amplitud()
- Paso 2, el Δx -> calcular_delta_x(n)
- Paso 3, la coordenada x_i -> calcular_coordenada(i, n, tipo)
- Paso 4, evaluar f(x_i) -> FuncionPolinomial.evaluar(x)
- Armar la suma -> suma_riemann(n, tipo)

Así cada método tiene un porqué y no es código puesto nada más para rellenar
