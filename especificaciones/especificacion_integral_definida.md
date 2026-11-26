# Especificación de la clase IntegralDefinida

Archivo donde va: clases/integral_definida.py

## 1. Identificación de la clase

**Nombre:** IntegralDefinida

**Objetivo:** Calcular el área bajo la curva con sumas de Riemann, siguiendo los mismos 4
pasos que usé en la libreta

**Responsabilidad:** Esta clase sabe del intervalo y de cómo partirlo en rectángulos No sabe
cómo se evalúa la función, para eso le pide ayuda al objeto FuncionPolinomial que trae
guardado Tampoco guarda historial ni habla con el usuario

Esta es la clase principal del proyecto Cada método sale directo de un paso del
procedimiento:

- Paso 1 definir la amplitud -> calcular_amplitud()
- Paso 2 escoger el tamaño de los subintervalos -> calcular_delta_x(n)
- Paso 3 establecer la coordenada x_i -> calcular_coordenada(i, n, tipo)
- Paso 4 expresar f en términos de x_i -> se la pido a self.funcion.evaluar(x)
- Armar la suma -> suma_riemann(n, tipo)

## 2. Atributos

- funcion -> FuncionPolinomial -> El objeto de la función que voy a integrar -> Se recibe en el constructor
- limite_inferior -> float -> El valor de a, donde empieza el intervalo -> Se recibe en el constructor
- limite_superior -> float -> El valor de b, donde termina el intervalo -> Se recibe en el constructor

Aquí hay algo que quiero poder explicar: el atributo funcion no es un número ni un texto, es
**otro objeto** Eso es lo que hace que las dos clases colaboren

## 3. Constructor __init__

**Qué recibe:** self, funcion, limite_inferior, limite_superior

**Qué hace:**

1. Revisa que funcion sea un objeto de la clase FuncionPolinomial Si no, lanza TypeError
2. Revisa que los dos límites sean números Si no, lanza TypeError
3. Guarda los tres en self.funcion, self.limite_inferior y self.limite_superior

**Qué no hace:** No revisa si a es mayor que b El objeto se puede crear igual, y quien
pregunta si el intervalo sirve es el método es_intervalo_valido() Lo hice así porque si el
constructor truena, el usuario pierde la función que ya había definido

## 4. Métodos

### calcular_amplitud(self)

**Objetivo:** Sacar el ancho total del intervalo Es el paso 1

**Entradas:** ninguna

**Atributos que usa:** self.limite_inferior y self.limite_superior

**Algoritmo:**

```
devolver self.limite_superior - self.limite_inferior
```

**Resultado:** un float con la amplitud A

**Comprobación:** con a = -2 y b = 3 debe dar 5, igual que en mi libreta

### calcular_delta_x(self, n)

**Objetivo:** Sacar el ancho de cada rectángulo Es el paso 2

**Entradas:** n, el número de subintervalos

**Atributos que usa:** los dos límites, a través de calcular_amplitud()

**Algoritmo:**

```
si n no es entero o es menor que 1:
    lanzar ValueError
devolver self.calcular_amplitud() / n
```

**Resultado:** un float con el delta x

**Validaciones:** n tiene que ser entero y mayor o igual a 1, si no truena con ValueError

**Comprobación:** con a = -2, b = 3 y n = 5 debe dar 1.0, porque 5/5 = 1

### calcular_coordenada(self, i, n, tipo)

**Objetivo:** Dar la coordenada x del rectángulo número i Es el paso 3

**Entradas:**

- i -> int -> el número de rectángulo, va de 1 hasta n
- n -> int -> cuántos rectángulos hay en total
- tipo -> str -> derecho, izquierdo o medio

**Atributos que usa:** self.limite_inferior

**Algoritmo:**

