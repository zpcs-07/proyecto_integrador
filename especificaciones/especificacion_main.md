# Especificación del programa principal (main.py)

## 1. Qué hace main.py

Es el único archivo que habla con el usuario Muestra el menú, pide los datos, crea los
objetos, les llama sus métodos e imprime lo que devuelven

Las clases nunca usan input ni print

El menú es corto a propósito: nada más lo necesario para resolver el ejercicio, o sea
definir, calcular y salir

## 2. El menú

```
  AREA BAJO LA CURVA - SUMAS DE RIEMANN
1. Definir la funcion y el intervalo
2. Calcular el area
3. Salir
```

Lo dejé sin marcos a propósito El menú se vuelve a imprimir cada vuelta, y con marcos ocupaba
7 renglones cada vez Así las capturas alcanzan a mostrar el cálculo completo

## 3. Objetos que se crean

- funcion -> FuncionPolinomial -> Empieza en None y se crea en la opción 1
- integral -> IntegralDefinida -> Empieza en None y se crea también en la opción 1, después de leer los límites

**Por qué empiezan en None:** al abrir el programa no hay nada definido Si el usuario se va
directo a la opción 2, hay que avisarle en vez de tronar

## 4. Funciones de apoyo (van sueltas en main.py, no son métodos)

### mostrar_menu()

Imprime el menú de arriba No devuelve nada

### pedir_entero(mensaje, minimo, maximo)

Pide un entero y no suelta al usuario hasta que meta uno válido

```
repetir para siempre:
    texto = input(mensaje)
    intentar convertir texto a int
    si falla la conversion:
        imprimir "Eso no es un numero entero, intenta otra vez"
        seguir con la siguiente vuelta
    si el numero esta fuera del rango:
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

El 1 es derecho porque es el que usé en el ejercicio original

## 5. Qué hace cada opción

### Opción 1 - Definir la función y el intervalo

1. Pide el grado, de 0 a 10
2. Arma una lista vacía de coeficientes
3. Repite grado + 1 veces pidiendo cada coeficiente, empezando por la potencia más alta
4. Crea el objeto funcion
5. Imprime la función con a_texto()
6. Pide a y después b
7. Crea el objeto integral
8. Llama es_intervalo_valido() Si da False, avisa que a no puede ser mayor que b y deja
   integral en None
9. Si está bien, confirma el intervalo

Junté la función y el intervalo en la misma opción porque no sirve de nada tener una sin el
otro

### Opción 2 - Calcular el área

1. Si integral es None, avisa y regresa al menú
2. Pide n, de 1 a 1000000
3. Pide el tipo con pedir_tipo()
4. Imprime el paso 1 con calcular_amplitud()
5. Imprime el paso 2 con calcular_delta_x(n)
6. Pide detalle_rectangulos(n, tipo, 5) y recorre la lista imprimiendo cada renglón
7. Imprime el resultado de suma_riemann(n, tipo), redondeado a 6 decimales

Esta opción imprime mis cuatro pasos en una sola pantalla, en el mismo orden de la libreta
Por eso no necesito opciones separadas para la amplitud o los rectángulos

Los rectángulos se muestran hasta los primeros 5 aunque n sea enorme Con eso basta para
comprobar a mano y no me llena la pantalla El redondeo se hace al imprimir, nunca dentro de
la clase

### Opción 3 - Salir

1. Imprime la despedida
2. Corta el ciclo

## 6. Secuencia general del programa

```
funcion = None
integral = None

repetir mientras no se elija salir:
    mostrar_menu()
    opcion = pedir_entero("Elige una opcion: ", 1, 3)
    segun la opcion, hacer lo de la seccion 5
    si la opcion es 3, cortar el ciclo

imprimir despedida
```

## 7. Condiciones de salida

- El programa solo termina con la opción 3
- Ninguna otra opción corta el ciclo Si algo sale mal, se avisa y se regresa al menú
- Nunca debe terminar por un error de Python Todas las entradas pasan por pedir_entero o
  pedir_decimal

## 8. Reglas que no se pueden cambiar

- **RM1** Las opciones son 3 y van en ese orden No se agregan ni se quitan
- **RM2** Ninguna clase usa input ni print, solo main.py
- **RM3** El redondeo es de 6 decimales, y solo al imprimir
- **RM4** Antes de usar integral siempre se revisa que no sea None
- **RM5** Todos los números pasan por pedir_entero o pedir_decimal, nunca por input directo
- **RM6** No se agrega ninguna opción de cálculo exacto por antiderivada Aquí se trabaja solo
  con sumas de Riemann
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
