# Etapa 1 — Análisis del problema

## 1. Nombre del problema y asignatura

**Problema:** Cálculo del área bajo la curva usando la integral definida, resuelta como
límite de una suma de Riemann

**Asignatura donde lo estudié:** Cálculo Fue uno de los ejemplos que vimos cuando entramos
al tema de integrales definidas La idea era entender de dónde sale realmente la integral:
que es una suma de rectangulitos y que entre más rectángulos metes, más se acerca al área
verdadera

La evidencia del ejercicio original está en
evidencias/problema_original/ejercicio_original_integral_definida.jpg

## 2. Descripción, justificación y planteamiento original

### De qué va el problema

Tengo una función f(x) y un intervalo [a, b] Quiero saber cuánta área hay entre la curva,
el eje x y las dos rectas verticales que pasan por a y por b

El método que usé en Cálculo es partir el intervalo en n pedazos iguales, armar un
rectángulo sobre cada pedazo, sumar todas las áreas de los rectángulos y después hacer que
n se vaya al infinito:

```
Área = lim (n→∞) Σ (i=1 hasta n) f(x_i) · Δx
```

### Por qué este problema sirve para el proyecto

Porque se parte solo en pedazos que no tienen nada que ver entre sí, y de ahí salen las
clases: la función nada más necesita saber evaluarse en un punto, la integral necesita los
límites y el número de rectángulos, y el historial solo guarda lo que fui calculando Cada
una tiene su propia responsabilidad

Para armar la suma hay que recorrer los n rectángulos uno por uno, o sea un ciclo, y los
coeficientes de la función se guardan en una lista También hay varias cosas que validar
(que n sea entero positivo, que los coeficientes sean números, que el intervalo tenga
sentido), así que entran condiciones

Y no se reduce a pedir dos números y hacer una operación, que es justo lo que el proyecto
no acepta

### Planteamiento original (tal cual lo hice en la libreta)

> Ejemplos integrales definidas
>
> Calcular la integral desde -2 hasta 3 de (x + 3) dx usando la definición de integral
> definida como límite de una suma de Riemann

Y el procedimiento que seguí fueron 4 pasos:

1. Definir la amplitud del intervalo: A = x_f − x_i
2. Escoger el tamaño de los subintervalos: Δx = A / n
3. Establecer la coordenada x del i-ésimo subintervalo: x_i = x_0 + i·Δx
4. Expresar f(x) en términos de x_i

## 3. Entradas

- grado -> int -> de 0 a 10 -> Grado del polinomio que voy a integrar
- coeficientes -> list[float] -> deben ser grado + 1 valores numéricos -> Los coeficientes de la función, del término de mayor potencia al término independiente
- limite_inferior (a) -> float -> cualquier número real -> Dónde empieza el intervalo
- limite_superior (b) -> float -> cualquier número real -> Dónde termina el intervalo
- n -> int -> mayor o igual a 1 -> En cuántos rectángulos parto el intervalo
- tipo_punto -> str -> derecho, izquierdo o medio -> Qué punto de cada subintervalo uso para la altura del rectángulo
- opcion_menu -> int -> una de las opciones mostradas -> Lo que elijo en el menú

## 4. Procesos: fórmulas, reglas y decisiones

### Las fórmulas

1. **Amplitud del intervalo:** A = b − a, es el paso 1 de mi procedimiento
2. **Tamaño del subintervalo:** Δx = A / n, es el paso 2
3. **Coordenada del punto i**, que es el paso 3:
   - extremo derecho: x_i = a + i·Δx, con i de 1 a n (el que usé en la libreta)
   - extremo izquierdo: x_i = a + (i−1)·Δx
   - punto medio: x_i = a + (i − 0.5)·Δx
4. **Evaluar la función:** f(x) = c_n·x^n + ... + c_1·x + c_0, es el paso 4
5. **Suma de Riemann:** S(n) = Σ (i=1 hasta n) f(x_i) · Δx

### Reglas y decisiones que el programa debe respetar

- **R1** Si a es mayor que b, aviso al usuario y no calculo hasta que lo corrija En mi
  ejercicio el orden importa porque el signo del resultado cambia
- **R2** Si a es igual a b, el resultado es 0 directo, sin hacer ninguna suma
- **R3** El resultado puede salir negativo si la curva va por debajo del eje x Eso no es un
  error del programa, es lo que significa la integral