```
delta = self.calcular_delta_x(n)
si tipo es "derecho":
    devolver self.limite_inferior + i * delta
si tipo es "izquierdo":
    devolver self.limite_inferior + (i - 1) * delta
si tipo es "medio":
    devolver self.limite_inferior + (i - 0.5) * delta
si no:
    lanzar ValueError
```

**Resultado:** un float con la coordenada x_i

**Validaciones:** tipo tiene que ser uno de los tres textos permitidos, e i tiene que estar
entre 1 y n

**Comprobación:** con a = -2, n = 5 y tipo derecho, para i = 1 debe dar -1, porque
-2 + 1(1) = -1 Es exactamente la fórmula x_i = -2 + (5/n)i de mi libreta

### suma_riemann(self, n, tipo)

**Objetivo:** Calcular el área aproximada sumando todos los rectángulos

**Entradas:** n y tipo, igual que arriba El tipo por defecto es derecho

**Atributos que usa:** self.funcion y los dos límites

**Algoritmo:**

```
si limite_inferior es igual a limite_superior:
    devolver 0
delta = self.calcular_delta_x(n)
suma = 0
repetir con i de 1 hasta n:
    x = self.calcular_coordenada(i, n, tipo)
    suma = suma + self.funcion.evaluar(x)
devolver suma * delta
```

**Resultado:** un float con el área aproximada

**Validaciones:** las que ya hacen calcular_delta_x y calcular_coordenada, no las repito

**Comprobación:** con f(x) = x + 3, a = -2, b = 3, n = 5 y tipo derecho debe dar exactamente
20.0 Con n = 10 debe dar 18.75 y con n = 100 debe dar 17.625 Conforme n crece se va pegando
al 17.5 que saqué a mano

**Nota del saco el delta de la suma:** multiplico por delta hasta el final en vez de hacerlo
dentro del ciclo porque es la misma operación repetida n veces Da igual el resultado pero
son menos cuentas

### detalle_rectangulos(self, n, tipo, cuantos)

**Objetivo:** Darme los primeros rectángulos uno por uno para poder comprobar el resultado a
mano con lápiz

**Entradas:** n, tipo, y cuantos (cuántos rectángulos quiero ver, por defecto 5)

**Atributos que usa:** self.funcion

**Algoritmo:**

```
detalle = lista vacia
limite = el menor entre cuantos y n
delta = self.calcular_delta_x(n)
repetir con i de 1 hasta limite:
    x = self.calcular_coordenada(i, n, tipo)
    altura = self.funcion.evaluar(x)
    area = altura * delta
    agregar a detalle la lista [i, x, altura, area]
devolver detalle
```

**Resultado:** una lista de listas, donde cada una trae el número de rectángulo, su x, su
altura y su área

**Validaciones:** cuantos tiene que ser entero y mayor que 0

### es_intervalo_valido(self)

**Objetivo:** Decir si se puede calcular con el intervalo que tengo guardado

**Entradas:** ninguna

**Algoritmo:**

```
devolver self.limite_inferior <= self.limite_superior
```

**Resultado:** True o False

## 5. Reglas que no se pueden cambiar

- **RI1** La i del ciclo va de 1 hasta n, no de 0 hasta n-1 Así está en mi libreta y así
  tiene que quedar, porque la fórmula x_i = x_0 + i·Δx depende de eso
- **RI2** El tipo por defecto es derecho, porque ese fue el que usé para resolver el
  ejercicio original
- **RI3** suma_riemann no redondea El redondeo se hace al imprimir, en main.py
- **RI4** Esta clase no evalúa la función por su cuenta Siempre le pide el valor a
  self.funcion.evaluar() Si se copia la fórmula del polinomio aquí adentro, se rompe la
  separación entre las dos clases
- **RI5** La clase nunca usa input ni print
- **RI6** No se agrega ningún método de antiderivada ni de cálculo exacto El programa trabaja
  solo con la definición de suma de Riemann
- **RI7** Si a es igual a b el resultado es 0, sin entrar al ciclo
