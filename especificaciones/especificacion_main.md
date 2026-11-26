# Especificación del programa principal (main.py)

## 1. Qué hace main.py

Es el único archivo que habla con el usuario Muestra el menú, pide los datos, crea los
objetos, les llama sus métodos e imprime lo que devuelven Las clases no usan input ni print
nunca

El menú es corto a propósito: nada más lo necesario para resolver el ejercicio, o sea
definir, calcular y salir

## 2. El menú

```
  AREA BAJO LA CURVA - SUMAS DE RIEMANN
1. Definir la funcion y el intervalo
2. Calcular el area
3. Salir
```

Lo dejé sin marcos a propósito El menú se reimprime cada vuelta del ciclo, y con marcos
ocupaba 7 renglones cada vez, así que las capturas no alcanzaban a mostrar el cálculo
completo

## 3. Objetos que se crean

- funcion -> FuncionPolinomial -> Empieza valiendo None y se crea en la opción 1
- integral -> IntegralDefinida -> Empieza valiendo None y se crea también en la opción 1, después de leer los límites

**Por qué empiezan en None:** al abrir el programa no hay nada definido, así que si el
usuario se va directo a la opción 2 hay que avisarle en vez de tronar

## 4. Funciones de apoyo (no son métodos, van sueltas en main.py)

### mostrar_menu()

Imprime el menú de arriba No devuelve nada

### pedir_entero(mensaje, minimo, maximo)

Pide un número entero y no suelta al usuario hasta que meta uno válido

```
repetir para siempre:
    texto = input(mensaje)
    intentar convertir texto a int
    si falla la conversion:
        imprimir "Eso no es un numero entero, intenta otra vez"
        seguir con la siguiente vuelta
    si el numero esta fuera del rango minimo-maximo:
        imprimir el rango permitido
        seguir con la siguiente vuelta
    devolver el numero
```

### pedir_decimal(mensaje)

Igual que la anterior pero con float y sin rango

```
repetir para siempre:
    texto = input(mensaje)
    intentar convertir texto a float
    si falla la conversion:
        imprimir "Eso no es un numero, intenta otra vez"
        seguir con la siguiente vuelta
    devolver el numero
```

### pedir_tipo()

Pide qué punto del rectángulo usar y devuelve derecho, izquierdo o medio

```
mostrar las tres opciones numeradas
opcion = pedir_entero("Elige: ", 1, 3)
si opcion es 1 devolver "derecho"
si opcion es 2 devolver "izquierdo"
si opcion es 3 devolver "medio"
```

El 1 es derecho porque es el que usé en el ejercicio original, así queda de primero

## 5. Qué hace cada opción

### Opción 1 - Definir la función y el intervalo

1. Pide el grado con pedir_entero("Grado del polinomio: ", 0, 10)
2. Arma una lista vacía de coeficientes
3. Repite grado + 1 veces, pidiendo con pedir_decimal el coeficiente de cada potencia,
   empezando por la más alta
4. Crea el objeto: funcion = FuncionPolinomial(coeficientes)
5. Imprime la función con funcion.a_texto()
6. Pide a con pedir_decimal("Limite inferior (a): ")
7. Pide b con pedir_decimal("Limite superior (b): ")
8. Crea el objeto: integral = IntegralDefinida(funcion, a, b)
9. Llama integral.es_intervalo_valido() Si devuelve False, avisa que a no puede ser mayor
   que b, deja integral en None y regresa al menú
10. Si está bien, confirma el intervalo

Junté la función y el intervalo en una sola opción porque no sirve de nada tener una sin el
otro

### Opción 2 - Calcular el área

1. Si integral es None, imprime "Primero define la funcion y el intervalo con la opcion 1" y
   regresa al menú
2. Pide n con pedir_entero("Numero de rectangulos (n): ", 1, 1000000)
3. Pide el tipo con pedir_tipo()
4. Imprime el paso 1 con integral.calcular_amplitud()
5. Imprime el paso 2 con integral.calcular_delta_x(n)
6. Llama detalle = integral.detalle_rectangulos(n, tipo, 5) y recorre la lista con un ciclo
   imprimiendo cada renglón con su número de rectángulo, su x, su altura y su área
7. Llama resultado = integral.suma_riemann(n, tipo) y lo imprime redondeado a 6 decimales

Esta opción imprime los cuatro pasos de mi procedimiento en una sola pantalla, en el orden de
la libreta Por eso no necesito opciones separadas para la amplitud o los rectángulos

Los rectángulos se muestran hasta los primeros 5 aunque n sea enorme, porque con eso basta
para comprobar a mano y no me llena la pantalla El redondeo se hace al imprimir, nunca dentro
de la clase

### Opción 3 - Salir

1. Imprime un mensaje de despedida
2. Corta el ciclo del menú

## 6. Secuencia general del programa

```
funcion = None
integral = None

repetir mientras no se elija salir:
    mostrar_menu()
    opcion = pedir_entero("Elige una opcion: ", 1, 3)
    segun la opcion, hacer lo que dice la seccion 5
    si la opcion es 3, cortar el ciclo

imprimir despedida
```

## 7. Condiciones de salida

- El programa solo termina con la opción 3
- Ninguna otra opción corta el ciclo Si algo sale mal, se avisa y se regresa al menú
- El programa no debe terminar nunca por un error de Python Todas las entradas pasan por
  pedir_entero o pedir_decimal, que no dejan pasar texto que no sea número

## 8. Reglas que no se pueden cambiar

- **RM1** Las opciones del menú son 3 y están en ese orden No se agregan ni se quitan
- **RM2** Ninguna clase usa input ni print, solo main.py
- **RM3** El redondeo para imprimir es de 6 decimales, y solo al imprimir
- **RM4** Antes de usar integral siempre se revisa que no sea None
- **RM5** Todas las entradas de números pasan por pedir_entero o pedir_decimal, no se usa
  input directo para números
- **RM6** No se agrega ninguna opción de cálculo exacto por antiderivada El programa trabaja
  solo con sumas de Riemann
- **RM7** No se agregan opciones de guardar en archivo ni de ver la función por separado El
  menú se queda en tres

## 9. Cómo colaboran las dos clases

```
main.py
   |
   |-- crea --> FuncionPolinomial (guarda los coeficientes en una lista)
   |                    ^
   |                    | le pide evaluar(x)
   |-- crea --> IntegralDefinida (guarda la funcion y los limites)
```

El objeto integral trae adentro al objeto funcion Cuando necesita la altura de un rectángulo
no la calcula, se la pide a funcion Esa es la colaboración entre las dos clases
