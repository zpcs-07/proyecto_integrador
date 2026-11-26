# Etapa 5 — Cómo usé GitHub Copilot

## 1. ¿Cómo utilizaste las especificaciones para solicitar código a Copilot?

Primero escribí los archivos de la carpeta especificaciones/ Ahí puse los atributos de cada
clase, el pseudocódigo de cada método y una lista de reglas numeradas

Después le pedí cada clase pasándole su especificación La de IntegralDefinida la pedí en dos
partes, porque si le pides todo junto se pierde

## 2. ¿Qué revisaste o modificaste del código generado?

Lo primero que revisaba era si había respetado las reglas Las tres que más vigilé:

- que los coeficientes quedaran de mayor a menor potencia
- que la i del ciclo fuera de 1 a n y no de 0 a n-1
- que suma_riemann le pidiera la altura a self.funcion.evaluar(x), en vez de copiar la
  fórmula del polinomio adentro

Las tres las cumplió

Lo único que agregó sin que se lo pidiera fue rechazar booleanos en los coeficientes Lo dejé
porque en Python True vale 1, y si se cuela nadie se da cuenta

## 3. ¿Copilot generó una respuesta incorrecta o distinta de lo solicitado?

Sí, una El método a_texto escribía el .0 cuando los coeficientes venían como decimales:

```
FuncionPolinomial([1, 3]).a_texto()      ->  f(x) = x + 3
FuncionPolinomial([1.0, 3.0]).a_texto()  ->  f(x) = x + 3.0
```

El segundo caso es justo como lo usa el programa, porque main.py pide los coeficientes con
pedir_decimal y siempre llegan como float

La culpa no fue de Copilot Hizo lo que decía mi especificación, y mi especificación nunca
dijo qué hacer con un float que vale entero Le pedí que corrigiera nada más a_texto y que no
tocara evaluar ni el constructor Lo resolvió con is_integer() y quedó bien, el 2.5 se sigue
escribiendo con su decimal

Después actualicé la especificación, porque si no el documento dice una cosa y el código hace
otra

## 4. ¿Cómo comprobaste el funcionamiento de clases y métodos?

Con los números de mi libreta, método por método:

- calcular_amplitud() con a = -2 y b = 3 -> 5
- calcular_delta_x(5) -> 1.0
- calcular_coordenada(1, 5, derecho) -> -1.0
- evaluar(-1) -> 2.0
- suma_riemann(5) -> 20.0 y suma_riemann(100) -> 17.625

Esos números salen de la fórmula S(n) = 17.5 + 12.5/n, no del programa Así estaba comparando
el código contra las matemáticas, y no contra sí mismo

También lo probé con otras funciones para ver que no estuviera amarrado a mi caso Todo quedó
en documentacion/02_pruebas.md

## 5. ¿Qué ventajas y limitaciones observaste?

Lo bueno es que escribe rápido lo aburrido, como el ciclo de a_texto con todos sus casos Y
cuando las reglas están numeradas, las respeta

Lo malo es que no adivina lo que no está escrito, y de ahí salió el error del .0 También le
gusta agregar de más, y si le pides mucho de un jalón sale peor

Al final Copilot es tan bueno como el documento que le das

## 6. ¿Por qué es necesario comprender código producido con ayuda de IA?

Por dos razones que me pasaron aquí

La primera es que si no lo entiendes, no le encuentras los errores El bug del .0 lo encontré
leyendo el método línea por línea, no porque algo me avisara Un programa que corre sin tronar
no es un programa correcto

La segunda es que tengo que poder defenderlo Si me preguntan por qué la i empieza en 1, o por
qué IntegralDefinida guarda adentro un objeto en lugar de los coeficientes, la única forma de
contestar es haber entendido qué hace cada parte El que entrega el proyecto soy yo