- **R4** Si el usuario escribe algo que no es número, el programa lo rechaza y vuelve a
  preguntar Nunca debe tronar con un error de Python
- **R5** n tiene que ser entero y mayor o igual a 1 Si meten 0 o negativo, se rechaza
- **R6** No se puede calcular nada si todavía no hay función definida ni intervalo El menú
  avisa en lugar de dejar que explote
- **R7** La lista de coeficientes tiene que tener exactamente grado + 1 elementos Si no, se
  pide de nuevo

## 5. Salidas esperadas

- La función escrita bonita, tipo f(x) = x + 3
- La amplitud A del intervalo
- El Δx para la n que elegí
- La suma de Riemann S(n) con el valor del área aproximada
- El detalle de los primeros rectángulos (su x_i y su f(x_i)) para poder comprobarlo a mano
- El historial de todo lo que calculé en la sesión

## 6. Ejemplo original resuelto

Este es el ejercicio de la foto, es el que tiene que reproducir el programa

**Integral:** desde -2 hasta 3 de (x + 3) dx

**Paso 1 — amplitud del intervalo:**

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

El término 25/(2n) se va a 0 cuando n tiende a infinito, entonces queda:

```
Área = 5 + 25/2 = 35/2 = 17.5 u²
```

**Resultado conocido: 35/2 = 17.5 u²**

### Lo que debería dar el programa

Como mi suma usa el extremo derecho, el programa con esta misma función y este mismo
intervalo tiene que acercarse a 17.5 conforme le suba la n Con n chica el número sale más
alto y conforme crece se va pegando al 17.5, que es justo lo que dice el límite

## 7. Alcance de la aplicación

Lo que va a hacer el programa:

1. Pedir una función polinomial (grado y coeficientes) y guardarla
2. Mostrar la función escrita de forma legible
3. Pedir y validar el intervalo [a, b]
4. Calcular la amplitud A y el Δx para una n dada
5. Calcular la suma de Riemann con extremo derecho, izquierdo o punto medio
6. Mostrar el detalle de los rectángulos para poder comprobarlo a mano
7. Guardar cada cálculo en un historial y poder consultarlo
8. Salir de forma ordenada

Lo que **no** va a hacer:

- Funciones que no sean polinomios (nada de seno, coseno, exponenciales o fracciones con x
  abajo)
- Integrales impropias o con límites infinitos
- Gráficas, porque es aplicación de consola

## 8. Comprobación de que cumple los requisitos técnicos

- Problema de otra materia -> Sí, es de Cálculo, y tengo la foto de la libreta como evidencia
- Entradas, procesos y salidas identificables -> Sí, están en las secciones 3, 4 y 5
- Reglas, validaciones o decisiones -> Sí, las reglas R1 a R7
- Viable en consola -> Sí, todo es entrada de números por teclado y salida de texto
- Al menos dos clases con responsabilidades distintas -> Sí, van tres: FuncionPolinomial representa y evalúa la función, IntegralDefinida hace las sumas de Riemann, e HistorialCalculos guarda y consulta los resultados
- Ejemplo original verificable -> Sí, el 17.5 de la libreta
- Variables, operaciones, condiciones, ciclos -> Sí, ciclos para evaluar el polinomio y para acumular la suma de Riemann, y condiciones en todas las validaciones
- Al menos una lista -> Sí, dos: la lista de coeficientes de la función y la lista de cálculos del historial
- main.py y módulos de clases separados -> Sí, main.py con el menú y el paquete clases con un archivo por clase

## 9. Nota sobre el diseño

Me gustó que los 4 pasos del procedimiento de la libreta se traducen casi uno a uno en
métodos de la clase IntegralDefinida:

| Paso en la libreta | Método en el programa |
|---|---|
| Paso 1: definir amplitud A = x_f − x_i | calcular_amplitud() |
| Paso 2: escoger Δx = A/n | calcular_delta_x(n) |
| Paso 3: establecer x_i = x_0 + i·Δx | calcular_coordenada(i, n, tipo) |
| Paso 4: expresar f(x) en términos de x_i | FuncionPolinomial.evaluar(x) |
| Armar la suma | suma_riemann(n, tipo) |

Así cada método tiene un porqué claro y no es código inventado nada más para rellenar
